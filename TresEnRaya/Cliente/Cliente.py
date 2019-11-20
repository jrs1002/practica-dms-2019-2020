#!/urs/bin/python
#-*- coding: utf-8 -*-

#Imports
from socket import *
import time
import json
from _thread import *
from InterfazJugador import InterfazJugador

#Clase Cliente
class Cliente:
    def ini(self):
        """
        Inicializa el puerto y el host.

        Return:
        host, port 
        """
        host = "0.0.0.0"
        port = 9494
        return host, port

    def crearSocket(self):
        """
        Devuelve un nuevo socket siguiendo el esquema del protocolo TCP

        Return:
        s -- socket
        """
        s = socket(AF_INET, SOCK_STREAM)
        return s

    def conectarse (self, host, port, s):
        """
        Conecta con el puerto y host pasados.

        Parámetros:
        host
        port --puerto
        s --socket
        """
        s.connect((host, port))

    def intentoConexion(self, host, port, s):
        """
        Si el puerto no esta siendo usado y la dirección pasada
        es correcta, se conecta al servidor

        Parámetros:
        host
        port --puerto
        s --socket
        """
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
        """
        Realiza el envio de mensajes Cliente-->Servidor

        Parámetros:
        s --socket
        msg --mensaje a enviar
        """
        while True:
            try:
                s.send(msg.encode("UTF-8"))
                break
            except:
                print("Error\n")
                print("Se intentará en 5 seg")
                time.sleep(5)

    def recibir(self, s):
        """
        Gestiona los mensajes recibidos del Servidor.

        Parámetros:
        s -- socket 

        Return:
        mensaje recibido 
        """
        while True:
            try:
              reply = s.recv(2048)
              return reply.decode("UTF-8")

            except:
                input("Pulse para refrescar")

    def recibirEspecial(self, s):
        """
        Se recibe el número asignado al cliente y se le asigna.

        Parámetros:
        s --socket
        """
        self.client = s.recv(2048).decode("UTF-8") #Recibe el identificador del cliente
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

    def inicializarJugador(self, s):
        """
        Se incializa un jugador, para ello se requiere de un cliente y su id

        Parámetros:
        s -- socket

        Return:
        idJugador --id del jugador correspondiente al cliente.
        """
        print(self.recibir(s))   # Se pregunta al jugador si quiere inciar el juego
        msg ="102***"       # Codigo del mensaje
        msg += input()      # Respuesta del jugador 1 si 0 no
        self.enviar(s,msg)

        msg,obj = self.interpretarMensaje(self.recibir(s))

        if(msg=="201"):
            idJugador = int(obj)
            return InterfazJugador(idJugador)

    def __init__(self):
        """
        Se inicializan las variables.
        """
        self.client = ""

    def main(self):
        """
        Main de la clase Servidor
        """
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
            #Se convierte el objeto devuelto por jugar a str
            #json.dumps(objeto) que te lo devuelve en str
            if (mens == '100'): 
                exit = True
            else:
                self.enviar(s,mens+"***"+obj)

        print("\nTe esperamos pronto!")
        time.sleep(5)
        s.close()
        s = None

    def __del__(self):
        """
        Destruye los socket que no son nulos al final de la ejecución.
        """
        # TODO 
        pass
        
#Se crea el Cliente
cliente = Cliente()
#Llamada al main
cliente.main()

