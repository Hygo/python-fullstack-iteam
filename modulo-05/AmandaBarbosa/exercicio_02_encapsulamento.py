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

    Atributos privados (não devem ser acessados diretamente de fora da classe):
        __titular (str): Nome do titular da conta.
        __saldo (float): Saldo atual da conta (não pode ser negativo).
        __historico (list): Registro de todas as operações realizadas.
    """

    def __init__(self, titular, saldo_inicial=0.0):
        """
        Inicializa a conta bancária.

        Args:
            titular (str): Nome do titular.
            saldo_inicial (float): Saldo inicial da conta (padrão: 0.0).
        """
        # TODO: Atribua o titular ao atributo PRIVADO __titular
        # Dica: atributos privados usam dois underscores: self.__titular
        self.__titular = titular

        # TODO: Valide o saldo_inicial. Se for negativo, defina como 0.0 e avise o usuário.
        # Atribua ao atributo PRIVADO __saldo
        if saldo_inicial < 0:
            print("Aviso: Saldo inicial não pode ser negativo. Definido como R$ 0.00.")
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

        Args:
            novo_titular (str): Novo nome para o titular.
        """
        # TODO: Valide se novo_titular é uma string não vazia (use strip() para remover espaços).
        # Se válido, atualize __titular e registre no histórico.
        # Se inválido, levante um ValueError com mensagem explicativa.
        if isinstance(novo_titular, str) and novo_titular.strip():
            antigo_titular = self.__titular
            self.__titular = novo_titular.strip()
            self.__historico.append(f"Titular alterado de {antigo_titular} para {self.__titular}")
        else:
            raise ValueError("O nome do titular não pode ser vazio ou inválido.")

    # --- MÉTODOS DE OPERAÇÃO ---

    def depositar(self, valor):
        """
        Realiza um depósito na conta.

        Args:
            valor (float): Valor a ser depositado (deve ser positivo).
        """
        # TODO: Valide se o valor é positivo.
        # Se sim: adicione ao __saldo e registre no __historico.
        # Se não: imprima uma mensagem de erro.
        if valor > 0:
            self.__saldo += valor
            self.__historico.append(f"Depósito de R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print(f"Erro: Valor de depósito R$ {valor:.2f} deve ser positivo.")

    def sacar(self, valor):
        """
        Realiza um saque da conta.

        Args:
            valor (float): Valor a ser sacado.

        Returns:
            bool: True se o saque foi bem-sucedido, False caso contrário.
        """
        # TODO: Valide duas condições:
        #   1. O valor deve ser positivo.
        #   2. O valor não pode ser maior que o saldo disponível.
        # Se ambas forem atendidas: subtraia do __saldo, registre no __historico e retorne True.
        # Caso contrário: informe o erro e retorne False.
        if valor <= 0:
            print(f"Erro: Valor de saque R$ {valor:.2f} deve ser positivo.")
            return False
        elif valor > self.__saldo:
            print(f"Erro: Saldo insuficiente para o saque de R$ {valor:.2f}. Saldo atual: R$ {self.__saldo:.2f}")
            return False
        else:
            self.__saldo -= valor
            self.__historico.append(f"Saque de R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            return True

    def exibir_extrato(self):
        """
        Exibe o extrato completo da conta com todas as operações do histórico.
        """
        print("\n============================================")
        print(f"  EXTRATO - CONTA DE {self.titular}")
        print("============================================")
        print("Histórico de Operações:")
        for operacao in self.__historico:
            print(f" > {operacao}")
        print("--------------------------------------------")
        print(f"Saldo Atual: R$ {self.saldo:.2f}")
        print("============================================\n")


# =============================================================================
# BLOCO DE TESTES
# =============================================================================

if __name__ == "__main__":

    print("=" * 50)
    print("  SISTEMA BANCÁRIO")
    print("=" * 50)

    conta = ContaBancaria("Amanda", 1000.00)

    conta.depositar(500.00)

    conta.sacar(200.00)

    conta.sacar(5000.00)

    # valor negativo 
    conta.depositar(-100.00)

    # extrato da conta
    conta.exibir_extrato()

    try:
        print(conta.__saldo)
    except AttributeError as e:
        print(f"Desafio Atributo Privado: Sucesso! Não foi possível acessar diretamente. Erro: {e}")

    conta.titular = "Carlos Mendes Silva"
    print(f"Novo titular alterado via setter: {conta.titular}")

    print("\nExercício concluído!")