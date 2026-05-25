"""
=============================================================
AVALIAÇÃO — Módulos 03 e 04
Curso de Capacitação Full Stack – ITEAM
Professor: Msc. Hygo Sousa De Oliveira

Aluno(a): <Jennison Enthony Oliveira Diniz>
Data    : <25/05/2025>
=============================================================

INSTRUÇÕES:
  1. Substitua cada "?" pela letra da sua resposta (A, B, C, D ou E).
  2. Leia o enunciado completo no README.md antes de responder.
  3. Analise o código mentalmente — evite executar antes de decidir.
  4. Você pode adicionar comentários justificando sua escolha.
  5. Suba este arquivo em: alunos/<seu_nome>/mod03-mod04.py
=============================================================
"""

# ──────────────────────────────────────────────────────────────
# MÓDULO 03 — ESTRUTURA DE DADOS (10 questões)
# ──────────────────────────────────────────────────────────────

# ------------------------------------------------------------
# Q01 🟢 — Listas: indexação negativa
#
# frutas = ["maçã", "banana", "uva", "laranja"]
# frutas[1] = "abacaxi"
# frutas.append("manga")
# print(frutas[-2])
#
# A) "uva"
# B) "laranja"
# C) "abacaxi"
# D) "manga"
# E) IndexError: list index out of range
# ------------------------------------------------------------
Q01 = "B"   # substitua pelo sua resposta


# ------------------------------------------------------------
# Q02 🟢 — Tuplas: imutabilidade
#
# coordenadas = (10, 20, 30)
# coordenadas[1] = 99
# print(coordenadas)
#
# A) (10, 99, 30)
# B) (10, 20, 30) — atribuição ignorada silenciosamente
# C) TypeError: 'tuple' object does not support item assignment
# D) ValueError: índice inválido
# E) (99, 20, 30) — índice 0 é substituído
# ------------------------------------------------------------
Q02 = "C"


# ------------------------------------------------------------
# Q03 🟢 — Dicionários: método .get() com valor padrão
#
# aluno = {"nome": "Ana", "nota": 9.5, "ativo": True}
# resultado = aluno.get("email", "não informado")
# print(resultado)
#
# A) None
# B) KeyError: 'email'
# C) "não informado"
# D) False
# E) "Ana"
# ------------------------------------------------------------
Q03 = "C"


# ------------------------------------------------------------
# Q04 🟢 — Conjuntos: eliminação de duplicatas
#
# numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
# unicos = set(numeros)
# print(len(unicos))
#
# A) 10
# B) 9
# C) 8
# D) 7
# E) 6
# ------------------------------------------------------------
Q04 = "D"


# ------------------------------------------------------------
# Q05 🟡 — Listas: .sort(reverse=True) + slicing
#
# notas = [7.0, 8.5, 6.0, 9.0, 5.5]
# notas.sort(reverse=True)
# print(notas[1:3])
#
# A) [9.0, 8.5]
# B) [8.5, 7.0]
# C) [8.5, 6.0]
# D) [7.0, 6.0]
# E) [9.0, 7.0]
# ------------------------------------------------------------
Q05 = "B"


# ------------------------------------------------------------
# Q06 🟡 — Dicionários: list comprehension com .items()
#
# estoque = {"caneta": 10, "caderno": 5, "borracha": 0}
# vazios = [item for item, qtd in estoque.items() if qtd == 0]
# print(vazios)
#
# A) ["caneta", "caderno"]
# B) {"borracha": 0}
# C) ["borracha"]
# D) [0]
# E) []
# ------------------------------------------------------------
Q06 = "C"


# ------------------------------------------------------------
# Q07 🟡 — Conjuntos: operação .difference()
#
# turma_a = {"Ana", "Bruno", "Carlos", "Diana"}
# turma_b = {"Carlos", "Diana", "Eduardo", "Flávia"}
# resultado = turma_a.difference(turma_b)
# print(len(resultado))
#
# A) 2
# B) 3
# C) 4
# D) 6
# E) 8
# ------------------------------------------------------------
Q07 = "A"


# ------------------------------------------------------------
# Q08 🟡 — List comprehension com filtro e transformação
#
# numeros = range(1, 11)
# pares_quadrados = [n ** 2 for n in numeros if n % 2 == 0]
# print(pares_quadrados)
#
# A) [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# B) [4, 16, 36, 64, 100]
# C) [2, 4, 6, 8, 10]
# D) [4, 8, 12, 16, 20]
# E) [1, 9, 25, 49, 81]
# ------------------------------------------------------------
Q08 = "B"


# ------------------------------------------------------------
# Q09 🔴 — Dicionários aninhados + sum() + generator
#
# empresa = {
#     "nome": "ITEAM",
#     "equipes": {
#         "backend":  {"lider": "Hygo", "membros": 5},
#         "frontend": {"lider": "Ana",  "membros": 3},
#     }
# }
# total = sum(
#     equipe["membros"]
#     for equipe in empresa["equipes"].values()
# )
# print(total)
#
# A) 2
# B) 5
# C) 3
# D) 8
# E) {"backend": 5, "frontend": 3}
# ------------------------------------------------------------
Q09 = "D"


# ------------------------------------------------------------
# Q10 🔴 — Estruturas combinadas: lista de dicts + comprehension
#
# dados = [
#     {"nome": "Carlos",  "notas": [7, 8, 9]},
#     {"nome": "Beatriz", "notas": [10, 10, 9]},
#     {"nome": "Diego",   "notas": [5, 6, 4]},
# ]
# aprovados = [
#     d["nome"]
#     for d in dados
#     if sum(d["notas"]) / len(d["notas"]) >= 7.0
# ]
# print(aprovados)
#
# A) ["Carlos", "Beatriz", "Diego"]
# B) ["Beatriz"]
# C) ["Carlos", "Beatriz"]
# D) ["Carlos", "Diego"]
# E) []
# ------------------------------------------------------------
Q10 = "C"


