#IMPORTS
from socket import *
import time
from _thread import *

#FUNCIONES
def ini():
    host = "0.0.0.0"
    port = 9797
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

def enviar(s):
    while True:
        global exit
        try:
            msg = input("")
            msg = client +": " + msg
            if msg == client+": salir":
                exit = True
                msg = "El "+client+" cliente se ha ido"
                s.send(msg.encode("UTF-8"))
                s.close
                break
            else:
                s.send(msg.encode("UTF-8"))
                start_new_thread(recibir,(s,)) 
        except:
            print("Error\n")
            print("Se intentará en 5 seg")
            time.sleep(5)

def recibir(s):
    while True:
        try:
          reply = s.recv(2048)
          print(reply.decode("UTF-8"))
          break

        except:
            print("Error\n")
            print("Se intentará en 5 seg")
            time.sleep(5)

def recibirEspecial(s):
    global client
    client = s.recv(2048).decode("UTF-8") #Recibe el identificador del cliente
    print("Cliente"+ client)

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
    print("Escribiendo el mensaje\n")
    start_new_thread(enviar,(s,))

    while exit!=True:   # Necesarios para que los hilos no mueran
        pass

    print("\nLo lamentamos, ha ocurrido un error.")
    print("Cerrando la ventana en 5 seg")
    time.sleep(10)

main()


