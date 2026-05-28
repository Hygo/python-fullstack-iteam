# main.py
# =============================================================================
# ITEAM | Projeto: Salão de Beleza & Barbearia
# Arquivo: main.py
# Assunto: Ponto de entrada — integra todos os módulos do projeto
#
# Execute a partir da pasta raiz:
#   python main.py
# =============================================================================
#
# ----------------------------------------------------------------------------
#  BUG 14 — Funcionario instanciado com argumentos na ordem errada
#  ONDE  : criação de  func_ana  e  func_carlos
#  ERRO  : os argumentos estão na ordem  (cargo, nome, cpf, telefone, salario)
#          mas  Funcionario.__init__  espera  (nome, cpf, telefone, cargo, salario).
#  DICA  : reordene os argumentos na chamada:
#          Funcionario("Ana Costa", "111.222.333-44", "(92)99999-1111", "Cabeleireira", 2200.00)
# ----------------------------------------------------------------------------

from salao.modelos.funcionario import Funcionario, Coordenador
from salao.modelos.equipamento import Equipamento
from salao.equipes.cabelo    import EquipeCabelo
from salao.equipes.manicure  import EquipeManicure
from salao.equipes.spa       import EquipeSpa
from salao.gestao.salao      import Salao


def main():
    print("\n" + "=" * 52)
    print("  SISTEMA DE GESTAO — SALAO ITEAM BEAUTY")
    print("=" * 52 + "\n")

    # ------------------------------------------------------------------
    # 1. Coordenador
    # ------------------------------------------------------------------
    coord = Coordenador(
        nome           = "Mariana Oliveira",
        cpf            = "000.111.222-33",
        telefone       = "(92) 98888-0000",
        salario_base   = 5000.00,
        percentual_bonus = 0.20,
    )
    print(f"Coordenadora: {coord}\n")

    # ------------------------------------------------------------------
    # 2. Salão
    # ------------------------------------------------------------------
    salao = Salao(
        nome        = "Salão ITEAM Beauty",
        endereco    = "Av. Amazonas, 1000 — Manaus/AM",
        coordenador = coord,
    )

    # ------------------------------------------------------------------
    # 3. Funcionários
    #    BUG 14: argumentos fora de ordem nos dois primeiros
    # ------------------------------------------------------------------
    # func_ana = Funcionario(
    #     "Cabeleireira",        # ← ERRADO: deveria ser o nome primeiro
    #     "111.222.333-44",
    #     "(92)99999-1111",
    #     "Ana Costa",           # ← ERRADO: deveria ser o cargo aqui
    #     2200.00,
    # )

    # func_carlos = Funcionario(
    #     "Barbeiro",            # ← ERRADO: mesmo problema de ordem
    #     "222.333.444-55",
    #     "(92)99999-2222",
    #     "Carlos Melo",
    #     2000.00,
    # )

    # Estes dois estão corretos (para referência)
    func_lucia = Funcionario("Lúcia Ferreira",  "333.444.555-66",
                             "(92)99999-3333", "Manicure", 1900.00)
    func_bia   = Funcionario("Beatriz Santos",  "444.555.666-77",
                             "(92)99999-4444", "Esteticista", 2100.00)

    # ------------------------------------------------------------------
    # 4. Equipes
    # ------------------------------------------------------------------
    print("\n[Montando equipes...]")
    eq_cabelo   = EquipeCabelo()
    eq_manicure = EquipeManicure()
    eq_spa      = EquipeSpa()

    eq_cabelo.adicionar_membro(func_ana)
#     eq_cabelo.adicionar_membro(func_carlos)
#     eq_manicure.adicionar_membro(func_lucia)
#     eq_spa.adicionar_membro(func_bia)

#     # ------------------------------------------------------------------
#     # 5. Equipamentos
#     # ------------------------------------------------------------------
#     print("\n[Cadastrando equipamentos...]")
#     equip1 = Equipamento("EQ001", "Cadeira Hidráulica",   "Cadeira reclinável para corte", 1800.00)
#     equip2 = Equipamento("EQ002", "Secador Profissional",  "2400W, bivolt",                  650.00)
#     equip3 = Equipamento("EQ003", "Maca de Massagem",     "Espuma D45, suporte 200kg",      980.00)
#     equip4 = Equipamento("EQ004", "Autoclave",            "Esterilizador 21L",             3200.00)

#     # ------------------------------------------------------------------
#     # 6. Registra tudo no salão
#     # ------------------------------------------------------------------
    print("\n[Registrando no salão...]")
    salao.adicionar_equipe(eq_cabelo)
    salao.adicionar_equipe(eq_manicure)
    salao.adicionar_equipe(eq_spa)

#     salao.adicionar_equipamento(equip1)
#     salao.adicionar_equipamento(equip2)
#     salao.adicionar_equipamento(equip3)
#     salao.adicionar_equipamento(equip4)

#     # ------------------------------------------------------------------
#     # 7. Relatórios
#     # ------------------------------------------------------------------
#     salao.listar_equipes()

#     print()
#     eq_cabelo.listar_membros()
#     eq_manicure.listar_membros()
#     eq_spa.listar_membros()

#     salao.listar_equipamentos()
#     salao.relatorio_financeiro()

#     # ------------------------------------------------------------------
#     # 8. Polimorfismo em ação
#     # ------------------------------------------------------------------
#     print("\n" + "=" * 52)
#     print("  ATENDIMENTOS DO DIA")
#     print("=" * 52)
#     atendimentos = [
#         (eq_cabelo,   "João Neto",    "Corte degradê"),
#         (eq_manicure, "Paula Lima",   "Nail art"),
#         (eq_spa,      "Renata Costa", "Relaxamento"),
#         (eq_cabelo,   "Pedro Alves",  "Barba completa"),
#     ]
#     for equipe, cliente, servico in atendimentos:
#         equipe.realizar_servico(cliente, servico)   # Duck Typing: mesma chamada, tipos diferentes

#     print("\n  Sistema encerrado. Até logo!\n")


# if __name__ == "__main__":
#     main()
