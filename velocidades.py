#2. Alertas telemáticas.

def calcular_alertas_velocidad(velocidades):
    """
    Calcula el promedio de una lista de velocidades y devuelve las posiciones
    de las correas transportadoras que están por encima del promedio.
    """
    if not velocidades:
        return []

    
    suma_velocidades = 0
    
    for velocidad in velocidades:
        suma_velocidades += velocidad
    promedio = suma_velocidades / len(velocidades)

    # Encontrar las posiciones de las velocidades por encima del promedio
    posiciones_sobre = []
    for i in range(len(velocidades)):
        if velocidades[i] > promedio:
            posiciones_sobre.append(i)

    return posiciones_sobre


    
#velocidades de prueba
velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

alertas = calcular_alertas_velocidad(velocidad)
print(alertas)