matriz2x2 = [[1.2], [3,4]]
matriz3x2 = [[1,2],
             [3,4],
             [5,6]]
print(matriz[1])
print(matriz[1][2]) #primeiro o indice, depois o elemento
matriz[1][2] = "a"

#matriz com list comprehension

matriz = [[0 for i in range(3)] for x in range(3)] #primeiro item é o valor que quer adicionar
print(matriz)

matriz = [[i for i in range(3)] for x in range(3)]
lista = [1,2,3]
matriz = [[i for i in lista] for x in range(3)]
        
matriz2 = []
for i in range(3):
            sublista=[]
            matriz2.append(sublista)
            for x in range(3):
                sublista.append(x)
            print(matriz2)
