lista_1 = ["Ana", "Maria", "Joana", 3, ["azul, rosa"]]
print(lista_1)

lista_1.insert(2, "Dani")
lista_1.append("vermelho")
print(lista_1)

lista_1.remove("Ana")
print(lista_1)

lista_2 = lista_1.copy
print(id(lista_1))
print(id(lista_2))

num = [2,7,3.5,24]
i=1
for i in num:
    print(i*5)

lista_num = [1,2,3,4,5,6]
print(lista_num[3:5])


