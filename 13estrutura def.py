def exibiMenu():
    print ("##### MENU #####\n")
    print("0- SAIR\n")
    print("1- SOMAR\n")
    print("2-SUBTRAIR\n")
    print("3-MULTIPLICAR\n")
    print("4-DIVIDIR\n")
    
    opcao = int(input("escolha uma opção: "))
    return opcao
def somar (numero1,numero2):
    resultado= numero1 +numero2
    return resultado
def subtrair (numero1,numero2):
    resultado= numero1-numero2
    return resultado
def multiplicar(numero1,numero2):
    resultado = numero1*numero2
    return resultado
def dividir (numero1,numero2):
    resultado=numero1/numero2
    return resultado



i=0
opcao=1
num1=0
num2=0
resultado=0

while opcao!=0:
    opcao=exibiMenu()
    if opcao<=0:
        break
    
    num1=float(input("imforme o primeiro número para a operação: "))
    num2=float(input("informe o segundo número para a operação: "))
    if opcao ==1:
        resultado= somar(num1,num2)
    if opcao ==2:
        resultado= subtrair(num1,num2)
    if opcao ==3:
        resultado= multiplicar(num1,num2)
    if opcao ==4:
        resultado= dividir(num1,num2)
        
    print("resultado: %.1f\n\n" %resultado)


    
    

    














