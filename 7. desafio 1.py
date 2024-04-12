# escreva um programa para aprovar o empréstimo bancçario para a compra de uma casa. O programa vai perguntar o valor da casa, o salçario do computador e em quantos anos ele vai pagar. calcule o valor da prestação mensal, sabendo que ela nçao pode exceder 30% do salario ou então o emprestimo sera negado.
valor_casa = float(input("Valor da casa: "))
salario = float(input("Valor do salário: "))
prazo = float(input("Em quantos anos pretende pagar: "))
valor_mensal = valor_casa / (prazo*12)
print(f"A prestação mensal será de {valor_mensal:.2f}")
if valor_mensal <= (salario*0.30):
    print("Parabéns! Seu empréstimo foi concedido.")
else:
    print("infelizmente, seu emprétimo foi negado. ")