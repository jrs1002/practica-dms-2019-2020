# Imports
import sys
sys.path.append('..')
sys.path.append('../Biblioteca')
from Biblioteca import Tablero
from abc import ABC, abstractmethod #TODO: hay que poner abc???

# Clase Arbitro Abstracto
class Arbitro_Abstracto(ABC):

  @abstractmethod
   def __init__(self, _jugador1, _jugador2):
      raise NotImplementedError
   
   @abstractmethod
   def realizarMovimiento(self, mov):
      raise NotImplementedError
   
   @abstractmethod
   def comprobarMovimiento(self, mov):
      raise NotImplementedError
   
   @abstractmethod
   def esFin(self):
      raise NotImplementedError
   
   def turnoActual(self)
      """
        Se devuelve el turno actual.

        Return:
        turno -- Turno actual
        """
        return self.turno
   
   def cambiarTurno(self):
        """
        Se cambia el turno del jugador.
        """
        if(self.turno == 1):
            self.turno = 2
        else:
            self.turno = 1
   
   def dibujarTablero(self):
        """
        Se devuelve la representación del tablero actual y un 
        código mensaje 202 "devolver tablero"

        Return:
        int -- Código del mensaje de "devolver tablero"
        self.tablero.dibujarTablero() -- Representación del tablero
        """
        return "202", self.tablero.getTablero()