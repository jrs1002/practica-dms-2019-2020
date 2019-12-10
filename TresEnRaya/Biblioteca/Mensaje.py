# Imports
import json

"""
Clase de Capa de Comunicaciones.

Encapsula y desencapsula los mensajes y objetos de la comunicación.
"""
class Mensaje:
    def __init__(self, _code, _obj):
        """
        Método que inicializa el mensaje.
        Se inicializan las variables guardando el código
        y el objeto en un diccionario.

        Parámetros:
        _code -- Código del mensaje
        _obj -- Objeto del mensaje
        """
        self.content = {"code": _code, "obj": _obj}

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
        Convierte el mensaje en un String (JSON).

        Return:
        content -- Mensaje en JSON
        """
        return json.dumps(self.content)

    @classmethod
    def convertirEnObjeto(cls, _mensaje):
        """
        Convierte el mensaje pasado por parámetro en un objeto
        Mensaje.

        Parámetros:
        mensaje -- Mensaje a convertir

        Return:
        Mensaje -- Mensaje como instancia de la clase 
        """
        x = json.loads(_mensaje)
        return Mensaje(x["code"], x["obj"])
