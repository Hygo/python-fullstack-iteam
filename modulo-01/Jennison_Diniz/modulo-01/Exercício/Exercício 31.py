import json

# Dicionários de sistemas diferentes
cadastro = {"id": 1042, "nome": "Fernanda Costa", "email": "fernanda@empresa.com"}
perfil   = {
    "id": 1042,
    "cargo": "Engenheira de Software",
    "nivel": "Senior",
    "salario": 12500.00,
    "habilidades": ["Python", "Django", "PostgreSQL"]
}

# Mesclando os dicionários
funcionario_completo = {**cadastro, **perfil}

# Salvando em funcionario.json
with open("funcionario.json", "w", encoding="utf-8") as f:
    json.dump(funcionario_completo, f, indent=2, ensure_ascii=False)

# Lendo o arquivo de volta
with open("funcionario.json", "r", encoding="utf-8") as f:
    funcionario_lido = json.load(f)

# Exibindo formatado
print("--- Dados do Funcionário ---")
print(f"ID: {funcionario_lido['id']}")
print(f"Nome: {funcionario_lido['nome']}")
print(f"Email: {funcionario_lido['email']}")
print(f"Cargo: {funcionario_lido['cargo']}")
print(f"Nível: {funcionario_lido['nivel']}")
print(f"Salário: R$ {funcionario_lido['salario']:.2f}")
print("Habilidades:")
for i, habilidade in enumerate(funcionario_lido["habilidades"], start=1):
    print(f"  {i}. {habilidade}")
