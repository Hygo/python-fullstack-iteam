# salao/equipes/cabelo.py
# =============================================================================
# ITEAM | Projeto: Salão de Beleza & Barbearia
# Módulo : salao.equipes.cabelo
# Assunto: Herança e implementação de interface            (Seção 5.3.2)
# =============================================================================
#
# ----------------------------------------------------------------------------
#  BUG 9 — Classe não herda de Equipe
#  ONDE  : definição  class EquipeCabelo:
#  ERRO  : a classe deveria herdar de Equipe para respeitar o contrato
#          da interface. Sem herança, os métodos de Equipe não estão
#          disponíveis (adicionar_membro, listar_membros etc.).
#  DICA  : troque  class EquipeCabelo:  por  class EquipeCabelo(Equipe):
#          e não esqueça o  super().__init__("Cabelo & Barba")  no __init__.
# ----------------------------------------------------------------------------

from salao.equipes.equipe import Equipe


# BUG 9 CORRIGIDO: A classe agora herda diretamente de Equipe
class EquipeCabelo(Equipe):    
    """
    Equipe responsável pelos serviços de cabelo e barba.
    """

    def __init__(self):
        # BUG 9 CORRIGIDO: Chama o construtor da classe pai passando o nome correto.
        # A inicialização da lista de membros agora é herdada automaticamente.
        super().__init__("Cabelo & Barba") 

    def descricao_servicos(self) -> str:
        return "Corte, coloração, escova, barba e bigode."

    def realizar_servico(self, cliente: str, servico: str):
        print(f"  [Cabelo & Barba] Realizando '{servico}' para {cliente}.")

    def __str__(self):
        return f"Equipe '{self.nome_equipe}' | {len(self._membros)} membro(s)"