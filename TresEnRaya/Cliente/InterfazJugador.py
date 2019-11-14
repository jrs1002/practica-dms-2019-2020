import time
from Servidor.Arbitro import Arbitro


class InterfazJugador:
    """
    Mensajes Cliente a Servidor:
        100 -- Reinicio partida
        101 -- Fin juego
        102 -- Solicitar tablero

        Mensajes Servidor a Cliente:
        202 -- Envío del dibujo del tablero
        203 -- Movimiento incorrecto
    """

    def __init__(self, _jugador):
        """
        Método que inicializa la interfaz del jugador.

        Parámetros:
        _jugador -- Identificador de cliente
        """
        self.jugador = _jugador
        self.ficha = 'X' if (_jugador == 1 ) else 'O'
        self.tablero = None

        print('Eres el jugador' + self.jugador + ' con ficha ' + self.ficha + '.')

    def jugar(self, msg=None, obj = None):
        """
        En función del mensaje recibido se realiza una cierta acción.

        Parámetros:
        msg -- Mensaje recibido del Servidor
        obj -- Objeto recibido del Servidor
        """
        # Solicitar tablero --> Con mensaje 202 ya se va a imprimir

        # Solicitar movimiento --> Si es erroneo con mensaje 203 ya s evuelve a solicitar   
              
        if(msg != None):
            self.switch(msg, obj)  # Mirar lo del objeto

    def switch(self, msg, obj=None):
        """
        Función que define el switch para saber qué hacer en función del
        mensaje recibido.

        Parámetros:
        msg -- Mensaje recibido del Servidor
        obj -- Objeto recibido del Servidor

        Return:
        Acción a realizar
        """
        mensajes = {
             '202' : self.imprimirTablero(obj),       #Mirar como se hace
             '203' : self.solicitarMov()             # Si el movimiento es incorrecto volver a solicitar
        }

        return mensajes.get(msg)
    
    def imprimirTablero(self,_tablero):
        """
        Muestra por pantalla el tablero.

        Parámetros:
        _tablero -- Representación del tablero
        """
        self.tablero = _tablero
        print(_tablero)


    def solicitarMov(self):
        """
        Se solicita al jugador el movimiento.
        Se devuelve como un string "xy".

        Return:
        mov -- String con el movimiento introducido
        """
        mov = ""
        mov += input('Introduce la fila: ')
        mov += input('Introduce la columna: ')

        return mov

    #Meter en jugar los mensajes
    def solicitudReinicio(self):
        """
        Una vez se ha terminado el juego se pregunta si se quiere reiniciar
        Si no se quiere reiniciar, se finaliza el juego

        Return: 
        String -- Mensaje que envía el Cliente al Servidor
        """
        print('El juego ha finalizado.')
        self.imprimirTablero(self.tablero)

        resp = input('¿Desea Iniciar una nueva partida? (1)Sí, (2)No.')

        while(resp != 1 & resp != 2):
            resp = input('Opción erronea ¿desea iniciar una nueva partida? (1)Sí, (2)No.')

        if(resp == 1):
            return 100
        else:
            return 101