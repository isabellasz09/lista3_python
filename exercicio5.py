#no comercio o conceito de margem bruta e uma porcentagem que e aplicada ao preço de custo, para se obter o preço de venda.
#uma loja tem como politica comercial de aplicar uma margem bruta 45%  
#quando o preço de custo e menor ou igual a 100, se um produto custa mais doque isso a margem bruta e de 35%
#escreva um programa que leia o preço de custo do produto que mostre na tela qual e o seu preço de venda com duas casas decimais
print("Isabella Carolina de Souza")
preco= input("Qual é o valor do produto: ")
if  preco <= 100:
    margem = (preco*0.45)
    print("O preço do produto {}".format(margem))
else:
    preco > 100
    margem =  (preco*0.35)+ preco
    print("O reço do produto {}".format(margem))