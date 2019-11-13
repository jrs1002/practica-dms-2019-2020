class Tablero:
    def __init__(self):
        self.tab = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

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

    def pintarTablero(self):
        """
        Pide el tablero y lo muestra por pantalla.
        """
        print('    1 '+'  2 '+'  3 ')
        for i in range(3):
            print('  +---+---+---+')
            print((i+1)+' | ', end='')

            if(self.tab[i][0] == 0):
                print(' ', end='')

            elif(self.tab[i][0] == 1):
                print('X', end='')

            else:
                print('O', end='')

            print(' | ', end='')

            if(self.tab[i][1] == 0):
                print(' ', end='')

            elif(self.tab[i][1] == 1):
                print('X', end='')

            else:
                print('O', end='')

            if(self.tab[i][2] == 0):
                print(' ', end='')

            elif(self.tab[i][1] == 1):
                print('X', end='')

            else:
                print('O', end='')

            print(' |')

            print(' +---+---+---+')
