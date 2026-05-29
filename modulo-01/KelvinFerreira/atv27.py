### 🟡 Exercício 27 – JSON com Múltiplos Registros
# Crie lista com 3 funcionários, salve em funcionarios.json, leia e exiba em tabela
# formatada com o salário médio da equipe.

import json

funcionarios = [
    {"nome": "Lucas Ferreira",   "cargo": "Dev Backend",       "salario": 8500.00, "departamento": "TI"},
    {"nome": "Camila Rocha",     "cargo": "UX Designer",       "salario": 7200.00, "departamento": "Produto"},
    {"nome": "Rafael Mendes",    "cargo": "Analista de Dados",  "salario": 9100.00, "departamento": "TI"},
]

with open("funcionarios.json", "w", encoding="utf-8") as f:
    json.dump(funcionarios, f, indent=2, ensure_ascii=False)

with open("funcionarios.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

print(f"{'Nome':<20} {'Cargo':<22} {'Salário':>12} {'Depto':<12}")
print("-" * 70)
for func in dados:
    print(f"{func['nome']:<20} {func['cargo']:<22} R$ {func['salario']:>9.2f} {func['departamento']:<12}")

media = sum(f["salario"] for f in dados) / len(dados)
print("-" * 70)
print(f"{'Salário médio da equipe:':>46} R$ {media:>9.2f}")
