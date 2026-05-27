import json 

aluno = {
    "nome": "Pedro Henrique",
    "idade": 22,
    "curso": "Full Stack",
    "ativo": True,
    "notas": [8.5, 9.0, 7.5]
}

print(aluno)

aluno = json.dumps(aluno, indent=2)

print(aluno)

aluno = json.loads(aluno)

print(f"Nome do aluno: {aluno['nome']}\nMédia: {sum(aluno['notas'])/3}")