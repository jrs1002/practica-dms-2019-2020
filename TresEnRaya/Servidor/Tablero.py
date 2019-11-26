# Clase Tablero.
class Tablero:
    def __init__(self):
        """
        Método que inicializa el Servidor.
        Se inicializan las variables.
        """
        self.tab = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]



    # TODO def construirTablero(self,celdas)
    # TODO crear clase pieza
    
    def setFicha(self, color, posicionX, posicionY):
        """
        Coloca la ficha en la posición indicada.

        Parámetros:
        color -- Color de la ficha
        posicionX -- Posición X
        posicionY -- Posicion Y
        """
        self.tab[posicionX][posicionY] = color

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
