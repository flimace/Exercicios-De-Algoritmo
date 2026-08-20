contador = 0
nota = 0 
while 5 > contador:
    nota += int(input("Digite aqui a nota do aluno: "))
    contador = contador + 1

media = nota / 5
print(f"A média do aluno é: {media}")