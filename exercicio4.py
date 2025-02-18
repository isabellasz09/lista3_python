#no senailandia mulheres e homens podem servir o exercito do pais.
#O serviço e opcional e é muito comum que as pessoas se apresentem para o serviço em algum momento da vida existe uma única restrição 
#para o ingresso, que e a idade da pessoa:

#letra A: para mulheres a idade aceita é entre 21 e 34 anos
#letra B: para homens a idade aceita e entre 18 e 39 anos 
#escreva um programa que leia ter dados de entrada: NOME,IDADE é SEXO e informe se a pessoa será aceita ou não para p serviço.
#obs.: Para o sexo deve ser lido apenas um caractere que pode ser "f" ou "F" para feminino, "m" ou "M" para masculino qualquer coisa diferente deve ser informado
nome=input("Qual seu nome: ")
idade=int(input("qual sua idade: "))
sexo=input("Qual seu sexo: ")
if sexo == "F".lower() and idade >=21 and idade <=34:
    print("Você pode servir")
elif sexo == "f".lower() and idade >=21 and idade <=34:
    print("Você pode servir")
elif sexo == "M".lower() and idade >=18 and idade <=39:
    print("Você pode servir")
elif sexo == "m".lower() and idade >=18 and idade <=39:
    print("Você pode servir")
else: 
    print("Voce nao podde servir")