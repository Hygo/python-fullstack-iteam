# =============================================================================
# ITEAM - CURSO DE CAPACITAÇÃO EM DESENVOLVIMENTO FULL STACK
# Programação em Python | Módulo 5 - Programação Orientada a Objetos
# =============================================================================
#
# EXERCÍCIO 05 - PROJETO INTEGRADOR: SISTEMA DE BIBLIOTECA
#
# Tema: Biblioteca Digital da ITEAM
#
# Objetivo:
#   Integrar TODOS os conceitos do Módulo 5 em um mini-sistema funcional:
#   encapsulamento, herança, polimorfismo, composição e métodos especiais.
#
# Estrutura de classes:
#
#   ItemBiblioteca (classe base)
#       ├── Livro
#       └── Revista
#
#   Pessoa (classe base)
#       ├── Aluno   (pode realizar até 3 empréstimos simultâneos)
#       └── Professor (pode realizar até 5 empréstimos simultâneos)
#
#   Biblioteca (usa COMPOSIÇÃO: "tem" listas de itens e membros)
#
# Conceitos integrados:
#   ✔ Classes e objetos                    (5.2)
#   ✔ Encapsulamento com @property         (5.3.1 e 5.5.1)
#   ✔ Herança e super()                    (5.3.2 e 5.6)
#   ✔ Polimorfismo (método info_completa)  (5.3.3 e 5.7)
#   ✔ Métodos especiais __str__ e __eq__   (5.4)
#   ✔ Composição: Biblioteca "tem" itens   (5.5)
#   ✔ Princípio da Responsabilidade Única  (5.8)
#
# Referência: Módulo 5 completo da Apostila ITEAM
# =============================================================================


# =============================================================================
# PARTE 1 - HIERARQUIA DE ITENS DO ACERVO
# =============================================================================

class ItemBiblioteca:
    """
    Classe base para todos os itens do acervo da biblioteca.

    Atributos:
        __codigo (str): Código único do item (privado).
        titulo (str): Título do item.
        ano_publicacao (int): Ano de publicação.
        __disponivel (bool): Status de disponibilidade (privado).
    """

    def __init__(self, codigo, titulo, ano_publicacao):
        """
        Args:
            codigo (str): Código único do item.
            titulo (str): Título do item.
            ano_publicacao (int): Ano de publicação.
        """
        # TODO: Atribua codigo a __codigo (privado), titulo e ano_publicacao normalmente
        # O item começa disponível por padrão: self.__disponivel = True
        self.__codigo = None
        self.titulo = None
        self.ano_publicacao = None
        self.__disponivel = True

    @property
    def codigo(self):
        """Retorna o código do item (somente leitura)."""
        # TODO: Retorne __codigo
        pass

    @property
    def disponivel(self):
        """Retorna True se o item está disponível para empréstimo."""
        # TODO: Retorne __disponivel
        pass

    def emprestar(self):
        """
        Marca o item como indisponível. Retorna True se conseguiu, False se já estava emprestado.

        Returns:
            bool: Sucesso da operação.
        """
        # TODO: Se __disponivel for True, mude para False e retorne True.
        # Se já estiver False, retorne False (item já emprestado).
        pass

    def devolver(self):
        """
        Marca o item como disponível novamente.

        Returns:
            bool: Sucesso da operação (False se já estava disponível).
        """
        # TODO: Se __disponivel for False, mude para True e retorne True.
        # Se já estiver True, retorne False (item não estava emprestado).
        pass

    def info_completa(self):
        """
        Retorna uma string com informações completas do item.
        DEVE SER SOBRESCRITO pelas subclasses.
        """
        raise NotImplementedError("Subclasses devem implementar info_completa()")

    def __str__(self):
        """Representação resumida do item."""
        status = "✅ Disponível" if self.disponivel else "❌ Emprestado"
        return f"[{self.codigo}] {self.titulo} ({self.ano_publicacao}) - {status}"

    def __eq__(self, outro):
        """Dois itens são iguais se possuem o mesmo código."""
        # TODO: Compare self.codigo com outro.codigo
        pass


# -----------------------------------------------------------------------------
# Subclasse: Livro
# -----------------------------------------------------------------------------

class Livro(ItemBiblioteca):
    """
    Representa um livro no acervo.

    Atributos extras:
        autor (str): Nome do autor.
        isbn (str): Código ISBN do livro.
        num_paginas (int): Número de páginas.
    """

    def __init__(self, codigo, titulo, ano_publicacao, autor, isbn, num_paginas):
        # TODO: Chame super().__init__() com os parâmetros da classe pai
        # TODO: Atribua os atributos específicos do Livro
        self.autor = None
        self.isbn = None
        self.num_paginas = None

    def info_completa(self):
        """
        Retorna informações completas do livro.

        Returns:
            str: Bloco formatado com todos os dados do livro.
        """
        # TODO: Retorne (ou imprima) uma string formatada com todos os atributos:
        # Tipo, Código, Título, Autor, ISBN, Ano, Páginas, Disponibilidade
        pass


