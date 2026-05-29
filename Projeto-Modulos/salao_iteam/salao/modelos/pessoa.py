# salao/modelos/pessoa.py
# =============================================================================
# ITEAM | Projeto: Salão de Beleza & Barbearia
# Módulo : salao.modelos.pessoa
# Assunto: Classes, Atributos, Encapsulamento e @property  (Seção 5.2 e 5.3.1)
# =============================================================================
#
# ----------------------------------------------------------------------------
#  BUG 1 — Atributo privado declarado errado
#  ONDE  : linha com  self.nome  (dentro de __init__)
#  ERRO  : o atributo deveria ser PRIVADO (__nome), mas está público (nome).
#          Isso quebra o encapsulamento: qualquer código externo pode alterar
#          o nome sem nenhuma validação.
#  DICA  : troque  self.nome = nome  por  self.__nome = nome
#          e faça o mesmo para  self.cpf  →  self.__cpf
# ----------------------------------------------------------------------------
#
# ----------------------------------------------------------------------------
#  BUG 2 — @property retornando atributo errado
#  ONDE  : getter  def nome(self)
#  ERRO  : está retornando  self.nome  (recursão infinita!) em vez de
#          self.__nome  (o atributo privado correto).
#  DICA  : troque  return self.nome  por  return self.__nome
#          Faça o mesmo para o getter de cpf.
# ----------------------------------------------------------------------------


class Pessoa:
    """
    Classe BASE que representa qualquer pessoa do salão.
    Demonstra encapsulamento com atributos privados e @property.
    """

    def __init__(self, nome: str, cpf: str, telefone: str):
        # BUG 1 ↓  atributos deveriam ser privados (__nome, __cpf)
        self.__nome     = nome.strip().title()   # CORRIGIDO
        self.__cpf    = cpf.strip()
        self.telefone = telefone.strip()

    # --- getters (leitura controlada) ---

    @property
    def nome(self):
        # BUG 2 ↓  recursão infinita! deveria retornar self.__nome
        return self.__nome   #CORRIGIDO

    @property
    def cpf(self):
        return self.__cpf

    # --- setter com validação ---

    @nome.setter
    def nome(self, valor: str):
        if not valor.strip():
            raise ValueError("O nome não pode ser vazio.")
        self.__nome = valor.strip().title()

    # --- representação ---

    def __str__(self):
        return f"Pessoa: {self.nome} | CPF: {self.cpf} | Tel: {self.telefone}"

    def __repr__(self):
        return f"Pessoa(nome='{self.nome}', cpf='{self.cpf}')"
