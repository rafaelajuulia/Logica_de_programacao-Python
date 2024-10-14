capital=float(input("informe o capital inicial: "))
juros=float(input("informe os juros utilizados: "))
tempo=int(input("informe o tempo em meses: "))
calculom=capital*(1+juros/100)**tempo
print(calculom)# Não esquecer
if calculom>=0.1:
    print("Os juros ja renderam mais que 10%")
else:
    print("Os juros ainda não renderam mais que 10%")

# Esse código serve para que o usuário informe 
# o valor monetário, e que o programa calcule 
# juros compostos aplicados ao longo de um 
# intervalo de tempo, e diga se os juros já 
# renderam mais que 10% Crie um programa em Python que receba um valor monetário e calcule juros compostos aplicados ao longo de um intervalo de tempo, e diga se os juros já renderam mais que 10%
