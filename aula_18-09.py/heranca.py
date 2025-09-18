class Mamifero:
   def __init__(self, especie, habitat):
    self.especie = especie
    self.habitat = habitat
   
    def __str__(self):
        return "O mamífero da espécie {self.especie}, da raça {self.raca} pode ser localizado no {self.habitat}",
   
   def movimentar(self):
     print("Caminhando")

   def amamentar(self):
     print("alimentando o filhote")

class Cachorro(Mamifero):
  def __init__(self, especie, habitat, raca):
    super().__init__(especie,habitat)
    self.raca = raca

def __str__(self):
    return f"{super().__str__()} da raça {self.raca}"

def correr_moto(self):
      print("O cachorro esta correndo atrás da moto")
    
dog01 = Cachorro("Canis familiaris", "Rua do seu zé", "caramelo")
print(dog01)
dog01.movimentar()
dog01.correr_moto()

# Herança hierárquica:
class Gato(Mamifero):
   def __init__(self, especie, habitat, raca, cor_olho):
    super().__init__(especie,habitat)
    self.raca = raca
    self.cor_olho = cor_olho

    def __str__(self):
        return "O mamífero da espécie {self.especie}, da raça {self.raca} com olhos na cor {self.cor_olho} pode ser encontrado no habitat {self.habitat}",
   
   def arranhar(self):
      print("o gato está arranhando o arranhador")
    
cat01 = Gato("Felinis", "Cama da vovó", "Siamês", "azul")
print(cat01)
cat01.arranhar()

# Herança múltipla:
class AnimaisVoadores:
   def movimentar(self):
     print("Voando")
    
class Morcego(Mamifero, AnimaisVoadores):
   ...

zubat = Morcego("Desmodus rotundus", "pé de jambo")
print(zubat)
zubat.movimentar()
Morcego.__mro__

# Herança multinível
class Animal:
  def __init__(self, especie, habitat):
    self.especie = especie
    self.habitat = habitat

class Mamifero(Animal):
    def movimentar(self):
     print("Caminhando")

    def __init__(self, especie, habitat):
    self.especie = especie
    self.habitat = habitat
   
    def __str__(self):
        return "O mamífero da espécie {self.especie}, da raça {self.raca} pode ser localizado no {self.habitat}",
   
    def amamentar(self):
     print("alimentando o filhote")

class Cachorro(Mamifero):
  def __init__(self, especie, habitat, raca):
    super().__init__(especie,habitat)
    self.raca = raca




# Herança híbrida
class Voadores:
   def movimentar(self):
     print("Voando")
    
class Aquaticos:
   