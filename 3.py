#concersor de celsius para fazenda
C = int(input("Digite a temperatura em Celsius: "))
F = (9/5)*C+32

print(f'A temperatura convertida de Celsius para Fatentait é: {F}\n ')

#calculo do aluguel de um carro
print('calculo do aluguel de um carro\n')
dia = int(input('Quantos dias você ficou com o automóvel?\n '))
km = float(input('Quantos km você rodou?\n '))
preco_dia = dia*60
preco_km = km*0.15
preco_final = preco_dia +preco_km

print(f'O preço a pagar pelo aluguel do carro é {preco_final} reais.')

