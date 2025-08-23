x = int(input("Informe o primeiro numero:"))
y = int(input("Informe o segundo numero:"))
operacao = input("Informe a operaçao")

if  y !=0:
    print (x/y)
elif True:
    print ("Ok")
else:
    print("O valor informado para o segundo numero tem que ser diferente de 0")

#menor de idade -> paga meia
#adulto -> não tem promoção
# idoso tem gratuidade

# Sistema promocional cinema

idade_cliente = int(input("Informe a idade do cliente: "))
dia_quarta = input("É quarta-feira?")

if idade_cliente>=60:
    print("cortesia de 100%")
elif dia_quarta == "s":
    print("cortesia de 50%")
else:
    if  idade_cliente<18:
        print("Cliente paga meia")

    elif idade_cliente>=50:
        print("cortesia de 10%")
    else:
        print("cliente sem cortesia")