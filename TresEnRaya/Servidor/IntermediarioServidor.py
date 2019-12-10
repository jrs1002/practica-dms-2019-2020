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
        fin = 0
        # Tablero pintado en InterfazJugador --> solicitarMov
        if(msg == "101"):
            fin = "203"
            obj = "0"

        # Solicitar tablero
        if(msg == "103"):
            fin, obj = self.dibujarTablero()

        # Movimiento a realizar
        if(msg == "104"):
            fin, obj = self.realizarMovimiento(elem)

        # Se ha realizado el movimiento y se ha actualizado el tablero
        if(msg == '105'):
            fin = self.esFin()
            if (fin == self.turno):
                return "200", str(self.turno), self.turno  # Codigo fin ganando
            elif (fin == "0"):
                return "200", "0", self.turno  # Codigo fin empate

            self.cambiarTurno()
            fin, obj = self.dibujarTablero()

        # Se devuelve el codigo de respuesta, el objeto y el turno
        return fin, obj, self.turno