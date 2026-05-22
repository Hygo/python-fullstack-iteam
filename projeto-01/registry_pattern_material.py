"""
=============================================================
REGISTRY PATTERN EM PYTHON
Do if/else ao padrão profissional — passo a passo

Curso de Capacitação Full Stack – ITEAM
Professor: Msc. Hygo Sousa De Oliveira

Referências:
  dev.to/dentedlogic/stop-writing-giant-if-else-chains-...
  github.com/SughoshKulkarni/Python-Registry
=============================================================

SUMÁRIO
  PARTE 1 — O problema: cadeia de if/elif que cresce sem controle
  PARTE 2 — Diagnóstico: por que isso é ruim?
  PARTE 3 — Solução nível 1: dicionário simples (Registry básico)
  PARTE 4 — Solução nível 2: classe Registry reutilizável
  PARTE 5 — Solução nível 3: auto-registro com decorator
  PARTE 6 — Decision Engine: separando roteamento de execução
  PARTE 7 — Comparativo final e regra de ouro
=============================================================
"""


# ==============================================================
# PARTE 1 — O PROBLEMA
# Imagine um sistema de notificações que precisa enviar mensagens
# por diferentes canais. Começa pequeno e vai crescendo…
# ==============================================================

print("=" * 65)
print("PARTE 1 — O problema: if/elif crescendo sem controle")
print("=" * 65)


# ── VERSÃO 1 (ingênua) ── funciona, mas já tem cheiro ruim
def enviar_notificacao_v1(canal: str, mensagem: str) -> None:
    """Sistema de notificações – versão original com if/elif."""

    if canal == "email":
        print(f"[EMAIL] Enviando: {mensagem}")

    elif canal == "sms":
        print(f"[SMS] Enviando: {mensagem}")

    elif canal == "push":
        print(f"[PUSH] Enviando: {mensagem}")

    # ← Seis meses depois o time pede Slack, WhatsApp e Telegram...
    elif canal == "slack":
        # TODO: Brian vai revisar isso depois
        print(f"[SLACK] Enviando: {mensagem}")

    elif canal == "whatsapp":
        if len(mensagem) > 160:
            print(f"[WHATSAPP] Mensagem longa — truncando para 160 chars")
            mensagem = mensagem[:160]
        print(f"[WHATSAPP] Enviando: {mensagem}")

    elif canal == "telegram":
        print(f"[TELEGRAM] Enviando: {mensagem}")

    elif canal == "discord":
        # ATENÇÃO: discord exige formato diferente em prod
        print(f"[DISCORD] Enviando: {mensagem}")

    elif canal == "teams":
        print(f"[TEAMS] Enviando: {mensagem}")

    # ← Um ano depois: mais 6 canais, lógica condicional aninhada,
    #   comentários desatualizados, ninguém quer tocar nisso.
    else:
        print(f"[ERRO] Canal desconhecido: {canal}")


# Teste da versão problemática
enviar_notificacao_v1("email", "Reunião às 14h")
enviar_notificacao_v1("sms", "Seu código é 4821")
enviar_notificacao_v1("fax", "Canal inexistente")   # ← erro silencioso


# ==============================================================
# PARTE 2 — DIAGNÓSTICO: por que isso é ruim?
# ==============================================================

print("\n" + "=" * 65)
print("PARTE 2 — Diagnóstico: os 3 pecados capitais do if/elif")
print("=" * 65)

"""
PECADO 1 — Viola o Open/Closed Principle (OCP)
    Para ADICIONAR um canal novo, você tem que MODIFICAR
    a função existente. Qualquer bug introduzido pode quebrar
    todos os outros canais.

PECADO 2 — Complexidade cresce linearmente
    O tempo de leitura e manutenção cresce com cada novo elif.
    Com 30 canais, ninguém lê o código inteiro antes de editar.

PECADO 3 — Dificuldade de teste
    Para testar o canal "whatsapp", você precisa passar pelo
    bloco inteiro da função. Os casos são acoplados.

SOLUÇÃO → Registry Pattern
    Separar O QUE FAZER (as funções de envio)
    de COMO ESCOLHER (a lógica de lookup).
"""

print("Diagnóstico registrado. Ver comentários no código.")


# ==============================================================
# PARTE 3 — SOLUÇÃO NÍVEL 1: dicionário simples
# A forma mais direta de aplicar o padrão.
# ==============================================================

print("\n" + "=" * 65)
print("PARTE 3 — Nível 1: Registry como dicionário simples")
print("=" * 65)


