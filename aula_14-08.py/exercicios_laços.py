for i in range(1,11):
    print(i)

num = int(input("Digite um número:"))
for mult in range(1,11):
    mult*=num
    print(mult)

soma = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    soma += numero

print("A soma dos números digitados é:", soma)
