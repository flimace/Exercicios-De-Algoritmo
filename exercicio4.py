saldo = 0

def consultar_saldo():
    print(f"Seu saldo atual é de: R$ {saldo}")
    
def saque():
    global saldo # especificar se a variável é global ou local para poder ser alterada na função logo no início da função.
    saque = float(input(f"Digite o valor que deseja sacar: R$ "))
    if saldo >= saque:
        saldo -= saque
        print(f"Saque de R$ {saque} realizado com sucesso!")
    else:
        print("Saldo insuficiente para realizar o saque.")
        
def deposito():
    valor_depositado = float(input(f"Digite o valor que deseja depositar: R$ "))
    global saldo
    saldo = saldo + valor_depositado
    print(f"Depósito de R$ {valor_depositado} realizado com sucesso!")
    print(f"Seu saldo atual é de: R$ {saldo}")

while True:
    print("\n=== Menu ===")
    print("1. Consultar saldo")
    print("2. Sacar")
    print("3. Depositar")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        consultar_saldo()
    elif opcao == "2":
        saque()
    elif opcao == "3":
        deposito()
    elif opcao == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")