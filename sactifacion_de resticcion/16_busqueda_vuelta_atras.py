#codigo para busqueda vuelta atras

def vuelta_atras(grafo, inicio, meta):
    def valido(x, y):
        if x >= 0 and x < len(grafo) and y >= 0 and y < len(grafo[0]) and grafo[x][y] == 0:
            return True
        else:
            return False

    def solu(x, y):
        if x == meta[0] and y == meta[1]:
            return True

        if valido(x, y):
            grafo[x][y] = 2  # Marcar como visitado

            pasos = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            for i in pasos:
                nuev_x, nuevo_y = x + i[0], y + i[1]
                if solu(nuev_x, nuevo_y):
                    return True

            grafo[x][y] = 0  # Desmarcar como no visitado

        return False

    if solu(inicio[0], inicio[1]):
        return grafo
    else:
        return None

grafo = [
    [0, 'E', 0, 0, 0],
    [0, 'E', 0, 'S', 0],
    [0, 0, 0, 0, 0],
    [0, 'S', 'S', 'S', 0],
    [0, 0, 0, 0, 0]
]

inicio = (0, 0)
meta = (4, 4)

res = vuelta_atras(grafo, inicio, meta)
if res:
    print('Ruta encontrada:')
    for row in res:
        print(row)
else:
    print('No se encontró una ruta.')