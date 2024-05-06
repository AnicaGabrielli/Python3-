#escreva um desafio que leia a velocidade de um carro e, caso ela esteja acima de 80, imprima que o morista foi multado e a multa. A multa é de 7 reais por km acima do permitido.
velocidade = float(input("Qual a velocidade atual do seu veículo? "))
if velocidade > 80:
    print("MULTADO! A sua velocidade está acima do limite.")
    multa = (velocidade-80)*7
    print(f'A sua multa foi de {multa:.2f} R$.')
print("Dirija com segurança. Tenha um bom dia!")
