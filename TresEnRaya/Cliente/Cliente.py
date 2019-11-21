#Imports
from socket import *
import time
import json
from _thread import *
from InterfazJugador import InterfazJugador

#Clase Cliente
class Cliente:
    def __init__(self):
        """
        Se inicializan las variables.
        """
        self.client = ""
        self.s = socket(AF_INET, SOCK_STREAM)
        self.host = "0.0.0.0"
        self.port = 9494
        self.exit=False

    def __del__(self):
        """
        Destruye los socket que no son nulos al final de la ejecución.
        """
        if self.s==None:
            self.s=None

    def conectarse(self):
        """
        Conecta con el puerto y host pasados.
        """
        self.s.connect((self.host, self.port))

    def intentoConexion(self):
        """
        Si el puerto no esta siendo usado y la dirección pasada
        es correcta, se conecta al servidor
        """
        while True:
            print("\nIntentando conectarse a :", self.host + ":" + str(self.port))
            try:
                self.conectarse()
                break
            except:
                print("No hay servidor en:", self.host + ":" + str(self.port))
                print("Se intentará de nuevo en 5 segundos\n")
                time.sleep(5)

    def enviar(self,msg):
        """
        Realiza el envio de mensajes Cliente-->Servidor

        Parámetros:
        msg --mensaje a enviar
        """
        while True:
            try:
                self.s.send(msg.encode("UTF-8"))
                break
            except:
                print("Error\n")
                print("Se intentará en 5 seg")
                time.sleep(5)

    def recibir(self):
        """
        Gestiona los mensajes recibidos del Servidor.

        Return:
        mensaje recibido 
        """
        while True:
            try:
              reply = self.s.recv(2048)
              return reply.decode("UTF-8")

            except:
                input("Pulse para refrescar")

    def recibirId(self):
        """
        Se recibe el número asignado al cliente y se le asigna.
        """
        self.client = self.s.recv(2048).decode("UTF-8") #Recibe el identificador del cliente
        print("Cliente"+ self.client)

    def interpretarMensaje(self, msg):
        """
        Interpreta el mensaje pasado.

        Parámetros:
        mensaje

        Return:
        mensaje interpretado
        """
        if (len(msg) > 3):
            msg = msg.split("***")
            return msg[0], msg[1]

    def inicializarJugador(self):
        """
        Se incializa un jugador, para ello se requiere de un cliente y su id

        Return:
        idJugador --id del jugador correspondiente al cliente.
        """
        print(self.recibir())   # Se pregunta al jugador si quiere inciar el juego
        msg ="102***"       # Codigo del mensaje
        msg += input()      # Respuesta del jugador 1 si 0 no
        self.enviar(msg)

        msg,obj = self.interpretarMensaje(self.recibir())

        if(msg=="201"):
            idJugador = int(obj)
            return InterfazJugador(idJugador)

    def main(self):
        """
        Main de la clase Cliente
        """
        self.intentoConexion()
        self.recibirId()
        print("\nConexión establecida\nEl servidor es:", self.host+":"+str(self.port)+"\n")

        jugador = self.inicializarJugador()

        while not self.exit:   # Necesarios para que los hilos no mueran
            """
            Aqui se realiza la comuniación con jugador
            """
            mens, obj = self.interpretarMensaje(self.recibir())
            mens, obj = jugador.jugar(mens,obj)
            #Se convierte el objeto devuelto por jugar a str
            #json.dumps(objeto) que te lo devuelve en str
            if (mens == '100'): 
                self.exit = True
            else:
                self.enviar(mens+"***"+obj)

        print("\nTe esperamos pronto!")
        time.sleep(5)
        self.s.close()
        self.s = None
        
#Se crea el Cliente
cliente = Cliente()
#Llamada al main
cliente.main()

