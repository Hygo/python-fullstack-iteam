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
        entrada = input("\nDigite o nome da turma: ")
        
        # Verifica se o usuário deseja sair
        if entrada.strip().lower() == "sair":
            return None
        
        # Valida a turma de acordo com as regras do módulo de validação
        if validar_turma(entrada):
            return entrada.strip()
        else:
            print("❌ Nome de turma inválido. Tente novamente.")


def obter_aluno():
    """
    Solicita ao usuário o nome do aluno em loop até receber uma entrada válida.
    Se o usuário digitar "sair", retorna None.

    Retorno:
        str ou None
    """
    while True:
        entrada = input("\nDigite o nome completo do aluno: ")
        
        # Verifica se o usuário deseja sair
        if entrada.strip().lower() == "sair":
            return None
        
        # Valida o aluno de acordo com as regras do módulo de validação
        if validar_aluno(entrada):
            return entrada.strip()
        else:
            print("❌ Nome inválido. Digite o nome e o sobrenome (mínimo 2 palavras).")


def obter_nota(numero_da_nota):
    """
    Solicita uma nota ao usuário em loop até receber um valor válido.

    Parâmetros:
        numero_da_nota (int): 1, 2 ou 3 — usado na mensagem exibida ao usuário

    Retorno:
        float: a nota validada e convertida
    """
    while True:
        entrada = input(f"Digite a Nota {numero_da_nota}: ")
        
        nota_validada = validar_nota(entrada)
        
        # Se a nota for válida, ela retorna um float, caso contrário retorna None
        if nota_validada is not None:
            return nota_validada
        else:
            print("❌ Nota inválida. Digite um número válido entre 0.0 e 10.0.")


def main():
    """
    Função principal que coordena o fluxo do programa.
    """
    print("=" * 45)
    print("  Sistema de Lançamento de Notas")
    print("  Digite 'sair' a qualquer momento para encerrar")
    print("=" * 45)

    # Passo 1: Captura o nome da turma
    turma = obter_turma()
    if turma is None:
        print("\nEncerrando o sistema...")
        return

    # Passo 2: Loop para cadastrar múltiplos alunos na turma selecionada
    while True:
        # a) Captura o nome do aluno
        aluno = obter_aluno()
        if aluno is None:
            break  # Sai do loop de alunos se digitar "sair"

        # b) Captura as três notas do aluno
        nota1 = obter_nota(1)
        nota2 = obter_nota(2)
        nota3 = obter_nota(3)

        # c) Salva as notas no arquivo JSON e exibe mensagem de sucesso
        salvar_nota(turma, aluno, nota1, nota2, nota3)
        print(f"\n✅ Dados de {aluno} salvos com sucesso!")

        # d) Exibe todos os registros daquela turma atualizados
        ler_notas(turma)

    # Passo 3: Mensagem de encerramento final (após quebrar o loop de alunos)
    print("\nLançamentos finalizados. Encerrando o sistema... Até logo!")


# ── Ponto de entrada do programa ──────────────────────────
if __name__ == "__main__":
    main()