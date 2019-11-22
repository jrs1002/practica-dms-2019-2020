#Imports
from socket import *
from _thread import *
import time
import sys
import json
from Tablero import Tablero
from Arbitro import Arbitro
from Mensaje import Mensaje  

#Clase Servidor
class Servidor:
    def __init__(self):
        """
        Se inicializan las variables.
        """
        self.s = socket(AF_INET, SOCK_STREAM)
        self.host = "0.0.0.0"
        self.port = 9494      
        self.lista_de_clientes = ["2","1"]   # El servidor le asigna un numero a los clientes segun esta lista
        self.client = ""     # Numero del cliente
        self.exit=False

    def __del__(self):
        """
        Destruye los socket que no son nulos al final de la ejecución.
        """
        if self.s==None: 
            self.s=None 

    def ligarSocket(self):
        """
        Relaciona un socket con el puerto y el host.
        
        Parámetros:
        s--socket
        host
        port --puerto
        """
        while True:
            try:
                self.s.bind((self.host, self.port))
                break
            except error as e:
                print("ERROR:", e)

    def conexiones(self):
        """
        Espera por la conexión de clientes.

        Parámetros:
        s--socket

        Return:
        cliente,direccion 
        """
        cliente, direccion = self.s.accept()
        print("\nConexión establecida.\nEl cliente es:", direccion[0] + ":" + str(direccion[1])+"\n")
        return cliente, direccion

    def recibir(self,cliente):
        """
        Gestiona los mensajes recibidos de los clientes.

        Parámetros:
        cliente 

        Return:
        mensaje recibido 
        """
        while True:
            try:
              reply = cliente.recv(2048)
              return reply.decode("UTF-8")
              break
            except:
                print("\nRecv: No responde, se intentará en 5 seg\n")
                time.sleep(5)

    def enviarId(self,cliente):
        """
        Se asgina un número al cliente pasado y se le envia.

        Parámetros:
        cliente
        """
        self.client = self.lista_de_clientes.pop()
        cliente.send(self.client.encode("UTF-8")) #Envia al cliente su nº de cliente(1 o 2)

    def enviar_Mensaje(self,mensaje,cliente): 
        """
        Envia mensajes Servidor->Cliente

        Parámetros:
        mensaje--mensaje que se quiere enviar
        cliente--cliente al que se le quiere enviar el mensaje
        """
        while True:
            try:
                cliente.send(mensaje.encode("UTF-8"))
                break
            except:
                print("\nSend: No responde, se intentará en 5 seg")
                time.sleep(5)

    def enviar_Mensaje_Codificado(self,cod,obj,cliente):
        """
        Crea un objeto Mensaje con el código de mensaje y el objeto
        se lo envia al cliente
        """
        while True:
            try:
                mensaje = Mensaje(cod,obj)
                cadena = mensaje.convertirEnCadena()
                cliente.send(cadena.encode("UTF-8"))
                break
            except:
                print("\nSend_esp: No responde, se intentará en 5 seg")
                time.sleep(5)

    def interpretarMensaje(self,msg): 
        """
        Interpreta el mensaje pasado.

        Parámetros:
        mensaje

        Return:
        mensaje interpretado
        """
        print(msg)
        mensaje = Mensaje.convertirEnObjeto(msg)
        return mensaje

    def inicializarJugador(self,cliente, id):
        """
        Se incializa un jugador, para ello se requiere de un cliente y su id

        Parámetros:
        cliente -- cliente en el que se encuentra el jugador
        id      -- id del jugador  
        """
        self.enviar_Mensaje("¿Desea empezar el juego?",cliente)
        respuesta = self.recibir(cliente)
        mensaje = self.interpretarMensaje(respuesta)

        if (mensaje.getCode() == "102"):
            if mensaje.getObj() == "1":
                print("El jugador " + str(id) + " quiere jugar, se le envía el código de jugador")
                self.enviar_Mensaje_Codificado("201",str(id),cliente) 
            else: 
                print("El jugador " + str(id) + " no quiere jugar, finalizar conexión")

    def main(self):
        """
        Main de la clase Servidor
        """
        self.ligarSocket()
        self.s.listen(2)     #2 clientes

        print("\n\n/********************************\\\n   Esperando a los clientes\n\n")

        # Se inicializan los clientes 
        cliente1,direccion1 = self.conexiones()
        self.enviarId(cliente1)               # Espero conexion del 1 cliente

        cliente2,direccion2 = self.conexiones()
        self.enviarId(cliente2)              # Espero conexion del 2 cliente

        # PROBANDO LA CONEXION
        # Le damos el identificador a cada Cliente
        self.inicializarJugador(cliente1,1)
        self.inicializarJugador(cliente2,2)
        print("\n********************************\n\n")
        arbitro = Arbitro(1,2)    

        # INICIA EL JUEGO
        cliente = cliente1 # Empieza jugando el jugador1
        mens,obj,dest = arbitro.arbitrar("103") # Le muestra el tablero

        self.enviar_Mensaje_Codificado(mens,obj,cliente)  # Le envia un 202 tablero

        while not self.exit:   # Necesarios para que los hilos no mueran
            """
            Aqui tendremos que meter la comunicación con jugador
            recibir mensaje
            pasarselo a jugador
            enviar respuesta
            """
            mensaje = self.interpretarMensaje(self.recibir(cliente))
            mens, obj, dest = arbitro.arbitrar(mensaje.getCode(),mensaje.getObj())

            if (mens == "200"):        
                self.enviar_Mensaje_Codificado(mens,obj,cliente1)     
                self.enviar_Mensaje_Codificado(mens,obj,cliente2)     
                self.exit = True
            elif dest == 1:
                print("mens a cliente1")
                cliente = cliente1
                self.enviar_Mensaje_Codificado(mens,obj,cliente)
            else:
                print("mens a cliente2")
                cliente = cliente2
                self.enviar_Mensaje_Codificado(mens,obj,cliente)
                
        print("\nLos jugadores han terminado de jugar\n")
        time.sleep(5)
        self.s.close()
        self.s = None

#Creación del Servidor
servidor = Servidor()
#Llamada al main
servidor.main()

