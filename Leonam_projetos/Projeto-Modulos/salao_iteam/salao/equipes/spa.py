# salao/equipes/spa.py
# =============================================================================
# ITEAM | Projeto: Salão de Beleza & Barbearia
# Módulo : salao.equipes.spa
# Assunto: Atributos de instância e __init__               (Seção 5.2.2)
# =============================================================================
#
# ----------------------------------------------------------------------------
#  BUG 11 — Atributo 'pacotes_disponiveis' usado sem ser declarado no __init__
#  ONDE  : método  descricao_servicos  e  realizar_servico
#  ERRO  : o código referencia  self.pacotes_disponiveis, mas esse atributo
#          nunca é criado no  __init__. Isso gera AttributeError na execução.
#  DICA  : adicione no __init__, após o super().__init__:
#          self.pacotes_disponiveis = ["Relaxamento", "Pedras quentes",
#                                      "Aromaterapia", "Drenagem"]
# ----------------------------------------------------------------------------

from salao.equipes.equipe import Equipe


class EquipeSpa(Equipe):
    """
    Equipe responsável pelos serviços de spa e bem-estar.
    """

    def __init__(self):
        super().__init__("Spa & Bem-estar")
        # BUG 11 ↓  atributo 'pacotes_disponiveis' não declarado aqui
        # DICA: adicione a linha abaixo após o super().__init__:
        # self.pacotes_disponiveis = ["Relaxamento", "Pedras quentes", "Aromaterapia", "Drenagem"]
        super().__init__("Spa & Bem-estar")
        self.pacotes_disponiveis = ["Relaxamento", "Pedras quentes", "Aromaterapia", "Drenagem"]  # ← CORRIGIDO: atributo declarado corretamente

    def descricao_servicos(self) -> str:
        # BUG 11 ↓  AttributeError: 'EquipeSpa' object has no attribute 'pacotes_disponiveis'
        pacotes = ", ".join(self.pacotes_disponiveis)   # ← ERRO em tempo de execução
        return f"Serviços de spa: {pacotes}."

    def realizar_servico(self, cliente: str, servico: str):
        # BUG 11 ↓  mesmo problema aqui
        if servico not in self.pacotes_disponiveis:     # ← ERRO em tempo de execução
            print(f"  [Spa] Serviço '{servico}' não disponível.")
            return
        print(f"  [Spa] Iniciando pacote '{servico}' para {cliente}. Relaxe!")
