#condições aninhadas - condições dentro de condições
nome = str(input("QUAL É O SEU NOME?")).upper()
if nome == "GUANABARA":
    print(f"QUE NOME BONITO!")
elif nome == "PEDRO" or nome == "MARIA" or nome =="PAULO":
    print("SEU NOME É BEM COMUM NO BRASIL.")
elif nome in 'ANA CLÁUDIA JÉSSICA JULIANA':
    print("BELO NOME FEMININO!")
else:
    print("SEU NOME É BEM NORMAL.")
print(f"TENHA UM BOM DIA, {nome}!")