import json

funcionarios = [
    {"nome": "Lucas Oliveira",  "cargo": "Dev Backend",      "salario": 8500.00, "departamento": "Tecnologia"},
    {"nome": "Carla Mendes",    "cargo": "UX Designer",      "salario": 7200.00, "departamento": "Produto"},
    {"nome": "Rafael Torres",   "cargo": "Data Analyst",     "salario": 9100.00, "departamento": "Dados"},
]

# Salva em JSON
with open("funcionarios.json", "w", encoding="utf-8") as f:
    json.dump(funcionarios, f, indent=2, ensure_ascii=False)

# Lê o arquivo
with open("funcionarios.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

# Exibe tabela formatada
print(f"{'Nome':<20} {'Cargo':<20} {'Salário':>12} {'Departamento':<15}")
print("-" * 70)
for func in dados:
    print(f"{func['nome']:<20} {func['cargo']:<20} R$ {func['salario']:>8.2f} {func['departamento']:<15}")

media = sum(f["salario"] for f in dados) / len(dados)
print("-" * 70)
print(f"Salário médio da equipe: R$ {media:.2f}")
