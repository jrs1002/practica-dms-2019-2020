import time

# Clase InterfazJugador
class InterfazJugador:

    def __init__(self, _jugador):
        """
        Método que inicializa la interfaz del jugador.
        Se establece el jugador (id) pasado por parámetro. 
        Se establece ficha en función del id.
        Se muestra un mensaje al jugador indicándole qué jugador es
        y qué ficha tiene.

        Parámetros:
        _jugador -- Identificador de cliente
        """
        self.jugador = _jugador
        self.ficha = 'X' if (_jugador == 1) else 'O'

        print('\nEres el jugador ' + str(self.jugador) +
              ' con ficha ' + self.ficha + '.')

    def jugar(self, msg, elem=None):
        """
        En función del mensaje recibido se realiza una cierta acción.

        Parámetros:
        msg -- Mensaje recibido del Servidor
        elem -- Objeto recibido del Servidor

        Return:
        fin -- Código del mensaje a devolver en función de la acción realizada
        obj -- Objeto del mensaje a devolver en función de la acción realizada
        """

        if (msg == '200'):
            self.mostrarResultado(elem)
            return '100', '0'

        # Solicitar tablero --> Con mensaje 202 ya se va a imprimir
        # Si no se requiere ningún objeto se devolverá 0
        if (msg == '202'):
            fin, obj = self.imprimirTablero(elem)

        # Solicitar movimiento --> Si es erroneo con mensaje 203 ya se vuelve a solicitar
        if (msg == '203'):
            if (obj == '1'):
                print("\nMovimiento incorrecto, introduzca un nuevo movimiento.\n")
            fin, obj = self.solicitarMov()

        if (msg == '204'):
            fin, obj = self.imprimirTablero(elem)
            fin = '105'

        return fin, obj

    def mostrarResultado(self, obj):
        """
        Se muestra el resultado de la partida al jugador.

        Parámetros:
        obj -- Resultado de la partida
        """
        if (obj == "0"):
            print("\n****** HAS EMPATADO ******\n")
        elif (obj == str(self.jugador)):
            print("\n****** HAS GANADO  ******\n")
        else:
            print("\n****** HAS PERDIDO  ******\n")

    def imprimirTablero(self, _tablero):
        """
        Se muestra por pantalla el tablero.

        Parámetros:
        _tablero -- Representación del tablero
        """
        print(_tablero)

        return "101", "0"  # Código DONE (tablero impreso)

    def solicitarMov(self):
        """
        Se solicita al jugador el movimiento.
        Se devuelve como un string "xy".

        Return:
        int -- Código de mensaje
        mov -- String con el movimiento introducido
        """
        mov = input('Introduce la fila: ')
        mov += input('Introduce la columna: ')
        return "104", mov
