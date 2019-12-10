#Imports
from InterfazJugador import InterfazJugador as ij

"""
Clase de Capa de Comunicaciones.

Encargada de llamar a las funciones de InterfazJugador
dependiendo de los mensajes recibidos de Cliente.
"""
class IntermediarioCliente:

     def __init__(self):
        """
        Método que inicializa el Intermediario del Cliente.
        Se inicializan las variables.
        """
        self.cod = ''
        self.obj = ''

    def jugar(self, msg, elem=None):
        """
        En función del mensaje recibido se llama a la función
        correspondiente de InterfazJugador.

        Si no se requiere ningún objeto se devolverá 0. #TODO

        Parámetros:
        msg -- Mensaje recibido del Servidor
        elem -- Objeto recibido del Servidor

        Return:
        fin -- Código del mensaje a devolver en función de la acción realizada
        obj -- Objeto del mensaje a devolver en función de la acción realizada
        """
        # Solicitar salir del juego
        if (msg == '200'):
            ij.mostrarResultado(elem)
            return '100', '0'

        # Solicitar tablero --> Con mensaje 202 ya se va a imprimir
        if (msg == '202'):
            print("\n\n")
            fin, obj = ij.imprimirTablero(elem)

        # Solicitar movimiento --> Si es erróneo con mensaje 203 ya se vuelve a solicitar
        if (msg == '203'):
            if (elem == '1'):
                print("\nMovimiento incorrecto, introduzca un nuevo movimiento.\n")
            fin, obj = ij.solicitarMov()

        if (msg == '204'):
            fin, obj = ij.imprimirTablero(elem)
            print("\n\n")
            fin = '105'

        return fin, obj