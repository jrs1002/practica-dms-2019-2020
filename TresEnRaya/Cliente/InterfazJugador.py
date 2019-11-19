import time

class InterfazJugador:

    def __init__(self, _jugador):
        """
        Método que inicializa la interfaz del jugador.

        Parámetros:
        _jugador -- Identificador de cliente
        """
        self.jugador = _jugador
        self.ficha = 'X' if (_jugador == 1 ) else 'O'

        print('Eres el jugador' + str(self.jugador) + ' con ficha ' + self.ficha + '.')

    def jugar(self, msg, obj = None):
        """
        En función del mensaje recibido se realiza una cierta acción.

        Parámetros:
        msg -- Mensaje recibido del Servidor
        obj -- Objeto recibido del Servidor
        
        Return:
        fin -- Objeto a devolver
        """
        # Solicitar tablero --> Con mensaje 202 ya se va a imprimir
        # Si no se requiere ningún objeto se devolverá 0
        if (msg == '200'):
            self.mostrarResultado(obj)
            return '100','0'
            
        if (msg == '202'): 
            fin, obj = self.imprimirTablero(obj)      
        
        # Solicitar movimiento --> Si es erroneo con mensaje 203 ya se vuelve a solicitar   
        if (msg == '203'): 
            if (obj == '1'):
                print("\nMovimiento incorrecto, introduzca un nuevo movimiento\n")
            fin, obj = self.solicitarMov()
        
        if (msg == '204'): 
            fin, obj = self.imprimirTablero(obj)  
            fin = '105'

        return fin, obj

    def mostrarResultado(self,obj):
        if (obj == "0"):
            print("\n****** HAS EMPATADO ******\n")
        elif (obj == str(self.jugador)):
            print("\n****** HAS GANADO  ******\n")
        else:
            print("\n****** HAS PERDIDO  ******\n")


    def imprimirTablero(self,tablero):
        """
        Muestra por pantalla el  tablero.

        Parámetros:
        _tablero -- Representación del tablero
        """
        print(tablero)

        return "101","0" # Código DONE (tablero impreso)

    def solicitarMov(self):
        """
        Se solicita al jugador el movimiento.
        Se devuelve como un string "xy".

        Return:
        mov -- String con el movimiento introducido
        """
        mov =  input('Introduce la fila: ')
        mov += input('Introduce la columna: ')
        return "104", mov

    """
    def solicitudReinicio(self):
        Una vez se ha terminado el juego se pregunta si se quiere reiniciar
        Si no se quiere reiniciar, se finaliza el juego

        Return: 
        String -- Mensaje que envía el Cliente al Servidor
    
        print('El juego ha finalizado.')
        self.imprimirTablero(self.tablero)

        resp = input('¿Desea Iniciar una nueva partida? (1)Sí, (2)No.')

        while(resp != 1 & resp != 2):
            resp = input('Opción erronea ¿desea iniciar una nueva partida? (1)Sí, (2)No.')

        if(resp == 1):
            return 100
        else:
            return 101
    """