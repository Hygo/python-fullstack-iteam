# =============================================================================
# ITEAM - CURSO DE CAPACITAÇÃO EM DESENVOLVIMENTO FULL STACK
# Programação em Python | Módulo 5 - Programação Orientada a Objetos
# =============================================================================
#
# EXERCÍCIO 03 - HERANÇA E FUNÇÃO super()
#
# Tema: Systema de Funcionários de uma Empresa
#
# Objetivo:
#   Construir uma hierarquia de classes usando herança para modelar diferentes
#   tipos de funcionários de uma empresa, reutilizando código da classe pai e
#   especizando comportamentos nas classes filhas.
#
# Hierarquia proposta:
#
#          ┌─────────────┐
#          │  Funcionario │   ← Classe PAI (Superclasse)
#          └──────┬──────┘
#                 │ herança
#        ┌────────┴────────┐
#        ▼                 ▼
#  ┌──────────┐     ┌───────────┐
#  │  Gerente │     │ Estagiario│  ← Classes FILHAS (Subclasses)
#  └──────────┘     └───────────┘
#
# Conceitos trabalhados:
#   - Herança com classe entre parênteses: class Filha(Pai)
#   - Uso de super().__init__() para reaproveitar o construtor da classe pai
#   - Sobrescrita de métodos (Method Overriding)
#   - Adição de atributos e métodos específicos nas subclasses
#
# Referência: Seções 5.3.2 e 5.6 da Apostila ITEAM
# =============================================================================


# -----------------------------------------------------------------------------
# CLASSE PAI
# -----------------------------------------------------------------------------

class Funcionario:
    """
    Representa um funcionário genérico da empresa ITEAM.

    Atributos:
        nome (str): Nome completo do funcionário.
        cpf (str): CPF do funcionário.
        salario_base (float): Salário base mensal.
    """

    def __init__(self, nome, cpf, salario_base):
        """
        Inicializa um Funcionario.

        Args:
            nome (str): Nome do funcionário.
            cpf (str): CPF no formato '000.000.000-00'.
            salario_base (float): Salário base mensal.
        """
        # TODO: Atribua os parâmetros aos atributos de instância
        self.nome = nome
        self.cpf = cpf
        self.salario_base = float(salario_base)

    def calcular_salario(self):
        """
        Retorna o salário final do funcionário.
        Para a classe base, o salário final é igual ao salário base.

        Returns:
            float: Salário calculado.
        """
        # TODO: Retorne o salario_base
        return self.salario_base

    def exibir_info(self):
        """
        Exibe as informações do funcionário de forma formatada.
        """
        # TODO: Imprima as informações no formato:
        #
        # [Tipo: Funcionário]
        # Nome:         [nome]
        # CPF:          [cpf]
        # Salário Base: R$ [valor]
        # Salário Final: R$ [calcular_salario()]
        #
        # Dica: use type(self).__name__ para obter o nome real da classe do objeto
        print(f"[Tipo: {type(self).__name__}]")
        print(f"Nome:          {self.nome}")
        print(f"CPF:           {self.cpf}")
        print(f"Salário Base: R$ {self.salario_base:.2f}")
        print(f"Salário Final: R$ {self.calcular_salario():.2f}")

    def __str__(self):
        """Representação em string do funcionário."""
        return f"Funcionario({self.nome}, CPF: {self.cpf})"


# -----------------------------------------------------------------------------
# CLASSE FILHA 1: Gerente
# -----------------------------------------------------------------------------

