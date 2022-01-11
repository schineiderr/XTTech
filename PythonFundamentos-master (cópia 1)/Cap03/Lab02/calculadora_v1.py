# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************\n")

def calculadora(opcao):
    if opcao == 1:
        n1 = int(input("Digite o primeiro numero: "))
        n2 = int(input("Digite o segundo numero: "))
        soma = n1 + n2
        print(f"{n1} + {n2} = {soma}\n")

    elif opcao == 2:
        n1 = int(input("Digite o primeiro numero: "))
        n2 = int(input("Digite o segundo numero: "))
        subtracao = n1 - n2
        print(f"{n1} - {n2} = {subtracao}\n")

    elif opcao == 3:
        n1 = int(input("Digite o primeiro numero: "))
        n2 = int(input("Digite o segundo numero: "))
        multiplicacao = n1*n2
        print(f"{n1} * {n2} = {multiplicacao}\n")

    elif opcao == 4:
        n1 = int(input("Digite o primeiro numero: "))
        n2 = int(input("Digite o segundo numero: "))
        divisao = n1/n2
        print(f"{n1} / {n2} = {divisao}\n")

    else:
        print("Opssão imválida.\n")

print("Selecione o número da operação desejada:\n")
print("1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão\n5 - Fechar")

op = input("Digite sua opcao (1/2/3/4/5): ")
while op != '5':
    try:
        op = int(op)
        calculadora(op)
    except:
        print("Opssao imválida.\n")
        
    op = input("Digite sua opcao (1/2/3/4): ")
else:
    print("Programa Fechado - Obrigado por me usar e abusar de mim")










    
