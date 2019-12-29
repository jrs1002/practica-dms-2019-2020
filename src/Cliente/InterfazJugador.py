# Imports
import time
import sys
sys.path.append('..')
sys.path.append('../Biblioteca')
from Tablero import Tablero

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
        self.piezas = {1: 'X', 2: 'O'}

        print('| Eres el jugador ' + str(self.id) +
              '\t\t|\n|con ficha ' + self.getRepresentacion(self.id) + '\t\t\t|') 
    
    def getRepresentacion(self, _id):
        """
        Se obtiene la representación de la pieza genérica a partir del id
        pasado.

        Parámetros:
        _id -- Id de la pieza genérica

        Return: 
        piezas[_id] -- representación de la pieza 
        """
        return self.piezas[_id]

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
        return self.getRepresentacion(pieza.getId())

    def imprimirTablero(self, _tablero):
        """
        Se muestra por pantalla el tablero.

        Parámetros:
        _tablero -- Representación del tablero
        """
        tabl=Tablero.construirTablero(_tablero)
        tab=tabl.getTablero()
        tamX = tabl.getTamX()
        tamY = tabl.getTamY()

        for i in range(tamX):
            x = '\t' + str(i)

        x = ' \n'

        for i in range(tamY): 
            x += '   ' + '+---'*tamX+'+\n' + str(i+1) + '  | '
            for j in range(tamX):

                pos = tab[i][j]

                if(pos == None):
                    x += ' '
                else:
                    x += self.imprimirPieza(pos)

                x += ' | '

            x += '\n'

        x += '   ' + '+---' * tamX + '+\n'

        print(x)

    def solicitarMov(self):
        """
        Se solicita al jugador el movimiento.

        Return:
        mov -- Coordenadas del movimiento
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
        return mov