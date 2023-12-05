buscar =5

for numero in range (10): #este bucle itera 10 veces sobre la variable creada número (va de 0 a 9) 
    
    if numero == 5:  #Busca el valor 5, si este se encuentra lo imprime
        print ("El 5 está en la lista")
        break  #este break es importante para que salga del codigo una vez lo encutre
    else:
        print("No está")
        #aqui no hay que poner break ya que el for busca valor por valor y el 0 por ejemplo no es = buscar entonces
        #si lo  pusieramos se cumpliria la funcion del else y saldria del codigo



        buscar =7


for numero in range (10): #este bucle itera 10 veces sobre la variable creada número (va de 0 a 9) 
    
    if numero == 5:  #Busca el valor 5, si este se encuentra lo imprime
        print ("El 5 está en la lista")
    if numero !=7:
        print("No está") #aqui dice las posiciones en la que no se cumple la condición



for letra in "Hola que tal":   #simlemente recorre el string letra por letra
    print(letra)    