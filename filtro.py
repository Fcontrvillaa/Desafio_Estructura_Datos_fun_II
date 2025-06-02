
import sys 

def filtrar_productos(precios, umbral, tipo_filtro='mayor'):  #filtro por defecto mayor
    """
    Filtra un diccionario de productos por precio.
    """
    productos_filtrados = [] # almacenar los nombres de los productos que cumplen la condición

    if tipo_filtro == 'mayor': 

        for producto, precio in precios.items(): 
            if precio > umbral: 
                productos_filtrados.append(producto) 
        return f"Los productos mayores al umbral son: {', '.join(productos_filtrados)}" 
    
    elif tipo_filtro == 'menor': 
        for producto, precio in precios.items(): 
            if precio < umbral: 
                productos_filtrados.append(producto) 
        return f"Los productos menores al umbral son: {', '.join(productos_filtrados)}" 
    
    else: 
        return "Lo sentimos, no es una operación válida" # mensaje de error no es mayor ni menor

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

   

    if len(sys.argv) == 2: # si se proporciona solo el umbral
        try:
            umbral_valor = int(sys.argv[1]) 
            print(filtrar_productos(precios, umbral_valor))

        except ValueError: 
            print("Error: El umbral debe ser un número entero.")


    elif len(sys.argv) == 3: # umbral y el tipo de filtro
        try:
            umbral_valor = int(sys.argv[1])
            tipo_filtro_valor = sys.argv[2].lower() # segundo argumento a minúsculas
            
            print(filtrar_productos(precios, umbral_valor, tipo_filtro_valor))
        except ValueError: 
            print("Error: El umbral debe ser un número entero.")

    else: # Si no se entrega la cantidad correcta de argumentos
        print("Uso: python filtro.py <umbral> [mayor / menor]")
        print("Ej: python filtro.py 30000")
        print("Ej: python filtro.py 30000 menor")