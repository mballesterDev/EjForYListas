#2 ordenar tres números

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

if num1 > num2 and num2 > num3:
    print(num1, num2, num3)
elif num1 > num3 and num3 > num2:
    print(num1, num3, num2)
elif num2 > num1 and num1 > num3:
    print(num2, num1, num3)
elif num2 > num3 and num3 > num1:
    print(num2, num3, num1)
elif num3 > num1 and num1 > num2:
    print(num3, num1, num2)
else:
    print(num3, num2, num1)               

#3 

n1 =-1
while n1 < 0 or n1 > 999:
    n1 = int(input("Introduce un número entre 0 y 999"))
if n1 < 0 or n1 > 999:
    print("Número inválido")


#4
correo = "correoejemplo@gmailcom"
contraseña = 12345

r1 = input("Introduce tu correo")

if r1 == correo:
    print("Son iguales")
else:
    print ("No son iguales")    

r2 = int(input("Introduce tu contraseña"))

if r2 == contraseña:
    print("Son iguales")
else:
    print ("No son iguales")  

#5    


