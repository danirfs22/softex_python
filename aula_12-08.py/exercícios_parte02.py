a = 10
b = 3
soma = (a+b)
subtraçao = (a-b)
multiplicaçao = (a*b)
divisao = (a/b)
divisao_inteira = (a//b)
resto = (a%b)
potencia = (a**b)
print({soma}, {subtraçao}, {multiplicaçao}, {divisao}, {divisao_inteira}, {resto}, {potencia})

num1 = int(input("digite o primeiro numero:"))
num2 = int(input("digite o segundo numero:"))

print("soma", num1+num2)
print("subtraçao", num1-num2)
print("multiplicaçao", num1*num2)

if    num2!=0:
    print("divisao", num1/num2) 
else:
    print("o segundo numero tem que ser diferente de zero")

idade = int(input("digite a sua idade:"))
dias = 365*idade

print(f"você já viveu: {dias} dias")

largura = int(input("digite uma largura:"))
altura = int(input("digite uma altura:"))

area = largura*altura
print(f"a área do retângulo é: {area}")

compra = float(input("valor da compra:"))
valor_pago = float(input("valor pago:"))
troco = valor_pago - compra
print(f"seu troco é: R$ {troco}")

