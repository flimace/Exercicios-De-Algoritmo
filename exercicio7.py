tentativas = 0
senha_correta = "12345"

def verificar_senha():
    global senha_correta
    global tentativas

    while True:
        senha_usuario = str(input("Digite a senha: "))
        if senha_usuario == senha_correta:
            print("Senha correta! Acesso permitido.")
            break
        else:
            print("A senha está incorreta! Tente novamente.")
            tentativas += 1
            print(f"Você tentou {tentativas} vezes.")
verificar_senha()
