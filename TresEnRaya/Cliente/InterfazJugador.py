import time
from Servidor.Arbitro import Arbitro


class InterfazJugador:
    def __init__(self):
        self.destinatario = self.obtenerDestinatario()   # Se obtiene el árbitro
        self.fin = False                            # Se establece el fin de juego a falso
        self.mensaje = None                         # Se almacena el último mensaje recibido

    def jugar(self):
        """
        Mientras no se finalice el juego se obtiene el turno y se realiza una jugada
        """
        while(not self.fin):
            if(self.pedirTurno):
                print('Es su turno.')
                self.realizarJugada()
            else:
                time.sleep(1)

    def obtenerDestinatario(self):
        """
        Si el árbitro está creado, se obtiene
        Si no, se solicita al servidor que se cree uno
        """
        # TODO 
        return 1

    def pintarTablero(self):
        """
        Obtiene el tablero y lo imprime por pantalla.
        """
        self.pedirTablero().pintarTablero()

    def realizarJugada(self):
        """
        También va de mover
        Se pinta el tablero
        Se solicita al usuario un movimiento
        Se envía el movimiento al servidor
        Se muestra el tablero actualizado
        """
        self.pintarTablero()
        incorrecto = True
        while(incorrecto):
            x = input('Introduce la fila: ')
            y = input('Introduce la columna: ')
            self.enviarMensaje(self.destinatario, '101', [x-1, y-1])
            mensaje = self.esperarMensaje()

            # TODO comprobar código de mensaje
            if(mensaje.cod == '201'):
                incorrecto = True
                self.pintarTablero()
                print('Movimiento incorrecto, inroduzca un movimiento correcto.')
            elif(mensaje.cod == '207'):
                incorrecto = False
            elif(mensaje.cod == '203'):
                self.secuenciaFinalizacion()
        self.pintarTablero()
        print('Espere su turno.')

    def esperarMensaje(self):
        """
        Se queda en estado de espera hasta que recibe un mensaje
        Devuelve el mensaje
        """
        return self.mensaje

    def secuenciaFinalizacion(self):
        """
        Una vez se ha terminado el juego se pregunta si se quiere reiniciar
        Si no se quiere reiniciar, se finaliza el juego
        """
        print('El juego ha finalizado.')
        self.pintarTablero()
        print('¿Desea Iniciar una nueva partida?(1)Sí, (2)No.')
        resp = input()
        while(resp != 1 & resp != 2):
            print('Opción erronea ¿Desea Iniciar una nueva partida?(1)Sí, (2)No.')
            resp = input()
        if(resp == 1):
            self.enviarMensaje(self.destinatario, '104')
        else:
            self.enviarMensaje(self.destinatario, '105')
        resp = self.recibirMensaje()
        if(resp.cod == '204'):
            print('El juego se reiniciará.')
            time.sleep(1)
        else:
            print('La partida se ha finalizado.')
            self.fin = True

    def pedirTurno(self):
        """
        Envía un mensaje solicitando el turno y se queda a la espera de respuesta.
        Si la respuesta es la finalización, llama a secuenciaFinalización()
        Si no, devuelve el contenido del mensaje
        """
        self.enviarMensaje(self.destinatario, '103')
        mensaje = self.recibirMensaje()
        if(mensaje.cod == '203'):
            self.secuenciaFinalizacion()
        return mensaje.content  # TODO implementar

    def pedirTablero(self):
        """
        Envía un mensaje para obtener el tablero
        """
        self.enviarMensaje(self.destinatario, '102')
        return self.recibirMensaje().content

    def enviarMensaje(self, destinatario, codigo, contenido=None):
        """
        Envia el mensaje al destinatario
        """
        pass

    def recibirMensaje(self):
        """
        Se queda a la espera hasta que recibe un mensaje y lo devuelve
        """
        # TODO implementar la recepción del mensaje
        while (self.mensaje is None):
            time.sleep(1)
        return self.mensaje
