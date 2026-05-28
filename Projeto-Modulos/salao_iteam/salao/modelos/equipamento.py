# salao/modelos/equipamento.py
# =============================================================================
# ITEAM | Projeto: Salão de Beleza & Barbearia
# Módulo : salao.modelos.equipamento
# Assunto: Métodos Especiais (__str__, __repr__, __eq__)    (Seção 5.4)
# =============================================================================
#
# ----------------------------------------------------------------------------
#  BUG 5 — __str__ referenciando atributo que não existe
#  ONDE  : método  __str__  da classe  Equipamento
#  ERRO  : o método tenta acessar  self.descricao, mas o atributo foi
#          declarado como  self.__descricao  (privado). Fora da classe,
#          isso causaria AttributeError; dentro da classe também está
#          escrito errado — falta o prefixo __ correto.
#  DICA  : troque  self.descricao  por  self.__descricao  no __str__
# ----------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------
#  BUG 6 — __eq__ comparando pelo nome em vez do código
#  ONDE  : método  __eq__
#  ERRO  : dois equipamentos são considerados iguais se tiverem o mesmo NOME,
#          mas o correto é comparar pelo CÓDIGO (self.__codigo), que é único.
#  DICA  : troque  self.nome == outro.nome  por  self.__codigo == outro.__codigo
#          Lembre-se: acesso ao atributo privado de OUTRO objeto usa name-mangling:
#          outro._Equipamento__codigo
# ----------------------------------------------------------------------------


class Equipamento:
    """
    Representa um equipamento do salão (secador, cadeira, autoclave...).
    Demonstra métodos especiais dunder.
    """

    def __init__(self, codigo: str, nome: str, descricao: str, valor: float):
        self.__codigo   = codigo.strip().upper()
        self.__nome       = nome.strip().title()
        self.__descricao = descricao.strip()
        self.valor      = valor

    @property
    def codigo(self):
        return self.__codigo

    # BUG 5 ↓  atributo escrito errado dentro do método
    def __str__(self):
        return (
            f"[{self.__codigo}] {self.__nome} "
            f"| {self.__descricao} "        # ← ERRADO: deveria ser self.__descricao
            f"| R$ {self.valor:.2f}"
        )

    def __repr__(self):
        return f"Equipamento(codigo='{self.__codigo}', nome='{self.__nome}')"

    # BUG 6 ↓  comparando nome em vez do código único
    def __eq__(self, outro):
        if not isinstance(outro, Equipamento):
            return False
        return self.__codigo == outro._Equipamento__codigo    # ← ERRADO: deveria comparar self.__codigo == outro._Equipamento__codigo
