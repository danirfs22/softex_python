from abc import ABC, abstractmethod

#INTERFACE DAS CLASSES COMCRETAS
class midia(ABC):
    @abstractmethod
    def ler_midia(): ...
    
class ebook(midia):
    def __init__(self, tipo:str, nome:str):
        self.tipo = tipo
        self.nome = nome
    def ler_midia(self) -> str:
        print(f"Lendo o ebook: {self.nome}")

class audio(midia):
    def __init__(self, tipo:str, nome:str):
        self.tipo = tipo
        self.nome = nome
    def ler_midia(self) -> str:
        print(f"Ouvindo a música: {self.nome}")

musica01 = audio("mp3", "florentina")
musica01.ler_midia()

#criando as fábricas
class fabric_midia(ABC):
    @abstractmethod
    def fabric_method(self) -> midia:
        pass
    
class fabric_ebook(fabric_midia):
    def fabric_method(self, tipo:str, nome:str):
       return ebook(tipo,nome)
    
ebook = fabric_ebook().fabric_method("mobi", "Crepusculo")
ebook.ler_midia()


