# 🐍 Desafios – Módulo 1: Introdução ao Python
**Curso de Capacitação em Desenvolvimento Full Stack – ITEAM**  
Professor: Msc. Hygo Sousa De Oliveira

---

> **Como usar este repositório:**
> - Leia o enunciado de cada exercício com atenção.
> - Crie um arquivo `.py` para cada solução (ex: `ex01.py`, `ex02.py`...).
> - Os exercícios estão divididos em três níveis: 🟢 Básico | 🟡 Intermediário | 🔴 Avançado.
> - O gabarito está disponível em `gabarito.py`, mas tente resolver sozinho primeiro!

---

## 📅 Dia 1 – História, Filosofia e Configuração do Ambiente

### ⚙️ Exercício 00 – Configurando o Ambiente Virtual

Antes de escrever qualquer linha de código, todo projeto Python profissional começa com um **ambiente virtual** — um espaço isolado que garante que as dependências do seu projeto não conflitem com outros projetos ou com o Python do sistema.

Neste exercício você vai configurar o ambiente que será usado durante todo o curso.

**Passo a passo:**

**1. Verifique se o Python 3.12 está instalado:**
```bash
python3.12 --version
```
> Se não estiver instalado, baixe em [python.org/downloads](https://www.python.org/downloads/) e escolha a versão **3.12.x**.

**2. Crie o ambiente virtual com Python 3.12:**
```bash
python3.12 -m venv .venv
```
> O argumento `-m venv` invoca o módulo nativo de criação de ambientes virtuais.  
> `.venv` é o nome da pasta — o ponto na frente é uma convenção para indicar que é um diretório de configuração.

**3. Ative o ambiente virtual:**

| Sistema Operacional | Comando |
|---------------------|---------|
| Linux / macOS | `source .venv/bin/activate` |
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| Windows (CMD) | `.venv\Scripts\activate.bat` |

Quando ativado, o terminal exibirá o prefixo `(.venv)` antes do prompt:
```bash
(.venv) usuario@maquina:~/curso$
```

**4. Confirme que o ambiente está usando a versão correta:**
```bash
python --version
# Esperado: Python 3.12.x

which python        # Linux/macOS
where python        # Windows
# Deve apontar para dentro da pasta .venv
```

**5. Atualize o `pip` (gerenciador de pacotes):**
```bash
pip install --upgrade pip
```

**6. Crie o arquivo `.gitignore`** para não versionar a pasta do ambiente:
```bash
echo ".venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
```

**7. (Opcional) Congele as dependências para reprodutibilidade:**
```bash
pip freeze > requirements.txt
```

**✅ Critérios de conclusão:**
- [ ] Ambiente virtual criado com Python 3.12
- [ ] Ambiente ativado (prefixo `(.venv)` visível no terminal)
- [ ] `python --version` retorna `Python 3.12.x`
- [ ] `.gitignore` criado com `.venv/` listado

> 💡 *Nunca suba a pasta `.venv` para o GitHub — ela é gerada localmente e pode ter centenas de MB. O arquivo `requirements.txt` é o que permite que outra pessoa recrie o ambiente com `pip install -r requirements.txt`.*

---

### 🟢 Exercício 01 – O Clássico com Personalidade
Todo programador começa com "Hello, World!". Mas aqui vamos além:  
Escreva um script que exiba, em linhas separadas:
1. `Olá, Mundo!`
2. Seu nome completo
3. A frase: `Python: simples, poderoso e elegante.`

> 💡 *Dica: use a função `print()` três vezes.*

---     

### 🟢 Exercício 02 – Inspecionando o Ambiente
Escreva um script que importe o módulo `sys` e exiba:
1. A versão do Python instalada (`sys.version`)
2. O sistema operacional em uso (`sys.platform`)

---

### 🟢 Exercício 03 – O Zen na Prática
O **Zen of Python** pode ser acessado com `import this`.  
Escreva um script que:
1. Importe o módulo `this` para exibir o Zen.
2. Abaixo do import, adicione um comentário explicando com suas palavras **um** dos princípios que mais fez sentido para você.

---

### 🟡 Exercício 04 – Comentários como Documentação
Você recebeu o código abaixo **sem nenhum comentário**. Adicione comentários explicativos em cada linha e uma **docstring** no topo descrevendo o que o programa faz:

```python
nome = "Ana Lima"
idade = 29
salario = 4500.00
ativo = True
print(nome, idade, salario, ativo)
```

---

### 🟡 Exercício 05 – Primeira Análise de Erro
O código abaixo contém **erros propositais**. Identifique-os, corrija-os e explique em comentários o que estava errado:

```python
Print("Bem-vindo ao curso de Python")
nome = "Carlos
print("Aluno: " + nome)
print(Curso de Python)
```

---

### 🔴 Exercício 06 – Explorando Tipos com `type()`
Escreva um script que crie **6 variáveis** com os seguintes valores e tipos:
- Um número inteiro representando o ano atual
- Um número de ponto flutuante representando uma temperatura em Celsius
- Uma string com o nome de uma cidade brasileira
- Um booleano indicando se está chovendo
- O valor especial `None` atribuído a uma variável chamada `previsao`
- Uma string vazia

Para cada variável, exiba o **valor** e seu **tipo** com `type()`.

Formato de saída esperado:
```
2025 → <class 'int'>
28.5 → <class 'float'>
...
```

---

## 📅 Dia 2 – Variáveis, Tipos, Operadores, Entrada e Saída

### 🟢 Exercício 07 – Calculadora de Área
Uma construtora precisa calcular a área de terrenos retangulares.  
Escreva um script que:
1. Armazene a largura (`12.5`) e o comprimento (`30.0`) em variáveis
2. Calcule e exiba a **área** (largura × comprimento)
3. Exiba o resultado formatado: `Área do terreno: 375.0 m²`

---

### 🟢 Exercício 08 – Conversor de Temperatura
Escreva um script que converta uma temperatura de **Celsius para Fahrenheit** e para **Kelvin**.

Fórmulas:
- `F = (C × 9/5) + 32`
- `K = C + 273.15`

Use o valor `36.5°C` e exiba os três valores formatados.

---

### 🟢 Exercício 09 – Boas-vindas Personalizada
Escreva um script que:
1. Solicite ao usuário seu **nome** (`input()`)
2. Solicite sua **idade**
3. Exiba: `Olá, [nome]! Você tem [idade] anos e nasceu por volta de [ano_nascimento].`

> 💡 *`input()` sempre retorna string. Para cálculos, converta com `int()`.*

---

### 🟢 Exercício 10 – Divisão Inteira e Resto
Dado que um caminhão comporta **850 kg** e cada caixa pesa **32 kg**:
1. Calcule quantas caixas **completas** cabem (`//`)
2. Calcule o **peso restante** que não completa uma caixa (`%`)
3. Exiba os dois valores com mensagens claras

---

### 🟡 Exercício 11 – Formatação Profissional com f-strings
Uma empresa de RH precisa gerar fichas de funcionários. Armazene os dados abaixo e exiba **formatados**:

Dados: Nome: `Mariana Souza` | Cargo: `Analista de Dados` | Salário: `7850.50` | Anos: `3`

Saída esperada:
```
=============================
     FICHA DO FUNCIONÁRIO    
=============================
Nome   : Mariana Souza
Cargo  : Analista de Dados
Salário: R$ 7.850,50
Tempo  : 3 ano(s) de empresa
=============================
```

---

### 🟡 Exercício 12 – Calculadora de IMC
Fórmula: `IMC = peso / altura²`

Solicite **peso** (kg) e **altura** (m) via `input()`, calcule o IMC e exiba com 2 casas decimais e mensagem informativa.

---

### 🟡 Exercício 13 – Operadores Lógicos e de Comparação
Sem usar `if`, armazene dois números e use `print()` para responder (True/False):
1. O primeiro número é maior que o segundo?
2. Os dois são iguais?
3. Ambos são positivos?
4. Pelo menos um é maior que 100?
5. O primeiro é diferente de zero?

---

### 🟡 Exercício 14 – Troca de Variáveis
Corrija o código abaixo de **duas formas**: com variável auxiliar e com o método idiomático do Python:

```python
a = 10
b = 20
a = b
b = a
print(a, b)  # Esperado: 20 10 — mas imprime 20 20
```

---

### 🟡 Exercício 15 – Calculadora de Desconto
Uma loja aplica 10% de desconto em todas as compras.  
Peça o **valor da compra**, calcule o desconto e valor final, exibindo tudo formatado em reais.

> 💡 *Não use `if` ainda — calcule diretamente com os operadores que você conhece.*

---

### 🔴 Exercício 16 – Distância entre Dois Pontos
Fórmula: `d = √((x2 - x1)² + (y2 - y1)²)`

Defina `P1 = (3, 4)` e `P2 = (7, 1)`, calcule a distância com `math.sqrt` e exiba com 4 casas decimais.

---

### 🔴 Exercício 17 – Análise de Nota Fiscal
Solicite via `input()`: descrição do produto, quantidade e preço unitário. Exiba:

```
===== NOTA FISCAL =====
Produto   : [descrição]
Quantidade: [qtd] unidade(s)
Preço Unit: R$ [preço]
Subtotal  : R$ [qtd × preço]
Imposto   : R$ [12% do subtotal]
Total     : R$ [subtotal + imposto]
=======================
```

---

### 🔴 Exercício 18 – Conversão de Unidades Encadeada
Solicite uma distância em **metros** e converta para: km, cm, mm, polegadas e pés. Exiba em tabela formatada com alinhamento usando f-strings.

---

### 🔴 Exercício 19 – Manipulação de Strings no Mundo Real
Você recebeu um e-mail mal formatado: `"   joao.silva@EMPRESA.com.br   "`

Escreva um script que:
1. Remova espaços extras (`.strip()`)
2. Normalize para minúsculas (`.lower()`)
3. Extraia o **usuário** (parte antes do `@`)
4. Extraia o **domínio** (parte depois do `@`)
5. Exiba cada resultado com uma label clara

---

### 🔴 Exercício 20 – Calculadora de Investimento Simples
Solicite: capital inicial, taxa de juros ao mês (%) e período em meses.

Fórmula: `M = C × (1 + i × t)`

Exiba capital, taxa, período, juros totais e montante final formatados.

---

## 📅 Parte Avançada – Typing, Docstrings e JSON

### 🟢 Exercício 21 – Sua Primeira Função com Docstring
Escreva uma função `saudacao` que receba um nome e retorne uma string de boas-vindas, com **docstring completa**:

```python
def saudacao(nome):
    """
    Retorna uma mensagem de boas-vindas personalizada.

    Args:
        nome (str): Nome da pessoa a ser saudada.

    Returns:
        str: String com a mensagem de boas-vindas.

    Example:
        >>> saudacao("Ana")
        'Olá, Ana! Seja bem-vinda ao curso.'
    """
```

Chame a função com 3 nomes diferentes e exiba os resultados.

---

### 🟢 Exercício 22 – Type Hints Básico
Reescreva as funções abaixo adicionando **type hints** nos parâmetros e no retorno:

```python
def calcular_area(largura, altura):
    return largura * altura

def formatar_nome(nome, sobrenome):
    return f"{nome} {sobrenome}".title()

def eh_maior_de_idade(idade):
    return idade >= 18
```

> 💡 *Sintaxe: `def funcao(param: tipo) -> tipo_retorno:`*

---

### 🟢 Exercício 23 – Lendo um JSON Simples
Dado o dicionário abaixo, converta para JSON com `json.dumps()` (indentação de 2 espaços), depois converta de volta com `json.loads()` e exiba o nome e a média das notas:

```python
aluno = {
    "nome": "Pedro Henrique",
    "idade": 22,
    "curso": "Full Stack",
    "ativo": True,
    "notas": [8.5, 9.0, 7.5]
}
```

---

### 🟡 Exercício 24 – Função Documentada com Typing: Conversor de Moeda
Escreva a função `converter_moeda` com type hints completos, docstring com `Args`, `Returns` e `Example`, que converta um valor em reais para dólar e euro.

Cotações: `1 USD = 5.15 BRL` | `1 EUR = 5.58 BRL`

A função deve retornar uma **tupla** `(valor_usd, valor_eur)`.

---

### 🟡 Exercício 25 – Salvando Dados em JSON
Escreva um script que:
1. Crie um dicionário de **produto de e-commerce**: `id`, `nome`, `preco`, `estoque`, `disponivel`, `categorias` (lista)
2. Salve em `produto.json` com `json.dump()` e indentação
3. Leia o arquivo de volta e exiba cada campo com uma label

> 💡 *Use `open("produto.json", "w") as f` para escrita e `"r"` para leitura.*

---

### 🟡 Exercício 26 – Typing com `Optional` e `Union`
Escreva a função `buscar_usuario` que:
- Receba um `id` (int) e um `nome` que pode ser `str` **ou** `None`
- Retorne um dicionário com os dados ou `None` se o id for negativo
- Use `Optional` e `Union` do módulo `typing`
- Tenha docstring completa

---

### 🟡 Exercício 27 – JSON com Múltiplos Registros
Escreva um script que:
1. Crie uma lista com **3 dicionários** de funcionários (nome, cargo, salário, departamento)
2. Salve em `funcionarios.json`
3. Leia e exiba em **tabela formatada**
4. Calcule e exiba o **salário médio** da equipe

---

### 🟡 Exercício 28 – Docstring Google Style + Juros Compostos
Reescreva a função abaixo com type hints e docstring no **padrão Google Style** (incluindo `Args`, `Returns`, `Raises` e `Example`):

```python
def calcular_juros_compostos(capital, taxa, periodo):
    return capital * (1 + taxa / 100) ** periodo
```

O campo `Raises` deve documentar o que acontece se `capital` ou `taxa` forem negativos.

---

### 🔴 Exercício 29 – Parser de JSON de API Meteorológica
Faça o parse da string JSON abaixo e exiba um boletim meteorológico amigável:

```python
resposta_api = """
{
    "cidade": "Manaus",
    "pais": "BR",
    "temperatura": {
        "atual": 32.4,
        "minima": 26.1,
        "maxima": 35.8,
        "sensacao": 38.2
    },
    "umidade": 87,
    "condicao": "Parcialmente nublado",
    "vento": { "velocidade_kmh": 12, "direcao": "NE" },
    "atualizado_em": "2025-01-15T14:30:00"
}
"""
```

---

### 🔴 Exercício 30 – Typing Avançado: `TypedDict`
Use `TypedDict` para criar estruturas tipadas de um **pedido de e-commerce**:

```python
from typing import TypedDict, List

class ItemPedido(TypedDict):
    produto: str
    quantidade: int
    preco_unitario: float

class Pedido(TypedDict):
    id_pedido: int
    cliente: str
    itens: List[ItemPedido]
    status: str
```

Crie um pedido de exemplo, serialize para JSON e exiba formatado.

---

### 🔴 Exercício 31 – Mesclando JSONs de Sistemas Diferentes
Mescle os dois dicionários abaixo em um único `funcionario_completo`, salve em JSON, leia e exiba formatado com a lista de habilidades numerada:

```python
cadastro = {"id": 1042, "nome": "Fernanda Costa", "email": "fernanda@empresa.com"}
perfil   = {"id": 1042, "cargo": "Engenheira de Software", "nivel": "Senior",
            "salario": 12500.00, "habilidades": ["Python", "Django", "PostgreSQL"]}
```

---

### 🔴 Exercício 32 – Validador de Cadastro com Typing
Escreva a função `validar_cadastro` com type hints e docstring completa:

```python
from typing import Dict, List, Any

def validar_cadastro(dados: Dict[str, Any]) -> Dict[str, List[str]]:
    ...
```

Regras: `nome` ≥ 3 chars | `email` com `@` e `.` | `idade` entre 18-120 | `cpf` com 11 dígitos numéricos.

Retorne `{"valido": [...], "erros": [...]}` e teste com dados válidos e inválidos.

---

### 🔴 Exercício 33 – Sistema de Log em JSON
Implemente três funções (com type hints e docstrings) para um sistema de log:

```python
def registrar_evento(arquivo: str, nivel: str, mensagem: str) -> None: ...
def ler_logs(arquivo: str) -> list: ...
def filtrar_por_nivel(logs: list, nivel: str) -> list: ...
```

Use `datetime` para timestamps. Registre ao menos 5 eventos (`"INFO"`, `"WARNING"`, `"ERROR"`) e demonstre a filtragem.

---

### 🔴 Exercício 34 – Configuração de Aplicação via JSON
1. Crie `config.json` com seções `app`, `banco` e `email`
2. Implemente `carregar_config(caminho: str) -> dict`
3. Implemente `obter_valor(config: dict, chave: str, padrao: any = None) -> any` que navegue por chaves aninhadas com notação de ponto (`"app.versao"` → `"1.0.0"`)
4. Demonstre com 5 chamadas diferentes

---

### 🔴 Exercício 35 – Relatório de Vendas: JSON + Typing
Implemente funções tipadas e documentadas para analisar o JSON abaixo:

```python
vendas_json = """
[
    {"mes": "Janeiro",  "produto": "Notebook", "quantidade": 45, "valor_unit": 3200.00},
    {"mes": "Janeiro",  "produto": "Mouse",    "quantidade": 120, "valor_unit": 89.90},
    {"mes": "Fevereiro","produto": "Notebook", "quantidade": 38, "valor_unit": 3200.00},
    {"mes": "Fevereiro","produto": "Teclado",  "quantidade": 75, "valor_unit": 149.90},
    {"mes": "Março",    "produto": "Monitor",  "quantidade": 30, "valor_unit": 1200.00},
    {"mes": "Março",    "produto": "Mouse",    "quantidade": 200,"valor_unit": 89.90}
]
"""
```

Funções requeridas:
- `calcular_total_mes(vendas: list, mes: str) -> float`
- `produto_mais_vendido(vendas: list) -> str`
- `receita_total(vendas: list) -> float`

---

### 🔴 Exercício 36 – Agenda de Contatos: CRUD em JSON
Implemente um mini sistema de agenda com persistência em `contatos.json`:

```python
def adicionar_contato(nome: str, telefone: str, email: str) -> None: ...
def listar_contatos() -> list: ...
def buscar_contato(nome: str) -> dict | None: ...
def remover_contato(nome: str) -> bool: ...
```

Demonstre as 4 operações: adicionar 3 contatos, listar, buscar um e remover um.

---

### 🔴 Exercício 37 – Serialização Customizada de Objetos para JSON
O `json` nativo não serializa objetos Python. Escreva:
1. Uma classe `Produto` com `nome`, `preco` e `criado_em` (datetime)
2. `produto_para_dict(produto: 'Produto') -> dict` (converte datetime para ISO string)
3. `dict_para_produto(dados: dict) -> 'Produto'` (converte de volta)
4. Serialize uma lista de 3 produtos e desserialize de volta

> 💡 *Use `datetime.isoformat()` e `datetime.fromisoformat()`.*

---

### 🔴 Exercício 38 – Typing com `Callable` e Generics
Escreva uma função genérica com type hints:

```python
from typing import TypeVar, List, Callable

T = TypeVar('T')
R = TypeVar('R')

def aplicar_transformacao(dados: List[T], funcao: Callable[[T], R]) -> List[R]:
    """..."""
```

Demonstre com:
1. Lista de strings → maiúsculas
2. Lista de floats → arredondados com 2 casas
3. Lista de dicionários → extraindo um campo específico

---

### 🔴 Exercício 39 – Pipeline de Dados: JSON + Typing
Implemente um pipeline de processamento encadeado:

```python
def carregar_dados(caminho: str) -> list[dict]: ...
def normalizar_dados(dados: list[dict]) -> list[dict]: ...
def enriquecer_dados(dados: list[dict]) -> list[dict]: ...
def exportar_resultado(dados: list[dict], caminho: str) -> None: ...
```

Entrada: JSON com 5 clientes com nomes irregulares, emails em maiúsculas e telefones sem formatação. O pipeline deve limpar, normalizar e exportar os dados tratados.

---

### 🔴 Exercício 40 – Desafio Final: Sistema de Cadastro Completo
Integre **tudo** que aprendeu para criar um mini sistema de cadastro de alunos.

**Requisitos:**
- Type hints e docstrings (Google Style) em **todas** as funções
- Persistência em `alunos.json`
- Cada aluno: `id`, `nome`, `email`, `idade`, `notas` (lista de floats), `ativo` (bool)

**Funções obrigatórias:**
```python
def cadastrar_aluno(nome: str, email: str, idade: int, notas: list[float]) -> dict: ...
def listar_alunos() -> list[dict]: ...
def buscar_por_nome(nome: str) -> dict | None: ...
def calcular_media_turma() -> float: ...
def exportar_relatorio() -> None: ...
```

`exportar_relatorio` gera `relatorio_turma.json` com: total de alunos, média geral, aluno com maior média e aluno com menor média.

**Demonstração obrigatória:** cadastrar 4 alunos → listar → buscar um → exibir média → exportar relatório.

> 🏆 *Este exercício é o seu portfólio do Módulo 1. Capriche nos comentários e na organização!*

---

## 📊 Tabela Resumo dos Exercícios

| # | Tópico Principal | Nível | Dia |
|---|-----------------|-------|-----|
| 00 | Ambiente virtual, Python 3.12, `.gitignore` | ⚙️ | 1 |
| 01 | `print()` básico | 🟢 | 1 |
| 02 | Módulo `sys`, ambiente | 🟢 | 1 |
| 03 | Zen of Python, `import` | 🟢 | 1 |
| 04 | Comentários e docstrings | 🟡 | 1 |
| 05 | Leitura e correção de erros | 🟡 | 1 |
| 06 | Tipos de dados e `type()` | 🔴 | 1 |
| 07 | Variáveis, operadores aritméticos | 🟢 | 2 |
| 08 | Expressões matemáticas | 🟢 | 2 |
| 09 | `input()`, `int()`, f-string | 🟢 | 2 |
| 10 | Divisão inteira `//` e módulo `%` | 🟢 | 2 |
| 11 | Formatação avançada com f-strings | 🟡 | 2 |
| 12 | `input()`, `float()`, operadores | 🟡 | 2 |
| 13 | Operadores lógicos e de comparação | 🟡 | 2 |
| 14 | Troca de variáveis | 🟡 | 2 |
| 15 | Expressões com desconto | 🟡 | 2 |
| 16 | `math`, potência, raiz quadrada | 🔴 | 2 |
| 17 | Nota fiscal, `input()`, formatação | 🔴 | 2 |
| 18 | Conversão encadeada, alinhamento | 🔴 | 2 |
| 19 | Métodos de string | 🔴 | 2 |
| 20 | Juros simples, fórmulas | 🔴 | 2 |
| 21 | Funções + docstring básica | 🟢 | 2+ |
| 22 | Type hints básico | 🟢 | 2+ |
| 23 | `json.dumps()` / `json.loads()` | 🟢 | 2+ |
| 24 | Typing + docstring: conversor | 🟡 | 2+ |
| 25 | `json.dump()` / `json.load()` (arquivo) | 🟡 | 2+ |
| 26 | `Optional`, `Union` do typing | 🟡 | 2+ |
| 27 | JSON com múltiplos registros | 🟡 | 2+ |
| 28 | Docstring Google Style + juros compostos | 🟡 | 2+ |
| 29 | Parser de JSON de API | 🔴 | 2+ |
| 30 | `TypedDict` | 🔴 | 2+ |
| 31 | Mescla de JSONs | 🔴 | 2+ |
| 32 | Validador com Typing + Docstring | 🔴 | 2+ |
| 33 | Sistema de log em JSON | 🔴 | 2+ |
| 34 | Config de app via JSON | 🔴 | 2+ |
| 35 | Relatório de vendas: JSON + Typing | 🔴 | 2+ |
| 36 | Agenda CRUD em JSON | 🔴 | 2+ |
| 37 | Serialização customizada para JSON | 🔴 | 2+ |
| 38 | `Callable` e Generics | 🔴 | 2+ |
| 39 | Pipeline de dados | 🔴 | 2+ |
| 40 | Sistema de cadastro completo | 🔴 | 2+ |

---

*Bons estudos! Lembre-se: o melhor código é aquele que você entende quando relê amanhã. 🐍*
