#Imports
import numpy as np

"""
Clase de Capa de Datos.
"""
class Tablero:
    def __init__(self, tamX, tamY):
        """
        Método que inicializa el Tablero en función del tamaño 
        pasado por parámetro.

        Parámetros:
        tamX - Número de filas del tablero
        tamY - Número de columnas del tablero
        """
        self.tab = np.zeros((tamX,tamY), np.int32) 

    # TODO def construirTablero(self,celdas)
    
    def setFicha(self, id, posicionX, posicionY):
        """
        Coloca la ficha en la posición indicada.

        Parámetros:
        color -- Color de la ficha
        posicionX -- Posición X
        posicionY -- Posicion Y
        """
        # TODO obtener el color a partir del id
        self.tab[posicionX][posicionY] = id

    def getTablero(self):
        """     
        Se devuelve el tablero.

        Return:
        tab -- Tablero
        """
        return self.tab

    def estaLleno(self):
        """
        Se comprueba si el tablero está lleno o no.

        Return:
        lleno -- Booleano que indica si el tablero está lleno o no
        """
        for i in range(3):
            for j in range(3):
                if(self.tab[i][j] == 0):
                    return False
        return True
