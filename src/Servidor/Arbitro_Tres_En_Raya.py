# Imports
import time
import sys
sys.path.append('..')
sys.path.append('../Biblioteca')
from Tablero import Tablero
from Pieza import Pieza
from Arbitro_Abstracto import Arbitro_Abstracto

# Clase Arbitro del Tres en Raya
class Arbitro_Tres_En_Raya(Arbitro_Abstracto):
     def __init__(self, _jugador1, _jugador2):
        """
        Se inicializa el árbitro con los jugadores que recibe como parámetro.
        Se instancia el tablero con el que se trabajará.
        Se establece el turno que empieza (jugador 1)

        Parámetros:
        jugador1 -- Primer jugador (contiene el código para enviar mensajes)
        jugador2 -- Segundo jugador (contiene el código para enviar mensajes)
        """
        super().__init__(_jugador1, _jugador2)
        self.tablero = Tablero(3,3)     # Tablero en el que se trabaja

     def turnoActual(self):
        """
        Se devuelve el turno actual,para ello, se llama a la función turnoActual del padre (Arbitro_Abstracto)
        """
        #Arbitro_Abstracto.turnoActual(self)
        super().turnoActual()

     def cambiarTurno(self):
        """
        Se cambia el turno del jugador,para ello, se llama a la función cambiarTurno del padre (Arbitro_Abstracto)
        """
        #Arbitro_Abstracto.cambiarTurno(self)
        super().cambiarTurno()

     def dibujarTablero(self):
        """
        Se devuelve la representación del tablero actual.

        Return:
        self.tablero.tableroToArray() -- Representación del tablero
        """
        return self.tablero.tableroToArray()

     def realizarMovimiento(self, mov):
        """
        Se comprueba si el movimiento pasado por parámetro es correcto.
        Si lo es, se coloca la ficha en la posición indicada por el movimiento.
        Se cambia de turno.

        Parámetros:
        mov -- Coordenadas xy con el destino del movimiento
        """
        movimiento = [mov[0]-1, mov[1]-1]

         # Movimiento correcto y actualizado en el tablero
        if (self.comprobarMovimiento(movimiento)):
            self.tablero.setPieza(Pieza(self.turno), movimiento[0], movimiento[1])
            return True, self.tablero.getTablero()
        
        # Movimiento incorrecto, vuelve a solicitar el movimiento al jugador
        else:
            return False,0

     def comprobarMovimiento(self, mov):
        """
        Se comprueba si el movimiento pasado por parámetros es válido.
        Para ello tiene en cuenta el jugador que ha enviado el movimiento 
        y el estado del tablero.

        Parámetros:
        mov -- [x,y] del destino del movimiento

        Return: 
        bool -- booleano que indica si es correcto o no
        """
        tab = self.tablero.getTablero()

        # Si el movimiento es correcto
        if (mov[0] < tab.getTamX() and mov[1] < tab.getTamY() and
            tab[mov[0]][mov[1]] == None and mov[0]>0 and mov[1]>0) :
            return True  # Movimiento correcto

        else:  # Movimiento incorrecto
            return False

     def esFin(self):
        """
        Se obtiene el tablero y busca jugadas ganadoras o si el tablero está lleno.

        Return:
        int -- Entero con el turno del ganador o 0 si es empate 
        """
        tab = self.tablero.getTablero()

        # Líneas horizontales
        if(tab[0][0] == tab[0][1] == tab[0][2] == self.turno):
            return self.turno
        if(tab[1][0] == tab[1][1] == tab[1][2] == self.turno):
            return self.turno
        if(tab[2][0] == tab[2][1] == tab[2][2] == self.turno):
            return self.turno

        # Líneas verticales
        if(tab[0][0] == tab[1][0] == tab[2][0] == self.turno):
            return self.turno
        if(tab[0][1] == tab[1][1] == tab[2][1] == self.turno):
            return self.turno
        if(tab[0][2] == tab[1][2] == tab[2][2] == self.turno):
            return self.turno

        # Diagonales
        if(tab[0][0] == tab[1][1] == tab[2][2] == self.turno):
            return self.turno
        if(tab[2][0] == tab[1][1] == tab[0][2] == self.turno):
            return self.turno

        if(self.tablero.estaLleno()):
            return "0"

        return -1

    
