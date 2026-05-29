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
    """

    def __init__(self, codigo, titulo, ano_publicacao):
        """
        Inicializa a estrutura base de um item do acervo.
        """
        # TODO: Atribua codigo a __codigo (privado), titulo e ano_publicacao normalmente
        self.__codigo = codigo
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.__disponivel = True

    @property
    def codigo(self):
        """Retorna o código do item (somente leitura)."""
        # TODO: Retorne __codigo
        return self.__codigo

    @property
    def disponivel(self):
        """Retorna True se o item está disponível para empréstimo."""
        # TODO: Retorne __disponivel
        return self.__disponivel

    def emprestar(self):
        """
        Marca o item como indisponível.
        """
        # TODO: Se __disponivel for True, mude para False e retorne True.
        if self.__disponivel:
            self.__disponivel = False
            return True
        return False

    def devolver(self):
        """
        Marca o item como disponível novamente.
        """
        # TODO: Se __disponivel for False, mude para True e retorne True.
        if not self.__disponivel:
            self.__disponivel = True
            return True
        return False

    def info_completa(self):
        """
        Método abstrato simulado. Deve ser sobrescrito pelas subclasses.
        """
        raise NotImplementedError("Subclasses devem implementar info_completa()")

    def __str__(self):
        """Representação resumida do item."""
        status = "✅ Disponível" if self.disponivel else "❌ Emprestado"
        return f"[{self.codigo}] {self.titulo} ({self.ano_publicacao}) - {status}"

    def __eq__(self, outro):
        """Dois itens são iguais se possuem o mesmo código."""
        # TODO: Compare self.codigo com outro.codigo protegendo contra tipos diferentes
        if not isinstance(outro, ItemBiblioteca):
            return False
        return self.codigo == outro.codigo


# -----------------------------------------------------------------------------
# Subclasse: Livro
# -----------------------------------------------------------------------------

class Livro(ItemBiblioteca):
    """
    Representa um livro no acervo.
    """

    def __init__(self, codigo, titulo, ano_publicacao, autor, isbn, num_paginas):
        # TODO: Chame super().__init__() com os parâmetros da classe pai e configure os atributos
        super().__init__(codigo, titulo, ano_publicacao)
        self.autor = autor
        self.isbn = isbn
        self.num_paginas = num_paginas

    def info_completa(self):
        """Retorna informações completas do livro."""
        # TODO: Retorne uma string formatada com todos os atributos
        status = "Disponível" if self.disponivel else "Emprestado"
        info = (
            f"\n📖 [LIVRO DETALHADO]\n"
            f"   Código:         {self.codigo}\n"
            f"   Título:         {self.titulo}\n"
            f"   Autor:          {self.autor}\n"
            f"   ISBN:           {self.isbn}\n"
            f"   Ano:            {self.ano_publicacao}\n"
            f"   Páginas:        {self.num_paginas}\n"
            f"   Status atual:   {status}"
        )
        print(info)
        return info


# -----------------------------------------------------------------------------
# Subclasse: Revista
# -----------------------------------------------------------------------------

class Revista(ItemBiblioteca):
    """
    Representa uma revista no acervo.
    """

    def __init__(self, codigo, titulo, ano_publicacao, editora, numero_edicao, periodicidade):
        # TODO: Chame super().__init__() e atribua os atributos específicos
        super().__init__(codigo, titulo, ano_publicacao)
        self.editora = editora
        self.numero_edicao = numero_edicao
        self.periodicidade = periodicidade

    def info_completa(self):
        """Retorna informações completas da revista."""
        # TODO: Retorne uma string formatada com todos os atributos da revista
        status = "Disponível" if self.disponivel else "Emprestado"
        info = (
            f"\n📰 [REVISTA DETALHADA]\n"
            f"   Código:         {self.codigo}\n"
            f"   Título:         {self.titulo}\n"
            f"   Editora:        {self.editora}\n"
            f"   Edição:         Nº {self.numero_edicao}\n"
            f"   Periodicidade:  {self.periodicidade}\n"
            f"   Ano:            {self.ano_publicacao}\n"
            f"   Status atual:   {status}"
        )
        print(info)
        return info


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
        """Registra um empréstimo para este membro."""
        # TODO: Verifique se pode emprestar e se o item está disponível
        if not self.pode_emprestar():
            print(f"❌ Falha: {self.nome} atingiu o limite máximo de {self.limite_emprestimos} empréstimos ativos.")
            return False
        
        if not item.disponivel:
            print(f"❌ Falha: O item '{item.titulo}' já está alugado por outro usuário.")
            return False

        # Se ambas as condições forem atendidas
        item.emprestar()
        self._emprestimos_ativos.append(item)
        print(f"✔️ Sucesso: '{item.titulo}' associado ao perfil de {self.nome}!")
        return True

    def registrar_devolucao(self, item):
        """Registra a devolução de um item."""
        # TODO: Verifique se 'item' está em self._emprestimos_ativos
        if item in self._emprestimos_ativos:
            item.devolver()
            self._emprestimos_ativos.remove(item)
            print(f"✔️ Devolução confirmada: '{item.titulo}' está de volta ao acervo.")
            return True
        
        print(f"❌ Erro: O item '{item.titulo}' não consta na ficha de empréstimos de {self.nome}.")
        return False

    def listar_emprestimos(self):
        """Exibe todos os itens atualmente emprestados pelo membro."""
        # TODO: Liste cada item usando __str__
        if not self._emprestimos_ativos:
            print("   Nenhum empréstimo pendente.")
        else:
            for item in self._emprestimos_ativos:
                print(f"   -> {item}")

    def __str__(self):
        tipo = type(self).__name__
        return f"{tipo}: {self.nome} | CPF: {self.cpf} | Empréstimos: {len(self._emprestimos_ativos)}/{self.limite_emprestimos}"


class AlunoMembro(Pessoa):
    """Aluno membro da biblioteca. Limite: 3 empréstimos simultâneos."""

    def __init__(self, nome, cpf, matricula):
        # TODO: Chame super().__init__() e atribua matricula
        super().__init__(nome, cpf)
        self.matricula = matricula

    @property
    def limite_emprestimos(self):
        # TODO: Retorne 3
        return 3


class ProfessorMembro(Pessoa):
    """Professor membro da biblioteca. Limite: 5 empréstimos simultâneos."""

    def __init__(self, nome, cpf, disciplina):
        # TODO: Chame super().__init__() e atribua disciplina
        super().__init__(nome, cpf)
        self.disciplina = disciplina

    @property
    def limite_emprestimos(self):
        # TODO: Retorne 5
        return 5


# =============================================================================
# PARTE 3 - CLASSE BIBLIOTECA (COMPOSIÇÃO)
# =============================================================================

class Biblioteca:
    """Gerencia o acervo e os membros da biblioteca através de Composição."""

    def __init__(self, nome):
        self.nome = nome
        self.__acervo = []
        self.__membros = []

    def adicionar_item(self, item):
        """Adiciona um item ao acervo."""
        # TODO: Verifique se o item já não está no acervo (usa o __eq__ interno)
        if item in self.__acervo:
            print(f"❌ Erro de Cadastro: Código '{item.codigo}' já existe no acervo. Item recusado.")
        else:
            self.__acervo.append(item)
            print(f"✨ Acervo Atualizado: '{item.titulo}' cadastrado com sucesso.")

    def cadastrar_membro(self, pessoa):
        """Cadastra um membro na biblioteca."""
        self.__membros.append(pessoa)
        print(f"👤 Novo Membro: {pessoa.nome} adicionado(a) ao sistema.")

    def buscar_item_por_codigo(self, codigo):
        """Busca um item no acervo pelo código."""
        # TODO: Percorra __acervo e retorne o item cujo .codigo == codigo.
        for item in self.__acervo:
            if item.codigo == codigo:
                return item
        return None

    def realizar_emprestimo(self, membro, codigo_item):
        """Realiza o empréstimo de um item para um membro."""
        # TODO: Use buscar_item_por_codigo() para encontrar o item.
        item = self.buscar_item_por_codigo(codigo_item)
        if item is None:
            print(f"❌ Operação Cancelada: Item com código '{codigo_item}' não existe.")
        else:
            membro.registrar_emprestimo(item)

    def realizar_devolucao(self, membro, codigo_item):
        """Registra a devolução de um item."""
        item = self.buscar_item_por_codigo(codigo_item)
        if item is None:
            print(f"❌ Operação Cancelada: Item com código '{codigo_item}' não pertence ao acervo.")
        else:
            membro.registrar_devolucao(item)

    def exibir_acervo(self):
        """Exibe todos os itens do acervo com seu status."""
        print(f"\n📚 ACERVO - {self.nome}")
        print("=" * 55)
        if not self.__acervo:
            print("  Acervo vazio.")
        else:
            for item in self.__acervo:
                print(f"  {item}")
        print("=" * 55)

    def exibir_membros(self):
        """Exibe todos os membros cadastrados."""
        print(f"\n👥 MEMBROS - {self.nome}")
        print("=" * 55)
        if not self.__membros:
            print("  Nenhum membro cadastrado.")
        else:
            for membro in self.__membros:
                print(f"  {membro}")
        print("=" * 55)


# =============================================================================
# BLOCO DE TESTES - SIMULAÇÃO COMPLETA DO SISTEMA
# =============================================================================

if __name__ == "__main__":

    print("=" * 55)
    print("  BIBLIOTECA DIGITAL - ITEAM")
    print("=" * 55)

    # 1. Criação da biblioteca
    biblioteca = Biblioteca("Biblioteca ITEAM")

    # 2. Criação de itens do acervo
    livro1  = Livro("L001", "Python para Principiantes", 2012, "Eugenia Bahit", "978-0000000001", 220)
    livro2  = Livro("L002", "A Beginner's Guide to Python 3", 2020, "John Hunt", "978-0000000002", 450)
    revista = Revista("R001", "Python Magazine", 2024, "Tech Press", 42, "Mensal")

    print("\n--- Carregando Itens no Sistema ---")
    # 3. Adicionando itens ao acervo
    biblioteca.adicionar_item(livro1)
    biblioteca.adicionar_item(livro2)
    biblioteca.adicionar_item(revista)

    # DESAFIO: Tentando cadastrar duplicado
    print("\n--- Testando Desafio de Código Duplicado ---")
    livro_falso = Livro("L001", "Livro Clone Modificado", 2026, "Desconhecido", "000", 10)
    biblioteca.adicionar_item(livro_falso)

    print("\n--- Registrando Usuários ---")
    # 4. Cadastrando membros
    aluno     = AlunoMembro("Ana Lima", "111.222.333-44", "2024001")
    professor = ProfessorMembro("Prof. Carlos", "555.666.777-88", "Programação")
    biblioteca.cadastrar_membro(aluno)
    biblioteca.cadastrar_membro(professor)

    # 5. Exibindo acervo inicial
    biblioteca.exibir_acervo()

    print("\n--- Processando Movimentações de Saída ---")
    # 6. Realizando empréstimos válidos
    biblioteca.realizar_emprestimo(aluno, "L001")
    biblioteca.realizar_emprestimo(professor, "R001")

    # 7. Exibindo estado após empréstimos
    biblioteca.exibir_acervo()

    # 8. Listando itens vinculados ao aluno
    print("\n📋 Extrato de Empréstimos - ANA LIMA:")
    aluno.listar_emprestimos()

    # DESAFIO: Forçando o limite de empréstimos estourar (Aluno limite 3)
    print("\n--- Testando Desafio de Limite Máximo (Ana) ---")
    livro_extra1 = Livro("L003", "Estruturas de Dados", 2021, "Dev", "111", 300)
    livro_extra2 = Livro("L004", "Algoritmos Avançados", 2023, "Dev", "222", 500)
    biblioteca.adicionar_item(livro_extra1)
    biblioteca.adicionar_item(livro_extra2)
    
    # Tentando atingir o limite e depois estourar
    biblioteca.realizar_emprestimo(aluno, "L002") # 2º item (ok)
    biblioteca.realizar_emprestimo(aluno, "L003") # 3º item (ok)
    biblioteca.realizar_emprestimo(aluno, "L004") # 4º item (Deve Bloquear!)

    print("\n--- Processando Movimentações de Entrada ---")
    # 9. Realizando devolução
    biblioteca.realizar_devolucao(aluno, "L001")
    
    # 10. Polimorfismo puro rodando no relatório detalhado
    print("\n--- Relatórios Detalhados (Polimorfismo) ---")
    livro1.info_completa()
    revista.info_completa()

    print("\nExercício concluído!")
    