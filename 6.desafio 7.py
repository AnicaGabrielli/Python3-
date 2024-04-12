#escreva um progama que pergunte o salário de um funcionário e de o valor do seu aumento. Para salários superiores a R$ 1250, calcule um aumento de 10%, para inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o seu salario? '))
if salario > 1250:
    salario = salario * 1.10
else:
    salario = salario*1.15
print(f'Seu salário atual com aumento é {salario}')