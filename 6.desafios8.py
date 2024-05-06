#faça um programa que receba as medidas de tres retas e mostre se elas podem formar ou não um triangulo.
r1 = float(input("Qual o comprimento da reta 1? "))
r2 = float(input("Qual o comprimento da reta 2? "))
r3 = float(input("Qual o comprimento da reta 3? "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print("Sim, pode-se formar um triângulo!")
else:
    print("Não podemos formar um triangulo.3")
