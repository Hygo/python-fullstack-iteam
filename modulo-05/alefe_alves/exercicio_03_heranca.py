# =============================================================================
# ITEAM - CURSO DE CAPACITAÇÃO EM DESENVOLVIMENTO FULL STACK
# Programação em Python | Módulo 5 - Programação Orientada a Objetos
# =============================================================================
#
# EXERCÍCIO 03 - HERANÇA E FUNÇÃO super()
#
# Tema: Sistema de Funcionários de uma Empresa
#
# Objetivo:
#   Construir uma hierarquia de classes usando herança para modelar diferentes
#   tipos de funcionários de uma empresa, reutilizando código da classe pai e
#   especializando comportamentos nas classes filhas.
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
        self.salario_base = salario_base

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
        print(f"""
        [Tipo: {type(self).__name__ }]
        Nome:         {self.nome}
        CPF:          {self.cpf}
        Salário Base: R$ {self.salario_base}
        Salário Final: R$ {self.calcular_salario()}""")

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
        self.bonus_percentual = bonus_percentual

    def calcular_salario(self):
        """
        Calcula o salário do Gerente: salário base + bônus.

        O bônus é calculado como: salario_base * bonus_percentual

        Returns:
            float: Salário base + valor do bônus.
        """
        # TODO: Calcule o bônus e retorne a soma com o salário base.
        # Dica: você pode usar super().calcular_salario() para obter o salário base.
        base = super().calcular_salario()
        return  base + (base * self.bonus_percentual)

    def exibir_info(self):
        """
        Sobrescreve o método da classe pai, adicionando info do departamento e bônus.
        """
        # TODO: Chame super().exibir_info() para exibir as informações base,
        # depois adicione as informações específicas do Gerente:
        #   Departamento: [departamento]
        #   Bônus:        R$ [valor do bônus]
        super().exibir_info()
        print(f"""
        Departamento: {self.departamento}
        Bônus:        R$ {self.bonus_percentual}
        """)


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
        self.carga_horaria = carga_horaria

    def calcular_salario(self):
        """
        Calcula o salário do estagiário proporcional à carga horária.
        A bolsa é proporcional: (carga_horaria / 30) * salario_base.

        Returns:
            float: Bolsa proporcional.
        """
        # TODO: Calcule e retorne a bolsa proporcional
        return (self.carga_horaria/30) * super().calcular_salario()

    def exibir_info(self):
        """
        Sobrescreve o método da classe pai, adicionando info do curso e carga horária.
        """
        # TODO: Chame super().exibir_info() e adicione:
        #   Curso:          [curso]
        #   Carga Horária:  [carga_horaria]h/semana
        super().exibir_info()
        print(f"""
        Curso:          {self.curso}
        Carga Horária:  {self.carga_horaria} h/semana
        """)


# =============================================================================
# BLOCO DE TESTES
# =============================================================================

if __name__ == "__main__":

    print("=" * 55)
    print("  SISTEMA DE FUNCIONÁRIOS - ITEAM")
    print("=" * 55)

    # TODO: Instancie um objeto Funcionario genérico e chame exibir_info()
    # func = Funcionario("João Silva", "111.222.333-44", 3000.00)
    func = Funcionario("João Silva", "111.222.333-44", 3000.00)
    func.exibir_info()

    print("\n" + "-" * 55)

    # TODO: Instancie um Gerente com 20% de bônus e exiba as informações
    gerente = Gerente("Carlos Alves", "111.111.111-11", 3000.00, "Vendas", 0.2)
    gerente.exibir_info()
    print("\n" + "-" * 55)

    # TODO: Instancie um Estagiario com 25h semanais e exiba as informações
    estagiario = Estagiario("Pedro Castro", "222.222.222-22", 1000.00, "Adiministração", 20)
    estagiario.exibir_info()
    print("\n" + "-" * 55)

    # TODO (DESAFIO): Crie uma lista com todos os funcionários e percorra-a,
    # chamando exibir_info() para cada um.
    # Observe como o Python chama o método correto para cada tipo!
    # funcionarios = [func, gerente, estagiario]
    # for f in funcionarios:
    #     f.exibir_info()
    
    funcionarios = [func, gerente, estagiario]
    for f in funcionarios:
        f.exibir_info()
    print("\nExercício concluído!")
