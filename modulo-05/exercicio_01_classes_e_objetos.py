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

        Args:
            nome (str): Nome completo do aluno.
            idade (int): Idade do aluno.
            matricula (str): Código de matrícula.
        """
        # TODO: Atribua os parâmetros aos atributos de instância usando 'self'
        self.nome = None          # substitua None pelo parâmetro correto
        self.idade = None         # substitua None pelo parâmetro correto
        self.matricula = None     # substitua None pelo parâmetro correto
        self.notas = []           # lista vazia para armazenar as notas

    def adicionar_nota(self, nota):
        """
        Adiciona uma nota à lista de notas do aluno.

        Args:
            nota (float): Nota a ser adicionada (deve estar entre 0 e 10).
        """
        # TODO: Valide se a nota está entre 0 e 10.
        # Se estiver no intervalo válido, adicione à lista self.notas
        # e imprima uma mensagem de confirmação.
        # Caso contrário, informe que a nota é inválida.
        pass

    def calcular_media(self):
        """
        Calcula e retorna a média aritmética das notas do aluno.

        Returns:
            float: Média das notas, ou 0.0 se não houver notas.
        """
        # TODO: Calcule a média das notas.
        # Dica: use sum() e len() para calcular a média.
        # Lembre-se de tratar o caso em que self.notas está vazio (divisão por zero!).
        pass

    def obter_situacao(self):
        """
        Retorna a situação do aluno (Aprovado, Recuperação ou Reprovado)
        com base na média calculada.

        Returns:
            str: Situação do aluno.
        """
        # TODO: Com base na média, retorne a situação:
        #   - Média >= 7.0: "Aprovado"
        #   - Média >= 5.0 e < 7.0: "Recuperação"
        #   - Média < 5.0: "Reprovado"
        pass

    def apresentar(self):
        """
        Imprime na tela as informações completas do aluno de forma formatada.
        """
        # TODO: Imprima as informações do aluno no seguinte formato:
        #
        # =============================
        # Nome:      [nome do aluno]
        # Matrícula: [código]
        # Idade:     [idade] anos
        # Média:     [média formatada com 1 casa decimal]
        # Situação:  [situação]
        # =============================
        pass


# =============================================================================
# BLOCO DE TESTES - Execute este arquivo para verificar sua implementação
# =============================================================================

if __name__ == "__main__":

    print("=" * 50)
    print("  SISTEMA DE CADASTRO DE ALUNOS - ITEAM")
    print("=" * 50)

    # TODO: Crie pelo menos 2 objetos da classe Aluno com dados diferentes
    # Exemplo:
    # aluno1 = Aluno("Ana Lima", 20, "2024001")

    # TODO: Adicione pelo menos 3 notas para cada aluno usando o método adicionar_nota()

    # TODO: Chame o método apresentar() para cada aluno e verifique os resultados

    # TODO (DESAFIO): Tente adicionar uma nota inválida (ex: 11 ou -1) e veja o que acontece

    print("\nExercício concluído!")
