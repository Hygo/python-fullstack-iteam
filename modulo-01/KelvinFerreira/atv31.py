### 🔴 Exercício 31 – Mesclando JSONs de Sistemas Diferentes
# Mescle os dois dicionários em funcionario_completo, salve em JSON,
# leia e exiba formatado com a lista de habilidades numerada.

import json

cadastro = {"id": 1042, "nome": "Fernanda Costa", "email": "fernanda@empresa.com"}
perfil   = {"id": 1042, "cargo": "Engenheira de Software", "nivel": "Senior",
            "salario": 12500.00, "habilidades": ["Python", "Django", "PostgreSQL"]}

funcionario_completo = {**cadastro, **perfil}

with open("funcionario_completo.json", "w", encoding="utf-8") as f:
    json.dump(funcionario_completo, f, indent=2, ensure_ascii=False)

with open("funcionario_completo.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

print("===== FUNCIONÁRIO COMPLETO =====")
print(f"ID    : {dados['id']}")
print(f"Nome  : {dados['nome']}")
print(f"Email : {dados['email']}")
print(f"Cargo : {dados['cargo']}")
print(f"Nível : {dados['nivel']}")
print(f"Salário: R$ {dados['salario']:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print("Habilidades:")
for i, habilidade in enumerate(dados["habilidades"], 1):
    print(f"  {i}. {habilidade}")
print("================================")
