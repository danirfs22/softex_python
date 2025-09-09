class Cachorro:
    especie = "Canis lupus familiaris"
    def __init__(self, nome,raca, idade): # Método construtor - o self é obrigatorio
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def __str__(self):
        return f"Especie: {self.especie}\nNome: {self.nome}\nRaça: {self.raca}\nIdade: {self.idade}"

doguinho01 = Cachorro("Rex", "caramelo", 2)
print(doguinho01)

#adicionando metodos
def latir(self):
    print("AU AU")

auau1 = Cachorro("Bob", "Pinscher", 15)
print(auau1)
auau1.latir()

