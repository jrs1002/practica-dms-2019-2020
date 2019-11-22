#Imports
import json

#Clase mensaje
class Mensaje:
    def __init__(self,code,obj):
        """
        Se inicializan las variables.
        Guardando el codigo y el objeto en un diccionario
        """        
        self.content = { "code": code,"obj": obj }

    def getCode(self):
        return self.content["code"]

    def getObj(self):
        return self.content["obj"]
        
    def convertirEnCadena(self):
        """
        Convirte el mensaje en un String(JSON)

        Return:
                Mensaje en JSON
        """
        return json.dumps(self.content)

    @classmethod
    def convertirEnObjeto(cls,mensaje):
        """
        Convierte el mensaje en un objeto.

        Parámetros:

        Return:
                Mensaje (clase mensaje)
        """
        x =  json.loads(mensaje)
        return Mensaje(x["code"],x["obj"])
