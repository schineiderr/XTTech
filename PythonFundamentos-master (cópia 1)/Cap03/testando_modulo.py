import Lab02.calculadora_v1

print("Selecione o número da operação desejada:\n")
print("1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão\n5 - Fechar")
op = input("Digite sua opcao (1/2/3/4/5): ")

while op != '5':
    try:
        op = int(op)
        calculadora(op)
    except:
        print("Opssao imválida.\n")
        
    op = input("Digite sua opcao (1/2/3/4/5): ")
else:
    print("Programa Fechado - Obrigado por me usar e abusar de mim")
