import random
import math

#1
numAleatorio2 = print(random.randint(1, 100))

print("Introduce dos números y te diré cuál es el mayor")
n1 = input("Introduce el primer número")
n2 = input("Introduce el segundo número")

n1 = int(n1)
n2 = int(n2)

if n1 > n2:
    print(f"{n1} es mayor que {n2}")
elif n1 < n2:
    print(f"{n2} es mayor que {n1}")
else:
    print("Los números son iguales")

# Este programa compara dos números y muestra cuál es el mayor independientemente de su signo

# Imprime un mensaje para solicitar al usuario que introduzca dos números
print("Introduce dos números y te diré cuál es el mayor independientemente de su signo")

# Lee el primer número ingresado por el usuario
n1 = input("Introduce el primer número")
n2 = input("Introduce el segundo número")

# Convierte los números ingresados a enteros
n1 = int(n1)
n2 = int(n2)

# Obtiene el valor absoluto de los números ingresados
n1 = abs(n1)
n2 = abs(n2)

# Compara los números y muestra el resultado
if n1 > n2:
    print(f"{n1} es mayor que {n2}")
else:
    print(f"{n2} es mayor que {n1}")

#5
print(math.sqrt(25))

#6
n1 = float(input("Introduce una nota y la redondearé"))
print(round(n1))
print(math.ceil(n1))
print(math.floor(n1))

#7
print("Introduce la base y su exponente al cuál será elevado")
base = int(input("Introduce la base"))
exponente = int(input("Introduce el exponente"))
print(math.pow(base, exponente))