# Imports
import time
from Biblioteca import Pieza

"""
Clase de Capa de Presentación.

Encargada de comunicarse con el jugador.
"""
class InterfazJugador:

    def __init__(self, _id):
        """
        Método que inicializa la interfaz del jugador.
        Se establece el jugador (id) pasado por parámetro. 
        Se establece ficha en función del id.
        Se muestra un mensaje al jugador indicándole qué jugador es
        y qué ficha tiene.

        Parámetros:
        _id -- Identificador de cliente
        """
        self.id = _id

        """
        Diccionario con las piezas genéricas de los juegos.
        """
        self.piezas = {'X': 'X', 'O': 'O'}

        print('| Eres el jugador ' + str(self.id) +
              '\t\t|\n|con ficha ' + self.getRepresentacion(self.id) + '\t\t\t|') 
    
    def getRepresentacion(self, _rep):
        """
        Se obtiene la representación de la pieza genérica a partir del id
        pasado.

        Parámetros:
        _rep -- Representación de la pieza genérica

        Return:

        """
        return self.piezas[_rep]

    def mostrarResultado(self, obj):
        """
        Se muestra el resultado de la partida al jugador.

        Parámetros:
        obj -- Resultado de la partida
        """
        if (obj == "0"):
            print("\n****** HAS EMPATADO ******\n")
        elif (obj == str(self.id)):
            print("\n****** HAS GANADO  ******\n")
        else:
            print("\n****** HAS PERDIDO  ******\n")

    def imprimirPieza(self, pieza):
        """
        Se muestra por pantalla la representación de la pieza

        Parámetros:
        pieza -- Id de la pieza
        """
        return self.getRepresentacion(pieza.getRepresentacion())

    def imprimirTablero(self, _tablero):
        """
        Se muestra por pantalla el tablero.

        Parámetros:
        _tablero -- Representación del tablero
        """
        # Se instancia el tablero (construirTablero) con las celdas pasadas
        # Recorro el tablero:
            # Si hay una instancia de Pieza llamo a imprimirPieza
            # Si no imprimo un hueco

        x = '    1    2    3 \n'
        for i in range(3):
            x += '   +---+---+---+\n' + str(i+1) + '  | '
            for j in range(3):

                pos = _tablero[i][j]

                if(pos == 0):
                    x += ' '

                # Si en la posición hay una instancia de Pieza se imprime
                # su representación 
                # TODO mirar (isinstance(pos, Pieza))
                else:
                    x += self.imprimirPieza(pos)

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