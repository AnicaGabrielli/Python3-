#desenvolova um programa que receba a distancia de uma viagem. Em caso de vigens ate 200km, cobre R$ 0.50 por km, em viagens maiores, cobre R$ 0.40 por km.
distancia = float(input("Qual a distância da sua viagem em km ? "))
'''if distancia <= 200:
    preco = distancia*0.50
else:
    preco = distancia*0.45'''
preco = distancia*0.50 if distancia<=200 else distancia*0.45
print(f"O valor da passagem será de {preco:.2f}")
