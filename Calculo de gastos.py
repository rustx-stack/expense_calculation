valor = input("Digite o valor do maço: R$ ")
valor = float(valor)

macos = input("Quantidade de maços por dia: ")
macos = float(macos)

anos = input("Quantidade de anos: ")
anos = float(anos)

custo = valor * macos * anos * 365

print(f"Você já gastou R$ {custo:.2f} fumando!")