class Gerente(Funcionario):
    """
    Representa um Gerente, que É UM Funcionario com bônus adicional.

    Atributos herdados: nome, cpf, salario_base
    Atributos próprios:
        departamento (str): Departamento que o gerente lidera.
        bonus_percentual (float): Percentual de bônus sobre o salário base (ex: 0.20 = 20%).
    """

    def __init__(self, nome, cpf, salario_base, departamento, bonus_percentual):
        """
        Inicializa um Gerente, reaproveitando o construtor da classe pai.

        Args:
            nome (str): Nome do gerente.
            cpf (str): CPF do gerente.
            salario_base (float): Salário base.
            departamento (str): Nome do departamento.
            bonus_percentual (float): Percentual do bônus (entre 0 e 1).
        """
        # TODO: Use super().__init__() para inicializar os atributos da classe pai
        # (nome, cpf, salario_base)
        super().__init__(nome, cpf, salario_base)

        # TODO: Atribua os novos atributos específicos do Gerente
        self.departamento = departamento
        self.bonus_percentual = float(bonus_percentual)

    def calcular_salario(self):
        """
        Calcula o salário do Gerente: salário base + bônus.

        O bônus é calculado como: salario_base * bonus_percentual

        Returns:
            float: Salário base + valor do bônus.
        """
        # TODO: Calcule o bônus e retorne a soma com o salário base.
        # Dica: você pode usar super().calcular_salario() para obter o salário base.
        salario_pai = super().calcular_salario()
        bonus = salario_pai * self.bonus_percentual
        return salario_pai + bonus

    def exibir_info(self):
        """
        Sobrescreve o método da classe pai, adicionando info do departamento e bônus.
        """
        # TODO: Chame super().exibir_info() para exibir as informações base,
        # depois adicione as informações específicas do Gerente:
        #   Departamento: [departamento]
        #   Bônus:        R$ [valor do bônus]
        super().exibir_info()
        bonus_valor = super().calcular_salario() * self.bonus_percentual
        print(f"Departamento:  {self.departamento}")
        print(f"Bônus:        R$ {bonus_valor:.2f}")


# -----------------------------------------------------------------------------
# CLASSE FILHA 2: Estagiario
# -----------------------------------------------------------------------------

class Estagiario(Funcionario):
    """
    Representa um Estagiário, que É UM Funcionario com carga horária reduzida.

    Atributos herdados: nome, cpf, salario_base
    Atributos próprios:
        curso (str): Curso que o estagiário está cursando.
        carga_horaria (int): Horas trabalhadas por semana (máximo: 30h).
    """

    def __init__(self, nome, cpf, salario_base, curso, carga_horaria):
        """
        Inicializa um Estagiário.

        Args:
            nome (str): Nome do estagiário.
            cpf (str): CPF.
            salario_base (float): Bolsa-auxílio mensal.
            curso (str): Nome do curso de graduação.
            carga_horaria (int): Horas semanais (máx 30).
        """
        # TODO: Use super().__init__() para inicializar os atributos da classe pai
        super().__init__(nome, cpf, salario_base)

        # TODO: Atribua os atributos específicos.
        # Se a carga_horaria for maior que 30, defina como 30 e avise o usuário.
        self.curso = curso
        if carga_horaria > 30:
            print(f"Aviso: Carga horária de {carga_horaria}h excede o limite legal. Definida para 30h.")
            self.carga_horaria = 30
        else:
            self.carga_horaria = int(carga_horaria)

    def calcular_salario(self):
        """
        Calcula o salário do estagiário proporcional à carga horária.
        A bolsa é proporcional: (carga_horaria / 30) * salario_base.

        Returns:
            float: Bolsa proporcional.
        """
        # TODO: Calcule e retorne a bolsa proporcional
        return (self.carga_horaria / 30) * super().calcular_salario()

    def exibir_info(self):
        """
        Sobrescreve o método da classe pai, adicionando info do curso e carga horária.
        """
        # TODO: Chame super().exibir_info() e adicione:
        #   Curso:          [curso]
        #   Carga Horária:  [carga_horaria]h/semana
        super().exibir_info()
        print(f"Curso:         {self.curso}")
        print(f"Carga Horária: {self.carga_horaria}h/semana")


# =============================================================================
# BLOCO DE TESTES
# =============================================================================

if __name__ == "__main__":

    print("=" * 55)
    print("  SISTEMA DE FUNCIONÁRIOS")
    print("=" * 55)

    func = Funcionario("João Silva", "111.222.333-44", 3000.00)
    func.exibir_info()

    print("\n" + "-" * 55)

    gerente = Gerente("Mariana Souza", "222.333.444-55", 8000.00, "Tecnologia", 0.20)
    gerente.exibir_info()

    print("\n" + "-" * 55)

    estagiario = Estagiario("Pedro Santos", "333.444.555-66", 1500.00, "Engenharia de Software", 25)
    estagiario.exibir_info()

    print("\n" + "-" * 55)

    print("--- EXECUÇÃO DO DESAFIO (POLIMORFISMO) ---\n")
    funcionarios = [func, gerente, estagiario]
    for f in funcionarios:
        f.exibir_info()
        print()

    print("Exercício concluído!")