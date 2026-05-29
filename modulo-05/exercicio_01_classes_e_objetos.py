# =============================================================================
# ITEAM - CURSO DE CAPACITAÇÃO EM DESENVOLVIMENTO FULL STACK
# Programação em Python | Módulo 5 - Programação Orientada a Objetos
# =============================================================================
#
# EXERCÍCIO 01 - CLASSES, OBJETOS, ATRIBUTOS E MÉTODOS
#
# Tema: Sistema de Cadastro de Alunos
#
# Objetivo:
#   Criar uma classe Aluno que modele um estudante de um curso de programação,
#   praticando a definição de classes, instanciação de objetos, atributos de
#   instância e métodos.
#
# Conceitos trabalhados:
#   - Definição de classe com 'class'
#   - Método construtor __init__()
#   - Atributos de instância (self.atributo)
#   - Métodos de instância
#   - Instanciação de objetos
#
# Referência: Seções 5.2.1, 5.2.2 e 5.2.3 da Apostila ITEAM
# =============================================================================


class Aluno:
    """
    Representa um aluno matriculado no curso de programação.

    Atributos:
        nome (str): Nome completo do aluno.
        idade (int): Idade do aluno em anos.
        matricula (str): Código único de matrícula.
        notas (list): Lista de notas obtidas pelo aluno.
    """

    def __init__(self, nome, idade, matricula):
        """
        Inicializa um novo objeto Aluno.
        """
        # TODO: Atribua os parâmetros aos atributos de instância usando 'self'
        self.nome = nome          # Substituído None pelo parâmetro nome
        self.idade = idade        # Substituído None pelo parâmetro idade
        self.matricula = matricula  # Substituído None pelo parâmetro matricula
        self.notas = []           # Lista vazia para armazenar as notas

    def adicionar_nota(self, nota):
        """
        Adiciona uma nota à lista de notas do aluno.

        Args:
            nota (float): Nota a ser adicionada (deve estar entre 0 e 10).
        """
        # TODO: Valide se a nota está entre 0 e 10.
        if 0 <= nota <= 10:
            self.notas.append(nota)
            print(f"Nota {nota} adicionada com sucesso para o(a) aluno(a) {self.nome}!")
        else:
            print(f"Erro: A nota {nota} é inválida! Digite um valor entre 0 e 10.")

    def calcular_media(self):
        """
        Calcula e retorna a média aritmética das notas do aluno.

        Returns:
            float: Média das notas, ou 0.0 se não houver notas.
        """
        # TODO: Calcule a média das notas.
        # Trata o caso em que self.notas está vazio para evitar ZeroDivisionError
        if not self.notas:
            return 0.0
        
        return sum(self.notas) / len(self.notas)

    def obtener_situacao(self):
        """
        Retorna a situação do aluno (Aprovado, Recuperação ou Reprovado)
        com base na média calculada.

        Returns:
            str: Situação do aluno.
        """
        # TODO: Com base na média, retorne a situação:
        media = self.calcular_media()
        
        if media >= 7.0:
            return "Aprovado"
        elif media >= 5.0:
            return "Recuperação"
        else:
            return "Reprovado"

    def apresentar(self):
        """
        Imprime na tela as informações completas do aluno de forma formatada.
        """
        # TODO: Imprima as informações do aluno no formato solicitado
        media = self.calcular_media()
        situacao = self.obtener_situacao()
        
        print("\n=============================")
        print(f"Nome:      {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Idade:     {self.idade} anos")
        print(f"Média:     {media:.1f}")
        print(f"Situação:  {situacao}")
        print("=============================")


# =============================================================================
# BLOCO DE TESTES - Execute este arquivo para verificar sua implementação
# =============================================================================

if __name__ == "__main__":

    print("=" * 50)
    print("  SISTEMA DE CADASTRO DE ALUNOS - ITEAM")
    print("=" * 50)

    # 1. Criando 2 objetos da classe Aluno com dados diferentes
    aluno1 = Aluno("Carlos Souza", 22, "ITEAM2026-01")
    aluno2 = Aluno("Mariana Silva", 19, "ITEAM2026-02")

    print("\n--- Cadastrando Notas ---")
    # 2. Adicionando 3 notas válidas para o aluno 1
    aluno1.adicionar_nota(8.5)
    aluno1.adicionar_nota(7.0)
    aluno1.adicionar_nota(9.0)

    # 3. Adicionando 3 notas válidas para o aluno 2
    aluno2.adicionar_nota(5.5)
    aluno2.adicionar_nota(6.0)
    aluno2.adicionar_nota(4.5)

    # 4. DESAFIO: Tentando adicionar notas inválidas
    print("\n--- Testando o Desafio (Validação de Notas) ---")
    aluno1.adicionar_nota(-1.5)  # Deve exibir mensagem de erro
    aluno2.adicionar_nota(11.0)  # Deve exibir mensagem de erro

    print("\n--- Relatório Final dos Alunos ---")
    # 5. Chamando o método apresentar() para exibir o resultado final
    aluno1.apresentar()
    aluno2.apresentar()

    print("\nExercício concluído!")