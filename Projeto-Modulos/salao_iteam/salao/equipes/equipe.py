# salao/equipes/equipe.py
# =============================================================================
# ITEAM | Projeto: Salão de Beleza & Barbearia
# Módulo : salao.equipes.equipe
# Assunto: Interface / Classe Abstrata com ABC             (Seção 5.3.3 e 5.7)
# =============================================================================
#
# ----------------------------------------------------------------------------
#  BUG 7 — Classe abstrata sem herdar de ABC
#  ONDE  : definição  class Equipe:
#  ERRO  : a classe tenta usar @abstractmethod, mas não herda de ABC.
#          Sem isso, o Python NÃO vai impedir que Equipe seja instanciada
#          diretamente, e os métodos abstratos viram métodos comuns.
#  DICA  : troque  class Equipe:  por  class Equipe(ABC):
#          e certifique-se de que o import  from abc import ABC, abstractmethod
#          está presente (já está correto aqui).
# ----------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------
#  BUG 8 — @abstractmethod faltando no método realizar_servico
#  ONDE  : método  realizar_servico
#  ERRO  : o método deveria ser abstrato (forçar subclasses a implementar),
#          mas está faltando o decorador @abstractmethod.
#  DICA  : adicione  @abstractmethod  na linha antes de  def realizar_servico
# ----------------------------------------------------------------------------
from abc import ABC, abstractmethod
from salao.modelos.funcionario import Funcionario


# BUG 7 CORRIGIDO: A classe agora herda de ABC para se tornar genuinamente abstrata
class Equipe(ABC):          
    """
    Interface base para todas as equipes do salão.
    Define o contrato que TODA equipe deve cumprir.
    """

    def __init__(self, nome_equipe: str):
        self.nome_equipe  = nome_equipe
        self._membros: list[Funcionario] = []    # protegido (convenção _)

    def adicionar_membro(self, funcionario: Funcionario):
        """Adiciona um funcionário à equipe."""
        if not isinstance(funcionario, Funcionario):
            raise TypeError("Apenas Funcionario pode ser adicionado à equipe.")
        self._membros.append(funcionario)
        print(f"  + {funcionario.nome} adicionado(a) à equipe '{self.nome_equipe}'.")

    def listar_membros(self):
        """Exibe todos os membros da equipe."""
        print(f"\n  Equipe: {self.nome_equipe}")
        print("  " + "-" * 36)
        if not self._membros:
            print("  (nenhum membro cadastrado)")
        for m in self._membros:
            print(f"  • {m}")

    @abstractmethod       
    def descricao_servicos(self) -> str:
        """Retorna os serviços oferecidos pela equipe."""
        pass

    # BUG 8 CORRIGIDO: Adicionado o decorador @abstractmethod
    @abstractmethod
    def realizar_servico(self, cliente: str, servico: str):  
        """Registra a realização de um serviço."""
        pass

    def __str__(self):
        return f"Equipe '{self.nome_equipe}' | {len(self._membros)} membro(s)"
    