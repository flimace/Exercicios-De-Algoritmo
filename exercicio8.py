numero_total_mercadoria = int(input("Digite o número total de mercadorias: "))
precos = []
try:
    for i in range(numero_total_mercadoria):
        preco = float(input("Digite o preço do produto: "))
        precos.append(preco)
except ValueError:
    print("Digite os valores em valores decimais.")
valor_total = sum(precos)
media = valor_total / numero_total_mercadoria 

print(f"O valor total em estoque é: R${valor_total}")
print(f"A média dos valores das mercadorias é: R${media}")
