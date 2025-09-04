# 1 - Escreva um programa que peça ao usuário para digitar um número. Trate o erro caso ele digite algo que não seja um número inteiro.

# try:
#     idade = int(input("Digite um número: "))
# except ValueError:
#     print("Só informar número inteiro")

# 2 - Peça ao usuário dois números e tente multiplicá-los. Se o usuário digitar algo inválido, exiba uma mensagem de erro
# try:
#     num1 = int(input("Informe o primeiro numero: "))
#     num2 = int(input("Informe o segundo numero: "))
#     mult = num1*num2
#     print(mult)
# except:
#     print("Só informar numeros")

# #3 - Crie um programa que peça ao usuário um número inteiro. Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.
# try:
#     num1 = int(input("Informe o primeiro numero: "))
#     num2 = int(input("Informe o segundo numero: "))
#     mult = num1*num2
#     print(mult)
# except:
#     print("Só informar numeros")
# else:
# #     print(mult)

# # 4 - Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.
# try:
#     arquivo = open('dados.txt')
#     print("Arquivo aberto com sucesso!")
# except FileNotFoundError:
#     print("O arquivo 'dados.txt' não foi encontrado.")
# finally:
#     print("Encerrando programa.")

#5 - Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se b for igual a zero. Caso contrário, retorne o resultado da divisão.

def divisao (a,b):
    if b==0:   
        raise ZeroDivisionError ("não é possivel dividir por zero")
    return a/b
try:
    a = int(input("Informe o primeiro numero: "))
    b = int(input("Informe o segundo numero: "))
    resultado = a/b
except ZeroDivisionError as e:
    print(e)
print(resultado)

  
      
      

 
    
    

    