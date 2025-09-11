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

# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

#     def informacoes(self):
#         print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")
    
# carro01 = Carro("Chevrolet", "Onix", 2025)
# carro02 = Carro("Fiat", "Uno", 2022)
# carro03 = Carro("Renault", "Logan", 2024)

# carro01.informacoes()
# carro02.informacoes()
# carro03.informacoes()

# #4 - Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos (por exemplo, mudar o ano). Imprima antes e depois da alteração.
# class Carro:
#    def __init__(self, marca,modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

#5 - Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método depositar(valor) que aumenta o saldo e um método sacar(valor) que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques.
class ContaBancaria:
   
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.operacoes = []

    def __str__(self):
        return f"Conta do titular {self.titular} tem {self.saldo} de saldo"
    
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["Deposito", valor])
        print(f"Foi depositado {valor} reais na sua conta")
    
    def saque(self, valor):
        self.saldo -= valor
        self.operacoes.append(["Saque", valor])
        print(f"Foi sacado {valor} reais na sua conta")

    def extrato(self):
        for operacao in self.operacoes:
            print(operacao)
        print(f"Saldo: {self.saldo}")

conta1 = ContaBancaria("João",60)
conta2 = ContaBancaria("Bruna", 1000)

print(conta1)
print(conta2)

conta1.deposito(300)
conta1.saque(100)
conta2.saque(250)
conta1.extrato()