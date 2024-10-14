emp= float(input("qual o valor do emprestimo: R$" ))
sal= float(input("Informe o seu salário:  R$ "))
meses= int(input("Em quantos meses deseja pagar? "))
prestacao= int(emp/(meses))
minimo= sal * 30/100
if prestacao <= minimo:
    print ("O emprestimo foi CONCEDIDO ")
    print("O valor da parcela a ser paga por mês é:", prestacao)
else:
    print ("Emprestimo NEGADO ") 