# ── PASSO 1: extraia cada bloco do if/elif para uma função própria ──
def _enviar_email(mensagem: str) -> None:
    print(f"[EMAIL] Enviando: {mensagem}")

def _enviar_sms(mensagem: str) -> None:
    print(f"[SMS] Enviando: {mensagem}")

def _enviar_push(mensagem: str) -> None:
    print(f"[PUSH] Enviando: {mensagem}")

def _enviar_slack(mensagem: str) -> None:
    print(f"[SLACK] Enviando: {mensagem}")

def _enviar_whatsapp(mensagem: str) -> None:
    if len(mensagem) > 160:
        mensagem = mensagem[:160]
    print(f"[WHATSAPP] Enviando: {mensagem}")


# ── PASSO 2: mapeie canal → função em um dicionário ──
# Perceba: guardamos a REFERÊNCIA da função, não a chamamos aqui.
CANAL_REGISTRY: dict[str, callable] = {
    "email":    _enviar_email,
    "sms":      _enviar_sms,
    "push":     _enviar_push,
    "slack":    _enviar_slack,
    "whatsapp": _enviar_whatsapp,
}


# ── PASSO 3: a função principal vira uma simples consulta ao dict ──
def enviar_notificacao_v2(canal: str, mensagem: str) -> None:
    """
    Versão com registry de dicionário.
    Para adicionar um canal: adicione a função + uma linha no dict.
    Esta função em si NUNCA mais precisará ser modificada.
    """
    handler = CANAL_REGISTRY.get(canal)

    if handler is None:
        raise ValueError(f"Canal desconhecido: '{canal}'. "
                         f"Disponíveis: {list(CANAL_REGISTRY.keys())}")

    handler(mensagem)


# Teste — mesmo comportamento, código 10x mais limpo
enviar_notificacao_v2("email",    "Reunião às 14h")
enviar_notificacao_v2("whatsapp", "Código: 4821")

try:
    enviar_notificacao_v2("fax", "agora dá erro explícito")
except ValueError as e:
    print(f"[ValueError] {e}")

# ← Adicionar "telegram" agora é APENAS isso:
def _enviar_telegram(mensagem: str) -> None:
    print(f"[TELEGRAM] Enviando: {mensagem}")

CANAL_REGISTRY["telegram"] = _enviar_telegram
enviar_notificacao_v2("telegram", "Nova função registrada em runtime!")


# ==============================================================
# PARTE 4 — SOLUÇÃO NÍVEL 2: classe Registry reutilizável
# Encapsulamos o dicionário em uma classe com validações,
# tornando o padrão genérico e reutilizável em qualquer contexto.
# ==============================================================

print("\n" + "=" * 65)
print("PARTE 4 — Nível 2: classe Registry genérica e reutilizável")
print("=" * 65)


class Registry:
    """
    Implementação genérica do Registry Pattern.

    Encapsula um dicionário com:
      - Validação de chave duplicada no register()
      - KeyError explícito no get()
      - Suporte ao operador `in` via __contains__
      - Listagem de chaves disponíveis

    Uso:
        registry = Registry()
        registry.register("pdf", exportar_pdf)
        handler = registry.get("pdf")
        handler(dados)
    """

    def __init__(self, nome: str = "Registry") -> None:
        self._store: dict = {}
        self._nome  = nome

    def register(self, chave: str, valor) -> None:
        """
        Registra um par chave → valor.

        Raises:
            ValueError: se a chave já estiver registrada.
        """
        if chave in self._store:
            raise ValueError(
                f"[{self._nome}] Chave '{chave}' já registrada. "
                f"Use update() para sobrescrever explicitamente."
            )
        self._store[chave] = valor
        print(f"  ✅ [{self._nome}] '{chave}' registrado.")

    def get(self, chave: str):
        """
        Recupera o valor associado à chave.

        Raises:
            KeyError: se a chave não existir.
        """
        if chave not in self._store:
            raise KeyError(
                f"[{self._nome}] Chave '{chave}' não encontrada. "
                f"Disponíveis: {self.listar_chaves()}"
            )
        return self._store[chave]

    def update(self, chave: str, valor) -> None:
        """Sobrescreve um registro existente (ex.: feature flags)."""
        self._store[chave] = valor
        print(f"  🔄 [{self._nome}] '{chave}' atualizado.")

    def unregister(self, chave: str) -> None:
        """Remove um registro do dicionário."""
        if chave not in self._store:
            raise KeyError(f"[{self._nome}] '{chave}' não encontrado.")
        del self._store[chave]
        print(f"  🗑️  [{self._nome}] '{chave}' removido.")

    def listar_chaves(self) -> list[str]:
        """Retorna a lista de todas as chaves registradas."""
        return list(self._store.keys())

    def __contains__(self, chave: str) -> bool:
        """Permite usar `if chave in registry:` naturalmente."""
        return chave in self._store

    def __repr__(self) -> str:
        return f"Registry(nome={self._nome!r}, chaves={self.listar_chaves()})"


