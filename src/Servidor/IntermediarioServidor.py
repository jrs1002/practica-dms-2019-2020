#IMPORTS
from Arbitro_Conecta_4 import Arbitro_Conecta_4
from Arbitro_Tres_En_Raya import Arbitro_Tres_En_Raya

"""
Clase de Capa de Comunicaciones.

Encargada de llamar a las funciones de Árbitro dependiendo 
de los mensajes recibidos del Servidor.
"""
class IntermediarioServidor:
     def __init__(self,respuesta):
        """
        Método que inicializa el Intermediario del Servidor.
        Se inicializan las variables.
        """
        self.cod = ""
        self.obj = ""
        self.arbitro=self.inicializarArbitro(respuesta)

     def inicializarArbitro(self,respuesta):
        """
        Según la opción de juego que seleccione el Cliente, 1(Tres en Raya) o 2(Conecta 4, se inicializará el arbitro de un juego u otro.
        Siendo la respuesta el número de opción escogida, y por tanto, el juego seleccionado.

        Parámetros:
        respuesta -- Mensaje que contiene la opción de juego elegida por el CLiente(1-Tres en Raya y 2- Conecta 4)
        """
        if(respuesta=="1"):
            arbi=Arbitro_Tres_En_Raya(1,2) #Arbitro de Tres en Raya
        elif(respuesta=="2"):
            arbi=Arbitro_Conecta_4(1,2) #Arbitro de Conecta 4
        return arbi

     def arbitrar(self,msg,elem=None):
        """
        En función del mensaje recibido se realiza una cierta acción.

        Parámetros:
        msg -- Mensaje recibido del Cliente
        elem -- Objeto recibido del Cliente 

        Return:
        fin -- Código del mensaje a devolver en función de la acción realizada
        obj -- Objeto del mensaje a devolver en función de la acción realizada
        turno -- Turno actual
        """
        #turno=self.arbitro.turnoActual()

        # Tablero pintado en InterfazJugador --> solicitarMov
        if(msg == "101"):
            self.cod = "203"
            self.obj = "0"

        # Solicitar tablero
        if(msg == "103"):
            self.cod="202"
            self.obj = self.arbitro.dibujarTablero()

        # Movimiento a realizar
        if(msg == "104"):
            self.cod, self.obj = self.arbitro.realizarMovimiento(elem)
            if (self.cod):
                self.cod = "204"
            else:
                self.cod = "203"
                self.obj = "1"

        # Se ha realizado el movimiento y se ha actualizado el tablero 
        if(msg == '105'):
            self.obj = self.arbitro.esFin()
            
            if (self.cod == turno):
                self.cod = "200"
                self.obj = str(turno)  # Codigo fin ganando
            elif (self.cod == "0"):
                self.cod = "200"
                self.obj = "0"  # Codigo fin empate

            turno=self.arbitro.cambiarTurno()
            self.obj = self.arbitro.dibujarTablero()

        # Se devuelve el codigo de respuesta, el objeto y el turno
        return self.cod, self.obj, turno