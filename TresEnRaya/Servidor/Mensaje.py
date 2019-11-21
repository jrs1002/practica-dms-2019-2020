#Imports
import json

#Clase mensaje
class mensaje:

	def __init__(self,code,obj):
		"""
        Se inicializan las variables.
        """
		self.code = code
		self.obj=obj
	
	def convertirEnCadena(self):
		"""
        Convierte el objeto pasado en una cadena.

        Parámetros:
        cadena -- String pasado a convertir en objeto

        Return:
		objeto 
        """
		return json.dumps(obj)

	def convertirEnObjeto(self):
		"""
        Convierte la cadena pasada en un objeto.

        Parámetros:
        obj -- Objeto pasado a convertir en String

        Return:
		cadena
        """
		#return json.loads((self.cod,self.obj)) --> lo convierte en tupla
		return json.loads(code)
