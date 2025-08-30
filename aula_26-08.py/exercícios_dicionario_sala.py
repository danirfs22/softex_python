# 1 - Crie um dicionário vazio chamado cadastro e adicione os seguintes pares chave-valor:
# cadastro = { }
# cadastro["nome"] = "Lucas"
# cadastro["idade"] = "25"
# cadastro["email"] = "lucas@email.com"
# print(cadastro)

#2 - Usando o dicionário abaixo, use o método .get() para obter o valor da chave "telefone", retornando "Não informado" se a chave não existir.

# cliente = {"nome": "Amanda", "idade": 31}
# telefone = False

# if telefone in cliente:
#     print(dicionario.get(telefone))
# else:
#     print("Telefone Não informado")
#     print(cliente)

#3 - Utilize um laço for para imprimir todas as chaves do dicionário abaixo.

# livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}
# for chave, valor in livro.items():
#     print(f"{chave}: {valor}")

#4 - Adicione uma nova chave chamada "disponível" ao dicionário acima com o valor True.
# livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}
# # livro["disponível"] = True
# # print(livro)

# #5 - Use o método .pop() para remover a chave "ano" do dicionário livro. Imprima o valor removido.
# livro.pop("ano")
# print(livro)

#6 - Crie um dicionário compras com pelo menos 3 itens (nome do produto como chave e preço como valor). Em seguida, use .values() para calcular o total da compra.

# compras = {"arroz": 4, "leite": 6, "café": 15}
# total = sum(compras.values())

# print(f"O total da compra é:{total}")

# 7 - Dado o dicionário:

# frutas = {"maçã": 3, "banana": 5, "laranja": 2}
# # Imprima as frutas que têm mais de 2 unidades usando um laço for.
# for fruta, quantidade in frutas.items():
#     if quantidade > 2:
#         print(f"{fruta}:{quantidade} unidades")

#8 - Verifique se a chave "senha" está presente no dicionário abaixo. Se não estiver, adicione-a com o valor "123456".

# usuario = {"login": "joaosilva"}
# senha = 123456
# if senha in usuario:
#     print(senha)
# else:
#     usuario.update({"senha":123456})
#     print(usuario)

#9 - Use o método .items() para iterar sobre o dicionário abaixo e imprima frases como "A capital de SP é São Paulo".

# capitais = {"SP": "São Paulo", "RJ": "Rio de Janeiro", "MG": "Belo Horizonte"}      
           
# for estado, capital in capitais.items():
#     print(f"A capital de {estado} é {capital}")


#Dado o dicionário abaixo, atualize o valor da chave "estoque" somando 10 unidades ao valor atual.

produto = {"nome": "Teclado", "estoque": 15}
produto.update({"estoque":15+10})
print(produto)