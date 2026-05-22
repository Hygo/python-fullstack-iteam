import json

cadastro = {"id": 1042, "nome": "Fernanda Costa", "email": "fernanda@empresa.com"}
perfil   = {"id": 1042, "cargo": "Engenheira de Software", "nivel": "Senior",
            "salario": 12500.00, "habilidades": ["Python", "Django", "PostgreSQL"]}

funcionario_completo = cadastro | perfil

with open("funcionario_completo.json", "w", encoding="utf-8") as f:
    json.dump(funcionario_completo, f, indent=4)

print(f"ID: {funcionario_completo['id']} | Nome: {funcionario_completo['nome']}")
print(f"Cargo: {funcionario_completo['cargo']} ({funcionario_completo['nivel']})")
print("Habilidades:")
for i, hab in enumerate(funcionario_completo["habilidades"], 1):
    print(f"  {i}. {hab}")