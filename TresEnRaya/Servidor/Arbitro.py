#Imports
from Tablero import Tablero
import time

#Clase Arbitro
class Arbitro:
    def __init__(self, jugador1, jugador2):
        """
        Inicializa el árbitro con dos jugadores que recibe como parámetro.
        Se crea el tablero con el que se trabajará.

        Parámetros:
        jugador1 -- Primer jugador (contiene el código para enviar mensajes)
        jugador2 -- Segundo jugador (contiene el código para enviar mensajes)
        """
        self.jugador1 = jugador1    # Primer jugador
        self.jugador2 = jugador2    # Segundo jugador
        self.tablero = Tablero()    # Tablero en el que se trabaja
        self.turno = 1              # Turno actual

    def arbitrar(self,msg,elem=None):
        # Cuando se reciba un mensaje 102 se tiene que enviar el tablero y se envia el código de 
        # mensaje 202
        #100 -- Reinicio partida
        #101 -- Fin juego
        #102 -- dibujarTablero
        #103 -- Envio de coordenadas

        # cuando haya acabado la partida esFin() == True
        #   llamar solicitud reinicio de InterfazJugador()
        #       - Si ambos quieren reiniciar (ambos código 100) llamar reiniciar()
        #       - Si uno quiere reiniciar y el otro no enviar un código para mandar
        #         salir (Cliente) al jugador que no quiere y el otro se quede esperando (un tiempo)
        #         y si no se encuentra a nadie se dice que ha finalizado la partida
        #       - Si ambos quieren salir mandar salir (Cliente)
        
        fin=0
        if(msg=="101"):
            fin = "203"
            obj = "0"
        
        if(msg=="103"):
            fin, obj = self.dibujarTablero()
        
        if(msg=="104"):
            fin, obj = self.realizarMovimiento(elem)

        if(msg=='105'):
            fin = self.esFin()
            if ( fin == self.turno):
                return  "200", str(self.turno), self.turno # Codigo fin ganando
            elif (fin == "0"):
                return "200", "0" ,self.turno# Codigo fin empate

            self.cambiarTurno()
            fin, obj = self.dibujarTablero()

        # Se devuelve el codigo de respuesta, el objeto y el turno1
        print(self.turno)
        return fin, obj, self.turno
            

    def realizarMovimiento(self, mov):
        """
        Coloca la ficha en la posición indicada por movimiento.
        Cambia de turno.

        Parámetros:
        movimiento -- Coordenadas [x,y] del destino del movimiento
        """
        movimiento = [int(mov[0])-1,int(mov[1])-1]
        
        correcto = self.comprobarMovimiento(movimiento)
        if ( correcto == 1 ):

            self.tablero.setFicha(self.turno, movimiento[0], movimiento[1])
            
            # Movimiento correcto y actualizado en el tablero
            return "204",self.tablero.dibujarTablero()

        if ( correcto == 2 ):
            print("Movimiento incorrecto")
            # TODO Volver a solicitar movimiento al mismo jugador
            return "203", "1"

        if ( correcto == 0 ):
            print("Celda ocupada")

    def comprobarMovimiento(self, movimiento):
        """
        Comprueba si el movimiento pasado por parámetros es válido.
        Para ello tiene en cuenta el jugador que ha enviado el movimiento 
        y el estado del tablero.

        Envia un mensaje al jugador:
        203 -- Movimiento incorrecto

        Parámetros:
        mov -- int "xy" del destino del movimiento

        Return: 
        int -- codigo de movimiento
        """
        #TODO : RETURN 0????
        #IMPORTANTE
        tab = self.tablero.getTablero()
        posibilidades = [0, 1, 2]

        # Si el movimiento es correcto
        if ( (movimiento[0] in posibilidades) and 
             (movimiento[1] in posibilidades) and
             (tab[movimiento[0]][movimiento[1]] == 0) ):
            return 1 # Movimiento correcto

        else: # Movimiento incorrecto
            return 2
   
    def esFin(self):
        """
        Obtiene el tablero y busca jugadas ganadoras o si el tablero está lleno.

        Return:
        int
        """
        tab = self.tablero.getTablero()

        # Líneas horizontales
        if(tab[0][0] == tab[0][1] == tab[0][2] == self.turno):
            return self.turno
        if(tab[1][0] == tab[1][1] == tab[1][2] == self.turno): 
            return self.turno
        if(tab[2][0] == tab[2][1] == tab[2][2]  == self.turno ):
            return self.turno

        # Líneas verticales
        if(tab[0][0] == tab[1][0] == tab[2][0]  == self.turno):
            return self.turno
        if(tab[0][1] == tab[1][1] == tab[2][1]  == self.turno):
            return self.turno
        if(tab[0][2] == tab[1][2] == tab[2][2]  == self.turno ):
            return self.turno

        # Diagonales
        if(tab[0][0] == tab[1][1] == tab[2][2]  == self.turno):
            return self.turno
        if(tab[2][0] == tab[1][1] == tab[0][2]  == self.turno ):
            return self.turno

        if(self.tablero.estaLleno()):
            return "0"

        return -1

    def turnoActual(self):
        """
        Devuelve al servidor el turno actual.

        Return:
        turno -- Turno actual
        """
        return self.turno

    def cambiarTurno(self):
        """
        Cambia el turno del jugador.
        """        
        if(self.turno == 1):
            self.turno = 2
        else:
            self.turno = 1

    def dibujarTablero(self):
        """
        Devuelve la representación del tablero actual y un mensaje 202 "devolver tablero"

        Return:
        202 -- mensaje de "devolver tablero"
        self.tablero.dibujarTablero() -- representación del tablero
        """ 
        return "202", self.tablero.dibujarTablero()