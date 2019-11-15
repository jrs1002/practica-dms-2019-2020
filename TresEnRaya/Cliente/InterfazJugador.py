import time


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
        self.tablero = None # Se almacena el último tablero recibido del servidor

        print('Eres el jugador' + str(self.jugador) + ' con ficha ' + self.ficha + '.')

    def jugar(self, msg=None, obj = None):
        """
        En función del mensaje recibido se realiza una cierta acción.

        Parámetros:
        msg -- Mensaje recibido del Servidor
        obj -- Objeto recibido del Servidor
        
        Return:
        fin -- Objeto a devolver
        """
        # Solicitar tablero --> Con mensaje 202 ya se va a imprimir

        # Solicitar movimiento --> Si es erroneo con mensaje 203 ya se vuelve a solicitar   
      
        fin = 0 # Si no se requiere ningún objeto se devolverá 0
        
        if (msg == '202'): self.imprimirTablero(obj)
        if (msg == '203'): fin = self.solicitarMov()

        return fin

    
    def imprimirTablero(self,_tablero):
        """
        Muestra por pantalla el  tablero.

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
        mov =  input('Introduce la fila: ')
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