# ── Recriando o sistema de notificações com a classe Registry ──
print("\nCriando o NotificationRegistry:")
notif_registry = Registry(nome="NotificationRegistry")

notif_registry.register("email",    _enviar_email)
notif_registry.register("sms",      _enviar_sms)
notif_registry.register("whatsapp", _enviar_whatsapp)
notif_registry.register("telegram", _enviar_telegram)

print(f"\n{notif_registry}")


def enviar_notificacao_v3(canal: str, mensagem: str) -> None:
    """Versão com classe Registry — sem if/elif em lugar algum."""
    handler = notif_registry.get(canal)
    handler(mensagem)


print()
enviar_notificacao_v3("email",    "Versão com classe Registry!")
enviar_notificacao_v3("telegram", "Funciona perfeitamente.")

# Verificando existência sem try/except
if "slack" in notif_registry:
    enviar_notificacao_v3("slack", "slack está registrado")
else:
    print("'slack' ainda não registrado — ok, sem erro.")


# ==============================================================
# PARTE 5 — SOLUÇÃO NÍVEL 3: auto-registro com decorator
# O handler se registra sozinho no momento em que é definido.
# ==============================================================

print("\n" + "=" * 65)
print("PARTE 5 — Nível 3: auto-registro com decorator")
print("=" * 65)

"""
O decorator de registro funciona assim:

    @registrar("chave")
    def minha_funcao(...):
        ...

É equivalente a:

    def minha_funcao(...): ...
    registry.register("chave", minha_funcao)

A vantagem: a função e seu registro ficam juntos no código.
A desvantagem: o arquivo DEVE ser importado para o decorator rodar.
Para contextos simples (tudo em um arquivo), é a forma mais limpa.
"""

# Criamos um novo registry para este exemplo
exportador_registry = Registry(nome="ExportadorRegistry")


def registrar_exportador(formato: str):
    """
    Decorator factory: retorna um decorator que registra a função.

    Uso:
        @registrar_exportador("pdf")
        def exportar_pdf(dados): ...
    """
    def decorator(func):
        exportador_registry.register(formato, func)
        return func          # ← retorna a função intacta
    return decorator


# Agora cada handler "sabe" se registrar sozinho
@registrar_exportador("pdf")
def exportar_pdf(dados: dict) -> None:
    print(f"[PDF] Exportando: {dados}")

@registrar_exportador("csv")
def exportar_csv(dados: dict) -> None:
    print(f"[CSV] Exportando: {dados}")

@registrar_exportador("json")
def exportar_json(dados: dict) -> None:
    import json
    print(f"[JSON] Exportando:\n{json.dumps(dados, indent=2, ensure_ascii=False)}")

@registrar_exportador("xlsx")
def exportar_xlsx(dados: dict) -> None:
    print(f"[XLSX] Exportando: {dados}")


# A função de dispatch continua sem if/elif
def exportar(formato: str, dados: dict) -> None:
    """Despacha para o exportador correto via registry."""
    handler = exportador_registry.get(formato)
    handler(dados)


dados_teste = {"nome": "Ana Silva", "cargo": "Dev", "salario": 8500.0}

print()
exportar("pdf",  dados_teste)
exportar("json", dados_teste)
exportar("csv",  dados_teste)

# Adicionar XLSX? O arquivo principal não muda.
# Só crie a função com o decorator — pronto.
exportar("xlsx", dados_teste)


# ==============================================================
# PARTE 6 — DECISION ENGINE: separando roteamento de execução
# Quando a CHAVE de lookup depende de lógica complexa,
# extraímos essa lógica para um "Decision Engine" separado.
# ==============================================================

print("\n" + "=" * 65)
print("PARTE 6 — Decision Engine: separando roteamento de execução")
print("=" * 65)

"""
PROBLEMA: e se precisamos escolher o handler com base em
MÚLTIPLOS parâmetros (valor da compra, tipo de cliente, horário)?

ERRADO: colocar essa lógica dentro do registry ou do dispatcher.
CERTO:  criar uma função separada que transforma contexto → chave.

    contexto (dados brutos)
        ↓
    [Decision Engine] → chave simples (string)
        ↓
    [Registry]        → handler correto
        ↓
    [Handler]         → executa a ação
"""

