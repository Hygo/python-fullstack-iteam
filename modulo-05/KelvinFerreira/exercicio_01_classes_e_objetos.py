# =============================================================================
# ITEAM - CURSO DE CAPACITAÇÃO EM DESENVOLVIMENTO FULL STACK
# Programação em Python | Módulo 5 - Programação Orientada a Objetos
# =============================================================================
#
# EXERCÍCIO 01 - CLASSES, OBJETOS, ATRIBUTOS E MÉTODOS
#
# Aluno: Kelvin Araújo Ferreira
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
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
            print(f"Nota {nota} adicionada para {self.nome}.")
        else:
            print(f"Nota inválida: {nota}. Deve estar entre 0 e 10.")

    def calcular_media(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def obter_situacao(self):
        media = self.calcular_media()
        if media >= 7.0:
            return "Aprovado"
        elif media >= 5.0:
            return "Recuperação"
        return "Reprovado"

    def apresentar(self):
        print("=" * 29)
        print(f"Nome:      {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Idade:     {self.idade} anos")
        print(f"Média:     {self.calcular_media():.1f}")
        print(f"Situação:  {self.obter_situacao()}")
        print("=" * 29)


# =============================================================================
# BLOCO DE TESTES
# =============================================================================

if __name__ == "__main__":

    print("=" * 50)
    print("  SISTEMA DE CADASTRO DE ALUNOS - ITEAM")
    print("=" * 50)

    aluno1 = Aluno("Kelvin Araújo Ferreira", 22, "2024001")
    aluno1.adicionar_nota(9.5)
    aluno1.adicionar_nota(8.0)
    aluno1.adicionar_nota(10.0)

    aluno2 = Aluno("Ryan Kayky", 21, "2024002")
    aluno2.adicionar_nota(5.5)
    aluno2.adicionar_nota(6.0)
    aluno2.adicionar_nota(4.0)

    print()
    aluno1.apresentar()
    print()
    aluno2.apresentar()

    # Desafio: nota inválida
    print()
    aluno1.adicionar_nota(11)
    aluno1.adicionar_nota(-1)

    print("\nExercício concluído!")
