### 🟢 Exercício 23 – Lendo um JSON Simples
# Converta o dicionário para JSON com json.dumps(), depois converta de volta com
# json.loads() e exiba o nome e a média das notas.

import json

aluno = {
    "nome": "Pedro Henrique",
    "idade": 22,
    "curso": "Full Stack",
    "ativo": True,
    "notas": [8.5, 9.0, 7.5]
}

json_str = json.dumps(aluno, indent=2, ensure_ascii=False)
print("JSON gerado:")
print(json_str)

dados = json.loads(json_str)
media = sum(dados["notas"]) / len(dados["notas"])

print(f"\nNome  : {dados['nome']}")
print(f"Média : {media:.2f}")
