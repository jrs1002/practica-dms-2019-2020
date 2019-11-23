# Imports
from socket import *
from _thread import *
import time
import sys
import json
from Tablero import Tablero
from Arbitro import Arbitro
from Mensaje import Mensaje

# Clase Servidor
class Servidor:
    def __init__(self):
        """
        Método que inicializa el Servidor.
        Se inicializan las variables.
        Se crea el socket.
        Se establecen el host y el puerto.
        Se crea la lista con los clientes.
        """
        self.s = socket(AF_INET, SOCK_STREAM)
        self.host = "0.0.0.0"
        self.port = 9494
        # El servidor le asigna un número a los clientes según esta lista
        self.lista_de_clientes = ["2", "1"]
        self.client = ""     # Número del cliente
        self.exit = False

    def __del__(self):
        """
        Se destruyen los socket que no son nulos al final de la ejecución.
        """
        if self.s == None:
            self.s = None

    def ligarSocket(self):
        """
        Se relaciona un socket con el puerto y el host.
        """
        while True:
            try:
                self.s.bind((self.host, self.port))
                break
            except error as e:
                print("\nERROR: ", e, "\n")

    def conexiones(self):
        """
        Se espera a la conexión de clientes.

        Return:
        cliente -- Cliente
        direccion -- Dirección del cliente
        """
        cliente, direccion = self.s.accept()
        print("| Conexión establecida.\t\t|")
        print("| El cliente es:\t\t|\n|\t", direccion[0] + ":" + str(direccion[1])+"\t|")
        return cliente, direccion

    def recibir(self, _cliente):
        """
        Se gestionan los mensajes recibidos de los clientes.

        Parámetros:
        cliente -- Cliente que ha enviado el mensaje

        Return:
        reply.decode("UTF-8") -- Mensaje recibido 
        """
        while True:
            try:
                reply = _cliente.recv(2048)
                return reply.decode("UTF-8")
                break
            except:
                print("\nRecv: No responde.\n")
                print("Se intentará de nuevo en 5 segundos.\n")
                time.sleep(5)

    def enviarId(self, _cliente):
        """
        Se asigna un número al cliente pasado y se le envía.

        Parámetros:
        _cliente -- Cliente al que enviar el id
        """
        self.client = self.lista_de_clientes.pop()
        # Envia al cliente su número de cliente (1 o 2)
        _cliente.send(self.client.encode("UTF-8"))

    def enviar_Mensaje(self, msg, _cliente):
        """
        Se realiza el envio de mensajes de Cliente a Servidor.

        Parámetros:
        msg -- Mensaje a enviar
        _cliente -- Cliente al que se le quiere enviar el mensaje
        """
        while True:
            try:
                _cliente.send(msg.encode("UTF-8"))
                break
            except:
                print("\nSend: No responde.\n")
                print("Se intentará de nuevo en 5 segundos.\n")
                time.sleep(5)

    def enviar_Mensaje_Codificado(self, cod, obj, _cliente):
        """
        Se crea un objeto Mensaje con el código de mensaje y el objeto
        y se lo envía al Cliente.

        Parámetros:
        cod -- Código del mensaje
        obj -- Objeto del mensaje
        """
        while True:
            try:
                mensaje = Mensaje(cod, obj)
                cadena = mensaje.convertirEnCadena()
                _cliente.send(cadena.encode("UTF-8"))
                break
            except:
                print("\nSend_esp: No responde.\n")
                print("Se intentará de nuevo en 5 segundos.\n")
                time.sleep(5)

    def interpretarMensaje(self, msg):
        """
        Se interpreta el mensaje pasado por parámetro, convirtiéndolo
        en un objeto Mensaje.

        Parámetros:
        msg -- Mensaje que se tiene que interpretar

        Return:
        mensaje -- Mensaje interpretado
        """
        mensaje = Mensaje.convertirEnObjeto(msg)
        return mensaje

    def inicializarJugador(self, _cliente, id):
        """
        Se incializa un jugador, para lo que se requiere de un cliente y su id, 
        enviándole el id que se le ha asignado.

        Parámetros:
        _cliente -- Cliente en el que se encuentra el jugador
        id -- Id del jugador  
        """
               
        self.enviar_Mensaje("\n¿Desea empezar el juego?", _cliente)
        respuesta = self.recibir(_cliente)
        mensaje = self.interpretarMensaje(respuesta)

        if (mensaje.getCode() == "102"):
            if mensaje.getObj() == "1":
                print("| El jugador " + str(id) +
                      " quiere jugar.\t|\n| Se le envía el id de jugador.\t|")
                self.enviar_Mensaje_Codificado("201", str(id), _cliente)
            else:
                print("| El jugador " + str(id) +
                      " no quiere jugar.|\n| Finalizar conexión.\t\t|")

    def main(self):
        """
        Main de la clase Cliente en que se realizan las llamadas
        a las funciones de la misma.
        """
        self.ligarSocket()
        self.s.listen(2)  # 2 clientes

        print("\n\n_________________________________\n|   Esperando a los clientes\t|")

        # Inicialización de los clientes
        cliente1, direccion1 = self.conexiones()
        self.enviarId(cliente1)               # Espera conexión del 1 cliente

        cliente2, direccion2 = self.conexiones()
        self.enviarId(cliente2)              # Espera conexión del 2 cliente

        # PROBANDO LA CONEXION
        # Se le da el identificador a cada Cliente
        self.inicializarJugador(cliente1, 1)
        print("|-------------------------------|")
        self.inicializarJugador(cliente2, 2)
        print("|_______________________________|\n\n")
        arbitro = Arbitro(1, 2)

        # INICIA EL JUEGO
        cliente = cliente1  # Empieza jugando el jugador1
        mens, obj, dest = arbitro.arbitrar("103")  # Le muestra el tablero

        self.enviar_Mensaje_Codificado(
            mens, obj, cliente)  # Le envía un 202 tablero

        while not self.exit:   # Necesarios para que los hilos no mueran
            """
            Comunicación con el jugador
            """
            mensaje = self.interpretarMensaje(self.recibir(cliente))
            mens, obj, dest = arbitro.arbitrar(
                mensaje.getCode(), mensaje.getObj())

            if (mens == "200"):
                self.enviar_Mensaje_Codificado(mens, obj, cliente1)
                self.enviar_Mensaje_Codificado(mens, obj, cliente2)
                self.exit = True
            elif dest == 1:
                cliente = cliente1
                self.enviar_Mensaje_Codificado(mens, obj, cliente)
            else:
                cliente = cliente2
                self.enviar_Mensaje_Codificado(mens, obj, cliente)

        print("\nLos jugadores han terminado de jugar.\n")
        time.sleep(5)
        self.s.close()
        self.s = None

# Creación del Servidor
servidor = Servidor()
# Llamada al main
servidor.main()
