# ============================================================
# ARQUIVO PRINCIPAL: main.py
# Sistema de Lançamento de Notas — Nível Fácil
# ============================================================
# Este arquivo orquestra o programa inteiro.
# Ele usa as funções dos módulos em /funcoes para:
#   - Ler e validar entradas do usuário
#   - Salvar e exibir notas em JSON
# ============================================================

import sys
from funcoes.validacoes import checar_sair, validar_turma, validar_aluno, validar_nota
from funcoes.arquivo import salvar_nota, ler_notas

def encerrar_sistema():
    print("\nEncerrando o sistema. Até logo!")
    sys.exit()

def main():
    print("=============================================")
    print("  Sistema de Lançamento de Notas             ")
    print("  Digite 'sair' a qualquer momento para encerrar")
    print("=============================================")
    print()

    while True:
        turma = input("Nome da turma: ").strip()
        if checar_sair(turma):
            encerrar_sistema()
        if validar_turma(turma):
            break
        print("Erro: O nome da turma não pode ser vazio.\n")

    print()

    while True:
        while True:
            aluno = input("Nome do aluno (ou 'sair'): ").strip()
            if checar_sair(aluno):
                encerrar_sistema()
            if validar_aluno(aluno):
                break
            print("Erro: Digite o nome completo.\n")

        notas = []
        for i in range(1, 4):
            while True:
                nota_input = input(f"Nota {i}: ").strip()
                if checar_sair(nota_input):
                    encerrar_sistema()
                
                nota_validada = validar_nota(nota_input)
                if nota_validada is not None:
                    notas.append(nota_validada)
                    break
                print("Erro: A nota deve ser um número entre 0.0 e 10.0.\n")

        # Chama a função salvar_nota exatamente com os parâmetros do seu arquivo.py
        salvar_nota(turma, aluno, notas[0], notas[1], notas[2])
        
        print("\n✔ Nota salva com sucesso!")
        
        # Chama a função ler_notas para exibir os dados na tela
        ler_notas(turma)

if __name__ == "__main__":
    main()