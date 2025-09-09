#Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.
class Pessoa:
    nome = "Maria"
    idade = 30
# pessoa1 = Pessoa
# print(pessoa1)


# 2 - Expanda a classe Pessoa para incluir um método apresentar() que imprima uma frase como:"Olá, meu nome é João e tenho 25 anos.". Teste o método chamando-o a partir de um objeto.

def apresentar(self):
    print("Olá, meu nome é João e tenho 25 anos")
    pessoa1 = Pessoa("João",25)
    pessoa1.apresentar()

# #3 - Crie uma classe Carro com os atributos marca, modelo e ano. Use o método __init__ para inicializar esses valores. Crie três objetos e mostre suas informações

# class Carro:
#    def __init__(self, marca,modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
    
# carro01 = Carro("Chevrolet", "Onix", 2025)
# print(carro01)

# #4 - Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos (por exemplo, mudar o ano). Imprima antes e depois da alteração.
# class Carro:
#    def __init__(self, marca,modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

