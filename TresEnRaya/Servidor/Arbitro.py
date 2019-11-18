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
        if(msg=="100"):
            fin, obj = self.reiniciar()
        if(msg=="101"):
            fin = "203" # Se solicita el movimiento
            obj = "0" 

        if(msg=="103"):
            fin, obj = self.dibujarTablero()
        if(msg=="104"):
            fin, obj = self.realizarMovimiento(elem)
        # Se devuelve el codigo de respuesta, el objeto y el turno1
        return fin, obj, self.turno
            

    def realizarMovimiento(self, mov):
        """
        Coloca la ficha en la posición indicada por movimiento.
        Cambia de turno.

        Parámetros:
        movimiento -- Coordenadas [x,y] del destino del movimiento
        """
        movimiento = [int(mov[0]),int(mov[1])]
        correcto = self.comprobarMovimiento(movimiento)
        if ( correcto == 1 ):
            print("movimiento correctooooooooo")
            self.tablero.setFicha(self.turno, movimiento[0], movimiento[1])
            self.cambiarTurno()
            
        if ( correcto == 2 ):
            print("movimiento incorrectooooooo")
            # TODO Volver a solicitar movimiento al mismo jugador
            pass
        if ( correcto == 0 ):
            print("tablero llenooooooooooooooo")
            pass
            # TODO meter lo del reinicio

    def comprobarMovimiento(self, movimiento):
        """
        Obtiene un movimiento y comprueba si este es válido.
        Para ello tiene en cuenta el jugador que ha enviado el movimiento 
        y el estado del tablero.

        Envia un mensaje al jugador:
        203 -- Movimiento incorrecto

        Parámetros:
        mov -- int "xy" del destino del movimiento

        Return: 
        int -- codigo de movimiento
        """
        tab = self.tablero.getTablero()
        posibilidades = [0, 1, 2]

        # Si el movimiento es correcto
        if ( (movimiento[0] in posibilidades) and 
             (movimiento[1] in posibilidades) and
             (tab[movimiento[0]][movimiento[1]] == 0) ):
            if (self.esFin()):
                # TODO Si es fin de partida se consulta si se quiere reiniciar
                return 0 # Mensaje consultar reinicio
            return 1 # Movimiento correcto

        else: # Movimiento incorrecto
            return 2

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
        return False

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

    def dibujarTablero(self):
        return "202", self.tablero.dibujarTablero()