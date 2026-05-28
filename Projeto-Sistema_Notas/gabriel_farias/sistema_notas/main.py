# ============================================================
# ARQUIVO PRINCIPAL: main.py
# Sistema de Lançamento de Notas — Nível Fácil
# ============================================================

from funcoes.validacoes import validar_turma, validar_aluno, validar_nota
from funcoes.arquivo import salvar_nota, ler_notas


def obter_turma():
    while True:
        entrada = input("\nDigite o nome da turma: ").strip()

        if entrada.lower() == "sair":
            return None

        if validar_turma(entrada):
            return entrada

        print("❌ Nome de turma inválido. Tente novamente.")


def obter_aluno():
    while True:
        entrada = input("\nDigite o nome completo do aluno (ou 'sair' para encerrar): ").strip()

        if entrada.lower() == "sair":
            return None

        if validar_aluno(entrada):
            return entrada

        print("Nome inválido. Informe nome e sobrenome.")


def obter_nota(numero_da_nota):
    while True:
        entrada = input(f"  Nota {numero_da_nota} (0 a 10): ")

        nota = validar_nota(entrada)

        if nota is None:
            print("Nota inválida. Digite um número entre 0 e 10.")
        else:
            return nota


def main():
    print("=" * 45)
    print("  Sistema de Lançamento de Notas")
    print("  Digite 'sair' a qualquer momento para encerrar")
    print("=" * 45)

    # Passo 1: Captura a turma
    turma = obter_turma()
    if turma is None:
        print("\nEncerrando...")
        return

    # Passo 2: Loop de cadastro de alunos
    while True:

        # a) Captura o aluno
        aluno = obter_aluno()
        if aluno is None:
            break

        # b) Captura as três notas
        print(f"\n📝 Notas de {aluno}:")
        nota1 = obter_nota(1)
        nota2 = obter_nota(2)
        nota3 = obter_nota(3)

        # c) Salva e confirma
        salvar_nota(turma, aluno, nota1, nota2, nota3)
        print(f"\n✅ Notas de {aluno} salvas com sucesso!")

        # d) Exibe todos os registros da turma
        ler_notas(turma)

    # Passo 3: Mensagem de encerramento
    print("\n" + "=" * 45)
    print("  Programa encerrado. Até logo!")
    print("=" * 45)


if __name__ == "__main__":
    main()