produto= float(input("informe o valor do produto: R$"))
desconto= float(input("informe o valor do desconto (em %):"))
valor= produto* (desconto/100)
total=produto-valor
print("o desconto obtido foi de R$%.2f" % valor, "o valor total a ser pago é de R$%.2f" % total)