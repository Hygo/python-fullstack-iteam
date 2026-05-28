from funcoes.validacoes import validar_turma, validar_aluno, validar_nota
from funcoes.arquivo import salvar_nota, ler_notas


def obter_turma():
    """
    Solicita ao usuário o nome da turma.
    """
    while True:
        turma = input("Digite o nome da turma: ").strip()

        if turma.lower() == "sair":
            return None

        if validar_turma(turma):
            return turma
        else:
            print("❌ Turma inválida. Tente novamente.")


def obter_aluno():
    """
    Solicita o nome do aluno.
    """
    while True:
        aluno = input("Digite o nome do aluno: ").strip()

        if aluno.lower() == "sair":
            return None

        if validar_aluno(aluno):
            return aluno
        else:
            print("❌ Nome inválido. Digite nome e sobrenome.")


def obter_nota(numero_da_nota):
    """
    Solicita uma nota válida.
    """
    while True:
        valor = input(f"Digite a nota {numero_da_nota}: ").strip()

        nota = validar_nota(valor)

        if nota is None:
            print("❌ Nota inválida. Digite um valor entre 0 e 10.")
        else:
            return nota


def main():
    """
    Função principal do programa.
    """
    print("=" * 45)
    print("  Sistema de Lançamento de Notas")
    print("  Digite 'sair' a qualquer momento para encerrar")
    print("=" * 45)

    # Passo 1: obter turma
    turma = obter_turma()
    if turma is None:
        print("Encerrando...")
        return

    # Passo 2: loop de alunos
    while True:
        aluno = obter_aluno()

        if aluno is None:
            break

        nota1 = obter_nota(1)
        nota2 = obter_nota(2)
        nota3 = obter_nota(3)

        salvar_nota(turma, aluno, nota1, nota2, nota3)

        print("✅ Nota salva com sucesso!\n")

        # Exibe dados atualizados
        print(f"📄 Notas da turma {turma}:")
        ler_notas(turma)

    # Passo 3: encerramento
    print("\nSistema encerrado. Até mais!")


# Ponto de entrada
if __name__ == "__main__":
    main()