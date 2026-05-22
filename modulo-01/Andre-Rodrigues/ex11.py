nome = "Mariana Souza"
cargo = "Analista de Dados"
salario = 7850.50
anos_empresa = 3

print(f"Nome   : {nome}")
print(f"Cargo  : {cargo}")
print(f"Salário: R$ {salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print(f"Tempo  : {anos_empresa} ano(s) de empresa")