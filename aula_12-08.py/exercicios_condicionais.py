# num = int(input("Digite um número:"))
# if num%2==0:
#     print("Esse número é par!")
# else:
#     print("Esse número é ímpar!")

# nota = float(input("Digita a nota do aluno:"))

# if nota<5:
#     print("Reprovado")
# elif nota>=7:
#     print("Aprovado")
# else:
#     print("Recuperação")
    
# num1 = float(input("Digite o primeiro número:"))
# num2 = float(input("Digite o segundo número:"))

# if num1>num2:
#     print("O primeiro número é maior")
# else:
#     print("O segundo número é maior")
# if num1==num2:
#     print("os números são iguais!")

# idade = int(input("Digite sua idade:"))
# if idade>=65:
#     print("Idoso")
# elif idade<=12:
#     print("Criança")
# elif idade>=18:
#      print("Adulto")
# else:
#     print("Adolescente")


# for i in range(1,11):
#     print(i)

num =(int(input("Informe um número:")))

for i in range(1,11):
    print(f"{num} x {i} = {num * i}")


soma = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    soma += numero

print("A soma dos números digitados é:", soma)





