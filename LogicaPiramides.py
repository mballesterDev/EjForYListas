n = int(input("Introduce un número entero: "))

for fila in range(1, n+1, +1):   # el de la izquierda es lo que se va a imprimir  medio es el RANGO DE 1  A N SE HARA HASTA QUE SEA menor que n y -1 es lo que se le quita a la n
    for cantidad in range(fila):
        print("*", end=" ")
    
    print()

print()
for fila in range(n,0,-1):
    for cantidad in range(fila):
        print("*", end=" ")
    
    print()