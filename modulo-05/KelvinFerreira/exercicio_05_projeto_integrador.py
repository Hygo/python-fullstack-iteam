# =============================================================================
# ITEAM - CURSO DE CAPACITAÇÃO EM DESENVOLVIMENTO FULL STACK
# Programação em Python | Módulo 5 - Programação Orientada a Objetos
# =============================================================================
#
# EXERCÍCIO 05 - PROJETO INTEGRADOR: SISTEMA DE BIBLIOTECA
#
# Aluno: Kelvin Araújo Ferreira
# =============================================================================


# =============================================================================
# PARTE 1 - HIERARQUIA DE ITENS DO ACERVO
# =============================================================================

class ItemBiblioteca:
    """Classe base para todos os itens do acervo."""

    def __init__(self, codigo, titulo, ano_publicacao):
        self.__codigo = codigo
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.__disponivel = True

    @property
    def codigo(self):
        return self.__codigo

    @property
    def disponivel(self):
        return self.__disponivel

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            return True
        return False

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            return True
        return False

    def info_completa(self):
        raise NotImplementedError("Subclasses devem implementar info_completa()")

    def __str__(self):
        status = "✅ Disponível" if self.disponivel else "❌ Emprestado"
        return f"[{self.codigo}] {self.titulo} ({self.ano_publicacao}) - {status}"

    def __eq__(self, outro):
        if not isinstance(outro, ItemBiblioteca):
            return False
        return self.codigo == outro.codigo


# -----------------------------------------------------------------------------
# Subclasse: Livro
# -----------------------------------------------------------------------------

class Livro(ItemBiblioteca):
    """Representa um livro no acervo."""

    def __init__(self, codigo, titulo, ano_publicacao, autor, isbn, num_paginas):
        super().__init__(codigo, titulo, ano_publicacao)
        self.autor = autor
        self.isbn = isbn
        self.num_paginas = num_paginas

    def info_completa(self):
        status = "✅ Disponível" if self.disponivel else "❌ Emprestado"
        print(f"📖 LIVRO")
        print(f"   Código:        {self.codigo}")
        print(f"   Título:        {self.titulo}")
        print(f"   Autor:         {self.autor}")
        print(f"   ISBN:          {self.isbn}")
        print(f"   Ano:           {self.ano_publicacao}")
        print(f"   Páginas:       {self.num_paginas}")
        print(f"   Disponível:    {status}")


# -----------------------------------------------------------------------------
# Subclasse: Revista
# -----------------------------------------------------------------------------

class Revista(ItemBiblioteca):
    """Representa uma revista no acervo."""

    def __init__(self, codigo, titulo, ano_publicacao, editora, numero_edicao, periodicidade):
        super().__init__(codigo, titulo, ano_publicacao)
        self.editora = editora
        self.numero_edicao = numero_edicao
        self.periodicidade = periodicidade

    def info_completa(self):
        status = "✅ Disponível" if self.disponivel else "❌ Emprestado"
        print(f"📰 REVISTA")
        print(f"   Código:        {self.codigo}")
        print(f"   Título:        {self.titulo}")
        print(f"   Editora:       {self.editora}")
        print(f"   Edição:        nº {self.numero_edicao}")
        print(f"   Periodicidade: {self.periodicidade}")
        print(f"   Ano:           {self.ano_publicacao}")
        print(f"   Disponível:    {status}")


# =============================================================================
# PARTE 2 - HIERARQUIA DE MEMBROS (PESSOAS)
# =============================================================================

class Pessoa:
    """Classe base para membros da biblioteca."""

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self._emprestimos_ativos = []

    @property
    def limite_emprestimos(self):
        raise NotImplementedError

    def pode_emprestar(self):
        return len(self._emprestimos_ativos) < self.limite_emprestimos

    def registrar_emprestimo(self, item):
        if not self.pode_emprestar():
            print(
                f"❌ {self.nome} atingiu o limite de {self.limite_emprestimos} empréstimo(s)."
            )
            return False
        if not item.disponivel:
            print(f"❌ '{item.titulo}' não está disponível para empréstimo.")
            return False
        item.emprestar()
        self._emprestimos_ativos.append(item)
        print(f"✅ '{item.titulo}' emprestado para {self.nome}.")
        return True

    def registrar_devolucao(self, item):
        if item not in self._emprestimos_ativos:
            print(f"❌ '{item.titulo}' não está registrado para {self.nome}.")
            return False
        item.devolver()
        self._emprestimos_ativos.remove(item)
        print(f"✅ '{item.titulo}' devolvido por {self.nome}.")
        return True

    def listar_emprestimos(self):
        if not self._emprestimos_ativos:
            print(f"  {self.nome} não possui empréstimos ativos.")
            return
        for item in self._emprestimos_ativos:
            print(f"  {item}")

    def __str__(self):
        tipo = type(self).__name__
        return (
            f"{tipo}: {self.nome} | CPF: {self.cpf} | "
            f"Empréstimos: {len(self._emprestimos_ativos)}/{self.limite_emprestimos}"
        )


class AlunoMembro(Pessoa):
    """Aluno membro — limite de 3 empréstimos."""

    def __init__(self, nome, cpf, matricula):
        super().__init__(nome, cpf)
        self.matricula = matricula

    @property
    def limite_emprestimos(self):
        return 3