# -----------------------------------------------------------------------------
# Subclasse: Revista
# -----------------------------------------------------------------------------

class Revista(ItemBiblioteca):
    """
    Representa uma revista no acervo.

    Atributos extras:
        editora (str): Nome da editora.
        numero_edicao (int): Número da edição.
        periodicidade (str): Mensal, Semanal, Quinzenal etc.
    """

    def __init__(self, codigo, titulo, ano_publicacao, editora, numero_edicao, periodicidade):
        # TODO: Chame super().__init__() e atribua os atributos específicos
        self.editora = None
        self.numero_edicao = None
        self.periodicidade = None

    def info_completa(self):
        """Retorna informações completas da revista."""
        # TODO: Retorne uma string formatada com todos os atributos da revista
        pass


# =============================================================================
# PARTE 2 - HIERARQUIA DE MEMBROS (PESSOAS)
# =============================================================================

class Pessoa:
    """Classe base para membros da biblioteca."""

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self._emprestimos_ativos = []   # lista de objetos ItemBiblioteca

    @property
    def limite_emprestimos(self):
        """Deve ser definido pelas subclasses."""
        raise NotImplementedError

    def pode_emprestar(self):
        """Verifica se o membro pode realizar mais empréstimos."""
        return len(self._emprestimos_ativos) < self.limite_emprestimos

    def registrar_emprestimo(self, item):
        """
        Registra um empréstimo para este membro.

        Args:
            item (ItemBiblioteca): Item a ser emprestado.

        Returns:
            bool: True se o empréstimo foi registrado, False caso contrário.
        """
        # TODO: Verifique duas condições:
        #   1. self.pode_emprestar() deve ser True
        #   2. item.disponivel deve ser True
        # Se ambas forem True: chame item.emprestar(), adicione item a _emprestimos_ativos,
        # imprima mensagem de sucesso e retorne True.
        # Caso contrário: informe o motivo da falha e retorne False.
        pass

    def registrar_devolucao(self, item):
        """
        Registra a devolução de um item.

        Args:
            item (ItemBiblioteca): Item a ser devolvido.

        Returns:
            bool: True se a devolução foi registrada com sucesso.
        """
        # TODO: Verifique se 'item' está em self._emprestimos_ativos (use 'in' e __eq__)
        # Se estiver: chame item.devolver(), remova da lista e retorne True.
        # Se não estiver: informe que o item não estava registrado para este membro.
        pass

    def listar_emprestimos(self):
        """Exibe todos os itens atualmente emprestados pelo membro."""
        # TODO: Se _emprestimos_ativos estiver vazio, informe que não há empréstimos.
        # Caso contrário, liste cada item usando __str__ (basta usar print(item)).
        pass

    def __str__(self):
        tipo = type(self).__name__
        return f"{tipo}: {self.nome} | CPF: {self.cpf} | Empréstimos: {len(self._emprestimos_ativos)}/{self.limite_emprestimos}"


class AlunoMembro(Pessoa):
    """Aluno membro da biblioteca. Limite: 3 empréstimos simultâneos."""

    def __init__(self, nome, cpf, matricula):
        # TODO: Chame super().__init__() e atribua matricula
        self.matricula = None

    @property
    def limite_emprestimos(self):
        # TODO: Retorne 3
        pass


class ProfessorMembro(Pessoa):
    """Professor membro da biblioteca. Limite: 5 empréstimos simultâneos."""

    def __init__(self, nome, cpf, disciplina):
        # TODO: Chame super().__init__() e atribua disciplina
        self.disciplina = None

    @property
    def limite_emprestimos(self):
        # TODO: Retorne 5
        pass


# =============================================================================
# PARTE 3 - CLASSE BIBLIOTECA (COMPOSIÇÃO)
# =============================================================================

