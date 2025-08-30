tupla_vazia = ()
print(type(tupla_vazia))

tupla = ("casa", 2, [1,2,3], tupla_vazia) #não pode editar a tupla, mas sim a lista que estiver dentro dela
print(tupla)
tupla[2].append(6)
print(tupla)

tupla = ("João",)
print(type(tupla))
tupla_2 = ("João") #sem a vírgula, considera como string
tupla_3 = 1, 2, #mesmo sem os parênteses, considera como tupla
print(type(tupla_3))

tupla_nomes = ("João", "Pedro", "Sara")

lista_nomes = list(tupla_nomes)

tupla_nomes = tuple(lista_nomes)
print(tupla_nomes)
