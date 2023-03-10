print(" TABUADA ")
while True:
    numero = int(input("Digite um número: "))
    for a in range(1, 11):
        print(f"{numero} + {a} = {numero+a}")
    resp = str(input("Quer continuar? [S/N]: ")).strip().upper()
    while resp not in 'SsNn':
        resp = str(input("\033[0;31mPor favor digite [S OU N]: \033[m")).strip().upper()
    if resp in 'Nn':
        break
print("="*30)    
print("{:^30}".format("OBRIGADO VOLTE SEMPRE!"))
print("="*30)
