# 🗂️ Registry Pattern em Python

**Curso de Capacitação em Desenvolvimento Full Stack — ITEAM**
Professor: Msc. Hygo Sousa De Oliveira

> *"Stop writing giant if/else chains — master the Python Registry Pattern."*

---

## 📁 Arquivos deste módulo

| Arquivo | Descrição |
|---------|-----------|
| [`registry_pattern_material.py`](#-registry_pattern_materialpy) | Material didático com passo a passo completo |
| [`registry_atividades.py`](#-registry_atividadespy) | 5 desafios progressivos para os alunos |

---

## 📖 `registry_pattern_material.py`

Material de estudo executável. Cada parte imprime seu próprio cabeçalho e pode ser acompanhada linha a linha em sala de aula.

### Como executar

```bash
python registry_pattern_material.py
```

### Estrutura — 7 partes

#### Parte 1 — O Problema

Demonstra um sistema de notificações com `if/elif` que começa simples e vira um monstro com 8 canais, lógica aninhada e comentários desatualizados. O código **funciona**, mas já tem cheiro ruim.

```python
def enviar_notificacao_v1(canal: str, mensagem: str) -> None:
    if canal == "email":
        ...
    elif canal == "sms":
        ...
    elif canal == "slack":
        # TODO: Brian vai revisar isso depois  ← red flag
        ...
```

---

#### Parte 2 — Diagnóstico

Explica os **3 pecados capitais** do `if/elif` crescente, com comentários que ficam no código como referência de estudo:

| Pecado | Princípio violado |
|--------|------------------|
| Para adicionar, você modifica código existente | Open/Closed (OCP) |
| Complexidade cresce linearmente com as opções | Manutenibilidade |
| Impossível testar um canal sem passar pelos outros | Testabilidade |

---

#### Parte 3 — Nível 1: Dicionário Simples

**A refatoração mais direta.** Extrai cada bloco do `if/elif` para uma função própria e mapeia tudo em um dicionário.

```python
CANAL_REGISTRY: dict[str, callable] = {
    "email":    _enviar_email,
    "sms":      _enviar_sms,
    "whatsapp": _enviar_whatsapp,
}

def enviar_notificacao_v2(canal: str, mensagem: str) -> None:
    handler = CANAL_REGISTRY.get(canal)
    if handler is None:
        raise ValueError(f"Canal desconhecido: '{canal}'")
    handler(mensagem)
```

> Adicionar `"telegram"` é apenas `CANAL_REGISTRY["telegram"] = _enviar_telegram`. A função principal **nunca muda**.

---

#### Parte 4 — Nível 2: Classe Registry Reutilizável

Encapsula o dicionário em uma classe com validações, tornando o padrão portável para qualquer contexto do projeto.

```python
class Registry:
    def register(self, chave: str, valor) -> None: ...
    def get(self, chave: str): ...
    def update(self, chave: str, valor) -> None: ...   # feature flags
    def unregister(self, chave: str) -> None: ...
    def __contains__(self, chave: str) -> bool: ...    # suporte a `in`
    def listar_chaves(self) -> list[str]: ...
```

---

#### Parte 5 — Nível 3: Auto-registro com Decorator

O handler **se registra sozinho** no momento em que é definido. A função e sua "ficha de registro" ficam juntas no código.

```python
@registrar_exportador("pdf")
def exportar_pdf(dados: dict) -> None:
    print(f"[PDF] Exportando: {dados}")

# equivale a:
# def exportar_pdf(dados): ...
# registry.register("pdf", exportar_pdf)
```

---

#### Parte 6 — Decision Engine

Quando a **chave de lookup depende de lógica complexa** (múltiplos parâmetros, regras de negócio), extrai-se essa lógica para uma função separada.

```
Contexto (dados brutos)
    ↓
[Decision Engine]  →  chave simples (str)
    ↓
[Registry]         →  handler correto
    ↓
[Handler]          →  executa a ação
```

```python
def decidir_processador(pedido: Pedido) -> str:
    if pedido.valor > 5000 and pedido.tipo_cliente == "vip":
        return "pagamento:vip_alto_valor"
    ...
    return "pagamento:padrao"

def processar_pedido(pedido: Pedido) -> None:
    chave   = decidir_processador(pedido)   # engine → chave
    handler = registry.get(chave)           # registry → handler
    handler(pedido)                         # sem if/elif aqui
```

---

#### Parte 7 — Comparativo Final e Regra de Ouro

```
┌─────────────────────┬──────────────────┬───────────────────────┐
│ Critério            │ if/elif          │ Registry Pattern      │
├─────────────────────┼──────────────────┼───────────────────────┤
│ Adicionar opção     │ Modifica função  │ Nova linha no dict    │
│ Remover opção       │ Apaga elif       │ unregister()          │
│ Trocar em runtime   │ Impossível       │ update()              │
│ Testar isolado      │ Difícil          │ Direto na função      │
│ Open/Closed (OCP)   │ ❌ Viola         │ ✅ Respeita           │
└─────────────────────┴──────────────────┴───────────────────────┘
```

> ✅ Use Registry quando a lista de opções **cresce com o tempo**.
> ❌ Não use para 2–3 condições fixas que nunca mudam.

---

## 🏋️ `registry_atividades.py`

Cinco desafios progressivos. Cada um apresenta um código **ANTES** com `if/elif` funcionando e uma seção `# SUA SOLUÇÃO AQUI` para o aluno implementar o Registry.

### Como executar

```bash
python registry_atividades.py
```

### Regra de ouro para todas as atividades

> O comportamento de saída do bloco `[DEPOIS]` deve ser **idêntico** ao bloco `[ANTES]`. Se os `print`s mudarem, revise a solução.

---

### Atividade 1 — Calculadora de Operações 🟢 Básico

**Contexto:** calculadora aritmética com 6 operações.
**Conceito central:** dicionário simples + lambdas como valores.

```python
# ANTES
def calcular_antes(operacao: str, a: float, b: float) -> float:
    if operacao == "soma":
        return a + b
    elif operacao == "subtracao":
        return a - b
    # ... +4 operações
```

**O que implementar:**
- `OPERACOES_REGISTRY` mapeando nome → lambda ou função
- `calcular_depois()` consultando o dicionário
- Tratar `ZeroDivisionError` e operação inexistente com `ValueError`
- **Desafio extra:** adicionar operação `"raiz"` (√a) **sem tocar** em `calcular_depois()`

---

### Atividade 2 — Sistema de Relatórios 🟢 Básico+

**Contexto:** gerador de relatórios com 5 formatos diferentes.
**Conceito central:** classe `Registry` reutilizável.

```python
# ANTES
def gerar_relatorio_antes(formato: str, dados: dict) -> None:
    if formato == "resumo":
        ...
    elif formato == "detalhado":
        ...
    # ... +3 formatos
```

**O que implementar:**
- A classe `Registry` completa (`register`, `get`, `__contains__`)
- Uma função isolada para cada formato
- `gerar_relatorio_depois()` sem nenhum `if/elif`
- **Desafio extra:** adicionar formato `"json_pretty"` registrando apenas uma nova função

---

### Atividade 3 — Pipeline de Validação de Dados 🟡 Intermediário

**Contexto:** validador de formulário com 6 tipos de campo (`email`, `cpf`, `telefone`, `cep`, `idade`, `nome`).
**Conceito central:** decorator `@registrar_validador("tipo")` + Registry em cadeia.

```python
# ANTES
def validar_campo_antes(tipo: str, valor) -> tuple[bool, str]:
    if tipo == "email":
        valido = "@" in str(valor) and "." in str(valor).split("@")[-1]
        return (valido, "" if valido else "Email inválido")
    elif tipo == "cpf":
        ...
```

**O que implementar:**
```python
validador_registry = Registry()

def registrar_validador(tipo: str):
    def decorator(func):
        validador_registry.register(tipo, func)
        return func
    return decorator

@registrar_validador("email")
def validar_email(valor) -> tuple[bool, str]:
    ...
```

- **Desafio extra:** adicionar validador `"url"` verificando `http://` ou `https://` sem tocar em `validar_campo_depois()`

---

### Atividade 4 — Motor de Descontos de E-commerce 🟡 Intermediário

**Contexto:** sistema de descontos com 7 regras que combinam valor do carrinho, tipo de cliente, cupom e dia da semana.
**Conceito central:** Decision Engine + Registry separados.

```python
@dataclass
class Carrinho:
    valor_total:     float
    cupom:           str | None
    tipo_cliente:    str    # "novo", "fiel", "vip"
    dia_semana:      int    # 0=seg … 6=dom
    quantidade_itens: int
```

**O que implementar:**

1. `decidir_regra(carrinho: Carrinho) -> str` — o engine com toda a lógica condicional, retornando chaves como `"cupom:blackfriday"`, `"cliente:vip:alto"`, `"fds:padrao"`, etc.
2. Um handler por chave, cada um retornando `tuple[float, str]`
3. `calcular_desconto_depois()` com apenas 2 linhas: engine + registry

**Desafio extra:** adicionar regra `"aniversario_loja"` (25% na quarta-feira com carrinho ≥ R$300) sem tocar em `calcular_desconto_depois()`

---

### Atividade 5 — Sistema de Processamento de Eventos 🔴 Avançado

**Contexto:** sistema de eventos com 7 tipos (`usuario.criado`, `pagamento.aprovado`, `sistema.erro`, etc.), cada um com lógica de negócio própria.
**Conceito central:** Registry completo + decorator + runtime update (feature flag).

```python
@dataclass
class Evento:
    tipo:       str
    payload:    dict
    prioridade: int    # 1=baixa … 4=crítica
    origem:     str    # "app", "api", "webhook", "cron"
```

**O que implementar:**

1. **Classe `Registry` completa** com `register`, `get`, `update`, `unregister`, `__contains__`, `listar_chaves`
2. **Decorator** `@registrar_evento("tipo")` para auto-registro
3. **Handler isolado** para cada tipo de evento
4. **`processar_evento_depois()`** com `try/except KeyError` para eventos sem handler
5. **Runtime update simulado:**

```python
# V2 do handler — swap em runtime sem reiniciar
evento_registry.update("pagamento.aprovado", handle_pagamento_aprovado_v2)
print("Feature flag ativo: novo handler de pagamento em produção!")
```

6. Relatório final: `print(evento_registry.listar_chaves())`

---

### Checklist de entrega

Para cada atividade, o aluno deve verificar:

- [ ] A saída é idêntica ao bloco `[ANTES]`
- [ ] A função principal **não contém** `if/elif` de roteamento
- [ ] Adicionar uma nova opção não exige modificar a função principal
- [ ] Exceções são tratadas explicitamente (`KeyError` / `ValueError`)
- [ ] O código está comentado e legível

---

## 📚 Referências

- [Stop Writing Giant if/else Chains — dev.to](https://dev.to/dentedlogic/stop-writing-giant-if-else-chains-master-the-python-registry-pattern-ldm)
- [Python-Registry — GitHub](https://github.com/SughoshKulkarni/Python-Registry)
- [Open/Closed Principle — pythontutorial.net](https://www.pythontutorial.net/python-oop/python-open-closed-principle/)

---

## 🗂️ Estrutura sugerida no repositório

```
modulo-XX-registry-pattern/
├── README.md                        ← este arquivo
├── registry_pattern_material.py     ← material didático (7 partes)
├── registry_atividades.py           ← 5 desafios para os alunos
└── alunos/
    └── seu_nome/
        └── registry_atividades.py   ← cópia com as soluções
```

---

*"Explicit is better than implicit." — Zen of Python 🐍*