class Biblioteca:
    """
    Gerencia o acervo e os membros da biblioteca.

    Esta classe usa COMPOSIÇÃO: ela "tem" listas de itens e membros,
    mas não herda nenhuma dessas classes.

    Atributos:
        nome (str): Nome da biblioteca.
        __acervo (list): Lista de ItemBiblioteca.
        __membros (list): Lista de Pessoa.
    """

    def __init__(self, nome):
        self.nome = nome
        self.__acervo = []
        self.__membros = []

    def adicionar_item(self, item):
        """Adiciona um item ao acervo."""
        # TODO: Verifique se o item já não está no acervo (use 'in' — funciona com __eq__).
        # Se não estiver: adicione a __acervo e confirme.
        # Se já estiver: informe que o item já existe.
        pass

    def cadastrar_membro(self, pessoa):
        """Cadastra um membro na biblioteca."""
        # TODO: Adicione o membro à lista __membros e confirme o cadastro.
        pass

    def buscar_item_por_codigo(self, codigo):
        """
        Busca um item no acervo pelo código.

        Returns:
            ItemBiblioteca ou None: O item encontrado, ou None.
        """
        # TODO: Percorra __acervo e retorne o item cujo .codigo == codigo.
        # Se não encontrar, retorne None.
        pass

    def realizar_emprestimo(self, membro, codigo_item):
        """
        Realiza o empréstimo de um item para um membro.

        Args:
            membro (Pessoa): Membro que quer o empréstimo.
            codigo_item (str): Código do item desejado.
        """
        # TODO: Use buscar_item_por_codigo() para encontrar o item.
        # Se não encontrar: informe "item não encontrado".
        # Se encontrar: chame membro.registrar_emprestimo(item).
        pass

    def realizar_devolucao(self, membro, codigo_item):
        """Registra a devolução de um item."""
        # TODO: Use buscar_item_por_codigo() e depois membro.registrar_devolucao(item).
        pass

    def exibir_acervo(self):
        """Exibe todos os itens do acervo com seu status."""
        print(f"\n📚 ACERVO - {self.nome}")
        print("=" * 55)
        if not self.__acervo:
            print("  Acervo vazio.")
        else:
            for item in self.__acervo:
                print(f"  {item}")   # usa __str__ do item
        print("=" * 55)

    def exibir_membros(self):
        """Exibe todos os membros cadastrados."""
        print(f"\n👥 MEMBROS - {self.nome}")
        print("=" * 55)
        if not self.__membros:
            print("  Nenhum membro cadastrado.")
        else:
            for membro in self.__membros:
                print(f"  {membro}")  # usa __str__ da Pessoa
        print("=" * 55)


# =============================================================================
# BLOCO DE TESTES - SIMULAÇÃO COMPLETA DO SISTEMA
# =============================================================================

if __name__ == "__main__":

    print("=" * 55)
    print("  BIBLIOTECA DIGITAL - ITEAM")
    print("=" * 55)

    # --- PASSO 1: Crie a biblioteca ---
    # biblioteca = Biblioteca("Biblioteca ITEAM")

    # --- PASSO 2: Crie itens do acervo ---
    # livro1  = Livro("L001", "Python para Principiantes", 2012,
    #                 "Eugenia Bahit", "978-0000000001", 220)
    # livro2  = Livro("L002", "A Beginner's Guide to Python 3", 2020,
    #                 "John Hunt", "978-0000000002", 450)
    # revista = Revista("R001", "Python Magazine", 2024,
    #                   "Tech Press", 42, "Mensal")

    # --- PASSO 3: Adicione os itens ao acervo ---
    # biblioteca.adicionar_item(livro1)
    # biblioteca.adicionar_item(livro2)
    # biblioteca.adicionar_item(revista)

    # --- PASSO 4: Cadastre membros ---
    # aluno    = AlunoMembro("Ana Lima", "111.222.333-44", "2024001")
    # professor = ProfessorMembro("Prof. Carlos", "555.666.777-88", "Programação")
    # biblioteca.cadastrar_membro(aluno)
    # biblioteca.cadastrar_membro(professor)

    # --- PASSO 5: Exiba o acervo e os membros ---
    # biblioteca.exibir_acervo()
    # biblioteca.exibir_membros()

    # --- PASSO 6: Realize empréstimos ---
    # biblioteca.realizar_emprestimo(aluno, "L001")
    # biblioteca.realizar_emprestimo(professor, "R001")

    # --- PASSO 7: Exiba o acervo novamente (veja as mudanças de status) ---
    # biblioteca.exibir_acervo()

    # --- PASSO 8: Liste os empréstimos dos membros ---
    # print("\n📋 Empréstimos da Ana:")
    # aluno.listar_emprestimos()

    # --- PASSO 9: Realize uma devolução ---
    # biblioteca.realizar_devolucao(aluno, "L001")
    # biblioteca.exibir_acervo()

    # --- PASSO 10: Polimorfismo - chame info_completa() para Livro e Revista ---
    # livro1.info_completa()
    # revista.info_completa()

    # TODO (DESAFIO): Tente emprestar mais itens do que o limite do Aluno (3)
    # e observe o comportamento do sistema.

    # TODO (DESAFIO): Tente adicionar o mesmo livro duas vezes ao acervo.

    print("\nExercício concluído!")
