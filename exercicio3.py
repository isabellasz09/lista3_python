#uma empresa financeira consegue empréstimos a pessoas físicas,
# quando o valor da parcela e menor 
#que 8% do salario da pessoa.
#escreva um programa que leia dois números REAIS o valor do salario 
#e o valor da parcela 
#informe se o empréstimo será concedido ou não.
print("Isabella Carolina de Souza")
salario = int(input("Digite o salario: "))
parcela = int(input("Digite o valor da parcela: "))
if parcela < 0.08 * salario:
    print("emprestimo concedido")
else:
    print("emprestimo negado")