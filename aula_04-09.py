#Erros e exceções
# Lidando com Exceções:
# try
# except (retorna o erro)
#else - não é obrigatório
# finally -  não é obrigatório (independente se der erro ou não, ele roda) - ideal p encerrar conexão com banco de dados
# raise - pode editar a mensagem de erro que quer passar para o usuário
# pode criar uma classe com o erro que você quer que apareça a mensagem, no Exception
try:
    num1 = 5
    num2 = 0
    divisao = num1/num2
except:
    print("nao é possivel dividir por zero")

    try:
    num1 = int(input("Informe o primeiro numero"))
    num2 = int(input("Informe o segundo numero"))
    num1/num2
except ZeroDivisionError:
    print("nao é possivel dividir por zero")
except ValueError:
    print("Só informar numeros")
except:
    print("algo deu errado, contate o suporte")
else:
    print(divisao)
finally:
    print("qualquer coisa")

raise

idade = int(input("informe a idade:"))
if idade <= 0:
    raise ValueError("idade não compatível")
    raise Exception("idade tem que ser maior que zero")

class erroIdade(Exception):
    pass
try:
    idade = int(input("informe a idade:"))
    if idade <= 0:
        raise Exception("idade tem que ser maior que zero")
except TypeError:
    print("apenas numeros")
except erroIdade:
    print(erroIdade)


