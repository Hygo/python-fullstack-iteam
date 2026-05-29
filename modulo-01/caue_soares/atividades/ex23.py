import json

aluno = {
    "nome": "Pedro Henrique",
    "idade": 22,
    "curso": "Full Stack",
    "ativo": True,
    "notas": [8.5, 9.0, 7.5]
}

# Converte dicionário para string JSON com indentação
json_str = json.dumps(aluno, indent=2, ensure_ascii=False)
print("=== JSON serializado ===")
print(json_str)

# Converte string JSON de volta para dicionário
aluno_restaurado = json.loads(json_str)

nome = aluno_restaurado["nome"]
media = sum(aluno_restaurado["notas"]) / len(aluno_restaurado["notas"])

print(f"\nNome : {nome}")
print(f"Média: {media:.2f}")
