#mais usado para trabalhar com dados, pode ver quantos elementos repetidos existem, não são ordenados e nem indexados
#não permite repetição de valores

livros = {"Duna", "Hannibal", "O pistoleiro"}
for livro in livros:
    print(livros)

    print("Hannibal" in livros)

    #depois de adicionado, um item não pode mais ser modificado
    livros = {"Duna", "Hannibal", "O pistoleiro"}
    livros_terror = ["Cujo", "IT", "Drácula"]
    livros.update(livros_terror) #usado quando quiser adicionar mais de 1 item
    print(livros)

