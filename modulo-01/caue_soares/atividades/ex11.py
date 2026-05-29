nome = "Mariana Souza"
cargo = "Analista de Dados"
salario = 7850.50
anos = 3

# Formata salário no padrão brasileiro (R$ 7.850,50)
inteiro = int(salario)
centavos = round((salario - inteiro) * 100)
salario_br = f"R$ {inteiro:,}".replace(",", ".") + f",{centavos:02d}"

print("=============================")
print("     FICHA DO FUNCIONÁRIO    ")
print("=============================")
print(f"Nome   : {nome}")
print(f"Cargo  : {cargo}")
print(f"Salário: {salario_br}")
print(f"Tempo  : {anos} ano(s) de empresa")
print("=============================")
