import json

funcionarios = [
    {
        "nome": "Álefe Alves", 
        "cargo": "Estudante", 
        "salario": 130.00, 
        "departamento": "CC"
    },
    {
        "nome": "Amanda de Brito", 
        "cargo": "Estudante", 
        "salario": 700.00, 
        "departamento": "CC"
    },
    {
        "nome": "Luciano dos Santos", 
        "cargo": "Estudante", 
        "salario": 130.00, 
        "departamento": "CC"
    }
]

with open("funcionarios.json", "w") as f:
    json.dump(funcionarios, f, indent=2)

with open("funcionarios.json", "r") as f:
    funcionarios = json.load(f)

salario_media = 0

for index, funcionario in enumerate(funcionarios):
    salario_media += funcionario["salario"]

    print(f"""
    ===== FUNCIONÁRIO {funcionario["nome"]} =====
    ID Funcionário             : {index}
    Nome do Funcionário        : {funcionario["nome"]}
    Cargo do Funcionário       : {funcionario["cargo"]}
    Salário do Funcionário     : R$ {funcionario["salario"]}
    Departamento do Funcionário: {funcionario["departamento"]}
    =======================
    """)

salario_media = salario_media / (len(funcionarios))

print(f"A média de salário dos funcionários é: {salario_media}")
