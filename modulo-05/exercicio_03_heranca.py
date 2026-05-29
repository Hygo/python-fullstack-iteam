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
        """
        # TODO: Atribua os parâmetros aos atributos de instância
        self.nome = nome
        self.cpf = cpf
        self.salario_base = float(salario_base)

    def calcular_salario(self):
        """
        Retorna o salário final do funcionário.
        Para a classe base, o salário final é igual ao salário base.
        """
        # TODO: Retorne o salario_base
        return self.salario_base

    def exibir_info(self):
        """
        Exibe as informações do funcionário de forma formatada.
        """
        # TODO: Imprima as informações no formato solicitado
        # type(self).__name__ descobre dinamicamente a classe real do objeto
        print(f"[Tipo: {type(self).__name__}]")
        print(f"Nome:          {self.nome}")
        print(f"CPF:           {self.cpf}")
        print(f"Salário Base:  R$ {self.salario_base:.2f}")
        print(f"Salário Final: R$ {self.calcular_salario():2f}")

    def __str__(self):
        """Representação em string do funcionário."""
        return f"Funcionario({self.nome}, CPF: {self.cpf})"


# -----------------------------------------------------------------------------
# CLASSE FILHA 1: Gerente
# -----------------------------------------------------------------------------

class Gerente(Funcionario):
    """
    Representa um Gerente, que É UM Funcionario com bônus adicional.
    """

    def __init__(self, nome, cpf, salario_base, departamento, bonus_percentual):
        """
        Inicializa um Gerente, reaproveitando o construtor da classe pai.
        """
        # TODO: Use super().__init__() para inicializar os atributos da classe pai
        super().__init__(nome, cpf, salario_base)

        # TODO: Atribua os novos atributos específicos do Gerente
        self.departamento = departamento
        self.bonus_percentual = float(bonus_percentual)

    def calcular_salario(self):
        """
        Calcula o salário do Gerente: salário base + bônus.
        """
        # TODO: Calcule o bônus e retorne a soma com o salário base.
        salario_base = super().calcular_salario()
        bonus = salario_base * self.bonus_percentual
        return salario_base + bonus

    def exibir_info(self):
        """
        Sobrescreve o método da classe pai, adicionando info do departamento e bônus.
        """
        # TODO: Chame super().exibir_info() para exibir as informações base,
        # depois adicione as informações específicas do Gerente:
        super().exibir_info()
        bonus_valor = super().calcular_salario() * self.bonus_percentual
        print(f"Departamento:  {self.departamento}")
        print(f"Bônus:         R$ {bonus_valor:.2f}")


# -----------------------------------------------------------------------------
# CLASSE FILHA 2: Estagiario
# -----------------------------------------------------------------------------

class Estagiario(Funcionario):
    """
    Representa um Estagiário, que É UM Funcionario com carga horária reduzida.
    """

    def __init__(self, nome, cpf, salario_base, curso, carga_horaria):
        """
        Inicializa um Estagiário.
        """
        # TODO: Use super().__init__() para inicializar os atributos da classe pai
        super().__init__(nome, cpf, salario_base)

        # TODO: Atribua os atributos específicos com validação da carga horária.
        self.curso = curso
        
        if carga_horaria > 30:
            print(f"Aviso: Carga horária de {carga_horaria}h excede o limite legal de estágio. Definida para 30h.")
            self.carga_horaria = 30
        else:
            self.carga_horaria = carga_horaria

    def calcular_salario(self):
        """
        Calcula o salário do estagiário proporcional à carga horária.
        """
        # TODO: Calcule e retorne a bolsa proporcional
        base = super().calcular_salario()
        return (self.carga_horaria / 30) * base

    def exibir_info(self):
        """
        Sobrescreve o método da classe pai, adicionando info do curso e carga horária.
        """
        # TODO: Chame super().exibir_info() e adicione os dados específicos
        super().exibir_info()
        print(f"Curso:         {self.curso}")
        print(f"Carga Horária: {self.carga_horaria}h/semana")


# =============================================================================
# BLOCO DE TESTES
# =============================================================================

if __name__ == "__main__":

    print("=" * 55)
    print("  SISTEMA DE FUNCIONÁRIOS - ITEAM")
    print("=" * 55)

    # 1. Instanciando um objeto Funcionario genérico
    print("\n--- Criando Funcionário Base ---")
    func = Funcionario("João Silva", "111.222.333-44", 3000.00)
    func.exibir_info()

    # 2. Instanciando um Gerente (20% de bônus)
    print("\n" + "-" * 55)
    print("--- Criando Gerente ---")
    gerente = Gerente("Ana Costa", "222.333.444-55", 8000.00, "Desenvolvimento", 0.20)
    gerente.exibir_info()

    # 3. Instanciando um Estagiário (25h semanais)
    print("\n" + "-" * 55)
    print("--- Criando Estagiário ---")
    estagiario = Estagiario("Pedro Santos", "333.444.555-66", 1500.00, "Análise e Des. de Sistemas", 25)
    estagiario.exibir_info()

    # 4. DESAFIO EXTRA: Validando limite do estagiário (> 30h)
    print("\n" + "-" * 55)
    print("--- Testando Limite de Carga Horária ---")
    estagiario_abuso = Estagiario("Lucas Lima", "444.555.666-77", 1500.00, "Ciência da Computação", 40)

    # 5. DESAFIO POLIMORFISMO: Percorrendo uma lista única de funcionários
    print("\n" + "-" * 55)
    print("--- DESAFIO: Relatório Polimórfico Integrado ---")
    
    funcionarios = [func, gerente, estagiario, estagiario_abuso]
    
    for f in funcionarios:
        print("\n" + "." * 35)
        # O Python descobre o método correto em tempo de execução!
        f.exibir_info()

    print("\nExercício concluído!")