from dataclasses import dataclass


@dataclass
class Pedido:
    valor:         float
    tipo_cliente:  str   # "vip", "normal", "novo"
    canal_origem:  str   # "app", "web", "loja"
    parcelado:     bool


# ── Decision Engine: contexto complexo → chave simples ──
def decidir_processador(pedido: Pedido) -> str:
    """
    Contém TODA a lógica de negócio para escolher o processador.
    Retorna uma chave simples que o registry entende.
    """
    if pedido.valor > 5000 and pedido.tipo_cliente == "vip":
        return "pagamento:vip_alto_valor"

    if pedido.valor > 5000:
        return "pagamento:alto_valor"

    if pedido.tipo_cliente == "novo" and not pedido.parcelado:
        return "pagamento:novo_cliente"

    if pedido.canal_origem == "loja":
        return "pagamento:presencial"

    return "pagamento:padrao"


# ── Registry de processadores ──
processador_registry = Registry(nome="ProcessadorRegistry")

def _processar_vip_alto_valor(p: Pedido) -> None:
    print(f"[VIP ALTO VALOR] R$ {p.valor:.2f} — concierge ativado 🎩")

def _processar_alto_valor(p: Pedido) -> None:
    print(f"[ALTO VALOR] R$ {p.valor:.2f} — revisão manual acionada")

def _processar_novo_cliente(p: Pedido) -> None:
    print(f"[NOVO CLIENTE] R$ {p.valor:.2f} — análise de crédito")

def _processar_presencial(p: Pedido) -> None:
    print(f"[PRESENCIAL] R$ {p.valor:.2f} — maquininha acionada 💳")

def _processar_padrao(p: Pedido) -> None:
    print(f"[PADRÃO] R$ {p.valor:.2f} — fluxo normal")


print()
processador_registry.register("pagamento:vip_alto_valor", _processar_vip_alto_valor)
processador_registry.register("pagamento:alto_valor",     _processar_alto_valor)
processador_registry.register("pagamento:novo_cliente",   _processar_novo_cliente)
processador_registry.register("pagamento:presencial",     _processar_presencial)
processador_registry.register("pagamento:padrao",         _processar_padrao)


# ── Dispatcher: une Decision Engine + Registry ──
def processar_pedido(pedido: Pedido) -> None:
    """
    NÃO contém if/elif.
    Delega a decisão ao engine e a execução ao registry.
    """
    chave   = decidir_processador(pedido)     # ← engine decide a chave
    handler = processador_registry.get(chave) # ← registry entrega o handler
    handler(pedido)                           # ← handler executa


# Teste com cenários variados
print()
processar_pedido(Pedido(6000.0, "vip",    "app",   False))
processar_pedido(Pedido(6000.0, "normal", "web",   True))
processar_pedido(Pedido(200.0,  "novo",   "web",   False))
processar_pedido(Pedido(150.0,  "normal", "loja",  False))
processar_pedido(Pedido(350.0,  "normal", "app",   True))


# ==============================================================
# PARTE 7 — COMPARATIVO FINAL E REGRA DE OURO
# ==============================================================

print("\n" + "=" * 65)
print("PARTE 7 — Comparativo final")
print("=" * 65)

print("""
┌─────────────────────┬──────────────────┬───────────────────────┐
│ Critério            │ if/elif          │ Registry Pattern      │
├─────────────────────┼──────────────────┼───────────────────────┤
│ Adicionar opção     │ Modifica função  │ Nova linha no dict    │
│ Remover opção       │ Apaga elif       │ unregister()          │
│ Trocar em runtime   │ Impossível       │ update()              │
│ Testar isolado      │ Difícil          │ Direto na função      │
│ Legibilidade        │ Cai com escala   │ Constante             │
│ Open/Closed (OCP)   │ ❌ Viola         │ ✅ Respeita           │
└─────────────────────┴──────────────────┴───────────────────────┘

REGRA DE OURO:
  ✅ Use Registry quando a lista de opções CRESCE com o tempo.
  ✅ Use Registry quando quiser adicionar opções SEM tocar no
     código existente (Open/Closed Principle).
  ❌ Não use Registry para 2-3 condições fixas que nunca mudam.
  ❌ Não use Registry se a lógica é uma simples função map().

  "Make it work → make it right → make it fast."
""")
