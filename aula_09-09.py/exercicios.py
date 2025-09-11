# 1 - Crie uma classe chamada Pessoa que tenha os atributos nome e idade. Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

# p1 = Pessoa("Maria", 25)
# p2 = Pessoa("João", 30)

# print("Nome:", p1.nome, "- Idade:", p1.idade)
# print("Nome:", p2.nome, "- Idade:", p2.idade)

# 2 - Expanda a classe Pessoa para incluir um método apresentar() que imprima uma frase como:"Olá, meu nome é João e tenho 25 anos.". Teste o método chamando-o a partir de um objeto.
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def apresentar(self):
#         print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# p1 = Pessoa("João", 25)
# p1.apresentar()

# 3 - Crie uma classe Carro com os atributos marca, modelo e ano. Use o método __init__ para inicializar esses valores. Crie três objetos e mostre suas informações

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")
    
carro01 = Carro("Chevrolet", "Onix", 2025)
carro02 = Carro("Fiat", "Uno", 2022)
carro03 = Carro("Renault", "Logan", 2024)

carro01.informacoes()
carro02.informacoes()
carro03.informacoes()

# #4 - Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos (por exemplo, mudar o ano). Imprima antes e depois da alteração.
# class Carro:
#    def __init__(self, marca,modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

