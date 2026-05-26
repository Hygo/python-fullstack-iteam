import json

cadastro = {"id": 1042, "nome": "Fernanda Costa", "email": "fernanda@empresa.com"}
perfil   = {"id": 1042, "cargo": "Engenheira de Software", "nivel": "Senior",
            "salario": 12500.00, "habilidades": ["Python", "Django", "PostgreSQL"]}

funcionario_completo = cadastro | perfil

dados_json = json.dumps(funcionario_completo)

dados = json.loads(dados_json)

print(f"""
===== FICHA FUNCIONÁRIO/A {dados["nome"]} =====
ID         : {dados["id"]}
Nome       : {dados["nome"]}
Email      : {dados["email"]}
Cargo      : {dados["cargo"]}
Nível      : {dados["nivel"]}
Sálario    : {dados["salario"]}
Habilidades: 
""", end="")

for i, habilidade in enumerate(funcionario_completo["habilidades"]):
    print(f"    {i+1}. {habilidade}",)
print("=======================")