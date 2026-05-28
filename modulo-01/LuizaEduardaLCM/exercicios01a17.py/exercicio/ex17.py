descricao = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade: "))
preco = float(input("Digite o preço do produto: "))
subTotal = quantidade * preco
imposto = subTotal * 0.12
              
print("===== NOTA FISCAL =====")
print("Produto       : ", descricao)
print("Quantidade    : ", quantidade)
print("Preço unitário: R$ ", preco)
print("Subtotal      : R$ ", subTotal)
print("Imposto       : R$ ", imposto)
print("Total         : R$ ", subTotal + imposto)
print("=======================")