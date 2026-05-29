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
        # BUG 11 CORRIGIDO: Atributo de instância declarado e inicializado corretamente no construtor
        self.pacotes_disponiveis = [
            "Relaxamento", 
            "Pedras quentes", 
            "Aromaterapia", 
            "Drenagem"
        ]

    def descricao_servicos(self) -> str:
        # Agora self.pacotes_disponiveis existe e a junção dos elementos funciona perfeitamente
        pacotes = ", ".join(self.pacotes_disponiveis)   
        return f"Serviços de spa: {pacotes}."

    def realizar_servico(self, cliente: str, servico: str):
        # A validação agora consegue ler os pacotes ativos sem gerar exceções
        if servico not in self.pacotes_disponiveis:     
            print(f"  [Spa] Serviço '{servico}' não disponível.")
            return
        print(f"  [Spa] Iniciando pacote '{servico}' para {cliente}. Relaxe!")
