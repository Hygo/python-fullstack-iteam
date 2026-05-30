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
        turma = input("\nDigite o nome da sala ou digite 'sair' para encerrar o programa: ")

        if turma.strip().lower() == "sair":
            return None
        
        if validar_turma(turma):
            return turma
        else:
            print("Error: Nome da turma Invalido, Tente novamente :/.\n")

def obter_aluno():
    """
    Solicita ao usuário o nome do aluno em loop até receber uma entrada válida.
    Se o usuário digitar "sair", retorna None.

    Retorno:
        str ou None
    """
    while True:
        aluno = input("\nDigite o nome e Sobrenome do aluno ou 'sair' para encerrar: ")
        
        if aluno.strip().lower() == "sair":
            return None
            
        if validar_aluno(aluno):
            return aluno
        else:
            print("Erro: Nome de aluno inválido. Tente novamente.")


def obter_nota(numero_da_nota):
    """
    Solicita uma nota ao usuário em loop até receber um valor válido.

    Parâmetros:
        numero_da_nota (int): 1, 2 ou 3 — usado na mensagem exibida ao usuário

    Retorno:
        float: a nota validada e convertida
    """
    while True:
        entrada = input(f"Digite a nota {numero_da_nota}: ")
        nota = validar_nota(entrada)
        
        if nota is not None:
            return nota
        else:
            print("Erro: Nota inválida. Digite um número válido (ex: 8.5).\n")
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
        print("Encerrando...")
        return
    
    while True:
        aluno = obter_aluno()
        if aluno is None:
            break

        nota1 = obter_nota(1)
        nota2 = obter_nota(2)
        nota3 = obter_nota(3)

        salvar_nota(turma, aluno, nota1, nota2, nota3)
        print(f"\n--- Notas do aluno '{aluno}' salvas com sucesso! ---")

        print("\nRegistros da turma até agora:")
        ler_notas(turma)
    print("\nPrograma de lançamento de notas encerrado. Até logo!")


# ── Ponto de entrada do programa ──────────────────────────
# Esta condicional garante que main() só é chamada quando
# este arquivo for executado diretamente (não quando importado).
if __name__ == "__main__":
    main()
