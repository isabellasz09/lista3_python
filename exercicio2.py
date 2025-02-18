#escreva um programa para exibir na tela o nome e a categoria de um lutador. o programa deve ler em STRING para o nome e o NUMERO REAL para o peso.
#conforme o peso ocorrera o enquadramento na categoria.

#maior ou igual a 52 e menor doque 65: categoria pena
#maior ou igual a 65 e menor doque 72: categoria leve
#maior ou igual a 72 e menor doque 79: categoria ligeiro
#maior ou igual a 79 e menor doque 86: meio médio 
#maior ou igual a 86 e menor doque 90: categoria médio
#maior ou igual a 90 e menor doque 100: meio pesado
#maior ou igual a 100: pesado
print("Isabella Carolina de Souza")
lutador=str(input("Nome do lutador:"))
peso=float(input("Digite o peso: "))
print(lutador)
if peso >= 52 and peso < 65:
    print("{} sua categoria é pena".format(lutador))
elif peso >= 65 and peso < 72:
    print("{} sua categoria é leve".format(lutador))
elif peso >= 72 and peso < 79:
    print("{} sua categoria é ligeiro".format(lutador))
elif peso >= 79 and peso < 86:
    print("{} sua categoria é meio medio".format(lutador))
elif peso >= 86 and peso < 90:
    print("{} sua categoria é medio".format(lutador))
elif peso >= 86 and peso < 100:
    print("{} sua categoria é meio pesado".format(lutador))
elif peso >= 100:
    print("{} sua categoria é pesado".format(lutador))
else:
    print("categoria invalida")
    