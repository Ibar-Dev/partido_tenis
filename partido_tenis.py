def punto():
    punto_para = input('Ingrese P1 o P2 para identificar cada puntuacion:\n').lower()

    while punto_para not in ('p1', 'p2'):
        punto_para = input('Por favor, ingrese "P1" o "P2" para identificar cada puntuacion:\n').lower()
    
    return punto_para


def partido():
    estado = [0, 15, 30, 40]
    p1 = 0
    p2 = 0
    winner = None

    while True:
        try:
            point = punto()
            if point == 'p1':
                p1 += 1
            elif point == 'p2':
                p2 += 1

            print('\nPuntuacion:')
            
            if p1 >= 4 or p2 >= 4:
                if p1 - p2 >= 2:
                    print('Partido para Player 1')
                    winner = 'Player 1'
                    break
                elif p2 - p1 >= 2:
                    print('Partido para Player 2')
                    winner = 'Player 2'
                    break
                elif p1 == p2:
                    print("Iguales")
                elif p1 > p2:
                    print("Ventaja Player 1")
                else:
                    print("Ventaja Player 2")
            else:
                print(f'Player 1: {estado[p1]} - Player 2: {estado[p2]}\n')
        except IndexError:
            print("Error: Puntaje fuera de rango. Reiniciando partida.")
            return None

    return winner


print("El ganador del partido es:", partido())
