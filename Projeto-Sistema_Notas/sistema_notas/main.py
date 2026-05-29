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
    # TODO: Use um loop while True para pedir o nome da turma com input().
    #       Chame validar_turma() com o valor digitado.
    #       - Se o valor digitado for "sair" (após .strip().lower()), retorne None.
    #       - Se validar_turma() retornar True, retorne o nome da turma.
    #       - Caso contrário, imprima uma mensagem de erro e repita o loop.
def obter_turma():
    while True:
        turma = input("\nNome da turma: ")
        if turma.strip().lower() == "sair":
            return None
        if validar_turma(turma):
            return turma
        print("Turma inválida. Não pode estar vazia. Tente de novo.")

def obter_aluno():
    """
    Solicita ao usuário o nome do aluno em loop até receber uma entrada válida.
    Se o usuário digitar "sair", retorna None.

    Retorno:
        str ou None
    """
    # TODO: Mesma lógica de obter_turma(), mas usando validar_aluno().
    #       Lembre de verificar "sair" antes de validar.
def obter_aluno():
    while True:
        aluno = input("\nNome do aluno (ou 'sair'): ")
        if aluno.strip().lower() == "sair":
            return None
        if validar_aluno(aluno):
            return aluno
        print("Nome inválido. Informe nome e sobrenome (mínimo 2 palavras).")

def obter_nota(numero_da_nota):
    """
    Solicita uma nota ao usuário em loop até receber um valor válido.

    Parâmetros:
        numero_da_nota (int): 1, 2 ou 3 — usado na mensagem exibida ao usuário

    Retorno:
        float: a nota validada e convertida
    """
    # TODO: Use um loop while True para pedir a nota com input().
    #       Chame validar_nota() com o valor digitado.
    #       - Se retornar None (inválido), exiba uma mensagem de erro.
    #       - Se retornar um float válido, retorne-o.
def obter_nota(numero_da_nota):
    while True:
        valor = input(f"Nota {numero_da_nota}: ")
        nota = validar_nota(valor)
        if nota is None:
            print("Nota inválida. Digite um número entre 0 e 10.")
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

    # TODO (Passo 1): Chame obter_turma() para capturar o nome da turma.
    #                 Se retornar None, imprima "Encerrando..." e encerre com return.

    # TODO (Passo 2): Inicie um loop while True para cadastrar múltiplos alunos.
    #                 Dentro do loop:
    #
    #   a) Chame obter_aluno(). Se retornar None, quebre o loop (break).
    #
    #   b) Chame obter_nota(1), obter_nota(2) e obter_nota(3)
    #      para capturar as três notas do aluno.
    #
    #   c) Chame salvar_nota() passando turma, aluno e as três notas.
    #      Exiba uma mensagem de sucesso após salvar.
    #
    #   d) Chame ler_notas() para exibir todos os registros da turma até agora.

    # TODO (Passo 3): Fora do loop, imprima uma mensagem de encerramento.

# Passo 1: captura a turma
    turma = obter_turma()
    if turma is None:
        print("Encerrando...")
        return

    # Passo 2: loop de cadastro de alunos
    while True:
        aluno = obter_aluno()
        if aluno is None:
            break

        nota1 = obter_nota(1)
        nota2 = obter_nota(2)
        nota3 = obter_nota(3)

        salvar_nota(turma, aluno, nota1, nota2, nota3)
        print("\n✔ Nota salva com sucesso!\n")

        ler_notas(turma)

    # Passo 3: mensagem final
    print("\nEncerrando o sistema. Até logo!")

# ── Ponto de entrada do programa ──────────────────────────
# Esta condicional garante que main() só é chamada quando
# este arquivo for executado diretamente (não quando importado).
if __name__ == "__main__":
    main()
