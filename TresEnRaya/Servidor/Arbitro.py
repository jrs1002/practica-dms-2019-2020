from Servidor.Tablero import Tablero
import time


class Arbitro:
    def __init__(self, jugador1, jugador2):
        """
        Inicializa el árbitro con dos jugadores que recibe como parámetro.
        Se crea el tablero con el que se trabajará.

        Param:
        jugador1 -- Primer jugador (contiene el código para enviar mensajes)
        jugador2 -- Segundo jugador (contiene el código para enviar mensajes)
        """
        self.jugador1 = jugador1    # Primer jugador
        self.jugador2 = jugador2    # Segundo jugador
        self.tablero = Tablero()    # Tablero en el que se trabaja
        self.fin = False            # Juego finalizado
        self.turno = 1              # Turno actual
        self.mensaje = None         # Último mensaje recibido

    def jugar(self):
        """
        Mientras no se haya terminado el juego, se queda a la espera de mensajes.
        """
        while(not self.fin):
            self.esperarMensaje()

    def esperarMensaje(self):
        """
        Se queda a la espera de un mensaje.
        Una vez lo recibe actúa en función de su código.
        """
        # TODO implementar la comunicación entre clases
        mensaje = self.recibirMensaje()
        operaciones = {'101': self.comprobarMovimiento(mensaje.content),
                       '102': self.mandarTablero(mensaje.destinatario),
                       '103': self.mandarTurno(mensaje.destinatario)}  # adaptar para que funcione lo de content y destinatario
        operaciones[mensaje.cod]  # adapatar al codigo de mensaje

    def recibirMensaje(self):
        """
        Se queda a la espera hasta que recibe un mensaje y lo devuelve.
        """
        # TODO implementar la recepción del mensaje
        while (self.mensaje is None):
            time.sleep(1)

        return self.mensaje

    def comprobarMovimiento(self, movimiento):
        """
        Obtiene un movimiento y comprueba si este es válido.
        Para ello tiene en cuenta el jugador que ha enviado el movimiento 
        y el estado del tablero.

        Envia un mensaje al jugador:
        207 -- Movimiento correcto
        201 -- Movimiento incorrecto

        Parámetros:
        movimiento -- Coordenadas [x,y] del destino del movimiento
        """
        tab = self.tablero.getTablero()
        posibilidades = [0, 1, 2]

        if (movimiento[0] in posibilidades & movimiento[1] in posibilidades & tab[movimiento[0]][movimiento[1]] == 0):
            self.realizarMovimiento(movimiento)
            if (self.esFin()):
                self.consultarReinicio()
            elif (self.turno == 1):
                self.enviarMensaje(self.jugador1, '207')
            else:
                self.enviarMensaje(self.jugador2, '207')

        else:
            if (self.turno == 1):
                self.enviarMensaje(self.jugador1, '201')
            else:
                self.enviarMensaje(self.jugador2, '201')

    def esFin(self):
        """
        Obtiene el tablero y busca jugadas ganadoras.
        Si la encuentra, devuelve True, si no False.
        """
        tab = self.tablero.getTablero()
        if(tab[0][0] == tab[0][1] == tab[0][2] | tab[1][0] == tab[1][1] == tab[1][2] | tab[2][0] == tab[2][1] == tab[2][2]):
            return True

        if(tab[0][0] == tab[1][0] == tab[2][0] | tab[0][1] == tab[1][1] == tab[2][1] | tab[0][2] == tab[1][2] == tab[2][2]):
            return True

        if(tab[0][0] == tab[1][1] == tab[1][2] | tab[2][0] == tab[1][1] == tab[0][2]):
            return True

        return False

    def realizarMovimiento(self, movimiento):
        """
        Obtiene una posición y coloca la ficha del turno correspondiente.
        El movimiento ha de ser validado previamente.

        Parámetros:
        movimiento -- Coordenadas [x,y] del destino del movimiento
        """
        self.tablero.setFicha(self.turno, movimiento[0], movimiento[1])
        
        if (self.turno == 1):
            self.turno = 2
        else:
            self.turno = 1

    def mandarTablero(self, destinatario):
        """
        Envía el tablero al destinatario
        """
        if (destinatario == self.jugador1):
            self.enviarMensaje(self.jugador1, '202', self.tablero.getTablero())
        else:
            self.enviarMensaje(self.jugador2, '202', self.tablero.getTablero())

    def mandarTurno(self, destinatario):
        """
        Se envia el turno al jugador que le corresponde
        """
        if (self.jugador1 == destinatario):
            if(self.turno == 1):
                self.enviarMensaje(destinatario, '205', True)
            else:
                self.enviarMensaje(destinatario, '205', False)
        else:
            if(self.turno == 2):
                self.enviarMensaje(destinatario, '205', True)
            else:
                self.enviarMensaje(destinatario, '205', False)

    def consultarReinicio(self):
        """
        Consulta si se quiere reiniciar el juego
        """
        self.enviarMensaje(self.jugador1, '203')
        self.enviarMensaje(self.jugador2, '203')
        time.sleep(1)
        if (self.esperarMensaje().cod == self.esperarMensaje().cod == 104):
            self.reiniciar()
        else:
            self.enviarMensaje(self.jugador1, '206')
            self.enviarMensaje(self.jugador2, '206')

    def reiniciar(self):
        """
        Se reinicia el juego
        """
        for i in range(3):
            for j in range(3):
                self.tablero.setFicha(0, i, j)

    def enviarMensaje(self, destinatario, codigo, contenido=None):  # TODO
        """
        Se envía el mensaje al destinatario
        """
        pass
