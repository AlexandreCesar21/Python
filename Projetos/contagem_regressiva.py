from time import sleep
print(" CONTAGEM REGRESSIVA ")
numero = int(input("Digite quantos segundos quer durar: "))
for a in range(1, numero+1):
    print(a)
    sleep(1)
print('FIM!')