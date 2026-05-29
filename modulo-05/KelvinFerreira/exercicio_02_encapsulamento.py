# =============================================================================
# ITEAM - CURSO DE CAPACITAÇÃO EM DESENVOLVIMENTO FULL STACK
# Programação em Python | Módulo 5 - Programação Orientada a Objetos
# =============================================================================
#
# EXERCÍCIO 02 - ENCAPSULAMENTO E @PROPERTY
#
# Aluno: Kelvin Araújo Ferreira
# =============================================================================


class ContaBancaria:
    """
    Representa uma conta bancária com saldo protegido por encapsulamento.
    """

    def __init__(self, titular, saldo_inicial=0.0):
        self.__titular = titular
        if saldo_inicial < 0:
            print("Saldo inicial negativo. Definido como R$ 0.00.")
            self.__saldo = 0.0
        else:
            self.__saldo = saldo_inicial
        self.__historico = []
        self.__historico.append(
            f"Conta criada para {titular} com saldo inicial R$ {self.__saldo:.2f}"
        )

    # --- PROPRIEDADES ---

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    # --- SETTER COM VALIDAÇÃO ---

    @titular.setter
    def titular(self, novo_titular):
        if not isinstance(novo_titular, str) or not novo_titular.strip():
            raise ValueError("O nome do titular não pode ser vazio.")
        self.__historico.append(
            f"Titular alterado de '{self.__titular}' para '{novo_titular.strip()}'"
        )
        self.__titular = novo_titular.strip()

    # --- MÉTODOS DE OPERAÇÃO ---

    def depositar(self, valor):
        if valor <= 0:
            print(f"Erro: valor de depósito inválido (R$ {valor:.2f}). Deve ser positivo.")
            return
        self.__saldo += valor
        self.__historico.append(f"Depósito de R$ {valor:.2f} | Saldo: R$ {self.__saldo:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= 0:
            print(f"Erro: valor de saque inválido (R$ {valor:.2f}). Deve ser positivo.")
            return False
        if valor > self.__saldo:
            print(
                f"Saldo insuficiente. Saldo atual: R$ {self.__saldo:.2f} | "
                f"Tentativa de saque: R$ {valor:.2f}"
            )
            return False
        self.__saldo -= valor
        self.__historico.append(f"Saque de R$ {valor:.2f} | Saldo: R$ {self.__saldo:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        return True

    def exibir_extrato(self):
        print("=" * 44)
        print(f"  EXTRATO - CONTA DE {self.__titular.upper()}")
        print("=" * 44)
        print("Histórico de Operações:")
        for operacao in self.__historico:
            print(f" > {operacao}")
        print("-" * 44)
        print(f"Saldo Atual: R$ {self.__saldo:.2f}")
        print("=" * 44)


# =============================================================================
# BLOCO DE TESTES
# =============================================================================

if __name__ == "__main__":

    print("=" * 50)
    print("  SISTEMA BANCÁRIO - ITEAM")
    print("=" * 50)

    conta = ContaBancaria("Carlos Mendes", 1000.00)

    conta.depositar(500.00)
    conta.sacar(200.00)
    conta.sacar(5000.00)        # saldo insuficiente
    conta.depositar(-100)       # valor inválido

    conta.exibir_extrato()

    # Desafio: acessar __saldo diretamente gera AttributeError
    try:
        print(conta.__saldo)
    except AttributeError as e:
        print(f"\nDesafio: {e}")

    # Desafio: alterar titular pelo setter
    conta.titular = "Carlos Mendes Atualizado"
    print(f"\nNovo titular: {conta.titular}")

    print("\nExercício concluído!")
