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
    while True:
        nome_turma = input("Informe o nome da turma: ")
        if validar_turma(nome_turma):
            return nome_turma
        
        nome_turma = nome_turma.strip().lower()
        if nome_turma == "sair":
            return None
        
        print("Erro: o nome informado não é valido (é vazio ou possui apenas espaços). Tente novamente.")


def obter_aluno():
    """
    Solicita ao usuário o nome do aluno em loop até receber uma entrada válida.
    Se o usuário digitar "sair", retorna None.

    Retorno:
        str ou None
    """
    # TODO: Mesma lógica de obter_turma(), mas usando validar_aluno().
    #       Lembre de verificar "sair" antes de validar.
    while True:
        nome_aluno = input("Informe o nome do/a aluno/a: ")
        if validar_aluno(nome_aluno):
            return nome_aluno
        
        nome_aluno = nome_aluno.strip().lower()
        if nome_aluno == "sair":
            return None
        
        print("Erro: o nome informado não é valido (deve ter pelo menos dois nomes: João Alves).\nTente novamente.")



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
    while True:
        nota = input("Informe a nota do aluno: ")
        if validar_nota(nota):
            return nota
        
        print("Erro: nota inválida, o valor deve estar no padrão (7,5 ou 7.5) e entre 0 e 10. Tente novamente.")



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
    turma = obter_turma()
    if turma is None:
        print("Encerrando...")
        return
    
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
    while True:
        aluno = obter_aluno()
        if aluno is None:
            break

        nota1 = obter_nota(1)

        nota2 = obter_nota(2)

        nota3 = obter_nota(3)

        salvar_nota(turma, aluno, float(nota1), float(nota2), float(nota3))
        print("Salvo com sucesso!!!")

        ler_notas(turma)

# ── Ponto de entrada do programa ──────────────────────────
# Esta condicional garante que main() só é chamada quando
# este arquivo for executado diretamente (não quando importado).
if __name__ == "__main__":
    main()
