frutas = ["limão", "banana", "morango", "coco"]
#print(frutas)

#adicionando elementos:
frutas.insert(1, "manga") #no insert tem que especificar o indice antes
print(frutas)

frutas.append("kiwi") #append adiciona sempre no final
print(frutas)

frutas_vermelhas = ["morango", "uva", "amora", "framboesa"]
frutas+=frutas_vermelhas
print(frutas)

#Remover elementos
print(frutas.count("morango"))
frutas.remove("morango") # o remove tem que escrever o que quer ser removido
print(frutas)
print(frutas.count("morango"))

print("primeiro pop")
frutas.pop() #sem especificar, remove o último elemento da lista
print(frutas)

print("segundo pop")
frutas.pop(4) #pode especificar o índice

del frutas[5:7]
print(frutas)



numeros = [3, 5, 77, 4, 1]
numeros2 = numeros

numeros2.append("42")

#cópia de lista
frutas2 = frutas[:]
frutas2 = frutas.copy()

frutas.extend(["jaca", "mamao"]) #adiciona varios elementos ao final da lista
frutas.index("morango")
print(frutas.index("morango")) #mostra o índice do elemento que você quer

frutas.sort() #ordena em ordem alfabetica
frutas.reverse() # ordena na ordem inversa
print(sorted(frutas)) #coloca na ordem alfabetica


'''
num1 = 3
print(id(num1))
num2 = num1
print(id(num2))
'''
