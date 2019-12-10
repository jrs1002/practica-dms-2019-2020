"""
Clase de Capa de Datos.
"""
class Pieza:
    def __init__(self, _id, _representacion):
        """
        Método que inicializa la pieza.
        Se inicializan las variables.

        Parámetros:
        _id             -- Id de la pieza (en función del id cliente)
        _representacion -- Representación de la pieza
        """
        self.id = _id
        self.representacion = _representacion

    def getId(self):
        """
        Se devuelve el id de la pieza almacenado.

        Return:
        id -- Id de la pieza
        """
        return self.id

    def getRepresentacion(self):
        """
        Se devuelve la representación de la pieza almacenada.

        Return:
        representacion -- Representacion de la pieza
        """
        return self.representacion