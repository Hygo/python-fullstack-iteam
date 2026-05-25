import json

# Lista de funcionários
funcionarios = [
    {"nome": "Alice", "carga": "40h", "salario": 3500.00, "departamento": "TI"},
    {"nome": "Bruno", "carga": "30h", "salario": 2800.00, "departamento": "Marketing"},
    {"nome": "Carla", "carga": "40h", "salario": 4200.00, "departamento": "Financeiro"}
]

# Salvando em funcionarios.json
with open("funcionarios.json", "w", encoding="utf-8") as f:
    json.dump(funcionarios, f, indent=2, ensure_ascii=False)

# Lendo o arquivo de volta
with open("funcionarios.json", "r", encoding="utf-8") as f:
    funcionarios_lidos = json.load(f)

# Exibindo em tabela formatada
print("--- Funcionários ---")
print(f"{'Nome':<10} {'Carga':<6} {'Salário':<10} {'Departamento':<12}")
print("-" * 40)
for f in funcionarios_lidos:
    print(f"{f['nome']:<10} {f['carga']:<6} R$ {f['salario']:<8.2f} {f['departamento']:<12}")

# Calculando salário médio
salarios = [f["salario"] for f in funcionarios_lidos]
media_salario = sum(salarios) / len(salarios)

print("\nSalário médio da equipe: R$ {:.2f}".format(media_salario))
