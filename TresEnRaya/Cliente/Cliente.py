#IMPORTS
from socket import *
import time
from _thread import *
from InterfazJugador import InterfazJugador

#FUNCIONES
def ini():
    host = "0.0.0.0"
    port = 9494
    return host, port

def crearSocket():
    s = socket(AF_INET, SOCK_STREAM)
    return s

def conectarse (host, port, s):
    s.connect((host, port))

def intentoConexion(host, port, s):
        while True:
            print("\nIntentando conectarse a :", host + ":" + str(port))
            try:
                conectarse(host, port, s)
                break
            except:
                print("No hay servidor en:", host + ":" + str(port))
                print("Se intentará de nuevo en 5 segundos\n")
                time.sleep(5)

def enviar(s,msg):
    while True:
        global exit
        try:
            s.send(msg.encode("UTF-8"))
            break
        except:
            print("Error\n")
            print("Se intentará en 5 seg")
            time.sleep(5)

def recibir(s):
    while True:
        try:
          reply = s.recv(2048)
          return reply.decode("UTF-8")

        except:
            input("Pulse para refrescar")

def recibirEspecial(s):
    global client
    client = s.recv(2048).decode("UTF-8") #Recibe el identificador del cliente
    print("Cliente"+ client)

def interpretarMensaje(msg):
    if (len(msg) > 3):
        msg = msg.split("---")
        return msg[0], msg[1]

def inicializarJugador(s):

    print(recibir(s))   # Se pregunta al jugador si quiere inciar el juego
    msg ="102---"       # Codigo del mensaje
    msg += input()      # Respuesta del jugador 1 si 0 no
    enviar(s,msg)

    msg,obj = interpretarMensaje(recibir(s))

    if(msg=="201"):
        idJugador = int(obj)
        return InterfazJugador(idJugador)

#VARIABLES GLOBALES
exit=False      # Si el cliente envia salir, exit se pone en true y el
                # el programa termina
client = ""

#MAIN
def main():

    host, port = ini()
    s = crearSocket()
    intentoConexion(host,port,s)
    recibirEspecial(s)
    print("\nConexión establecida\nEl servidor es:", host+":"+str(port)+"\n")

    jugador = inicializarJugador(s)
    

    while not exit:   # Necesarios para que los hilos no mueran
        """
        Aqui tendremos que meter la comunicación con jugador
        recibir mensaje
        pasarselo a jugador
        enviar respuesta
        """
        input("Pulse para continuar")
        mens, obj = interpretarMensaje(recibir(s))
        mens, obj = jugador.jugar(mens,obj)
        # if mensaje = finalizar : exit = True
        enviar(s,mens+"---"+obj)

    print("\nLo lamentamos, ha ocurrido un error.")
    print("Cerrando la ventana en 5 seg")
    time.sleep(10)

main()


