# calcula a área de uma parede (largura*altura ) mostra o valor e quantos litros de tinta precisa par pintá-la sabendo que 1l pinta 2m²

largura = float(input('Digite o valor da largura da parede: '))
altura = float(input('Digite o valor da altura: '))
m = largura*altura
qtinta = m/2
print(f'A metragem quadrada da parede é {m} e a quantidade de litros de tinta nescessária para pintar a parede é {qtinta}\n')

#recebe o preço de um produto e mostra ele com 5% de desconto.
preco = float(input('Digite o preço do produto:'))
desconto = preco - (preco*(5/100))
print(f'O valor do produto com desconto é: {desconto}\n')

#recebe o salário de um funcionário e mostra ele com 5% de aumento
salario = float(input('Digite o seu salário:'))
aumento = salario + (salario*(5/100))
print(f'O valor do salario com aumento de 5% é: {aumento}')

