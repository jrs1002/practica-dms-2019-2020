_tablero  = [[0,1,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0], [0,0,0,0,0,0,0],]

tamY = 6
tamX = 7

for i in range(tamX):
    x = '\t' + str(i)

x = ' \n'

for i in range(tamY): 
    x += '   ' + '+---'*tamX+'+\n' + str(i+1) + '  | '
    for j in range(tamX):

        pos = _tablero[i][j]

        if(pos == 0):
            x += ' '

        # Si en la posición hay una instancia de Pieza se imprime
        # su representación 
        # TODO mirar (isinstance(pos, Pieza))
        else:
            x += 'y'

        x += ' | '

    x += '\n'

x += '   ' + '+---' * tamX + '+\n'

print(x)