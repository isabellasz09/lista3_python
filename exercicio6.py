#as eleições municipais, os municípios com 200.000 eleitores
#ou mais tem segundo turno caso o primeiro colocado não tenha mais doque 50% dos votos.
#escreva um programa que leia: A QUANTIDADE DE ELEITORES, QUANTIDADE DE VOTOS e informe se haverá segundo turno ou não
cidade = input("Qual a cidade: ")
vts_candidato= int(input("Quantidade de votos do candidato: "))
num_votos= int(input("Qual a quantidade de votos: "))
porcentagem= num_votos/vts_candidato
if porcentagem <= 0.50:
    print ("Haverá segundo turno na",cidade)
else:
    print("Não haverá segundo turno")
