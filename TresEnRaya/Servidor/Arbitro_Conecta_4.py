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
        mov -- Coordenada de la columna con el destino del movimiento
        """
        tab = self.tablero.getTablero()

        # Movimiento correcto y actualizado en el tablero
        if (self.comprobarMovimiento(mov)):
            for i in tab.getTamX()-1:
                if(tab[i][mov]==None):
                    self.tablero.setPieza(Pieza(self.turno), i,mov)
                    return True, self.tablero.getTablero()
        
        # Movimiento incorrecto, vuelve a solicitar el movimiento al jugador.
        else:
            return False

    def comprobarMovimiento(self, mov):
        """
        Se comprueba si el movimiento pasado por parámetros es válido.
        Para ello tiene en cuenta el jugador que ha enviado el movimiento 
        y el estado del tablero.

        Parámetros:
        mov -- y del destino del movimiento

        Return: 
        bool -- booleano que indica si es correcto o no
        """
        tab = self.tablero.getTablero()

        # Si el movimiento es correcto
        if (mov < tab.getTamX() and mov > 0 and tab[tab.getTamY()-1][mov] == None):
            return True  # Movimiento correcto

        else:  # Movimiento incorrecto
            return False

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
         
        for i in tab.getTamX()-4: #TODO:El -4 es para que al hacer +3 no salte el error de irse de rango
            for j in tab.getTamY()-4:
                if tab[i][j]==tab[i+1][j+1]==tab[i+2][j+2]==tab[i+3][j+3]==self.turno):
                    turno=self.turno
            
                elif(tab[i][j]==tab[i][j+1]==tab[i][j+2]==tab[i][j+3]==self.turno)
                    turno=self.turno
                
                elif(tab[i][j]==tab[i+1][j]==tab[i+2][j]==tab[i+3][j]==self.turno)
                    turno=self.turno
                  
        return turno
