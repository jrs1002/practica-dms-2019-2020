#Imports
from #TODO importat arbitro ?? abstracto??

"""
Clase de Capa de Comunicaciones.

Encargada de llamar a las funciones de Árbitro dependiendo 
de los mensajes recibidos del Servidor.
"""
class IntermediarioServidor:

     def __init__(self):
        """
        Método que inicializa el Intermediario del Servidor.
        Se inicializan las variables.
        
        """
        self.cod = ''
        self.obj = ''

    def arbitrar(self, msg, elem=None):
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
            turno=arbitro.turnoActual()
            
            # Tablero pintado en InterfazJugador --> solicitarMov
            if(msg == "101"):
                self.cod = "203"
                self.obj = "0"

            # Solicitar tablero
            if(msg == "103"):
                self.cod="202"
                self.obj = self.dibujarTablero()

            # Movimiento a realizar
            if(msg == "104"):
                self.cod, self.obj = self.realizarMovimiento(elem)
                if (self.cod):
                    self.cod = "204"
                else:
                    self.cod = "203"
                    self.obj = "1"

            # Se ha realizado el movimiento y se ha actualizado el tablero 
            if(msg == '105'):
                self.obj = self.esFin()
                
                if (self.cod == turno):
                    self.cod = "200"
                    self.obj = str(turno)  # Codigo fin ganando
                elif (self.cod == "0"):
                    self.cod = "200"
                    self.obj = "0"  # Codigo fin empate

                arbitro.cambiarTurno()
                self.cod, self.obj = self.dibujarTablero()

            # Se devuelve el codigo de respuesta, el objeto y el turno
            return self.cod, self.obj, turno ##POR QUE DEVUELVE SIEMPRE TURNO?????????