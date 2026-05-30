# ============================================================
# ARQUIVO PRINCIPAL: main.py
# Sistema de Lançamento de Notas — Nível Fácil
# ============================================================
# Este arquivo orquestra o programa inteiro.
# Ele usa as funções dos módulos em /funcoes para:
#   - Ler e validar entradas do usuário
#   - Salvar e exibir notas em JSON
# ============================================================

from funcoes.validacoes import validar_turma, validar_aluno, validar_nota
from funcoes.arquivo import salvar_nota, ler_notas


def obter_turma():
    """
    Solicita ao usuário o nome da turma em loop até receber uma entrada válida.
    Se o usuário digitar "sair", retorna None para sinalizar encerramento.

    Retorno:
        str ou None
    """
    while True:
        nome_turma = input("Nome da turma: ")
        if nome_turma.strip().lower() == "sair":
            return None

        if validar_turma(nome_turma):
            return nome_turma.strip()

        print("Turma inválida. Digite um nome de turma válido.")


def obter_aluno():
    """
    Solicita ao usuário o nome do aluno em loop até receber uma entrada válida.
    Se o usuário digitar "sair", retorna None.

    Retorno:
        str ou None
    """
    while True:
        nome_aluno = input("\nNome do aluno (ou 'sair'): ")
        if nome_aluno.strip().lower() == "sair":
            return None

        if validar_aluno(nome_aluno):
            return nome_aluno.strip()

        print("Nome inválido. Digite nome e sobrenome do aluno.")


def obter_nota(numero_da_nota):
    """
    Solicita uma nota ao usuário em loop até receber um valor válido.

    Parâmetros:
        numero_da_nota (int): 1, 2 ou 3 — usado na mensagem exibida ao usuário

    Retorno:
        float: a nota validada e convertida
    """
    while True:
        valor_digitado = input(f"Nota {numero_da_nota}: ")
        nota = validar_nota(valor_digitado)
        if nota is None:
            print("Nota inválida. Digite um valor entre 0 e 10.")
            continue
        return nota


def main():
    """
    Função principal que coordena o fluxo do programa.
    """
    print("=" * 45)
    print("  Sistema de Lançamento de Notas")
    print("  Digite 'sair' a qualquer momento para encerrar")
    print("=" * 45)

    turma = obter_turma()
    if turma is None:
        print("\nEncerrando o sistema. Até logo!")
        return

    while True:
        aluno = obter_aluno()
        if aluno is None:
            break

        nota1 = obter_nota(1)
        nota2 = obter_nota(2)
        nota3 = obter_nota(3)

        salvar_nota(turma, aluno, nota1, nota2, nota3)
        print("\n✔ Nota salva com sucesso!")

        ler_notas(turma)

    print("\nEncerrando o sistema. Até logo!")


# ── Ponto de entrada do programa ──────────────────────────
# Esta condicional garante que main() só é chamada quando
# este arquivo for executado diretamente (não quando importado).
if __name__ == "__main__":
    main()
