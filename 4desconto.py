sapato = float(input("informe o valor do item"))
desconto = float(input("informe o valor do desconto"))
d = (desconto/ 100)* sapato
print("o valor do desconto é R$%.2f e o valor a ser cobrado pelo sapato é R$%.2f " %(d,sapato-d))  # correto