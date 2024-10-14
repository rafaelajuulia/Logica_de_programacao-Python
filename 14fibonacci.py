print("******FIBONACCI******")

n=int(input("quantos termos você quer mostrar? "))
a=0
b=1
conta=1
while conta<= n:
    c=a+b
    print(c)#não esquecer
    a=b
    b=c
    conta+=1
# Esse código vai pedir a quantidade de termos que você deseja saber
# da sequencia de fibonacci
# Os dois primeiros números da sequência de Fibonacci

a=0
b=1
for num in range(25):
    c=b
    b=a+b
    a=c
print(a)