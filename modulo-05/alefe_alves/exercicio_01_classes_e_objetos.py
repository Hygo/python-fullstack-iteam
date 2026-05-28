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
        #Feito
        self.nome = nome          # substitua None pelo parâmetro correto - Feito
        self.idade = idade         # substitua None pelo parâmetro correto - Feito
        self.matricula = matricula     # substitua None pelo parâmetro correto - Feito
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
        if 0 <= nota <= 10:
            self.notas.append(nota)
            print("Nota adicionada com sucesso.")
        else:
            print("Nota não cumpre os requisitos para ser adicionada (deve estar entre 0 e 10).")

    def calcular_media(self):
        """
        Calcula e retorna a média aritmética das notas do aluno.

        Returns:
            float: Média das notas, ou 0.0 se não houver notas.
        """
        # TODO: Calcule a média das notas.
        # Dica: use sum() e len() para calcular a média.
        # Lembre-se de tratar o caso em que self.notas está vazio (divisão por zero!).
        if(len(self.notas) > 0):
            return sum(self.notas) / len(self.notas)
        else:
            return 0.0




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
        media = self.calcular_media()
        if media < 5.0:
            return "Reprovado"
        elif media < 7.0: 
            return "Recuperação"
        else:
            return "Aprovado"


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
        print(f"""
        =============================
        Nome:      {self.nome}
        Matrícula: {self.matricula}
        Idade:     {self.idade} anos
        Média:     {self.calcular_media():.1f}
        Situação:  {self.obter_situacao()}
        =============================
""")


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
    aluno1 = Aluno("Carlos Pereira", 25, 2026019438)
    aluno2 = Aluno("Pedro Castro", 22, 2026891245)

    # TODO: Adicione pelo menos 3 notas para cada aluno usando o método adicionar_nota()
    aluno1.adicionar_nota(10)
    aluno1.adicionar_nota(5)
    aluno1.adicionar_nota(7)

    aluno2.adicionar_nota(7)
    aluno2.adicionar_nota(8)
    aluno2.adicionar_nota(9)
    

    # TODO: Chame o método apresentar() para cada aluno e verifique os resultados
    aluno1.apresentar()
    aluno2.apresentar()

    # TODO (DESAFIO): Tente adicionar uma nota inválida (ex: 11 ou -1) e veja o que acontece
    aluno2.adicionar_nota(11)
    print("\nExercício concluído!")
