#el switch en phyton no existe pero podemos crear algo similar 
import math

n1 = int(input("Introduce el primer número"))
n2 = int(input("Introduce el segundo número número"))

nElegido = int(input(""" Elije una opción:

1 sumar
2 restar
3 dividir
4 elevar
 """))

if nElegido is 1:
    print(n1+n2)
elif nElegido is 2:
    print(n1-n2)
elif nElegido is 3:
    print(n1/n2)
elif nElegido is 4:
    print(int(math.pow(n1,n2))) #para que nos de un entero y no decimales

