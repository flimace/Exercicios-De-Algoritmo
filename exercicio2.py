n = int(input("Digite um número inteiro: "))
if n % 2 == 0:
    soma = sum(range(2, n + 1, 2)) # 2 é o primeiro número par, n + 1 é o limite de adição e 2 é o passo para pegar apenas os números pares.
    print(f"A soma dos números pares de 1 até {n} é {soma}")
    
# range possui 3 argumentos: range(inicio, fim, passo)
# inicio = a repeticao começa a partir desse número
# fim = a repetição vai até esse número ou o argumento adiciona ou subtrai o valor
# passo = o valor que é adicionado a cada iteração, ou, o valor do pulo
# nessa situação, o passo é 2, então ele vai pular de 2 em 2 até chegar no limite do range, que é n + 1.