nome = "Mariana Souza"
cargo = "Analista de Dados"
salario = 7850.50
anos = 3

salario_formatado = f"{salario:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")

print("=============================")
print("     FICHA DO FUNCIONÁRIO    ")
print("=============================")
print(f"Nome   : {nome}")
print(f"Cargo  : {cargo}")
print(f"Salário: R$ {salario_formatado}")
print(f"Tempo  : {anos} ano(s) de empresa")
print("=============================")
