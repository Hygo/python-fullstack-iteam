# ============================================================
# ARQUIVO PRINCIPAL: main.py
# Sistema de Lançamento de Notas — Nível Fácil
# ============================================================

from funcoes.validacoes import validar_turma, validar_aluno, validar_nota
from funcoes.arquivo import salvar_nota, ler_notas


def obter_turma():
    """
    Solicita ao usuário o nome da turma em loop até receber uma entrada válida.
    Se o usuário digitar "sair", retorna None para sinalizar encerramento.
    """
    while True:
        turma = input("\nNome da turma: ").strip()
        if turma.lower() == "sair":
            return None
        if validar_turma(turma):
            return turma
        print("⚠ Nome de turma inválido. Tente novamente.")


def obter_aluno():
    """
    Solicita ao usuário o nome do aluno em loop até receber uma entrada válida.
    Se o usuário digitar "sair", retorna None.
    """
    while True:
        aluno = input("\nNome do aluno (ou 'sair'): ").strip()
        if aluno.lower() == "sair":
            return None
        if validar_aluno(aluno):
            return aluno
        print("⚠ Nome inválido. Informe nome e sobrenome.")


def obter_nota(numero_da_nota):
    """
    Solicita uma nota ao usuário em loop até receber um valor válido.

    Parâmetros:
        numero_da_nota (int): 1, 2 ou 3 — usado na mensagem exibida ao usuário

    Retorno:
        float: a nota validada e convertida
    """
    while True:
        valor = input(f"Nota {numero_da_nota}: ")
        nota = validar_nota(valor)
        if nota is None:
            print("⚠ Nota inválida. Digite um número entre 0.0 e 10.0.")
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

    # Passo 1: Capturar o nome da turma
    turma = obter_turma()
    if turma is None:
        print("\nEncerrando...")
        return

    # Passo 2: Loop para cadastrar múltiplos alunos
    while True:
        # a) Capturar o nome do aluno
        aluno = obter_aluno()
        if aluno is None:
            break

        # b) Capturar as três notas
        nota1 = obter_nota(1)
        nota2 = obter_nota(2)
        nota3 = obter_nota(3)

        # c) Salvar e exibir mensagem de sucesso
        salvar_nota(turma, aluno, nota1, nota2, nota3)
        print("\n✔ Nota salva com sucesso!")

        # d) Exibir todos os registros da turma
        ler_notas(turma)

    # Passo 3: Mensagem de encerramento
    print("\nEncerrando o sistema. Até logo!")


# ── Ponto de entrada do programa ──────────────────────────
if __name__ == "__main__":
    main()