# salao/equipes/manicure.py
# =============================================================================
# ITEAM | Projeto: Salão de Beleza & Barbearia
# Módulo : salao.equipes.manicure
# Assunto: Polimorfismo e Duck Typing                      (Seção 5.3.3 e 5.7)
# =============================================================================
#
# ----------------------------------------------------------------------------
#  BUG 10 — realizar_servico com assinatura diferente da interface
#  ONDE  : método  realizar_servico  de  EquipeManicure
#  ERRO  : a assinatura é  realizar_servico(self, cliente)  — falta o parâmetro
#          'servico'. Isso quebra o polimorfismo: quando o sistema chamar
#          equipe.realizar_servico(cliente, servico) para qualquer equipe,
#          a EquipeManicure vai lançar TypeError por argumento a mais.
#  DICA  : troque  def realizar_servico(self, cliente: str):
#          por    def realizar_servico(self, cliente: str, servico: str):
#          e use  servico  na mensagem de print.
# ----------------------------------------------------------------------------

from salao.equipes.equipe import Equipe


class EquipeManicure(Equipe):
    """
    Equipe responsável pelos serviços de manicure e pedicure.
    """

    def __init__(self):
        super().__init__("Manicure & Pedicure")

    def descricao_servicos(self) -> str:
        return "Manicure, pedicure, nail art e esmaltação em gel."

    # BUG 10 ↓  assinatura diferente — falta o parâmetro 'servico'
    def realizar_servico(self, cliente: str, servico: str):   # CORRIGIDO
        print(f"  [Manicure] Realizando '{servico}' para {cliente}.")  # CORRIGIDO

    