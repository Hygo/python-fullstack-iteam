import json

aluno = {
    "nome": "Pedro Henrique",
    "idade": 22,
    "curso": "Full Stack",
    "ativo": True,
    "notas": [8.5, 9.0, 7.5]
}

# Converter JSON
aluno_json = json.dumps(aluno, indent=2)
print("String JSON Gerada:\n", aluno_json)

dados_retornados = json.loads(aluno_json)
notas = dados_retornados["notas"]
media = sum(notas) / len(notas)

print(f"\nNome: {dados_retornados['nome']}")
print(f"Média das Notas: {media:.2f}")