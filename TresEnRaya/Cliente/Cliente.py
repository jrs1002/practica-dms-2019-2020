#IMPORTS
from socket import *
import time
from _thread import *
from InterfazJugador import InterfazJugador
class Cliente:
    #FUNCIONES
    def ini(self):
        host = "0.0.0.0"
        port = 9494
        return host, port

    def crearSocket(self):
        s = socket(AF_INET, SOCK_STREAM)
        return s

    def conectarse (self, host, port, s):
        s.connect((host, port))

    def intentoConexion(self, host, port, s):
            while True:
                print("\nIntentando conectarse a :", host + ":" + str(port))
                try:
                    self.conectarse(host, port, s)
                    break
                except:
                    print("No hay servidor en:", host + ":" + str(port))
                    print("Se intentará de nuevo en 5 segundos\n")
                    time.sleep(5)

    def enviar(self, s,msg):
        while True:
            try:
                s.send(msg.encode("UTF-8"))
                break
            except:
                print("Error\n")
                print("Se intentará en 5 seg")
                time.sleep(5)

    def recibir(self, s):
        while True:
            try:
              reply = s.recv(2048)
              return reply.decode("UTF-8")

            except:
                input("Pulse para refrescar")

    def recibirEspecial(self, s):
        self.client = s.recv(2048).decode("UTF-8") #Recibe el identificador del cliente
        print("Cliente"+ self.client)

    def interpretarMensaje(self, msg):
        if (len(msg) > 3):
            msg = msg.split("***")
            return msg[0], msg[1]

    def inicializarJugador(self, s):

        print(self.recibir(s))   # Se pregunta al jugador si quiere inciar el juego
        msg ="102***"       # Codigo del mensaje
        msg += input()      # Respuesta del jugador 1 si 0 no
        self.enviar(s,msg)

        msg,obj = self.interpretarMensaje(self.recibir(s))

        if(msg=="201"):
            idJugador = int(obj)
            return InterfazJugador(idJugador)

    def __init__(self):

        self.client = ""

    #MAIN
    def main(self):
        exit = False
        host, port = self.ini()
        s = self.crearSocket()
        self.intentoConexion(host,port,s)
        self.recibirEspecial(s)
        print("\nConexión establecida\nEl servidor es:", host+":"+str(port)+"\n")

        jugador = self.inicializarJugador(s)


        while not exit:   # Necesarios para que los hilos no mueran
            """
            Aqui tendremos que meter la comunicación con jugador
            recibir mensaje
            pasarselo a jugador
            enviar respuesta
            """
            mens, obj = self.interpretarMensaje(self.recibir(s))
            mens, obj = jugador.jugar(mens,obj)
            if (mens == '100'): 
                exit = True
            else:
                self.enviar(s,mens+"***"+obj)



        print("\nTe esperamos pronto!")
        time.sleep(5)
        s.close()
        s = None

    def __del__(self):
        # TODO 
        pass

cliente = Cliente()
cliente.main()

