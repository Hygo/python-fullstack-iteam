import json

equipe = [
    {"nome": "Andre Silva", "cargo": "Dev Backend", "salario": 8500.00, "departamento": "TI"},
    {"nome": "Breno Souza", "cargo": "Product Owner", "salario": 9200.00, "departamento": "Produto"},
    {"nome": "Carla Duarte", "cargo": "UX Designer", "salario": 7300.00, "departamento": "Design"}
]

#
with open("funcionarios.json", "w", encoding="utf-8") as f:
    json.dump(equipe, f, indent=4, ensure_ascii=False)


with open("funcionarios.json", "r", encoding="utf-8") as f:
    funcionarios = json.load(f)

# Tabela
print(f"{'Nome':<15} | {'Cargo':<15} | {'Salário':<10} | {'Departamento'}")
print("-" * 60)
total_salarios = 0.0

for func in funcionarios:
    print(f"{func['nome']:<15} | {func['cargo']:<15} | R$ {func['salario']:<8.2f} | {func['departamento']}")
    total_salarios += func["salario"]

media_salarial = total_salarios / len(funcionarios)
print("-" * 60)
print(f"Salário Médio da Equipe: R$ {media_salarial:.2f}")