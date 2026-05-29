### 🟡 Exercício 11 – Formatação Profissional com f-strings
# Uma empresa de RH precisa gerar fichas de funcionários.
# Armazene os dados abaixo e exiba formatados.

nome = "Mariana Souza"
cargo = "Analista de Dados"
salario = 7850.50
anos = 3

salario_fmt = f"{salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

print("=============================")
print("     FICHA DO FUNCIONÁRIO    ")
print("=============================")
print(f"Nome   : {nome}")
print(f"Cargo  : {cargo}")
print(f"Salário: R$ {salario_fmt}")
print(f"Tempo  : {anos} ano(s) de empresa")
print("=============================")
