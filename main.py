# Parametros con valor por defecto para parametros opcionales
# def sumar(a = 0, b = 0): # -> int Pista sobre que tipo de dato regresara la función, pero es opcional
# def sumar(a, b):
#     return a + b
#
# resultado = sumar()
# print(f'Resultado de la suma: {resultado}')
# print(f'Resultado de la suma: {sumar(5,3)}')

# def listarNombres(*nombres): #esta sintaxis convierte los parametros en un array, en la documentacion se representa (*args)
#     for nombre in nombres:
#         print(nombre)
#
# listarNombres('Juanito', 'Karlita', 'Marishuy', 'Netito', 'etc')
# listarNombres('Laura', 'Carlos')

"""
Crear una función para sumar los valores recibidos de tipo numérico,
utilizando argumentos varibales *args como parámetros de la función
y regreasr como resultado la suma de todos los valores pasados como argumentos.
"""
# def sumarNums(*args):
#     res = 0
#     for numero in args:
#         res += numero
#     return res
#
# resultado = sumarNums(1,2,3,4,5,6,7,8,9)
# print(f'Resultado final: {resultado}')

"""
Crear una función para multiplicar los valores reicibidos de tipo numérico,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la multiplicación de todos los valores pasados como argumentos.
"""
# def multiplicar(*args):
#     res = 1
#     for num in args:
#         res *= num
#     return res
#
# print(f'Resultado: {multiplicar(5,2,5,2,4)}')

# def listarTerminos(**terminos): # Parametros de llave valor (diccionario)
#     for llave, valor in terminos.items():
#         print(f'{llave}: {valor}')
#
# listarTerminos(IDE = 'Integrated development enviroment', PK = 'Primary key')
# listarTerminos(DBMS = 'Database management system')

# def desplegarNombres(nombres):
#     for nombre in nombres:
#         print(nombre)
#
# nombres = ['Juanito', 'Karla', 'Guillermo']
# desplegarNombres(nombres)
# desplegarNombres('Carlos') #Una cadena es una lista de carácteres
# desplegarNombres((10,11))
# desplegarNombres([12,13])

"""
    FUNCIONES RECURSIVAS
"""

# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120
# def factorial(numero):
#     if numero == 1:
#         return 1
#     else:
#         return numero * factorial(numero - 1)
#
# numero = int(input('Ingresa un número: '))
# resultado = factorial(numero)
# print(f'El factorial de {numero} es: {resultado}')

"""
Imprimir números de 5 a 1 de manera descendente usando funciones recursivas.
Puede ser cualquier valor porisivo, ejemplo, si pasamos el valor de 5, debe imprimir:
5
4
3
2
1
Si se pasan valores negativos no imprime nada
"""

# def descendente(numero):
#     if numero == abs(numero):
#         if numero == 0:
#             return 0
#         else:
#             print(numero)
#             return numero - descendente(numero - 1)
#     else:
#         print('Ingresa un valor positivo porfis')
#
# numero = int(input('Ingresa un número: '))
# descendente(numero)

# Solucion del curso
# def imprimirResursivo(numero):
#     if numero >= 1:
#         print(numero)
#         imprimirResursivo(numero - 1)
#     elif numero == 0:
#         return
#     elif numero <= 0:
#         print('Valor incorrecto')
#
# imprimirResursivo(5)

"""
Ejercicio: Calculadora de Impuestos.
Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
# Formula: pago_total = pago_sin_impuesto + (pago_sin_impuesto + (impuesto/100))
"""
# def calcularImpuesto(pagoBruto, impuesto):
#     return pagoBruto + pagoBruto * (impuesto/100)
#
# pago = float(input('Ingresa el pago bruto: $'))
# impuesto = float(input('Ingresa el porcentaje (%) de impuesto: '))
# print(f"""
# Pago bruto:.....................${pago}.00
# Impuesto:..............({impuesto}%)
# Total de impuesto:..............${pago * (impuesto/100)}.00
# -------------------------------------------
# Total a pagar:..................${calcularImpuesto(pago,impuesto)}.00
# """)

"""
Ejercicio: Convertidor de Temperatura
Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.
"""
def celAFah(tempC):
    return (tempC * 1.8) + 32

def fahACel(tempF):
    return (tempF - 32) / 1.8

print('Conversor de grados')
tipo = int(input('Selecciona el tipo de conversion [1 = C°->F°] [2 = F°->C°]: '))
if tipo == 1 or tipo == 2:
    temperatura = float(input('Ingresa la temperatura: '))
    conversion = 0
    if tipo == 1:
        print(f'{temperatura} en F° es: {celAFah(temperatura):.2f}°')
    else:
        print(f'{temperatura} en C° es: {fahACel(temperatura):.2f}°')
else:
    print('Selecciona una opcion válida [1-2]')

# Solución
# def celsius_fahrenheit(celsius):
#     return celsius * 9 / 5 + 32
#
# def fahrenheit_celsius(fahrenheit):
#     return(fahrenheit - 32) * 5 / 9
#
# celsius = float(input('Proporcione su valor en celsius: '))
# resultado = celsius_fahrenheit(celsius)
# print(f'{celsius} C° a F°: {resultado:.2f}°')
#
# fahrenheit = float(input('Porporcione su valor en fahrenheit: '))
# resultado = fahrenheit_celsius(fahrenheit)
# print(f'{fahrenheit} F° a C°: {resultado:.2f}°')

