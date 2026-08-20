n = int(input("Digite um número inteiro: "))

if n < 2:
    print(f"{n} não é um número primo.")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} não é um número primo.")
            break
    else:
        print(f"{n} é um número primo.")
        
# número primo é um número natural maior que 1 que pode ser dividido apenas por 1 e por ele mesmo.