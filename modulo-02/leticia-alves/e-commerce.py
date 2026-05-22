from dataclasses import dataclass


# Atividade 4 - Motor de Descontos de E-commerce
#Alunos: Leticia Alves e Rafael Nobrega de Lima

# Contexto: sistema de descontos para e-commerce. Conceito central: Decision Engine + Registry para separar regras e handlers.


@dataclass
class Carrinho:
    valor_total: float
    cupom: str | None
    tipo_cliente: str     
    dia_semana: int        
    quantidade_itens: int


# ---------------- Decision Engine ----------------

def decidir_regra(carrinho: Carrinho) -> str:

    # Regra extra
    if carrinho.dia_semana == 2 and carrinho.valor_total >= 300:
        return "aniversario_loja"

    # Cupom Black Friday
    if carrinho.cupom == "BLACKFRIDAY":
        return "cupom:blackfriday"

    # Cliente VIP com compra alta
    if carrinho.tipo_cliente == "vip" and carrinho.valor_total >= 500:
        return "cliente:vip:alto"

    # Cliente fiel
    if carrinho.tipo_cliente == "fiel":
        return "cliente:fiel"

    # Cliente novo
    if carrinho.tipo_cliente == "novo":
        return "cliente:novo"

    # Muitos itens
    if carrinho.quantidade_itens >= 10:
        return "itens:grande"

    # Fim de semana
    if carrinho.dia_semana >= 5:
        return "fds:padrao"

    return "padrao"


# ---------------- Handlers ----------------

def desconto_blackfriday(carrinho):
    return (0.30, "Desconto Black Friday")


def desconto_vip(carrinho):
    return (0.20, "Cliente VIP")


def desconto_fiel(carrinho):
    return (0.15, "Cliente fiel")


def desconto_novo(carrinho):
    return (0.05, "Cliente novo")


def desconto_itens(carrinho):
    return (0.10, "Muitos itens")


def desconto_fds(carrinho):
    return (0.08, "Fim de semana")


def desconto_aniversario(carrinho):
    return (0.25, "Aniversário da loja")


def desconto_padrao(carrinho):
    return (0.00, "Sem desconto")


# ---------------- Registry ----------------

registry = {
    "cupom:blackfriday": desconto_blackfriday,
    "cliente:vip:alto": desconto_vip,
    "cliente:fiel": desconto_fiel,
    "cliente:novo": desconto_novo,
    "itens:grande": desconto_itens,
    "fds:padrao": desconto_fds,
    "aniversario_loja": desconto_aniversario,
    "padrao": desconto_padrao
}


# ---------------- Função Final ----------------

def calcular_desconto_depois(carrinho):
    regra = decidir_regra(carrinho)
    return registry[regra](carrinho)


# ---------------- Teste ----------------

carrinho = Carrinho(
    valor_total=600,
    cupom=None,
    tipo_cliente="vip",
    dia_semana=1,
    quantidade_itens=5
)

print(calcular_desconto_depois(carrinho))