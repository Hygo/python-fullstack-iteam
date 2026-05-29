# salao/modelos/funcionario.py
# =============================================================================
# ITEAM | Projeto: Salão de Beleza & Barbearia
# Módulo : salao.modelos.funcionario
# Assunto: Herança, super() e Polimorfismo              (Seções 5.3.2 e 5.6)
# =============================================================================
#
# ----------------------------------------------------------------------------
#  BUG 3 — super().__init__() com argumentos errados
#  ONDE  : dentro de  Funcionario.__init__
#  ERRO  : a chamada  super().__init__(nome, cpf)  está passando apenas 2
#          argumentos, mas  Pessoa.__init__  exige 3: nome, cpf e telefone.
#  DICA  : troque por  super().__init__(nome, cpf, telefone)
# ----------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------
#  BUG 4 — calcular_comissao retorna valor fixo em vez de calcular
#  ONDE  : método  calcular_comissao  da classe  Coordenador
#  ERRO  : o método retorna  0  sempre, ignorando o atributo  percentual_bonus.
#          A fórmula correta é: salario_base * percentual_bonus
#  DICA  : troque  return 0  por  return self.salario_base * self.percentual_bonus
# ----------------------------------------------------------------------------

from salao.modelos.pessoa import Pessoa


class Funcionario(Pessoa):
    """
    Representa um funcionário do salão.
    Herda de Pessoa e adiciona cargo e salário base.
    """

    def __init__(self, nome: str, cpf: str, telefone: str,
                 cargo: str, salario_base: float):
        # BUG 3 CORRIGIDO: Passando corretamente nome, cpf e telefone para a classe pai
        super().__init__(nome, cpf, telefone)   
        self.cargo       = cargo.strip().title()
        self.salario_base = salario_base

    def calcular_salario(self) -> float:
        """Retorna o salário final. Pode ser sobrescrito pelas subclasses."""
        return self.salario_base

    def __str__(self):
        return (
            f"[{self.cargo}] {self.nome} "
            f"| Salário: R$ {self.calcular_salario():.2f}"
        )


class Coordenador(Funcionario):
    """
    Coordenador recebe salário base + bônus percentual.
    Demonstra sobrescrita de método (polimorfismo).
    """

    def __init__(self, nome: str, cpf: str, telefone: str,
                 salario_base: float, percentual_bonus: float):
        super().__init__(nome, cpf, telefone, "Coordenador", salario_base)
        self.percentual_bonus = percentual_bonus   # ex: 0.15 = 15 %

    def calcular_comissao(self) -> float:
        # BUG 4 CORRIGIDO: Agora calcula o bônus real com base no percentual
        return self.salario_base * self.percentual_bonus   

    def calcular_salario(self) -> float:
        """Salário do coordenador = base + bônus."""
        return self.salario_base + self.calcular_comissao()

    def __str__(self):
        return (
            f"[Coordenador] {self.nome} "
            f"| Base: R$ {self.salario_base:.2f} "
            f"| Bônus: R$ {self.calcular_comissao():.2f} "
            f"| Total: R$ {self.calcular_salario():.2f}"
        )