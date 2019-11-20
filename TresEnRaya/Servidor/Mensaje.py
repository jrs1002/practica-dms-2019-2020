#Imports
import json

#Clase mensaje
class mensaje:

	def __init__(self):

	def convertirEnCadena(self,obj):
		"""
        Convierte el objeto pasado en una cadena.

        Parámetros:
        cadena -- String pasado a convertir en objeto

        Return:
		objeto 
        """
		return json.dumps(obj)

	def convertirEnObjeto(self,cadena):
		"""
        Convierte la cadena pasada en un objeto.

        Parámetros:
        obj -- Objeto pasado a convertir en String

        Return:
		cadena
        """
		return json.loads(cadena)
