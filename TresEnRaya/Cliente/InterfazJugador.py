import time
from Servidor.Arbitro import Arbitro


class InterfazJugador:
    def __init__(self, _jugador):
        self.jugador = _jugador
        self.ficha = 'X' if (_jugador == 1 ) else 'O'
        self.tablero = None


    def jugar(self, msg, obj = None):
        """
        Mientras no se finalice el juego se obtiene el turno y se realiza una jugada
        102: solicitar tablero
        """
        mensajes = {
            '202': self.imprimirTablero(obj)     #Mirar como se hace
        }

    def imprimirTablero(self,_tablero):
        """
        Muestra por pantalla el tablero.
        """
        self.tablero = _tablero
        print(_tablero)

    def solicitarMov(self):
        mov=""
        mov += input('Introduce la fila: ')
        mov += " "
        mov += input('Introduce la columna: ')

        return mov


    #Meter en jugar los mensajes
    def solicitudReinicio(self):
        """
        Una vez se ha terminado el juego se pregunta si se quiere reiniciar
        Si no se quiere reiniciar, se finaliza el juego
        100: reinicio partida
        101: fin juego
        """
        print('El juego ha finalizado.')
        self.imprimirTablero(self.tablero)

        resp = input('¿Desea Iniciar una nueva partida?(1)Sí, (2)No.')
        while(resp != 1 & resp != 2):
            resp = input('Opción erronea ¿desea iniciar una nueva partida?(1)Sí, (2)No.')
        if(resp == 1):
            return 100
        else:
            return 101