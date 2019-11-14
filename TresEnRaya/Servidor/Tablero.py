class Tablero:
    def __init__(self):
        self.tab = [[0, 0, 0], [0, 0, 0], [1, 0, 1]]

    def setFicha(self, color, posicionX, posicionY):
        """
        Coloca la ficha en la posición indicada.
        """
        self.tab[posicionX][posicionY] = color

    def getTablero(self):
        """
        Devuelve el tablero.
        """
        return self.tab

    def dibujarTablero(self):
        """
        Pide el tablero y lo muestra por pantalla.
        """
        x = '    1    2    3 \n'
        for i in range(3):
            x += '   +---+---+---+\n' + str(i+1) +  '  | '
            for j in range(1, 3):

                if(self.tab[i][j] == 0):
                    x += ' '

                elif(self.tab[i][j] == 1):
                    x += 'X'

                else:
                    x += 'O'
                x += ' | '

            x += '  |\n'
        x += '   +---+---+---+'
        return x

    def estaLleno(self):
        lleno = True
        for i in range(3):
            for j in range(1, 3):
                 if(self.tab[i][j] == 0):
                     lleno = False
        return lleno
