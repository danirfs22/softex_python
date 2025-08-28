num = input("Informe um número de 1 a 5:")
match num:
    case "1" | "um":
        print("Você digitou 1")
case "2":
print("Você digitou 2")
case "3":
print("Você digitou 3")
case "4":
print("Você digitou 4")
case "5":
print("Você digitou 5")
case _:
print("Valor informado não encontrado")


num = input("Informe um número de 1 a 5:")
match num:
    case "1" | "2" | "3" | "4" | "5":
print(f"você digitou {num}")

num = input("Informe um número de 1 a 5:")
match num:
    case "1" | "2" | "3" | "4" | "5" if int(num) % 2 ==0:
    print(f"você digitou {num} que é par")
case_:
print("o valor informado não é par")
# Sistema de catalogação de livros
while True:
    opcao = input("Escolha uma opção:\n" \
    "1 - Adicionar um livro\n" \
    "2 - Editar informação de um livro cadastrado\n" \
    "3 - Pesquisar por um livro\n " \
    "4 - Deletar um livro\n" \
    "0 - Sair")

    match opcao:
        case "1":
            print("adicionando livro")
        case "2":
            print("editando um livro")
        case "3":
            print("pesquisando um livro")
        case "4":
            print("deletando um livro")
        case "0":
            break
        case _:
            print("Opção inválida")