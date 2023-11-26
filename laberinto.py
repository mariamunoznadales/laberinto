def laberinto(dimension, muros):
   #La función ´laberinto´tiene dos argumentos: dimension (tamaño) y ´muros' (las coordenadas que representan las ubicaciones del los muros)

    # Lista vacía para añadir las filas del laberinto.
    laberinto = []
    # Bucle para recorrer las finales del laberinto
    # i toma valores de 0 a dimension-1 
    for i in range(dimension):
        # Lista para añadir las casillas de la fila.
        fila = []
        # Bucle para recorrer las columnas del laberinto.
        # j toma valores de 0 a dimension-1.
        for j in range(dimension):
            # Condicional para comprobar si la coordenada está en el la lista de muros.
            if tuple([i, j]) in muro:
                # Si la coordenada está en la lista de muros ponemos una X en la casilla.
                fila.append('X')
            else:
                # Si la coordenada no está en el muro ponemos un espacio en blanco en la casilla.
                fila.append(' ')
        laberinto.append(fila)
    return laberinto

# Conjunto de coordenadas de las celdas con muro 
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) 
juego = laberinto(5, muro)   

#Juntar todas las listas en una sola
for i in juego:
    print(''.join(i))
