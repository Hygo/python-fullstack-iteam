import json

cadastro = {"id": 1042, "nome": "Fernanda Costa", "email": "fernanda@empresa.com"}
perfil   = {"id": 1042, "cargo": "Engenheira de Software", "nivel": "Senior",
            "salario": 12500.00, "habilidades": ["Python", "Django", "PostgreSQL"]}

# Mescla os dois dicionários (perfil sobrescreve chaves duplicadas)
funcionario_completo = {**cadastro, **perfil}

# Salva em JSON
with open("funcionario_completo.json", "w", encoding="utf-8") as f:
    json.dump(funcionario_completo, f, indent=2, ensure_ascii=False)

# Lê e exibe
with open("funcionario_completo.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

print(f"ID     : {dados['id']}")
print(f"Nome   : {dados['nome']}")
print(f"E-mail : {dados['email']}")
print(f"Cargo  : {dados['cargo']}")
print(f"Nível  : {dados['nivel']}")
print(f"Salário: R$ {dados['salario']:.2f}")
print("Habilidades:")
for i, hab in enumerate(dados["habilidades"], start=1):
    print(f"  {i}. {hab}")
