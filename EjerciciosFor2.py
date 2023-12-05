#Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo

r8 = int(input("Escribe un número entero")) 


r9 = int(input(f"Escribe un número entero mayor que {r8}")) 

while r9 <= r8:
    print("Error. El segundo número debe ser mayor que el primero.")
    r9 = int(input(f"Intenta de nuevo. Escribe un número entero mayor que {r8}: "))

for i in range (r8, r9 + 1):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
         print(f"{i} no es par") 


#9 Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

r9 = -1
while r9<0:
    r9 = int (input("Escribe un número mayor que cero"))

    if r9<0:
        print("Humano, tiene que ser mayor que 0")
    


for i in range(1, r9+1):
    
    if r9 % i == 0:
        print(i)

#10        