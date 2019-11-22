# Imports
import json

# Clase Mensaje
class Mensaje:
    def __init__(self, code, obj):
        """
        Método que inicializa el mensaje.
        Se inicializan las variables guardando el codigo
        y el objeto en un diccionario.

        Parámetros:
        code -- Código del mensaje
        obj -- Objeto del mensaje
        """
        self.content = {"code": code, "obj": obj}

    def getCode(self):
        """
        Se devuelve el código del mensaje almacenado.

        Return:
        code -- Código del mensaje
        """
        return self.content["code"]

    def getObj(self):
        """
        Se devuelve el objeto del mensaje almacenado.

        Return:
        code -- Objeto del mensaje
        """
        return self.content["obj"]

    def convertirEnCadena(self):
        """
        Convirte el mensaje en un String (JSON).

        Return:
        content -- Mensaje en JSON
        """
        return json.dumps(self.content)

    @classmethod
    def convertirEnObjeto(cls, mensaje):
        """
        Convierte el mensaje pasado por parámetro en un objeto
        Mensaje.

        Parámetros:
        mensaje -- Mensaje a convertir

        Return:
        Mensaje -- Mensaje como instancia de la clase 
        """
        x = json.loads(mensaje)
        return Mensaje(x["code"], x["obj"])
