frutas = ["limão", "banana", "morango", "coco", "banana"]
contagem_fruta = frutas.count("banana")
print(contagem_fruta)

while "banana" in frutas:
    frutas.remove("banana")

    lista1 = [num for num in range(10)] #cria uma lista de 0 a 9
    print(lista1)
    lista2 = [num for num in range(10) if num %2 ==0] #lista com numeros pares
    print(lista2)