#Imports
import numpy as np

"""
Clase de Capa de Datos.
"""
class Tablero:
    def __init__(self, _tamX, _tamY):
        """
        Método que inicializa el Tablero en función del tamaño 
        pasado por parámetro.

        Parámetros:
        _tamX - Número de filas del tablero
        _tamY - Número de columnas del tablero
        """
        self.tamX = _tamX
        self.tamY = _tamY

        self.tab = list()
        for i in range(_tamX):
            self.tab.append([None] * _tamY)

    @classmethod
    def construirTablero(cls,celdas):
        '''
        Método que crea el tablero según el array de celdas pasado por parámetro

        Parámetros:
        celdas -- Array de celdas 
        '''
        tablero = Tablero(len(celdas),len(celdas[0]))
        for i, fila in enumerate(celdas):
            for j, celda in enumerate(fila):
                if celda != 0:
                    pieza = Pieza(celda,)
                    tablero.setPieza(celda,i,j)
                else:
                    tablero[i][j]=None
        return tablero
    
    def tableroToArray(self):
        '''
        Método que convierte el tablero en un array
        '''
        array = [] 
        for i, fila in enumerate(self.tab):
            array.append([])
            for j, celda in enumerate(fila):
                if celda != None:
                    array[i],append(celda.getId())
                else:
                    array[i].append(0)
        return array
    
    def setPieza(self, pieza, posicionX, posicionY):
        """
        Coloca la pieza en la posición indicada.

        Parámetros:
        pieza -- Pieza a colocar
        posicionX -- Posición X
        posicionY -- Posicion Y
        """
        self.tab[posicionX][posicionY] = pieza

    def getTamX(self):
        """     
        Se devuelve el ancho del tablero.

        Return:
        tamX -- Ancho del tablero
        """
        return self.tamX

    def getTamY(self):
        """     
        Se devuelve el alto del tablero.

        Return:
        tamY -- Alto del tablero
        """
        return self.tamY

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
                if(self.tab[i][j] == None):
                    return False
        return True