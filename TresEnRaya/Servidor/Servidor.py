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
def ini():
    host = "0.0.0.0"
    port = 9494
    return host, port

def crearSocket():
    s = socket(AF_INET, SOCK_STREAM)
    return s

def ligarSocket(s, host, port):
    while True:
        try:
            s.bind((host, port))
            break
        except error as e:
            print("ERROR:", e)

def conexiones(s):
    cliente, direccion = s.accept()
    print("\nConexión establecida.\nEl cliente es:", direccion[0] + ":" + str(direccion[1])+"\n")
    return cliente, direccion

def recibir(cliente):
    while True:
        try:
          reply = cliente.recv(2048)
          return reply.decode("UTF-8")
          break
        except:
            print("\nRecv: No responde, se intentará en 5 seg\n")
            time.sleep(5)

def enviarEspecial(cliente):
    global lista_de_clientes,client
    client = lista_de_clientes.pop()
    cliente.send(client.encode("UTF-8")) #Envia al cliente su nº de cliente(1 o 2)

def enviar_Mensaje(mensaje,cliente): #Para enviar mensajes Servidor->Cliente
        try:
            cliente.send(mensaje.encode("UTF-8"))
        except:
            print("\nSend: No responde, se intentará en 5 seg")
            time.sleep(5)

def interpretarMensaje(msg):
    if (len(msg) > 3):
        msg = msg.split("***")
        return msg[0], msg[1]

def inicializarJugador(cliente, id):
    """
    Se incializa un jugador, para ello se requiere de un cliente y su id

    Parámetros:
    cliente -- cliente en el que se encuentra el jugador
    id      -- id del jugador  
    """
    enviar_Mensaje("¿Desea empezar el juego?",cliente)
    respuesta = recibir(cliente)
    cod, obj = interpretarMensaje(respuesta)

    if (cod == "102"):
        if obj == "1":
            print("El jugador " + str(id) + " quiere jugar, se le envía el código de jugador")
            enviar_Mensaje("201***"+str(id),cliente) 
        else: 
            # TODO añadir finalización de conexión
            print("El jugador " + str(id) + " no quiere jugar, finalizar conexión")

#VARIABLES GLOBALES
exit = False      # Utilizada en la desconexion/conexion de clientes

lista_de_clientes = ["2","1"]   # El servidor le asigna un numero a los clientes segun esta lista

client = ""     # Numero del cliente

#MAIN
def main():

    global exit
    host,port = ini()
    s = crearSocket()
    ligarSocket(s, host,port)
    s.listen(2)     #2 clientes

    print("\nEsperando por los clientes")

    # Se inicializan los clientes 
    cliente1,direccion1 = conexiones(s)
    enviarEspecial(cliente1)               # Espero conexion del 1 cliente

    cliente2,direccion2 = conexiones(s)
    enviarEspecial(cliente2)              # Espero conexion del 2 cliente

    # PROBANDO LA CONEXION
    # Le damos el identificador a cada Cliente
    inicializarJugador(cliente1,1)
    inicializarJugador(cliente2,2)
    
    arbitro = Arbitro(1,2)    

    # INICIA EL JUEGO
    cliente = cliente1 # Empieza jugando el jugador1
    mens,obj,dest = arbitro.arbitrar("103") # Le muestra el tablero
    enviar_Mensaje(mens+"***"+obj,cliente)  # Le envia un 202 tablero


    while not exit:   # Necesarios para que los hilos no mueran
        """
        Aqui tendremos que meter la comunicación con jugador
        recibir mensaje
        pasarselo a jugador
        enviar respuesta
        """
        mens, obj = interpretarMensaje(recibir(cliente))
        print(mens,obj)
        mens, obj, dest = arbitro.arbitrar(mens,obj)
        # if mens = finalizar : exit = True

        # Cuando cambie dest, se cambia el turno
        cliente = cliente1 if dest==1 else cliente2
        enviar_Mensaje(mens+"***"+obj,cliente)

#Llamada al main
main()
