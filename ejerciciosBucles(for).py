#1

r1 = input("Introduce una frase yb te la repetiré 10 veces ")

for repetir10 in range(10):
    print(r1)

#2


r2 = int(input("Dime tu edad y te diré todos los años que has cumplido"))

print("Has cumplido ya todos estos años!")


for añostotales in range (r2):
    print(añostotales +1) #el +1 porque no se puede cumplir 0 años

#3

r3 = int(input("Introduce un número y te diré todos los pares que hay entre 0 y ese número"))

print("Los pares son: ")
for numeros in range(r3):
    
    if numeros % 2 == 0:
        print(numeros)

#4
 

r4 = int(input("Dime un número y te diré si es primo "))
primo = True

for i in range (2, r4):
    if r4 % i == 0:
        primo = False
        break
   
if primo:
    print(f"{r4} es primo")
elif r4 == 1:
    print("es primo")
else:
    print(" No es primo")


#5
n = int(input("Introduce un número entero: "))

for fila in range(1, n+1, +1):   # el de la izquierda es lo que se va a imprimir  medio es el RANGO DE 1  A N SE HARA HASTA QUE SEA menor que n y -1 es lo que se le quita a la n
    for cantidad in range(fila):
        print("*", end=" ")
    
    print()   

#6 contador

for izquierda in range (0, 10, +1):
    for derecha in range (0,10):
        print(f"{izquierda} - {derecha}", end = " ")
        print()


#7 contador reemplazando 3 por E

for a in range(0, 10, 1):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                for e in range(0, 10):
                    
                    contador= f"{a} - {b} - {c} - {d} - {e}"
                    contadorModificado=(contador.replace("3", "E"))  
                    print(contadorModificado)


