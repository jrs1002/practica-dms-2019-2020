from Tablero import Tablero
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

    def arbitrar(self,msg,obj):
        """
        Mientras no se haya terminado el juego, se queda a la espera de mensajes.
        """
        
        # Cuando se reciba un mensaje 102 se tiene que enviar el tablero y se envia el código de 
        # mensaje 202
        #100 -- Reinicio partida
        #101 -- Fin juego
        #103 -- Envio de coordenadas

        # cuando haya acabado la partida esFin() == True
        #   llamar solicitud reinicio de InterfazJugador()
        #       - Si ambos quieren reiniciar (ambos código 100) llamar reiniciar()
        #       - Si uno quiere reiniciar y el otro no enviar un código para mandar
        #         salir (Cliente) al jugador que no quiere y el otro se quede esperando (un tiempo)
        #         y si no se encuentra a nadie se dice que ha finalizado la partida
        #       - Si ambos quieren salir mandar salir (Cliente)
        if(msg=="102"):
            return self.tablero.dibujarTablero()
        if(msg=="100"):
            return self.tablero.reiniciar()
        if(msg=="101"):
            return self.tablero.esFin()
        if(msg=="103"):
            return self.tablero.comprobarMovimiento()
             
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
        if(self.turnoActual == 1):
            self.turno = 2
        else:
            self.turno = 1

    def esFin(self):
        """
        Obtiene el tablero y busca jugadas ganadoras o si el tablero está lleno.

        Return:
        Bool -- True si se ha acabado el juego, False si no
        """
        tab = self.tablero.getTablero()

        if(tab[0][0] == tab[0][1] == tab[0][2] | tab[1][0] == tab[1][1] == tab[1][2] | tab[2][0] == tab[2][1] == tab[2][2]):
            return True

        if(tab[0][0] == tab[1][0] == tab[2][0] | tab[0][1] == tab[1][1] == tab[2][1] | tab[0][2] == tab[1][2] == tab[2][2]):
            return True

        if(tab[0][0] == tab[1][1] == tab[1][2] | tab[2][0] == tab[1][1] == tab[0][2]):
            return True

        if(self.tablero.estaLleno()):
            return True

        self.fin = False

    def comprobarMovimiento(self, mov):
        """
        Obtiene un movimiento y comprueba si este es válido.
        Para ello tiene en cuenta el jugador que ha enviado el movimiento 
        y el estado del tablero.

        Envia un mensaje al jugador:
        203 -- Movimiento incorrecto

        Parámetros:
        mov -- String "xy" del destino del movimiento

        Return: 
        String -- Mensaje que envía el Servidor al Cliente
        """
        # Convertimos el string movimiento a un array 
        movimiento = [int(mov[0]),int(mov[1])]

        tab = self.tablero.getTablero()
        posibilidades = [0, 1, 2]

        # Si el movimiento es correcto
        if (movimiento[0] in posibilidades & movimiento[1] in posibilidades & tab[movimiento[0]][movimiento[1]] == 0):
            self.realizarMovimiento(movimiento)
            self.esFin()

            # Si es fin de partida se consulta si se quiere reiniciar
            if (self.esFin()):
                return 0 # Mensaje consultar reinicio

        # Si el movimiento es incorrecto se manda un mensaje al cliente para volver
        # a solicitarlo
        else:
            return '203'    # Mirar

    def realizarMovimiento(self, movimiento):
        """
        Coloca la ficha en la posición indicada por movimiento.
        Cambia de turno.

        Parámetros:
        movimiento -- Coordenadas [x,y] del destino del movimiento
        """
        self.tablero.setFicha(self.turno, movimiento[0], movimiento[1])
        self.cambiarTurno()

    def reiniciar(self):
        """
        Se reinicia el juego.
        """
        # TODO julen: yo cambiaría este bucle por un método iniciarTablero en tablero
        
        for i in range(3):
            for j in range(3):
                self.tablero.setFicha(0, i, j)
        self.fin = False
        self.turno = 1

   