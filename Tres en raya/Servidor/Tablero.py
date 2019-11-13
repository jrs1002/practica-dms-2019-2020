class Tablero:
    def __init__(self):
        self.celdas = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def setFicha(self, color, posicionX, posicionY):
        """
        Coloca la ficha en la posición indicada
        """
        self.celdas[posicionX][posicionY] = color

    def getTablero(self):
        """
        Devuelve el tablero
        """
        return self.celdas
