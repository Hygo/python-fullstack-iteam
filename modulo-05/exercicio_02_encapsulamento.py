# =============================================================================
# ITEAM - CURSO DE CAPACITAÇÃO EM DESENVOLVIMENTO FULL STACK
# Programação em Python | Módulo 5 - Programação Orientada a Objetos
# =============================================================================
#
# EXERCÍCIO 02 - ENCAPSULAMENTO E @PROPERTY
#
# Tema: Sistema de Conta Bancária
#
# Objetivo:
#   Modelar uma conta bancária aplicando encapsulamento para proteger os dados
#   sensíveis do objeto, utilizando atributos privados e propriedades com
#   validação de dados.
#
# Conceitos trabalhados:
#   - Encapsulamento com atributos protegidos (_atributo) e privados (__atributo)
#   - Decorador @property para leitura controlada de atributos
#   - Decorador @atributo.setter para escrita com validação
#   - Proteção contra operações inválidas (saldo negativo, etc.)
#
# Referência: Seção 5.3.1 e 5.5.1 da Apostila ITEAM
# =============================================================================

class ContaBancaria:
    """
    Representa uma conta bancária com saldo protegido por encapsulamento.

    Atributos privados:
        __titular (str): Nome do titular da conta.
        __saldo (float): Saldo atual da conta (não pode ser negativo).
        __historico (list): Registro de todas as operações realizadas.
    """

    def __init__(self, titular, saldo_inicial=0.0):
        """
        Inicializa a conta bancária.
        """
        # TODO: Atribua o titular ao atributo PRIVADO __titular
        self.__titular = titular

        # TODO: Valide o saldo_inicial. Se for negativo, defina como 0.0 e avise o usuário.
        if saldo_inicial < 0:
            print("Aviso: Saldo inicial não pode ser negativo. Definido como R$ 0.00")
            self.__saldo = 0.0
        else:
            self.__saldo = float(saldo_inicial)

        # O histórico já está inicializado - adicione a primeira entrada
        self.__historico = []
        self.__historico.append(f"Conta criada para {titular} com saldo inicial R$ {self.__saldo:.2f}")

    # --- PROPRIEDADES (GETTERS) ---

    @property
    def titular(self):
        """Retorna o nome do titular da conta (somente leitura)."""
        # TODO: Retorne o atributo privado __titular
        return self.__titular

    @property
    def saldo(self):
        """Retorna o saldo atual da conta (somente leitura)."""
        # TODO: Retorne o atributo privado __saldo
        return self.__saldo

    # --- SETTER COM VALIDAÇÃO ---

    @titular.setter
    def titular(self, novo_titular):
        """
        Permite alterar o titular apenas se o novo nome não estiver vazio.
        """
        # TODO: Valide se novo_titular é uma string não vazia.
        if isinstance(novo_titular, str) and novo_titular.strip():
            nome_antigo = self.__titular
            self.__titular = novo_titular.strip()
            self.__historico.append(f"Titular alterado de '{nome_antigo}' para '{self.__titular}'")
        else:
            raise ValueError("Erro: O nome do titular não pode ser vazio ou inválido.")

    # --- MÉTODOS DE OPERAÇÃO ---

    def depositar(self, valor):
        """
        Realiza um depósito na conta.
        """
        # TODO: Valide se o valor é positivo.
        if valor > 0:
            self.__saldo += valor
            self.__historico.append(f"Depósito realizado: +R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print(f"Erro: Valor de depósito R$ {valor:.2f} deve ser estritamente positivo.")

    def sacar(self, valor):
        """
        Realiza um saque da conta.
        """
        # TODO: Valide duas condições: valor positivo e saldo disponível.
        if valor <= 0:
            print(f"Erro: Valor de saque R$ {valor:.2f} deve ser estritamente positivo.")
            return False
        elif valor > self.__saldo:
            print(f"Erro: Saque de R$ {valor:.2f} recusado. Saldo insuficiente (Saldo atual: R$ {self.__saldo:.2f}).")
            return False
        else:
            self.__saldo -= valor
            self.__historico.append(f"Saque realizado: -R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            return True

    def exibir_extrato(self):
        """
        Exibe o extrato completo da conta com todas as operações do histórico.
        """
        # TODO: Imprima um extrato formatado como solicitado
        print("\n============================================")
        print(f"  EXTRATO - CONTA DE {self.titular.upper()}")
        print("============================================")
        print("Histórico de Operações:")
        for operacao in self.__historico:
            print(f"  > {operacao}")
        print("--------------------------------------------")
        print(f"Saldo Atual: R$ {self.saldo:.2f}")
        print("============================================")


# =============================================================================
# BLOCO DE TESTES
# =============================================================================

if __name__ == "__main__":

    print("=" * 50)
    print("  SISTEMA BANCÁRIO - ITEAM")
    print("=" * 50)

    # 1. Crie uma conta para um titular com saldo inicial de R$ 1000.00
    conta = ContaBancaria("Carlos Mendes", 1000.00)

    # 2. Realize um depósito de R$ 500.00
    print("\n--- Testando Depósito ---")
    conta.depositar(500.00)

    # 3. Realize um saque de R$ 200.00
    print("\n--- Testando Saque Válido ---")
    conta.sacar(200.00)

    # 4. Tente realizar um saque de R$ 5000.00 (saldo insuficiente)
    print("\n--- Testando Saque Inválido (Insuficiente) ---")
    conta.sacar(5000.00)

    # 5. Tente depositar um valor negativo
    print("\n--- Testando Depósito Inválido ---")
    conta.depositar(-100.00)

    # 6. DESAFIO: Alterando o titular usando o setter
    print("\n--- Testando Alteração de Titular (Setter) ---")
    conta.titular = "Carlos Mendes Silva"
    print(f"Novo titular confirmado via Property: {conta.titular}")

    # 7. Exiba o extrato da conta
    conta.exibir_extrato()

    # 8. DESAFIO EXTRA: Forçando erro ao acessar __saldo diretamente
    print("\n--- Testando Segurança do Encapsulamento ---")
    try:
        print(conta.__saldo)  # Isso DEVE falhar!
    except AttributeError:
        print("Sucesso: O sistema bloqueou o acesso direto a 'conta.__saldo' (Atributo Privado)!")

    print("\nExercício concluído!")