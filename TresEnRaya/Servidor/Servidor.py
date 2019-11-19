#!/urs/bin/python
#-*- coding: utf-8 -*-

#Importaciones
from socket import *
from _thread import *
import time
import sys
from Tablero import Tablero
from Arbitro import Arbitro


#FUNCIONES
class Servidor:
    def ini(self):
        host = "0.0.0.0"
        port = 9494
        return host, port

    def crearSocket(self):
        s = socket(AF_INET, SOCK_STREAM)
        return s

    def ligarSocket(self,s, host, port):
        while True:
            try:
                s.bind((host, port))
                break
            except error as e:
                print("ERROR:", e)

    def conexiones(self,s):
        cliente, direccion = s.accept()
        print("\nConexión establecida.\nEl cliente es:", direccion[0] + ":" + str(direccion[1])+"\n")
        return cliente, direccion

    def recibir(self,cliente):
        while True:
            try:
              reply = cliente.recv(2048)
              return reply.decode("UTF-8")
              break
            except:
                print("\nRecv: No responde, se intentará en 5 seg\n")
                time.sleep(5)

    def enviarEspecial(self,cliente):
        self.client = self.lista_de_clientes.pop()
        cliente.send(self.client.encode("UTF-8")) #Envia al cliente su nº de cliente(1 o 2)

    def enviar_Mensaje(self,mensaje,cliente): #Para enviar mensajes Servidor->Cliente
            try:
                cliente.send(mensaje.encode("UTF-8"))
            except:
                print("\nSend: No responde, se intentará en 5 seg")
                time.sleep(5)

    def interpretarMensaje(self,msg):
        if (len(msg) > 3):
            msg = msg.split("***")
            return msg[0], msg[1]

    def inicializarJugador(self,cliente, id):
        """
        Se incializa un jugador, para ello se requiere de un cliente y su id

        Parámetros:
        cliente -- cliente en el que se encuentra el jugador
        id      -- id del jugador  
        """
        self.enviar_Mensaje("¿Desea empezar el juego?",cliente)
        respuesta = self.recibir(cliente)
        cod, obj = self.interpretarMensaje(respuesta)

        if (cod == "102"):
            if obj == "1":
                print("El jugador " + str(id) + " quiere jugar, se le envía el código de jugador")
                self.enviar_Mensaje("201***"+str(id),cliente) 
            else: 
                print("El jugador " + str(id) + " no quiere jugar, finalizar conexión")

    def __init__(self):
        self.exit = False      # Utilizada en la desconexion/conexion de clientes
        self.lista_de_clientes = ["2","1"]   # El servidor le asigna un numero a los clientes segun esta lista
        self.client = ""     # Numero del cliente

    #MAIN
    def main(self):

        host,port = self.ini()
        s = self.crearSocket()
        self.ligarSocket(s, host,port)
        s.listen(2)     #2 clientes

        print("\nEsperando por los clientes")

        # Se inicializan los clientes 
        cliente1,direccion1 = self.conexiones(s)
        self.enviarEspecial(cliente1)               # Espero conexion del 1 cliente

        cliente2,direccion2 = self.conexiones(s)
        self.enviarEspecial(cliente2)              # Espero conexion del 2 cliente

        # PROBANDO LA CONEXION
        # Le damos el identificador a cada Cliente
        self.inicializarJugador(cliente1,1)
        self.inicializarJugador(cliente2,2)
        
        arbitro = Arbitro(1,2)    

        # INICIA EL JUEGO
        cliente = cliente1 # Empieza jugando el jugador1
        mens,obj,dest = arbitro.arbitrar("103") # Le muestra el tablero
        self.enviar_Mensaje(mens+"***"+obj,cliente)  # Le envia un 202 tablero

        exit = True
        while not exit:   # Necesarios para que los hilos no mueran
            """
            Aqui tendremos que meter la comunicación con jugador
            recibir mensaje
            pasarselo a jugador
            enviar respuesta
            """
            mens, obj = self.interpretarMensaje(recibir(cliente))
            
            print("Recibido",mens,obj)
            
            mens, obj, dest = arbitro.arbitrar(mens,obj)

            if (mens == "200"):        
                self.enviar_Mensaje(mens+"***"+obj,cliente1)     
                self.enviar_Mensaje(mens+"***"+obj,cliente2)     
                exit = True
            elif dest == 1:
                print("mens a cliente1")
                cliente = cliente1
                self.enviar_Mensaje(mens+"***"+obj,cliente)
            else:
                print("mens a cliente2")
                cliente = cliente2
                self.enviar_Mensaje(mens+"***"+obj,cliente)
                
        print("\nLos jugadores han terminado de jugar\n")
        time.sleep(5)
        s.close()
        s = None

    def __del__(self):
        # Meter socket como atributo de la clase
        # Si no son nulos hacerlos nulos
        pass

#Llamada al main

servidor = Servidor()
servidor.main()
