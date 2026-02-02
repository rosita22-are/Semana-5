"""
Programa: Conversor de Temperatura
Descripción:
Este programa convierte una temperatura ingresada en grados Celsius
a grados Fahrenheit. Utiliza diferentes tipos de datos, identificadores
descriptivos y comentarios para explicar la lógica.
"""

def convertir_celsius_a_fahrenheit(grados_celsius):
    """
    Convierte grados Celsius a Fahrenheit.
    :param grados_celsius: float
    :return: float
    """
    grados_fahrenheit = (grados_celsius * 9 / 5) + 32
    return grados_fahrenheit


# Entrada de datos
nombre_usuario = input("Ingrese su nombre: ")  # string
edad_usuario = int(input("Ingrese su edad: "))  # integer
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))  # float

# Proceso
temperatura_fahrenheit = convertir_celsius_a_fahrenheit(temperatura_celsius)

# Uso de un boolean
es_mayor_de_edad = edad_usuario >= 18  # boolean

# Salida de resultados
print("\n--- Resultados ---")
print("Nombre del usuario:", nombre_usuario)
print("Edad:", edad_usuario)
print("¿Es mayor de edad?:", es_mayor_de_edad)
print("Temperatura en Celsius:", temperatura_celsius)
print("Temperatura en Fahrenheit:", temperatura_fahrenheit)
