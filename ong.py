# ong.py

def factorial(n): 
    """
    Calcula el factorial de un entero no negativo n
    El factorial de n es el producto de todos los enteros positivos menores o iguales a n
    Ejemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
    """
    if n == 0 or n == 1: # El factorial de 0 ó 1 es 1.
        return 1
    else: # n! = n * (n-1)!
        resultado = 1
        for i in range(2, n + 1): # Itera desde 2 hasta n
            resultado *= i # Multiplica el resultado actual por el número de la iteración
        return resultado



def productoria(lista): #
    """
    Calcula la productoria de todos los números en una lista
    Es la multiplicación de todos los elementos de la lista.
    """
    if not lista: # lista vacía
        return 1
    else:
        producto = 1 
        for numero in lista: 
            producto *= numero 
        return producto



def calcular(**kwargs): #
    """
    Controla los cálculos de factoriales y productorias segun los argumentos proporcionados
    Puede aceptar argumentos en cualquier orden y cantidad, con nombres como fact_i para factorial
    y prod_i para productoria.
    """
    
    
    resultados = [] 

    claves = kwargs.keys()

    for key in claves:
        if 'fact' in key: # busca clave 'fact'
            num = kwargs[key]
            res_factorial = factorial(num) # función factorial
            resultados.append(f"El factorial de {num} es {res_factorial}")

        elif 'prod' in key: # busca clave 'prod' 
            lista_numeros = kwargs[key] 
            res_productoria = productoria(lista_numeros) # función productoria
            resultados.append(f"La productoria de {lista_numeros} es {res_productoria}") 

    for resultado in resultados: # Imprime cada resultado almacenado
        print(resultado)

# PRUEBAS
print(" Prueba 1 ")
calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6) 

print("\n Prueba 2 ")
calcular(prod_2=[4, 6, 7, 4, 3], fact_3=7)

print("\n Prueba 3 ")
calcular(fact_4=4)

print("\n Prueba 4 ")
calcular(prod_3=[10, 2, 5])
