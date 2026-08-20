try:
    while True:
        valor = int(input(f"Digite um valor: "))
        if 1 <= valor <= 10:
            print(f"Você digitou o valor {valor}.")
            break
        else:
            print("O valor precisa estar entre 1 e 10. Tente novamente.")


except ValueError:
    print("Valor inválido. Por favor, digite um número inteiro.")

