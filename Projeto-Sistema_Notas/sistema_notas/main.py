# ============================================================
# ARQUIVO PRINCIPAL: main.py
# Sistema de Lançamento de Notas — Nível Fácil
# ============================================================

from funcoes.validacoes import validar_turma, validar_aluno, validar_nota
from funcoes.arquivo import salvar_nota, ler_notas


def obter_turma():
    """
    Solicita ao usuário o nome da turma em loop até receber uma entrada válida.
    Se o usuário digitar "sair", retorna None.
    """

    while True:

        nome_da_turma = input("Informe o nome da turma: ")

        if nome_da_turma.strip().lower() == "sair":
            return None

        if validar_turma(nome_da_turma):
            return nome_da_turma

        else:
            print("Nome inválido")


def obter_aluno():
    """
    Solicita ao usuário o nome do aluno em loop até receber uma entrada válida.
    Se o usuário digitar "sair", retorna None.
    """

    while True:

        nome_aluno = input("Digite o nome do aluno: ")

        # validar saída
        if nome_aluno.strip().lower() == "sair":
            return None

        # validar nome
        if validar_aluno(nome_aluno):
            return nome_aluno

        else:
            print("Nome inválido")


def obter_nota(numero_da_nota):
    """
    Solicita uma nota ao usuário em loop até receber um valor válido.

    Parâmetros:
        numero_da_nota (int): 1, 2 ou 3

    Retorno:
        float
    """

    while True:

        nota_do_aluno = input(
            f"Digite a {numero_da_nota}ª nota do aluno: "
        )

        nota = validar_nota(nota_do_aluno)

        if nota is None:
            print("Nota inválida")

        else:
            return nota


def main():
    """
    Função principal que coordena o fluxo do programa.
    """

    print("=" * 45)
    print("  Sistema de Lançamento de Notas")
    print("  Digite 'sair' a qualquer momento para encerrar")
    print("=" * 45)

    # obter turma
    turma = obter_turma()

    if turma is None:
        print("Encerrando...")
        return

    # loop de alunos
    while True:

        # obter aluno
        aluno = obter_aluno()

        if aluno is None:
            break

        # obter notas
        nota1 = obter_nota(1)
        nota2 = obter_nota(2)
        nota3 = obter_nota(3)

        # salvar
        salvar_nota(turma, aluno, nota1, nota2, nota3)

        print("Notas salvas com sucesso!")

        # exibir registros
        ler_notas(turma)
        print()

    print("Programa encerrado.")


# ponto de entrada
if __name__ == "__main__":
    main()