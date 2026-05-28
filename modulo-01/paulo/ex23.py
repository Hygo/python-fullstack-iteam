import json

aluno = {
    "nome": "Pedro Henrique",
    "idade": 22,
    "curso": "Full Stack",
    "ativo": True,
    "notas": [8.5, 9.0, 7.5]
}

json_str = json.dumps(aluno, indent=2)
print("JSON string:")
print(json_str)

aluno_lido = json.loads(json_str)
media = sum(aluno_lido["notas"]) / len(aluno_lido["notas"])

print(f"\nNome: {aluno_lido['nome']}")
print(f"Média das notas: {media:.2f}")
