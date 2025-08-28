def ola():
    print("Olá mundo")

ola()

def ola(msg):
    print(msg)

ola("Olá mundo")

def soma(num1, num2):
    valor_somado = num1+num2
    return valor_somado
valor = soma (2,2)
print(f"A soma retornou: {valor}")

valor_somado
def soma(num1, num2):
    global valor_somado = num1+num2
    valor_somado = num1+num2

if valor_somado >=1:
    return "maior que 1"

if valor_somado <=1:
    return "menor que 1"
valor = soma (0,12)
print(valor_somado)
