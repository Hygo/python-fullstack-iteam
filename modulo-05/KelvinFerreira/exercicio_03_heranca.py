# =============================================================================
# ITEAM - CURSO DE CAPACITAÇÃO EM DESENVOLVIMENTO FULL STACK
# Programação em Python | Módulo 5 - Programação Orientada a Objetos
# =============================================================================
#
# EXERCÍCIO 03 - HERANÇA E FUNÇÃO super()
#
# Aluno: Kelvin Araújo Ferreira
# =============================================================================


# -----------------------------------------------------------------------------
# CLASSE PAI
# -----------------------------------------------------------------------------

class Funcionario:
    """Representa um funcionário genérico da empresa ITEAM."""

    def __init__(self, nome, cpf, salario_base):
        self.nome = nome
        self.cpf = cpf
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def exibir_info(self):
        print(f"[Tipo: {type(self).__name__}]")
        print(f"Nome:          {self.nome}")
        print(f"CPF:           {self.cpf}")
        print(f"Salário Base:  R$ {self.salario_base:,.2f}")
        print(f"Salário Final: R$ {self.calcular_salario():,.2f}")

    def __str__(self):
        return f"Funcionario({self.nome}, CPF: {self.cpf})"


# -----------------------------------------------------------------------------
# CLASSE FILHA 1: Gerente
# -----------------------------------------------------------------------------

class Gerente(Funcionario):
    """Gerente com bônus sobre o salário base."""

    def __init__(self, nome, cpf, salario_base, departamento, bonus_percentual):
        super().__init__(nome, cpf, salario_base)
        self.departamento = departamento
        self.bonus_percentual = bonus_percentual

    def calcular_salario(self):
        bonus = self.salario_base * self.bonus_percentual
        return super().calcular_salario() + bonus

    def exibir_info(self):
        super().exibir_info()
        bonus = self.salario_base * self.bonus_percentual
        print(f"Departamento:  {self.departamento}")
        print(f"Bônus:         R$ {bonus:,.2f} ({self.bonus_percentual * 100:.0f}%)")


# -----------------------------------------------------------------------------
# CLASSE FILHA 2: Estagiario
# -----------------------------------------------------------------------------

class Estagiario(Funcionario):
    """Estagiário com bolsa proporcional à carga horária."""

    def __init__(self, nome, cpf, salario_base, curso, carga_horaria):
        super().__init__(nome, cpf, salario_base)
        self.curso = curso
        if carga_horaria > 30:
            print(f"Carga horária {carga_horaria}h excede o limite. Ajustada para 30h.")
            self.carga_horaria = 30
        else:
            self.carga_horaria = carga_horaria

    def calcular_salario(self):
        return (self.carga_horaria / 30) * self.salario_base

    def exibir_info(self):
        super().exibir_info()
        print(f"Curso:          {self.curso}")
        print(f"Carga Horária:  {self.carga_horaria}h/semana")


# =============================================================================
# BLOCO DE TESTES
# =============================================================================

if __name__ == "__main__":

    print("=" * 55)
    print("  SISTEMA DE FUNCIONÁRIOS - ITEAM")
    print("=" * 55)

    func = Funcionario("João Silva", "111.222.333-44", 3000.00)
    func.exibir_info()

    print("\n" + "-" * 55)

    gerente = Gerente(
        "Ana Paula", "444.555.666-77",
        8000.00, "Tecnologia", 0.20
    )
    gerente.exibir_info()

    print("\n" + "-" * 55)

    estagiario = Estagiario(
        "Kelvin Araújo", "999.888.777-66",
        1500.00, "Sistemas de Informação", 25
    )
    estagiario.exibir_info()

    print("\n" + "-" * 55)

    # Desafio: polimorfismo — mesmo loop, método correto para cada tipo
    print("\nTodos os funcionários (polimorfismo):")
    for f in [func, gerente, estagiario]:
        print(f"\n{f}")
        f.exibir_info()

    print("\nExercício concluído!")
