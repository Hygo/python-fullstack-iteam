import json

funcionarios = [
    {"nome": "Carlos", "cargo": "Desenvolvedor", "salario": 5000.00, "departamento": "TI"},
    {"nome": "Ana", "cargo": "Gerente", "salario": 8500.00, "departamento": "TI"},
    {"nome": "João", "cargo": "Suporte", "salario": 3200.00, "departamento": "Operações"}
]

with open("funcionarios.json", "w", encoding="utf-8") as f:
    json.dump(funcionarios, f, indent=4, ensure_ascii=False)

with open("funcionarios.json", "r", encoding="utf-8") as f:
    dados_lidos = json.load(f)

print(f"{'NOME':<15} | {'CARGO':<15} | {'DEPARTAMENTO':<15} | {'SALÁRIO':<10}")
print("-" * 65)
soma_salarios = 0
for func in dados_lidos:
    soma_salarios += func['salario']
    print(f"{func['nome']:<15} | {func['cargo']:<15} | {func['departamento']:<15} | R$ {func['salario']:>8.2f}")

print("-" * 65)
media_salario = soma_salarios / len(dados_lidos)
print(f"Salário Médio da equipe: R$ {media_salario:.2f}")
