# Imports
import sys
sys.path.append('..')
sys.path.append('../Biblioteca')
from Tablero import Tablero
from abc import ABC, abstractmethod #TODO: NO SE SI ES NECESARIO LO DE ABC

# Clase Arbitro Abstracto
class Arbitro_Abstracto(ABC):
   def __init__(self, _jugador1, _jugador2):
       """
       Se inicializa el árbitro con los jugadores que recibe como parámetro.
       Se establece el turno que empieza (jugador 1)

       Parámetros:
       jugador1 -- Primer jugador (contiene el código para enviar mensajes)
       jugador2 -- Segundo jugador (contiene el código para enviar mensajes)
       """
       self.jugador1 = _jugador1    # Primer jugador
       self.jugador2 = _jugador2    # Segundo jugador
       self.turno = 1               # Turno actual
   
   @abstractmethod
   def realizarMovimiento(self, mov):
      raise NotImplementedError
   
   @abstractmethod
   def comprobarMovimiento(self, mov):
      raise NotImplementedError
   
   @abstractmethod
   def esFin(self):
      raise NotImplementedError
   
   def turnoActual(self):
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