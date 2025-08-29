dict = {"casa":10} #tem que ter pelo menos 2 valores
# não pode repetir nome de chave, mas valor pode
#não é indexado

dicionario.popitem() #apaga o último "par" de itens da lista


#são ordenados, alterável e não aceita valores de chaves duplicados.

# No Python, os dicionários são definidos pelo uso de chaves com itens no formato chave:valor {chave:valor}. Seus itens são separados por virgula.


# Criando um dicionário
dicionario_vazio = {}
print(type(dicionario_vazio))
print(dicionario_vazio)

dicionario = {
    "nome": "Fred",
    "Idade": 30,
    "Nacionalidade": "Brasileiro",
    "Rico":False
}

print(dicionario)
     
<class 'dict'>
{}
{'nome': 'Fred', 'Idade': 30, 'Nacionalidade': 'Brasileiro', 'Rico': False}
#Acessando ítens

dicionario = {
    "id": 0,
    "nome": "Fred",
    "Idade": 36,
    "Nacionalidade": "Brasileiro",
    "Rico":False,
    "Filmes favoritos": "Sharknado", "Anaconda 3", "A balada do pistoleiro"
}

print(dicionario["nome"])
    
print(dicionario.get("nome"))

#Listando todos os ítens

print(dicionario.items())
     
dict_items([('nome', 'Fred'), ('Idade', 30), ('Nacionalidade', 'Brasileiro'), ('Rico', False)])
Listando todas as chaves

print(dicionario.keys())
     
dict_keys(['nome', 'Idade', 'Nacionalidade', 'Rico'])
Listando Valores

print(dicionario.values())
     
dict_values(['Fred', 30, 'Brasileiro', False])

#Adicionando ítens

dicionario["profissão"] = "Desenvolvedor"

print(dicionario)
     
{'nome': 'Fred', 'Idade': 30, 'Nacionalidade': 'Brasileiro', 'Rico': False, 'profissão': 'Desenvolvedor'}
#Adicionando e modificando ítens

dicionario["nome"] = "João"

print(dicionario)
     
{'nome': 'João', 'Idade': 30, 'Nacionalidade': 'Brasileiro', 'Rico': False, 'profissão': 'Desenvolvedor'}

dicionario.update({"Idade":25})
print(dicionario)
     
{'nome': 'João', 'Idade': 25, 'Nacionalidade': 'Brasileiro', 'Rico': False, 'profissão': 'Desenvolvedor', 'idade': 25}

dicionario.update({"Carro": True})
print(dicionario)
     
{'nome': 'João', 'Idade': 25, 'Nacionalidade': 'Brasileiro', 'Rico': False, 'profissão': 'Desenvolvedor', 'idade': 25, 'Carro': True}

#Removendo ítens

dicionario.pop("idade")
print(dicionario)
     
{'nome': 'João', 'Idade': 25, 'Nacionalidade': 'Brasileiro', 'Rico': False, 'profissão': 'Desenvolvedor', 'Carro': True}

dicionario.popitem()
print(dicionario)
     
{'nome': 'João', 'Idade': 25, 'Nacionalidade': 'Brasileiro', 'Rico': False, 'profissão': 'Desenvolvedor'}

dicionario.clear()
print(dicionario)
     
{}

dicionario = {
    "nome": "Fred",
    "Idade": 30,
    "Nacionalidade": "Brasileiro",
    "Rico":False
}

del dicionario["Rico"]
print(dicionario)
     
{'nome': 'Fred', 'Idade': 30, 'Nacionalidade': 'Brasileiro'}

del dicionario
print(dicionario)

#Copiando um dicionário

dicionario = {
    "nome": "Fred",
    "Idade": 30,
    "Nacionalidade": "Brasileiro",
    "Rico":False
}

dicionario2 = dicionario.copy()

print(f"Id de dicionario:  {id(dicionario)}\nId de dicionario2: {id(dicionario2)}")
     
Id de dicionario:  2480205868736
Id de dicionario2: 2480205858368

dicionario3 = dict(dicionario)
print(f"Id de dicionario:  {id(dicionario)}\nId de dicionario3: {id(dicionario3)}")
     
Id de dicionario:  2480205868736
Id de dicionario3: 2480206118464

#Iterando por um dicionário

for itens in dicionario.values():
    if itens == "Fred":
        print("Usuário localizado")
     

nomes_funcionarios =["Fred", "João", "Maria"]
dicionario_aleatorio = {
    "nomes":nomes_funcionarios,
    "função":["Desenvolvedor", "Tech Lead", "PO"],
}

print(dicionario_aleatorio["função"][2])
     
PO