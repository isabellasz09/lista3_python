#escreva um programa que forneça um tipo de aplicação financeira adequado a um investidor a partir de dois dados recebidos:
#grau de aceitação de risco e o valor a ser investido.
#o grau de aceitação de risco deve ser lido no teclado na forma BX ou AL, se o valor fornecido algo diferente disso o programa deve mostrar uma mensagem indicando que foi fornecido dado invalido.
#Para o valor, deve ser um numero REAL
print("Isabella Carolina de Souza")
aceitação = input("insira o grau de aceitação o seu investimento (BX/AL): ")
investimento= float(input("Agora, insira o valor de investimento: "))
if aceitação == 'Bx':
    if investimento < 1000.00:
        print("Invista na Renda Fixa")
    else:
        print("Invista na poupança")
if aceitação == 'Al':
    if investimento < 1000.00:
        print("Invista em Bitcoins")
    else:
        print("Invista em ações")