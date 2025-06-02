
import sys 

def filtrar_productos(precios, umbral, tipo_filtro='mayor'):  #filtro por defecto mayor
    """
    Filtra un diccionario de productos por precio.
    """
    productos_filtrados = [] # almacenar los nombres de los productos que cumplen la condición

    if tipo_filtro == 'mayor': 
        for producto, precio in precios.items(): # Itera sobre cada par producto-precio
            if precio > umbral: # Comprueba si el precio es estrictamente mayor que el umbral
                productos_filtrados.append(producto) # Agrega el nombre del producto a la lista
        return f"Los productos mayores al umbral son: {', '.join(productos_filtrados)}" # Formatea y devuelve la cadena
    elif tipo_filtro == 'menor': 
        for producto, precio in precios.items(): # Itera sobre cada par producto-precio
            if precio < umbral: # Comprueba si el precio es estrictamente menor que el umbral
                productos_filtrados.append(producto) # Agrega el nombre del producto a la lista
        return f"Los productos menores al umbral son: {', '.join(productos_filtrados)}" # Formatea y devuelve la cadena
    else: # Si el tipo de filtro no es 'mayor' ni 'menor'
        return "Lo sentimos, no es una operación válida" # mensaje de error

if __name__ == "__main__":
    # Diccionario de prueba
    precios = {
        'Notebook': 700000,
        'Teclado': 25000,
        'Mouse': 12000,
        'Monitor': 250000,
        'Escritorio': 135000,
        'Tarjeta de Video': 1500000
    }

    # sys.argv contiene los argumentos de la línea de comandos.
    # sys.argv[0] es el nombre del script (filtro.py).
    # sys.argv[1] es el primer argumento (el umbral).
    # sys.argv[2] es el segundo argumento (opcional, el tipo de filtro).

    if len(sys.argv) == 2: # Si se proporciona solo el umbral
        try:
            umbral_valor = int(sys.argv[1]) # Intenta convertir el primer argumento a entero
            # Llama a la función con el umbral y el filtro por defecto 'mayor'
            print(filtrar_productos(precios, umbral_valor))
        except ValueError: # Si el umbral no es un número válido
            print("Error: El umbral debe ser un número entero.")
    elif len(sys.argv) == 3: # Si se proporcionan el umbral y el tipo de filtro
        try:
            umbral_valor = int(sys.argv[1]) # Intenta convertir el primer argumento a entero
            tipo_filtro_valor = sys.argv[2].lower() # Obtiene el segundo argumento y lo convierte a minúsculas
            # Llama a la función con el umbral y el tipo de filtro especificado
            print(filtrar_productos(precios, umbral_valor, tipo_filtro_valor))
        except ValueError: # Si el umbral no es un número válido
            print("Error: El umbral debe ser un número entero.")
    else: # Si no se proporcionan la cantidad correcta de argumentos
        print("Uso: python filtro.py <umbral> [mayor|menor]")
        print("Ej: python filtro.py 30000")
        print("Ej: python filtro.py 30000 menor")