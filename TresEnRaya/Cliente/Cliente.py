# Imports
from socket import *
import time
import json
import sys
sys.path.append('..')
sys.path.append('../Biblioteca')
from _thread import *
from InterfazJugador import InterfazJugador
from Biblioteca import Mensaje

"""
Clase de Capa de Comunicaciones.

Envía al Servidor lo que devuelve el IntermediarioCliente.
Pasa a IntermediarioCliente lo que recibe del Servidor.
"""
class Cliente:
    def __init__(self):
        """
        Método que inicializa el Cliente.
        Se inicializan las variables.
        Se crea el socket.
        Se establecen el host y el puerto.
        """
        self.client = ""
        self.s = socket(AF_INET, SOCK_STREAM)
        self.host = "0.0.0.0"
        self.port = 9494
        self.exit = False

    def __del__(self):
        """
        Se destruyen los socket que no son nulos al final de la ejecución.
        """
        if self.s == None:
            self.s = None

    def conectarse(self):
        """
        Se conecta el socket con el puerto y host pasados por parámetro.
        """
        self.s.connect((self.host, self.port))

    def intentoConexion(self):
        """
        Si el puerto no esta siendo usado y la dirección pasada
        es correcta, se conecta al servidor.
        """
        while True:
            print("\n\n_________________________________")
            print("| Intentando conectarse a: \t|\n|\t",
                  self.host + ":" + str(self.port) + "\t\t|")
            try:
                self.conectarse()
                break
            except:
                print("\nNo hay servidor en: ",
                      self.host + ":" + str(self.port))
                print("Se intentará de nuevo en 5 segundos.\n")
                time.sleep(5)

    def enviar(self, msg):
        """
        Se realiza el envio de mensajes de Cliente a Servidor.

        Parámetros:
        msg -- Mensaje a enviar
        """
        while True:
            try:
                self.s.send(msg.encode("UTF-8"))
                break
            except:
                print("\nERROR\n")
                print("Se intentará de nuevo en 5 segundos.\n")
                time.sleep(5)

    def enviar_Mensaje_Codificado(self, cod, obj):
        """
        Se crea un objeto Mensaje con el código de mensaje y el objeto
        pasados por parámetro y se lo envia al Servidor.

        Parámetros:
        cod -- Código del mensaje
        obj -- Objeto del mensaje
        """
        while True:
            try:
                mensaje = Mensaje(cod, obj)
                cadena = mensaje.convertirEnCadena()
                self.s.send(cadena.encode("UTF-8"))
                break

            except:
                print("\nSend_esp: No responde.\n")
                print("Se intentará de nuevo en 5 segundos.\n")
                time.sleep(5)

    def recibir(self):
        """
        Se gestionan los mensajes recibidos del Servidor. 
        """
        while True:
            try:
                reply = self.s.recv(2048)
                return reply.decode("UTF-8")
            except:
                input("\nPulse para refrescar.")

    def recibirId(self):
        """
        Se recibe el número asignado al cliente y se le asigna.
        """
        # Recibe el identificador del cliente
        self.client = self.s.recv(2048).decode("UTF-8")

        print("|Cliente " + self.client + "\t\t\t|")

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

    def inicializarJugador(self):
        """
        Se incializa un jugador, para lo que se requiere de un cliente y su id.

        Return:
        InterfazJugador(idJugador) -- Instancia de la clase InterfazJugador con 
                                      el jugador correspondiente
        """
        print("|-------------------------------|")
        print("|"+self.recibir()+"\t|")   # Se pregunta al jugador si quiere iniciar el juego
        respuesta = input()
        mensaje = Mensaje("102", str(respuesta))
        cadena = mensaje.convertirEnCadena()
        self.enviar(cadena)

        mensaje = self.interpretarMensaje(self.recibir())

        if(mensaje.getCode() == "201"):
            idJugador = int(mensaje.getObj())
            return InterfazJugador(idJugador)

    def main(self):
        """
        Main de la clase Cliente en que se realizan las llamadas
        a las funciones de la misma.
        """
        self.intentoConexion()
        self.recibirId()
        print("| Conexión establecida.\t\t|")
        print("| El servidor es: ", self.host+":"+str(self.port)+"\t|")

        jugador = self.inicializarJugador()
        print("|_______________________________|\n\n")

        while not self.exit:   # Necesarios para que los hilos no mueran
            """
            Comuniación con el jugador.
            """
            mensaje = self.interpretarMensaje(self.recibir())
            cod, obj = jugador.jugar(mensaje.getCode(), mensaje.getObj())
            # Se convierte el objeto devuelto por jugar a str
            # json.dumps(objeto) que te lo devuelve en str
            if (cod == '100'):
                self.exit = True
            else:
                self.enviar_Mensaje_Codificado(cod, obj)

        print("\nTe esperamos pronto!")
        time.sleep(5)
        self.s.close()
        self.s = None

# Se crea el Cliente
cliente = Cliente()
# Llamada al main
cliente.main()
