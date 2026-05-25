import json

# Dicionário inicial
aluno = {
    "nome": "Pedro Henrique",
    "idade": 22,
    "curso": "Full Stack",
    "ativo": True,
    "notas": [8.5, 9.0, 7.5]
}

# Converter para JSON com indentação de 2 espaços
aluno_json = json.dumps(aluno, indent=2)
print("--- JSON Gerado ---")
print(aluno_json)

# Converter de volta para dicionário
aluno_dict = json.loads(aluno_json)

# Calcular média das notas
media_notas = sum(aluno_dict["notas"]) / len(aluno_dict["notas"])

# Exibir nome e média
print("\n--- Resultado ---")
print(f"Nome: {aluno_dict['nome']}")
print(f"Média das notas: {media_notas:.2f}")