class ProfessorMembro(Pessoa):
    """Professor membro — limite de 5 empréstimos."""

    def __init__(self, nome, cpf, disciplina):
        super().__init__(nome, cpf)
        self.disciplina = disciplina

    @property
    def limite_emprestimos(self):
        return 5


# =============================================================================
# PARTE 3 - CLASSE BIBLIOTECA (COMPOSIÇÃO)
# =============================================================================

class Biblioteca:
    """Gerencia o acervo e os membros da biblioteca."""

    def __init__(self, nome):
        self.nome = nome
        self.__acervo = []
        self.__membros = []

    def adicionar_item(self, item):
        if item in self.__acervo:
            print(f"⚠️  '{item.titulo}' (código {item.codigo}) já está no acervo.")
            return
        self.__acervo.append(item)
        print(f"✅ '{item.titulo}' adicionado ao acervo.")

    def cadastrar_membro(self, pessoa):
        self.__membros.append(pessoa)
        print(f"✅ {type(pessoa).__name__} '{pessoa.nome}' cadastrado(a).")

    def buscar_item_por_codigo(self, codigo):
        for item in self.__acervo:
            if item.codigo == codigo:
                return item
        return None

    def realizar_emprestimo(self, membro, codigo_item):
        item = self.buscar_item_por_codigo(codigo_item)
        if not item:
            print(f"❌ Item com código '{codigo_item}' não encontrado no acervo.")
            return
        membro.registrar_emprestimo(item)

    def realizar_devolucao(self, membro, codigo_item):
        item = self.buscar_item_por_codigo(codigo_item)
        if not item:
            print(f"❌ Item com código '{codigo_item}' não encontrado no acervo.")
            return
        membro.registrar_devolucao(item)

    def exibir_acervo(self):
        print(f"\n📚 ACERVO - {self.nome}")
        print("=" * 55)
        if not self.__acervo:
            print("  Acervo vazio.")
        else:
            for item in self.__acervo:
                print(f"  {item}")
        print("=" * 55)

    def exibir_membros(self):
        print(f"\n👥 MEMBROS - {self.nome}")
        print("=" * 55)
        if not self.__membros:
            print("  Nenhum membro cadastrado.")
        else:
            for membro in self.__membros:
                print(f"  {membro}")
        print("=" * 55)


# =============================================================================
# BLOCO DE TESTES - SIMULAÇÃO COMPLETA
# =============================================================================

if __name__ == "__main__":

    print("=" * 55)
    print("  BIBLIOTECA DIGITAL - ITEAM")
    print("=" * 55)

    # Passo 1 — criar a biblioteca
    biblioteca = Biblioteca("Biblioteca ITEAM")

    # Passo 2 — criar itens
    livro1  = Livro("L001", "Python para Principiantes", 2012,
                    "Eugenia Bahit", "978-0000000001", 220)
    livro2  = Livro("L002", "A Beginner's Guide to Python 3", 2020,
                    "John Hunt", "978-0000000002", 450)
    revista = Revista("R001", "Python Magazine", 2024,
                      "Tech Press", 42, "Mensal")

    # Passo 3 — adicionar ao acervo
    print()
    biblioteca.adicionar_item(livro1)
    biblioteca.adicionar_item(livro2)
    biblioteca.adicionar_item(revista)
    biblioteca.adicionar_item(livro1)   # desafio: item duplicado

    # Passo 4 — cadastrar membros
    print()
    aluno     = AlunoMembro("Ana Lima", "111.222.333-44", "2024001")
    professor = ProfessorMembro("Prof. Carlos", "555.666.777-88", "Programação")
    biblioteca.cadastrar_membro(aluno)
    biblioteca.cadastrar_membro(professor)

    # Passo 5 — exibir estado inicial
    biblioteca.exibir_acervo()
    biblioteca.exibir_membros()

    # Passo 6 — realizar empréstimos
    print()
    biblioteca.realizar_emprestimo(aluno, "L001")
    biblioteca.realizar_emprestimo(professor, "R001")
    biblioteca.realizar_emprestimo(aluno, "L001")   # já emprestado

    # Passo 7 — acervo após empréstimos
    biblioteca.exibir_acervo()

    # Passo 8 — listar empréstimos
    print("\n📋 Empréstimos da Ana:")
    aluno.listar_emprestimos()

    # Passo 9 — devolução
    print()
    biblioteca.realizar_devolucao(aluno, "L001")
    biblioteca.exibir_acervo()

    # Passo 10 — polimorfismo: info_completa para Livro e Revista
    print()
    livro1.info_completa()
    print()
    revista.info_completa()

    # Desafio: tentar ultrapassar limite do Aluno (máx 3)
    print("\n--- Desafio: limite de empréstimos ---")
    biblioteca.realizar_emprestimo(aluno, "L001")
    biblioteca.realizar_emprestimo(aluno, "L002")
    biblioteca.realizar_emprestimo(aluno, "R001")   # 3º → já passou pelo Prof.
    # acervo atualizado
    biblioteca.exibir_membros()

    print("\nExercício concluído!")
