from Servidor.Tablero import Tablero
import time


class Arbitro:
    def __init__(self, jugador1, jugador2):
        """
        Inicializa el árbitro con dos jugadores que recibe como parámetro.
        Se crea el tablero con el que se trabajará.

        Param:
        jugador1 -- Primer jugador (contiene el código para enviar mensajes)
        jugador2 -- Segundo jugador (contiene el código para enviar mensajes)
        """
        self.jugador1 = jugador1    # Primer jugador
        self.jugador2 = jugador2    # Segundo jugador
        self.tablero = Tablero()    # Tablero en el que se trabaja
        self.fin = False            # Juego finalizado
        self.turno = 1              # Turno actual
        self.mensaje = None         # Último mensaje recibido

    def arbitrar(self):
        """
        Mientras no se haya terminado el juego, se queda a la espera de mensajes.
        """
        while(not self.fin):
            self.esperarMensaje()

    def comprobarMovimiento(self, movimiento):
        """
        Obtiene un movimiento y comprueba si este es válido.
        Para ello tiene en cuenta el jugador que ha enviado el movimiento 
        y el estado del tablero.

        Envia un mensaje al jugador:
        207 -- Movimiento correcto
        201 -- Movimiento incorrecto

        Parámetros:
        movimiento -- Coordenadas [x,y] del destino del movimiento
        """
        tab = self.tablero.getTablero()
        posibilidades = [0, 1, 2]

        if (movimiento[0] in posibilidades & movimiento[1] in posibilidades & tab[movimiento[0]][movimiento[1]] == 0):
            self.realizarMovimiento(movimiento)
            self.esFin()

            if (self.fin):
                self.consultarReinicio()

            elif (self.turno == 1):
                self.enviarMensaje(self.jugador1, '207')

            else:
                self.enviarMensaje(self.jugador2, '207')

        else:
            if (self.turno == 1):
                self.enviarMensaje(self.jugador1, '201')
            else:
                self.enviarMensaje(self.jugador2, '201')

    def realizarMovimiento(self, movimiento):
        """
        Obtiene una posición y coloca la ficha del turno correspondiente.
        El movimiento ha de ser validado previamente.

        Parámetros:
        movimiento -- Coordenadas [x,y] del destino del movimiento
        """
        self.tablero.setFicha(self.turno, movimiento[0], movimiento[1])

        if (self.turno == 1):
            self.turno = 2
        else:
            self.turno = 1

    def esFin(self):
        """
        Obtiene el tablero y busca jugadas ganadoras.
        Si la encuentra, devuelve True, si no False.
        """
        tab = self.tablero.getTablero()
        if(tab[0][0] == tab[0][1] == tab[0][2] | tab[1][0] == tab[1][1] == tab[1][2] | tab[2][0] == tab[2][1] == tab[2][2]):
            self.fin = True

        if(tab[0][0] == tab[1][0] == tab[2][0] | tab[0][1] == tab[1][1] == tab[2][1] | tab[0][2] == tab[1][2] == tab[2][2]):
            self.fin = True

        if(tab[0][0] == tab[1][1] == tab[1][2] | tab[2][0] == tab[1][1] == tab[0][2]):
            self.fin = True

        self.fin = False

    def turnoActual(self):
        """
        Devuelve al servidor el turno actual.
        """
        return self.turno

    def reiniciar(self):
        """
        Se reinicia el juego
        """
        for i in range(3):
            for j in range(3):
                self.tablero.setFicha(0, i, j)
                self.fin = False
                self.turno = 1

   