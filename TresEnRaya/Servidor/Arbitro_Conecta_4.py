# Imports
import sys
sys.path.append('..')
sys.path.append('../Biblioteca')
from Biblioteca import Tablero

# Clase Arbitro de conecta 4
class Arbitro_Conecta4:
   
    def __init__(self, _jugador1, _jugador2):
        """
        Se inicializa el árbitro con los jugadores que recibe como parámetro.
        Se instancia el tablero con el que se trabajará.
        Se establece el turno que empieza (jugador 1)

        Parámetros:
        jugador1 -- Primer jugador (contiene el código para enviar mensajes)
        jugador2 -- Segundo jugador (contiene el código para enviar mensajes)
        """
        self.jugador1 = _jugador1    # Primer jugador
        self.jugador2 = _jugador2    # Segundo jugador
        self.tablero = Tablero(6,7)  # Tablero en el que se trabaja
        self.turno = 1               # Turno actual

    def realizarMovimiento(self, mov):
        """
        Se comprueba si el movimiento pasado por parámetro es correcto.
        Si lo es, se coloca la ficha en la posición indicada por el movimiento.
        Se cambia de turno.

        Parámetros:
        mov -- Coordenadas xy con el destino del movimiento
        """
        movimiento = [mov[0]-1, mov[1]-1]

        correcto = self.comprobarMovimiento(movimiento)

         # Movimiento correcto y actualizado en el tablero
        if (correcto == 1):
            self.tablero.setFicha(self.turno, movimiento[0], movimiento[1])
            return "204", self.tablero.getTablero()
        
        # Movimiento incorrecto, vuelve a solicitar el movimiento al jugador
        if (correcto == 2 ):
            return "203", "1"

    def comprobarMovimiento(self, mov):
        """
        Se comprueba si el movimiento pasado por parámetros es válido.
        Para ello tiene en cuenta el jugador que ha enviado el movimiento 
        y el estado del tablero.

        Parámetros:
        mov -- [x,y] del destino del movimiento

        Return: 
        int -- Entero que indica si es correcto o no
        """
        tab = self.tablero.getTablero()
        posibilidades = [0, 1, 2]

        # Si el movimiento es correcto
        if ((mov[0] in posibilidades) and
            (mov[1] in posibilidades) and
                (tab[mov[0]][mov[1]] == 0)):
            return 1  # Movimiento correcto

        else:  # Movimiento incorrecto
            return 2

    def esFin(self):
        """
        Se obtiene el tablero y busca jugadas ganadoras o si el tablero está lleno.

        Return:
        int -- Entero con el turno del ganador o 0 si es empate 
        """
        tab = self.tablero.getTablero()
        #Valor que se devolverá en el return(con el turno del ganador o 0 si es empate)
        turno=-1
        
        if(self.tablero.estaLleno()):
            return 0
         
        for i in len(tab)-4: #TODO:El -4 es para que al hacer +3 no salte el error de irse de rango
            for j in len(tab[0])-4:
                # Líneas horizontales
                if tab[i][j]==tab[i+1][j+1]==tab[i+2][j+2]==tab[i+3][j+3]==self.turno):
                    turno=self.turno
            
                elif(tab[i][j]==tab[i][j+1]==tab[i][j+2]==tab[i][j+3]==self.turno)
                    turno=self.turno
                
                elif(tab[i][j]==tab[i+1][j]==tab[i+2][j]==tab[i+3][j]==self.turno)
                    turno=self.turno
                  
        return turno
