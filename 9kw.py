consumo= float(input("qual consumo? "))
conta=input("qual a instalação que deseja fazer? (r,c,i) ")
if conta == "r":
    if consumo<= 500:
        preco =0.40
    else:
        preco=0.65
elif conta == "c":
    if consumo<= 1000:
        preco=0.55
    else:
        preco=0.50
elif conta == "i":
    if consumo  <= 5000:
        preco=0.55
    else:
        preco=0.60
valor= consumo*preco
print("o valor a ser pago sera: R$%.2f" % valor)