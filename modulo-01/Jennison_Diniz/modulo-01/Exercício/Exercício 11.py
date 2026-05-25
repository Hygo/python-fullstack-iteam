# Armazenando os dados da funcionária
nome = "Mariana Souza"
cargo = "Analista de Dados"
salario = 7850.50
anos_empresa = 3

# Criando a string do salário formatada no padrão brasileiro (R$ X.XXX,XX)
# Primeiro limitamos a duas casas decimais, depois trocamos o ponto da máquina pela vírgula
salario_formatado = f"R$ {salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Exibindo a ficha formatada profissionalmente
print("=============================")
print("     FICHA DO FUNCIONÁRIO    ")
print("=============================")
print(f"Nome   : {nome}")
print(f"Cargo  : {cargo}")
print(f"Salário: {salario_formatado}")
print(f"Tempo  : {anos_empresa} ano(s) de empresa")
print("=============================")