# Imports
from Tablero import Tablero
import time

# Clase Arbitro
class Arbitro:
    def __init__(self, _jugador1, _jugador2):
        """
        Se inicializa el árbitro con los jugadores que recibe como parámetro.
        Se instancia el tablero con el que se trabajará.
        Se establece el turno que empieza (jugador 1)

        Parámetros:
        jugador1 -- Primer jugador (contiene el código para enviar mensajes)
        jugador2 -- Segundo jugador (contiene el código para enviar mensajes)
        """
        self.jugador1 = _jugador1    # Primer jugador
        self.jugador2 = _jugador2    # Segundo jugador
        self.tablero = Tablero()     # Tablero en el que se trabaja
        self.turno = 1               # Turno actual

    def arbitrar(self, msg, elem=None):
        """
        En función del mensaje recibido se realiza una cierta acción.

        Parámetros:
        msg -- Mensaje recibido del Cliente
        elem -- Objeto recibido del Cliente

        Return:
        fin -- Código del mensaje a devolver en función de la acción realizada
        obj -- Objeto del mensaje a devolver en función de la acción realizada
        turno -- Turno actual
        """
        fin = 0
        # Tablero pintado en InterfazJugador --> solicitarMov
        if(msg == "101"):
            fin = "203"
            obj = "0"

        # Solicitar tablero
        if(msg == "103"):
            fin, obj = self.dibujarTablero()

        # Movimiento a realizar
        if(msg == "104"):
            fin, obj = self.realizarMovimiento(elem)

        # Se ha realizado el movimiento y se ha actualizado el tablero
        if(msg == '105'):
            fin = self.esFin()
            if (fin == self.turno):
                return "200", str(self.turno), self.turno  # Codigo fin ganando
            elif (fin == "0"):
                return "200", "0", self.turno  # Codigo fin empate

            self.cambiarTurno()
            fin, obj = self.dibujarTablero()

        # Se devuelve el codigo de respuesta, el objeto y el turno
        return fin, obj, self.turno

    def realizarMovimiento(self, mov):
        """
        Se comprueba si el movimiento pasado por parámetro es correcto.
        Si lo es, se coloca la ficha en la posición indicada por el movimiento.
        Se cambia de turno.

        Parámetros:
        mov -- Coordenadas xy con el destino del movimiento
        """
        movimiento = [mov[0]-1, mov[1]-1]

        correcto = self.comprobarMovimiento(movimiento)

         # Movimiento correcto y actualizado en el tablero
        if (correcto == 1):
            self.tablero.setFicha(self.turno, movimiento[0], movimiento[1])
            return "204", self.tablero.getTablero()
        
        # Movimiento incorrecto, vuelve a solicitar el movimiento al jugador
        if (correcto == 2 ):
            return "203", "1"

    def comprobarMovimiento(self, mov):
        """
        Se comprueba si el movimiento pasado por parámetros es válido.
        Para ello tiene en cuenta el jugador que ha enviado el movimiento 
        y el estado del tablero.

        Parámetros:
        mov -- [x,y] del destino del movimiento

        Return: 
        int -- Entero que indica si es correcto o no
        """
        tab = self.tablero.getTablero()
        posibilidades = [0, 1, 2]

        # Si el movimiento es correcto
        if ((mov[0] in posibilidades) and
            (mov[1] in posibilidades) and
                (tab[mov[0]][mov[1]] == 0)):
            return 1  # Movimiento correcto

        else:  # Movimiento incorrecto
            return 2

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

    def turnoActual(self):
        """
        Se devuelve el turno actual.

        Return:
        turno -- Turno actual
        """
        return self.turno

    def cambiarTurno(self):
        """
        Se cambia el turno del jugador.
        """
        if(self.turno == 1):
            self.turno = 2
        else:
            self.turno = 1

    def dibujarTablero(self):
        """
        Se devuelve la representación del tablero actual y un 
        código mensaje 202 "devolver tablero"

        Return:
        int -- Código del mensaje de "devolver tablero"
        self.tablero.dibujarTablero() -- Representación del tablero
        """
        return "202", self.tablero.getTablero()
