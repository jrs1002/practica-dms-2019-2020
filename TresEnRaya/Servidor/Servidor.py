#!/urs/bin/python
#-*- coding: utf-8 -*-

#Importaciones
from socket import *
from _thread import *
import time
import sys
from Tablero import Tablero

#FUNCIONES
def ini():
    host = "0.0.0.0"
    port = 9797
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
        global bandera
        try:
            reply = cliente.recv(2048)
            reply = reply.decode("UTF-8")

            if reply[0] == "1":
                print("Cliente", reply)

            elif reply[0] == "2":
                print("Cliente", reply)

            else:
                lista_de_clientes.append(reply[4])
                print("\nEl cliente "+reply[4]+" se ha ido")
                bandera = True
                break
        except:
            print("\nNo responde")
            print("Se intentará en 5 seg\n")
            time.sleep(5)

def enviarEspecial(cliente):
    global lista_de_clientes,client
    client = lista_de_clientes.pop()
    cliente.send(client.encode("UTF-8")) #Envia al cliente su nº de cliente(1 o 2)

def enviar_Mensaje(mensaje,cliente): #Para enviar mensajes Servidor-Cliente
        try:
            cliente.send(mensaje.encode("UTF-8"))
        except:
            print("\nError: no se ha enviado el mensaje")
            print("Se intentará en 5 seg\n")
            time.sleep(5)

#VARIABLES GLOBALES
bandera = False      # Utilizada en la desconexion/conexion de clientes

lista_de_clientes = ["2","1"]   # El servidor le asigna un numero a los clientes segun esta lista

client = ""     # Numero del cliente

#MAIN
def main():

    global bandera
    host,port = ini()
    s = crearSocket()
    ligarSocket(s, host,port)
    s.listen(2)     #2 clientes

    print("\nEsperando por los clientes")

    # Se inicializan los clientes 
    cliente1,direccion1 = conexiones(s)
    enviarEspecial(cliente1)               # Espero conexion del 1 cliente
    start_new_thread(recibir,(cliente1,)) #Para que coja los mensajes de los dos hilos de forma concurrente

    cliente2,direccion2 = conexiones(s)
    enviarEspecial(cliente2)              # Espero conexion del 2 cliente
    start_new_thread(recibir,(cliente2,))#Para que coja los mensajes de los dos hilos de forma concurrente

    # PROBANDO LA CONEXION
    tablero=Tablero()
    celdas=tablero.getTablero()
    enviar_Mensaje(str(celdas),cliente1)
     
    
    # En caso de desconectarse un cliente,esperara a que otro vuelve a conectarse
    while True: 
        if bandera != True:     
            cliente3,direccion3 = conexiones(s)
            enviarEspecial(cliente3)
            start_new_thread(recibir,(cliente3,))
            bandera = False

#Llamada al main
main()
