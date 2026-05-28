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
        self.nome = nome          
        self.idade = idade         
        self.matricula = matricula     
        self.notas = []           

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
            print(f"Nota {nota} adicionada com sucesso para o aluno {self.nome}.")
        else:
            print(f"Erro: A nota {nota} é inválida! Deve ser entre 0 e 10.")

    def calcular_media(self):
        """
        Calcula e retorna a média aritmética das notas do aluno.

        Returns:
            float: Média das notas, ou 0.0 se não houver notas.
        """
        # TODO: Calcule a média das notas.
        # Dica: use sum() e len() para calcular a média.
        # Lembre-se de tratar o caso em que self.notas está vazio (divisão por zero!).
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

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
        # TODO: Imprima as informações do aluno no seguinte formato:
        #
        # =============================
        media = self.calcular_media()
        situacao = self.obter_situacao()
        
        print("=============================")
        print(f"Nome:      {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Idade:     {self.idade} anos")
        print(f"Média:     {media:.2f}")
        print(f"Situação:  {situacao}")
        print("=============================")


# =============================================================================
# BLOCO DE TESTES - Execute este arquivo para verificar sua implementação
# =============================================================================

if __name__ == "__main__":

    print("=" * 50)
    print("  SISTEMA DE CADASTRO DE ALUNOS")
    print("=" * 50)

    # TODO: Crie pelo menos 2 objetos da classe Aluno com dados diferentes
    aluno1 = Aluno("Ana Lima", 20, "2024001")
    aluno2 = Aluno("Amanda", 27, "2023010244")

    # TODO: Adicione pelo menos 3 notas para cada aluno usando o método adicionar_nota()
    print("\n--- Adicionando Notas ---")
    aluno1.adicionar_nota(8.5)
    aluno1.adicionar_nota(7.0)
    aluno1.adicionar_nota(9.0)

    aluno2.adicionar_nota(5.5)
    aluno2.adicionar_nota(6.0)
    aluno2.adicionar_nota(4.5)

    # TODO (DESAFIO): Tente adicionar uma nota inválida (ex: 11 ou -1) e veja o que acontece
    print("\n--- Teste de Nota Inválida ---")
    aluno1.adicionar_nota(12.0)

    # TODO: Chame o método apresentar() para cada aluno e verifique os resultados
    print("\n--- Ficha dos Alunos ---")
    aluno1.apresentar()
    aluno2.apresentar()

    print("\nExercício concluído!")