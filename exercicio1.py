#escreva um programa que forneça um tipo de aplicação financeira adequado a um investidor a partir de dois dados recebidos:
#grau de aceitação de risco e o valor a ser investido.
#o grau de aceitação de risco deve ser lido no teclado na forma BX ou AL, se o valor fornecido algo diferente disso o programa deve mostrar uma mensagem indicando que foi fornecido dado invalido.
#Para o valor, deve ser um numero REAL
print("Isabella Carolina de Souza")
aceitação = input("insira o grau de aceitação o seu investimento (BX/AL)")
investimento = float(input("agora, insira o valor de investimento "))
if aceitação == "BX":
    if investimento < 1.000:
        print("invista na poupança")
else:
    print("invista na renda fixa")
if aceitação == "BX":
    if investimento < 1.000:
        print("invista na bitcons")
else:
    print("invista na ações")