# ──────────────────────────────────────────────────────────────
# MÓDULO 04 — DEFINIÇÃO E CHAMADA DE FUNÇÕES (7 questões)
# ──────────────────────────────────────────────────────────────

# ------------------------------------------------------------
# Q11 🟢 — Retorno implícito None sem return
#
# def somar(a, b):
#     resultado = a + b
#
# valor = somar(3, 4)
# print(valor)
#
# A) 7
# B) 0
# C) None
# D) TypeError: somar() missing return
# E) NameError: resultado is not defined
# ------------------------------------------------------------
Q11 = "C"


# ------------------------------------------------------------
# Q12 🟢 — Parâmetros com valor padrão (default)
#
# def saudar(nome, mensagem="Olá"):
#     print(f"{mensagem}, {nome}!")
#
# saudar("Ana")
# saudar("Bruno", "Bom dia")
#
# A) "Olá, Ana!" e "Olá, Bruno!"
# B) "Ana, Olá!" e "Bruno, Bom dia!"
# C) "Olá, Ana!" e "Bom dia, Bruno!"
# D) TypeError: saudar() missing 1 required argument
# E) None e None
# ------------------------------------------------------------
Q12 = "C"


# ------------------------------------------------------------
# Q13 🟡 — Escopo de variáveis: local vs global
#
# x = 10
#
# def alterar():
#     x = 99
#     print(x)
#
# alterar()
# print(x)
#
# A) 99 e 99
# B) 10 e 10
# C) 99 e 10
# D) 10 e 99
# E) UnboundLocalError: x referenced before assignment
# ------------------------------------------------------------
Q13 = "C"


# ------------------------------------------------------------
# Q14 🟡 — *args: parâmetros arbitrários
#
# def resumo(*valores):
#     return max(valores) - min(valores)
#
# print(resumo(3, 7, 1, 9, 2))
#
# A) 3
# B) 7
# C) 8
# D) 9
# E) TypeError: max() takes 1 positional argument but 5 were given
# ------------------------------------------------------------
Q14 = "C"


# ------------------------------------------------------------
# Q15 🟡 — Funções de primeira classe: callback
#
# def dobrar(n):
#     return n * 2
#
# def aplicar(funcao, valores):
#     return [funcao(v) for v in valores]
#
# resultado = aplicar(dobrar, [1, 2, 3, 4])
# print(resultado)
#
# A) [1, 2, 3, 4]
# B) [2, 4, 6, 8]
# C) [1, 4, 9, 16]
# D) TypeError: 'function' object is not iterable
# E) 8
# ------------------------------------------------------------
Q15 = "B"


# ------------------------------------------------------------
# Q16 🔴 — Funções recursivas: fatorial
#
# def fatorial(n):
#     if n <= 1:
#         return 1
#     return n * fatorial(n - 1)
#
# print(fatorial(4))
#
# A) 4
# B) 10
# C) 16
# D) 24
# E) RecursionError: maximum recursion depth exceeded
# ------------------------------------------------------------
Q16 = "D"


# ------------------------------------------------------------
# Q17 🔴 — **kwargs + dict comprehension + docstring
#
# def registrar(**dados):
#     """Registra informações arbitrárias de um objeto."""
#     return {k.upper(): v for k, v in dados.items()}
#
# info = registrar(nome="Hygo", cargo="Professor", ativo=True)
# print(info.get("CARGO"))
# print(registrar.__doc__[:10])
#
# A) "Professor" e "Registra i"
# B) "cargo"     e "Registra informações"
# C) None        e "Registra i"
# D) "Professor" e None
# E) KeyError: "CARGO" e "Registra i"
# ------------------------------------------------------------
Q17 = "A"


# ──────────────────────────────────────────────────────────────
# VERIFICADOR AUTOMÁTICO
# Execute este arquivo após preencher todas as respostas.
# Ele vai conferir o formato e avisar se algum campo ficou em branco.
# ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import sys

    respostas = {
        "Q01": Q01, "Q02": Q02, "Q03": Q03, "Q04": Q04, "Q05": Q05,
        "Q06": Q06, "Q07": Q07, "Q08": Q08, "Q09": Q09, "Q10": Q10,
        "Q11": Q11, "Q12": Q12, "Q13": Q13, "Q14": Q14, "Q15": Q15,
        "Q16": Q16, "Q17": Q17,
    }

    validas   = set("ABCDE")
    pendentes = [q for q, r in respostas.items() if r == "?"]
    invalidas = [q for q, r in respostas.items() if r != "?" and r not in validas]

    print("=" * 50)
    print("  VERIFICADOR DE RESPOSTAS")
    print("=" * 50)

    if pendentes:
        print(f"\n⚠️  Questões sem resposta ({len(pendentes)}):")
        for q in pendentes:
            print(f"   {q} → ainda '?'")

    if invalidas:
        print(f"\n❌  Respostas inválidas (use apenas A-E):")
        for q in invalidas:
            print(f"   {q} → '{respostas[q]}'")

    respondidas = [q for q, r in respostas.items() if r != "?" and r in validas]
    print(f"\n✅  Respondidas : {len(respondidas)}/17")
    print(f"⚠️   Pendentes   : {len(pendentes)}/17")

    if not pendentes and not invalidas:
        print("\n🎉 Todas as respostas preenchidas! Pronto para enviar.")
    else:
        print("\nComplete as respostas antes de fazer o commit.")
        sys.exit(1)