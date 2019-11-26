import time

# Clase InterfazJugador
"""
Capa de presentación
Encargada de comunicarse con el jugador
"""
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

        print('| Eres el jugador ' + str(self.jugador) +
              '\t\t|\n|con ficha ' + self.ficha + '\t\t\t|')

    def jugar(self, msg, elem=None):
        """
        En función del mensaje recibido se realiza una cierta acción.

        Si no se requiere ningún objeto se devolverá 0.

        Parámetros:
        msg -- Mensaje recibido del Servidor
        elem -- Objeto recibido del Servidor

        Return:
        fin -- Código del mensaje a devolver en función de la acción realizada
        obj -- Objeto del mensaje a devolver en función de la acción realizada
        """
        # Solicitar salir del juego
        if (msg == '200'):
            self.mostrarResultado(elem)
            return '100', '0'

        # Solicitar tablero --> Con mensaje 202 ya se va a imprimir
        if (msg == '202'):
            print("\n\n")
            fin, obj = self.imprimirTablero(elem)

        # Solicitar movimiento --> Si es erróneo con mensaje 203 ya se vuelve a solicitar
        if (msg == '203'):
            if (elem == '1'):
                print("\nMovimiento incorrecto, introduzca un nuevo movimiento.\n")
            fin, obj = self.solicitarMov()

        if (msg == '204'):
            fin, obj = self.imprimirTablero(elem)
            print("\n\n")
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

    def imprimirTablero(self, tablero):
        """
        Se muestra por pantalla el tablero.

        Parámetros:
        _tablero -- Representación del tablero
        """
        # TODO cambiaro por la instancia del tablero 
        # añadir un nuevo constructor a tablero
        x = '    1    2    3 \n'
        for i in range(3):
            x += '   +---+---+---+\n' + str(i+1) + '  | '
            for j in range(3):

                if(tablero[i][j] == 0):
                    x += ' '

                elif(tablero[i][j] == 1):
                    x += 'X'
                else:
                    x += 'O'
                x += ' | '

            x += '\n'
        x += '   +---+---+---+'
        print(x)
        return "101", "0"  # Código DONE (tablero impreso)

    def solicitarMov(self):
        """
        Se solicita al jugador el movimiento.

        Return:
        int -- Código de mensaje
        mov -- Coordenadas xy del movimiento
        """
        posibles = [1,2,3]
        while True:
            x = input('Introduce la fila: ')
            y = input('Introduce la columna: ')
            if (int(x) in posibles and int(y) in posibles):
                break
            else:
                print(" ** Movimientos fuera de rango **")
        mov = [int(x),int(y)]
        return "104", mov