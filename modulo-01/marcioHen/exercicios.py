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
    print("Olá, Mundo!")
    print("Marcio Henrique")
    print("Python: simples, poderoso e elegante.")
---     

### 🟢 Exercício 02 – Inspecionando o Ambiente
Escreva um script que importe o módulo `sys` e exiba:
1. A versão do Python instalada (`sys.version`)
2. O sistema operacional em uso (`sys.platform`)

    sys.version
    sys.platform
---

### 🟢 Exercício 03 – O Zen na Prática
O **Zen of Python** pode ser acessado com `import this`.  
Escreva um script que:
1. Importe o módulo `this` para exibir o Zen.
2. Abaixo do import, adicione um comentário explicando com suas palavras **um** dos princípios que mais fez sentido para você.
    import this
---

### 🟡 Exercício 04 – Comentários como Documentação
Você recebeu o código abaixo **sem nenhum comentário**. Adicione comentários explicativos em cada linha e uma **docstring** no topo descrevendo o que o programa faz:

```python
nome = "Ana Lima" # EXIBE O NOME DO FUNCIONÁRIO
idade = 29 #EXIBE A IDADE
salario = 4500.00 #EXIBE O SALARIO
ativo = True #EXIBIR SE O FUNCIONÁRIO ESTÁ ATIVO OU NÃO
print(nome, idade, salario, ativo) #EXIBIÇÃO DOS DADOS DO FUNCIONÁRIO

```


---

### 🟡 Exercício 05 – Primeira Análise de Erro
O código abaixo contém **erros propositais**. Identifique-os, corrija-os e explique em comentários o que estava errado:

```python
Print("Bem-vindo ao curso de Python") # "Print" deve ser "print"
nome = "Carlos" # ASPAS
print("Aluno: " + nome)   
print("Curso de Python") # FALTA ASPAS
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
"São Paulo" → <class 'str'>
False → <class 'bool'>
None → <class 'NoneType'>
"" → <class 'str'>

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

    largura = 12.5
    comprimento = 30.0
    area = largura * comprimento
    print(f"Área do terreno: {area} m²")
---

### 🟢 Exercício 08 – Conversor de Temperatura
Escreva um script que converta uma temperatura de **Celsius para Fahrenheit** e para **Kelvin**.

Fórmulas:
- `F = (C × 9/5) + 32`
- `K = C + 273.15`

Use o valor `36.5°C` e exiba os três valores formatados.
    celsius = 36.5
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
print(f"Temperatura: {celsius}°C = {fahrenheit:.1f}°F = {kelvin:.2f}K")

---

### 🟢 Exercício 09 – Boas-vindas Personalizada
Escreva um script que:
1. Solicite ao usuário seu **nome** (`input()`)
2. Solicite sua **idade**
3. Exiba: `Olá, [nome]! Você tem [idade] anos e nasceu por volta de [ano_nascimento].`

> 💡 *`input()` sempre retorna string. Para cálculos, converta com `int()`.*
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: ")) 
ano_atual = 2025
ano_nascimento = ano_atual - idade
print(f"Olá, {nome}! Você tem {idade} anos e nasceu por volta de {ano_nascimento}.")
---

### 🟢 Exercício 10 – Divisão Inteira e Resto
Dado que um caminhão comporta **850 kg** e cada caixa pesa **32 kg**:
1. Calcule quantas caixas **completas** cabem (`//`)
2. Calcule o **peso restante** que não completa uma caixa (`%`)
3. Exiba os dois valores com mensagens claras

capacidade_caminhao = 850
peso_caixa = 32
caixas_completas = capacidade_caminhao // peso_caixa
peso_restante = capacidade_caminhao % peso_caixa
print(f"Caixas completas que cabem: {caixas_completas}")
print(f"Peso restante no caminhão: {peso_restante} kg")

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

nome = "Mariana Souza"
cargo = "Analista de Dados"
salario = 7850.50
anos = 3
print("=" * 29)
print("     FICHA DO FUNCIONÁRIO    ")
print("=" * 29)
print(f"Nome   : {nome}")
print(f"Cargo  : {cargo}")
print(f"Salário: R$ {salario:,.2f}".replace(",", "
X").replace(".", ",").replace("X", "."))
print(f"Tempo  : {anos} ano(s) de empresa")
print("=" * 29)

---

### 🟡 Exercício 12 – Calculadora de IMC
Fórmula: `IMC = peso / altura²`

Solicite **peso** (kg) e **altura** (m) via `input()`, calcule o IMC e exiba com 2 casas decimais e mensagem informativa.

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / altura**2
print(f"Seu IMC é: {imc:.2f}")


---

### 🟡 Exercício 13 – Operadores Lógicos e de Comparação
Sem usar `if`, armazene dois números e use `print()` para responder (True/False):
1. O primeiro número é maior que o segundo?
2. Os dois são iguais?
3. Ambos são positivos?
4. Pelo menos um é maior que 100?
5. O primeiro é diferente de zero?

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print(f"O primeiro número é maior que o segundo? {num1 > num2}")
print(f"Os dois são iguais? {num1 == num2}")
print(f"Ambos são positivos? {num1 > 0 and num2 > 0}")
print(f"Pelo menos um é maior que 100? {num1 > 100 or
    num2 > 100}")
print(f"O primeiro é diferente de zero? {num1 != 0}")

---

### 🟡 Exercício 14 – Troca de Variáveis
Corrija o código abaixo de **duas formas**: com variável auxiliar e com o método idiomático do Python:

```python
a = 10
b = 20

c = a
a = b
b = c
print(a, b)


a, b = b, a
print(a, b)

```
    
---

### 🟡 Exercício 15 – Calculadora de Desconto
Uma loja aplica 10% de desconto em todas as compras.  
Peça o **valor da compra**, calcule o desconto e valor final, exibindo tudo formatado em reais.

> 💡 *Não use `if` ainda — calcule diretamente com os operadores que você conhece.*
valor_compra = float(input("Digite o valor da compra: R$ "))
desconto = valor_compra * 0.10
valor_final = valor_compra - desconto
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto (10%): R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")

---

### 🔴 Exercício 16 – Distância entre Dois Pontos
Fórmula: `d = √((x2 - x1)² + (y2 - y1)²)`

Defina `P1 = (3, 4)` e `P2 = (7, 1)`, calcule a distância com `math.sqrt` e exiba com 4 casas decimais.
import math
x1, y1 = 3, 4   
x2, y2 = 7, 1
distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"A distância entre P1 e P2 é: {distancia:.4f}")

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
descricao = input("Descrição do produto: ")
quantidade = int(input("Quantidade: "))
preco_unitario = float(input("Preço unitário: R$ "))
subtotal = quantidade * preco_unitario
imposto = subtotal * 0.12
total = subtotal + imposto
print("===== NOTA FISCAL =====")
print(f"Produto   : {descricao}")
print(f"Quantidade: {quantidade} unidade(s)")
print(f"Preço Unit: R$ {preco_unitario:.2f}")
print(f"Subtotal  : R$ {subtotal:.2f}")
print(f"Imposto   : R$ {imposto:.2f}")
print(f"Total     : R$ {total:.2f}")

---

### 🔴 Exercício 18 – Conversão de Unidades Encadeada
Solicite uma distância em **metros** e converta para: km, cm, mm, polegadas e pés. Exiba em tabela formatada com alinhamento usando f-strings.
metros = float(input("Digite a distância em metros: "))
km = metros / 1000
cm = metros * 100
mm = metros * 1000
polegadas = metros * 39.3701
pes = metros * 3.28084
print(f"{'Unidade':<12} {'Valor':>10}")
print(f"{'-'*22}")
print(f"{'Metros':<12} {metros:>10.2f}")
print(f"{'Km':<12} {km:>10.3f}")
print(f"{'Cm':<12} {cm:>10.2f}")
print(f"{'Mm':<12} {mm:>10.2f}")
print(f"{'Polegadas':<12} {polegadas:>10.2f}")
print(f"{'Pés':<12} {pes:>10.2f}")

---

### 🔴 Exercício 19 – Manipulação de Strings no Mundo Real
Você recebeu um e-mail mal formatado: `"   joao.silva@EMPRESA.com.br   "`

Escreva um script que:
1. Remova espaços extras (`.strip()`)
2. Normalize para minúsculas (`.lower()`)
3. Extraia o **usuário** (parte antes do `@`)
4. Extraia o **domínio** (parte depois do `@`)
5. Exiba cada resultado com uma label clara

email = "   joao.silva@EMPRESA.com.br   "
email = email.strip().lower()
usuario = email.split("@")[0]
dominio = email.split("@")[1]
print(f"Email: {email}")
print(f"Usuário: {usuario}")
print(f"Domínio: {dominio}")

---

### 🔴 Exercício 20 – Calculadora de Investimento Simples
Solicite: capital inicial, taxa de juros ao mês (%) e período em meses.

Fórmula: `M = C × (1 + i × t)`

Exiba capital, taxa, período, juros totais e montante final formatados.

capital = float(input("Capital inicial (R$): "))
taxa_juros = float(input("Taxa de juros mensal (%): "))
periodo = int(input("Período (meses): "))
juros_totais = capital * (taxa_juros / 100) * periodo
montante_final = capital + juros_totais
print(f"Capital inicial: R$ {capital:.2f}")
print(f"Taxa de juros: {taxa_juros:.2f}% ao mês")
print(f"Período: {periodo} meses")
print(f"Juros totais: R$ {juros_totais:.2f}")
print(f"Montante final: R$ {montante_final:.2f}")

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
    return f"Olá, {nome}! Seja bem-vinda ao curso."
print(saudacao("Ana"))
print(saudacao("Carlos"))
print(saudacao("Mariana"))


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


```
> 💡 *Sintaxe: `def funcao(param: tipo) -> tipo_retorno:`*
def calcular_area(largura: float, altura: float) -> float:
    return largura * altura

def formatar_nome(nome: str, sobrenome: str) -> str:
    return f"{nome} {sobrenome}".title()

def eh_maior_de_idade(idade: int) -> bool:
    return idade >= 18

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
import json
aluno_json = json.dumps(aluno, indent=2)
aluno_dict = json.loads(aluno_json)
nome = aluno_dict["nome"]
media_notas = sum(aluno_dict["notas"]) / len(aluno_dict["notas"])
print(f"Nome: {nome}")
print(f"Média das notas: {media_notas:.2f}")


---

### 🟡 Exercício 24 – Função Documentada com Typing: Conversor de Moeda
Escreva a função `converter_moeda` com type hints completos, docstring com `Args`, `Returns` e `Example`, que converta um valor em reais para dólar e euro.

Cotações: `1 USD = 5.15 BRL` | `1 EUR = 5.58 BRL`

A função deve retornar uma **tupla** `(valor_usd, valor_eur)`.
def converter_moeda(valor_brl: float) -> tuple[float, float]:
    """
    Converte um valor em reais para dólar e euro.
    Args:
        valor_brl (float): Valor em reais a ser convertido.
    Returns:
        tuple[float, float]: Uma tupla contendo o valor convertido em dólar e euro, respectivamente.
    Example:
        >>> converter_moeda(100)
        (19.42, 17.92)
    """
    cotacao_usd = 5.15
    cotacao_eur = 5.58
    valor_usd = valor_brl / cotacao_usd
    valor_eur = valor_brl / cotacao_eur
    return valor_usd, valor_eur
valor_brl = float(input("Digite o valor em reais: R$ "))
valor_usd, valor_eur = converter_moeda(valor_brl)
print(f"Valor em dólares: ${valor_usd:.2f}")
print(f"Valor em euros: €{valor_eur:.2f}")

---

### 🟡 Exercício 25 – Salvando Dados em JSON
Escreva um script que:
1. Crie um dicionário de **produto de e-commerce**: `id`, `nome`, `preco`, `estoque`, `disponivel`, `categorias` (lista)
2. Salve em `produto.json` com `json.dump()` e indentação
3. Leia o arquivo de volta e exiba cada campo com uma label

> 💡 *Use `open("produto.json", "w") as f` para escrita e `"r"` para leitura.*
import json
produto = {
    "id": 101,
    "nome": "Smartphone XYZ",
    "preco": 1999.99,
    "estoque": 50,
    "disponivel": True,
    "categorias": ["Eletrônicos", "Mobile", "Gadgets"]
}
with open("produto.json", "w") as f:
    json.dump(produto, f, indent=2)
with open("produto.json", "r") as f:
    produto_lido = json.load(f)
print(f"ID: {produto_lido['id']}")
print(f"Nome: {produto_lido['nome']}")
print(f"Preço: R$ {produto_lido['preco']:.2f}")
print(f"Estoque: {produto_lido['estoque']} unidades")
print(f"Disponível: {'Sim' if produto_lido['disponivel'] else 'Não'}")
print(f"Categorias: {', '.join(produto_lido['categorias'])}")

---

### 🟡 Exercício 26 – Typing com `Optional` e `Union`
Escreva a função `buscar_usuario` que:
- Receba um `id` (int) e um `nome` que pode ser `str` **ou** `None`
- Retorne um dicionário com os dados ou `None` se o id for negativo
- Use `Optional` e `Union` do módulo `typing`
- Tenha docstring completa
from typing import Optional, Union
def buscar_usuario(id: int, nome: Optional[str] = None) -> Optional[Union[dict, None]]:
    """
      Busca um usuário por ID e nome.
      Args:
          id (int): O ID do usuário a ser buscado. Deve ser um número inteiro positivo.
          nome (Optional[str]): O nome do usuário a ser buscado. Pode ser uma string ou None.   
    """
---

### 🟡 Exercício 27 – JSON com Múltiplos Registros
Escreva um script que:
1. Crie uma lista com **3 dicionários** de funcionários (nome, cargo, salário, departamento)
2. Salve em `funcionarios.json`
3. Leia e exiba em **tabela formatada**
4. Calcule e exiba o **salário médio** da equipe
import json
funcionarios = [
    {"nome": "Alice", "cargo": "Engenheira de Software", "salario": 12000.00, "departamento": "TI"},
    {"nome": "Bruno", "cargo": "Analista de Marketing", "salario": 8000.00, "departamento": "Marketing"},
    {"nome": "Carla", "cargo": "Gerente Financeira", "salario": 15000.00, "departamento": "Financeiro"}
]
with open("funcionarios.json", "w") as f:
    json.dump(funcionarios, f, indent=2)
with open("funcionarios.json", "r") as f:
    funcionarios_lidos = json.load(f)
print(f"{'Nome':<10} {'Cargo':<25} {'Salário':>10} {'Departamento':<15}")
print(f"{'-'*60}")
total_salarios = 0
for func in funcionarios_lidos:
    print(f"{func['nome']:<10} {func['cargo']:<25} R$ {func['salario']:>10.2f} {func['departamento']:<15}")
    total_salarios += func['salario']
media_salarios = total_salarios / len(funcionarios_lidos)
print(f"{'-'*60}")
print(f"Salário médio da equipe: R$ {media_salarios:.2f}")
   

---

### 🟡 Exercício 28 – Docstring Google Style + Juros Compostos
Reescreva a função abaixo com type hints e docstring no **padrão Google Style** (incluindo `Args`, `Returns`, `Raises` e `Example`):

```python
def calcular_juros_compostos(capital, taxa, periodo):
    return capital * (1 + taxa / 100) ** periodo
```

O campo `Raises` deve documentar o que acontece se `capital` ou `taxa` forem negativos.
def calcular_juros_compostos(capital: float, taxa: float, periodo: int) -> float:
    
    """
    Args:

        capital (float): O valor inicial investido. Deve ser um número positivo.
        taxa (float): A taxa de juros mensal em porcentagem. Deve ser um número positivo.
        periodo (int): O período do investimento em meses. Deve ser um número inteiro positivo.
    Returns:
        float: O montante final após a aplicação dos juros compostos.
    Raises:
        ValueError: Se o capital ou a taxa forem negativos, ou se o período for negativo.
    Example:
        >>> calcular_juros_compostos(1000, 5, 12)
        1795.8563260221306
    """
    if capital < 0:
        raise ValueError("O capital não pode ser negativo.")
    if taxa < 0:
        raise ValueError("A taxa de juros não pode ser negativa.")
    if periodo < 0:
        raise ValueError("O período não pode ser negativo.")
    return capital * (1 + taxa / 100) ** periodo

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
import json
resposta_api = json.loads(resposta_api)
print(f"Boletim Meteorológico - {resposta_api['cidade']}, {resposta_api['pais']}")
print(f"Temperatura Atual: {resposta_api['temperatura']['atual']}°C")
print(f"Temperatura Mínima: {resposta_api['temperatura']['minima']}°C")
print(f"Temperatura Máxima: {resposta_api['temperatura']['maxima']}°C")
print(f"Sensação Térmica: {resposta_api['temperatura']['sensacao']}°C")
print(f"Umidade: {resposta_api['umidade']}%")
print(f"Condição: {resposta_api['condicao']}")
print(f"Vento: {resposta_api['vento']['velocidade_kmh']} km/h, Direção: {resposta_api['vento']['direcao']}")
print(f"Última atualização: {resposta_api['atualizado_em']}")

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
import json
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
pedido_exemplo: Pedido = {
    "id_pedido": 12345,
    "cliente": "João Silva",
    "itens": [
        {"produto": "Notebook", "quantidade": 1, "preco_unitario": 3200.00},
        {"produto": "Mouse", "quantidade": 2, "preco_unitario": 89.90}
    ],
    "status": "Em processamento"
}
pedido_json = json.dumps(pedido_exemplo, indent=2)
print("Pedido de E-commerce:")
print(pedido_json)

---

### 🔴 Exercício 31 – Mesclando JSONs de Sistemas Diferentes
Mescle os dois dicionários abaixo em um único `funcionario_completo`, salve em JSON, leia e exiba formatado com a lista de habilidades numerada:

```python
cadastro = {"id": 1042, "nome": "Fernanda Costa", "email": "fernanda@empresa.com"}
perfil   = {"id": 1042, "cargo": "Engenheira de Software", "nivel": "Senior",
            "salario": 12500.00, "habilidades": ["Python", "Django", "PostgreSQL"]}
```
import json

cadastro = {
    "id": 1042,
    "nome": "Fernanda Costa",
    "email": "fernanda@empresa.com",
}
perfil = {
    "id": 1042,
    "cargo": "Engenheira de Software",
    "nivel": "Senior",
    "salario": 12500.00,
    "habilidades": ["Python", "Django", "PostgreSQL"],
}

funcionario_completo = cadastro | perfil

with open("funcionario_completo.json", "w", encoding="utf-8") as arquivo:
    json.dump(funcionario_completo, arquivo, indent=4, ensure_ascii=False)

with open("funcionario_completo.json", "r", encoding="utf-8") as arquivo:
    dados_carregados = json.load(arquivo)

print("========================================")
print("       PERFIL DO COLABORADOR            ")
print("========================================")
print(f"ID     : {dados_carregados['id']}")
print(f"Nome   : {dados_carregados['nome']}")
print(f"E-mail : {dados_carregados['email']}")
print(f"Cargo  : {dados_carregados['cargo']} ({dados_carregados['nivel']})")
print(f"Salário: R$ {dados_carregados['salario']:.2f}")
print("----------------------------------------")
print("Habilidades Técnicas:")

for indice, habilidade in enumerate(dados_carregados["habilidades"], start=1):
    print(f"  {indice}. {habilidade}")
print("========================================")



---

### 🔴 Exercício 32 – Validador de Cadastro com Typing
Escreva a função `validar_cadastro` com type hints e docstring completa:

```python
def validar_cadastro(nome: str, email: str, idade: int) -> bool:
    """
    Valida os dados de cadastro de um usuário.
    Args:
        nome (str): O nome completo do usuário. Deve conter pelo menos 3 caracteres.
        email (str): O endereço de e-mail do usuário. Deve conter "@" e ".".
        idade (int): A idade do usuário. Deve ser um número inteiro entre 18 e 120.
    Returns:
        bool: Retorna True se o cadastro for válido, caso contrário False.
    Example:
        >>> validar_cadastro("Ana Lima", "ana.lima@email.com", 25)
        True
    """
    if not (isinstance(nome, str) and len(nome) >= 3):
        return False
    if not (isinstance(email, str) and "@" in email and "." in email):
        return False
    if not (isinstance(idade, int) and 18 <= idade <= 120):
        return False
    return True
print(validar_cadastro("Ana Lima", "ana.lima@email.com", 25))
print(validar_cadastro("João", "joao.com", 17))
print(validar_cadastro("Maria", "maria@email", 30))

---

### 🔴 Exercício 33 – Sistema de Log em JSON
Implemente três funções (com type hints e docstrings) para um sistema de log:

```python
def registrar_evento(arquivo: str, nivel: str, mensagem: str) -> None: ...
def ler_logs(arquivo: str) -> list: ...
def filtrar_por_nivel(logs: list, nivel: str) -> list: ...
```

Use `datetime` para timestamps. Registre ao menos 5 eventos (`"INFO"`, `"WARNING"`, `"ERROR"`) e demonstre a filtragem.
import json
from datetime import datetime
def registrar_evento(arquivo: str, nivel: str, mensagem: str) -> None:
    """
    Registra um evento em um arquivo JSON de log.
    Args:
        arquivo (str): O caminho do arquivo de log onde o evento será registrado.
        nivel (str): O nível do evento (e.g., "INFO", "WARNING", "ERROR").
        mensagem (str): A mensagem descritiva do evento a ser registrado.
    Returns:
        None: Esta função não retorna nenhum valor. 
    Example:
        >>> registrar_evento("log.json", "INFO", "Sistema iniciado.")
    """
    evento = {
        "timestamp": datetime.now().isoformat(),
        "nivel": nivel,
        "mensagem": mensagem
    }
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []
    logs.append(evento)
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4, ensure_ascii=False)
def ler_logs(arquivo: str) -> list:
    """
    Lê os logs de um arquivo JSON.
    Args:
        arquivo (str): O caminho do arquivo de log a ser lido.
    Returns:
        list: Retorna uma lista de dicionários, onde cada dicionário representa um evento registrado no log.
    Example:
        >>> logs = ler_logs("log.json")
        >>> print(logs)
        [{'timestamp': '2025-01-15T14:30:00', 'nivel': 'INFO', 'mensagem': 'Sistema iniciado.'}]
    """
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def filtrar_por_nivel(logs: list, nivel: str) -> list:
    """
    Filtra os logs por um nível específico.
    Args:
        logs (list): Uma lista de dicionários representando os eventos registrados no log.
        nivel (str): O nível de log a ser filtrado (e.g., "INFO", "WARNING", "ERROR").
    Returns:
        list: Retorna uma lista de dicionários contendo apenas os eventos que correspondem ao nível especificado.
    Example:
        >>> logs = ler_logs("log.json")
        >>> erros = filtrar_por_nivel(logs, "ERROR")
        >>> print(erros)
        [{'timestamp': '2025-01-15T15:00:00', 'nivel': 'ERROR', 'mensagem': 'Falha na conexão com o banco de dados.'}]
    """
    return [log for log in logs if log["nivel"] == nivel]
registrar_evento("log.json", "INFO", "Sistema iniciado.")
registrar_evento("log.json", "WARNING", "Uso de memória acima de 80
%.")
registrar_evento("log.json", "ERROR", "Falha na conexão com o banco de dados.")
registrar_evento("log.json", "INFO", "Usuário 'admin' logou com sucesso.")
registrar_evento("log.json", "ERROR", "Erro ao processar a requisição.")
todos_logs = ler_logs("log.json")
erros = filtrar_por_nivel(todos_logs, "ERROR")
print("Eventos de nível ERROR:")
for erro in erros:
    print(f"{erro['timestamp']} - {erro['mensagem']}")

    
---

### 🔴 Exercício 34 – Configuração de Aplicação via JSON
1. Crie `config.json` com seções `app`, `banco` e `email`
2. Implemente `carregar_config(caminho: str) -> dict`
3. Implemente `obter_valor(config: dict, chave: str, padrao: any = None) -> any` que navegue por chaves aninhadas com notação de ponto (`"app.versao"` → `"1.0.0"`)
4. Demonstre com 5 chamadas diferentes

    import json
def carregar_config(caminho: str) -> dict:
    """
    Carrega a configuração de um arquivo JSON.
    Args:
        caminho (str): O caminho do arquivo JSON de configuração a ser carregado.
    Returns:

        dict: Retorna um dicionário contendo as configurações carregadas do arquivo JSON.
    Example:
        >>> config = carregar_config("config.json")
        >>> print(config)
        {'app': {'nome': 'MinhaApp', 'versao': '1.0.0'}, 'banco': {'host': 'localhost', 'porta': 5432}, 'email': {'smtp': 'smtp.empresa.com', 'porta': 587}}
    """
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)
def obter_valor(config: dict, chave: str, padrao: any = None) -> any:
    """
    Obtém um valor de configuração a partir de uma chave aninhada.
    Args:
        config (dict): O dicionário de configuração carregado.
        chave (str): A chave aninhada no formato de ponto (e.g., "app.versao").
        padrao (any, optional): O valor padrão a ser retornado se a chave não for encontrada. Padrão é None.
    Returns:
        any: Retorna o valor correspondente à chave especificada ou o valor padrão se a chave não for encontrada.
    Example:
        >>> config = carregar_config("config.json")
        >>> obter_valor(config, "app.versao")
        '1.0.0'
        >>> obter_valor(config, "banco.host")
        'localhost'
        >>> obter_valor(config, "email.smtp")
        'smtp.empresa.com'
        >>> obter_valor(config, "app.nome")
        'MinhaApp'
        >>> obter_valor(config, "app.descricao", "Sem descrição")
        'Sem descrição'
    """
    chaves = chave.split(".")
    valor = config
    for k in chaves:
        if isinstance(valor, dict) and k in valor:
            valor = valor[k]
        else:
            return padrao
    return valor
config = carregar_config("config.json")
print(obter_valor(config, "app.versao"))
print(obter_valor(config, "banco.host"))
print(obter_valor(config, "email.smtp"))
print(obter_valor(config, "app.nome"))
print(obter_valor(config, "app.descricao", "Sem descrição"))

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

    # 1. `calcular_total_mes(vendas: list, mes: str) -> float`: Total de vendas em um mês específico
    # 2. `produto_mais_vendido(vendas: list) -> str`: Produto com maior quantidade vendida no período
    # 3. `receita_total(vendas: list) -> float`: Receita total gerada no período
import json

vendas = json.loads(vendas_json)
def calcular_total_mes(vendas: list, mes: str) -> float:
    """
    Calcula o total de vendas em um mês específico.
    Args:
        vendas (list): Uma lista de dicionários representando as vendas.
        mes (str): O nome do mês para o qual o total de vendas deve ser calculado.
    Returns:
        float: O total de vendas para o mês especificado.
    Example:
        >>> calcular_total_mes(vendas, "Janeiro")
        144895.00
    """
    total = 0.0
    for venda in vendas:
        if venda["mes"].lower() == mes.lower():
            total += venda["quantidade"] * venda["valor_unit"]
    return total
def produto_mais_vendido(vendas: list) -> str:
    """Determina o produto mais vendido no período.
    Args:
        vendas (list): Uma lista de dicionários representando as vendas.
    Returns:
        str: O nome do produto mais vendido.
    Example:
        >>> produto_mais_vendido(vendas)
        'Mouse'
    """
    vendas_por_produto = {}
    for venda in vendas:
        produto = venda["produto"]
        quantidade = venda["quantidade"]
        vendas_por_produto[produto] = vendas_por_produto.get(produto, 0) + quantidade
    produto_mais_vendido = max(vendas_por_produto, key=vendas_por_produto.get)
    return produto_mais_vendido
def receita_total(vendas: list) -> float:
    """
    Calcula a receita total gerada no período.
    Args:
        vendas (list): Uma lista de dicionários representando as vendas.
    Returns:
        float: A receita total gerada.
    Example:
        >>> receita_total(vendas)
        549895.00
    """
    receita = 0.0
    for venda in vendas:
        receita += venda["quantidade"] * venda["valor_unit"]
    return receita
total_janeiro = calcular_total_mes(vendas, "Janeiro")
produto_top = produto_mais_vendido(vendas)
receita = receita_total(vendas)
print(f"Total de vendas em Janeiro: R$ {total_janeiro:.2f}")
print(f"Produto mais vendido: {produto_top}")
print(f"Receita total no período: R$ {receita:.2f}")


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
import json
def adicionar_contato(nome: str, telefone: str, email: str) -> None:
    """Adiciona um contato à agenda.
    Args:
        nome (str): O nome do contato a ser adicionado.
        telefone (str): O número de telefone do contato.
        email (str): O endereço de e-mail do contato.
    Returns:
        None: Esta função não retorna nenhum valor. 
    Example:
        >>> adicionar_contato("Maria Silva", "11987654321", "maria.silva@email.com")
    """
    with open("contatos.json", "r") as f:
        contatos = json.load(f)
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    with open("contatos.json", "w") as f:
        json.dump(contatos, f)
def listar_contatos() -> list:
    """Lista todos os contatos da agenda.
    Returns:
        list: Retorna uma lista de dicionários, onde cada dicionário representa um contato na agenda.
    Example:
        >>> listar_contatos()
        [{'nome': 'Maria Silva', 'telefone': '11987654321', 'email': 'maria.silva@email.com'}]
    """
    with open("contatos.json", "r") as f:
        return json.load(f)
def buscar_contato(nome: str) -> dict | None:
 

    with open("contatos.json", "r") as f:
        contatos = json.load(f)
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            return contato
    return None
def remover_contato(nome: str) -> bool:
    with open("contatos.json", "r") as f:
        contatos = json.load(f)
    for i, contato in enumerate(contatos):
        if contato["nome"].lower() == nome.lower():
            del contatos[i]
            with open("contatos.json", "w") as f:
                json.dump(contatos, f)
            return True
    return False
adicionar_contato("Maria Silva", "11987654321", "maria.silva@email.com")
adicionar_contato("João Souza", "11987654322", "joao.souza@email.com")
adicionar_contato("Ana Costa", "11987654323", "ana.costa@email.com")
print("Contatos adicionados.")

print("\nLista de contatos:")
for contato in listar_contatos():
    print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")

print("\nBuscando contato 'Maria Silva':")
contato = buscar_contato("Maria Silva")
if contato:
    print(f"Contato encontrado: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")

print("\nRemovendo contato 'Maria Silva':")
if remover_contato("Maria Silva"):
    print("Contato removido com sucesso.")
else:
    print("Contato não encontrado.")
print("\nLista de contatos após remoção:")
for contato in listar_contatos():
    print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")



---

### 🔴 Exercício 37 – Serialização Customizada de Objetos para JSON
O `json` nativo não serializa objetos Python. Escreva:
1. Uma classe `Produto` com `nome`, `preco` e `criado_em` (datetime)
2. `produto_para_dict(produto: 'Produto') -> dict` (converte datetime para ISO string)
3. `dict_para_produto(dados: dict) -> 'Produto'` (converte de volta)
4. Serialize uma lista de 3 produtos e desserialize de volta

> 💡 *Use `datetime.isoformat()` e `datetime.fromisoformat()`.*
import json
from datetime import datetime
class Produto:
    def __init__(self, nome: str, preco: float, criado_em: datetime):
        self.nome = nome
        self.preco = preco
        self.criado_em = criado_em
def produto_para_dict(produto: 'Produto') -> dict:
    return {
        "nome": produto.nome,
        "preco": produto.preco,
        "criado_em": produto.criado_em.isoformat()
    }
def dict_para_produto(dados: dict) -> 'Produto':
    return Produto(
        nome=dados["nome"],
        preco=dados["preco"],
        criado_em=datetime.fromisoformat(dados["criado_em"])
    )
produtos = [
    Produto("Notebook", 3200.00, datetime(2025, 1, 15, 10, 30)),
    Produto("Mouse", 89.90, datetime(2025, 1, 16, 11, 45)),
    Produto("Teclado", 149.90, datetime(2025, 1, 17, 9, 15))
]
produtos_dict = [produto_para_dict(p) for p in produtos]
produtos_json = json.dumps(produtos_dict, indent=2)
print("Produtos serializados em JSON:")
print(produtos_json)
produtos_dict_carregados = json.loads(produtos_json)
produtos_carregados = [dict_para_produto(d) for d in produtos_dict_carregados]
print("\nProdutos desserializados:")
for p in produtos_carregados:
    print(f"Nome: {p.nome}, Preço: R$ {p.preco:.2f}, Criado em: {p.criado_em}")

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

from typing import TypeVar, List, Callable
T = TypeVar('T')
R = TypeVar('R')
def aplicar_transformacao(dados: List[T], funcao: Callable[[T], R]) -> List[R]:
    """
    Aplica uma função de transformação a cada elemento de uma lista.
    Args:
        dados (List[T]): Uma lista de elementos do tipo T a serem transformados.
        funcao (Callable[[T], R]): Uma função que recebe um elemento do tipo T e retorna um elemento do tipo R.
    Returns:
        List[R]: Retorna uma nova lista contendo os resultados da aplicação da função a cada elemento da lista original.
    Example:
        >>> aplicar_transformacao(["maçã", "banana", "laranja"], str.upper)
        ['MAÇÃ', 'BANANA', 'LARANJA']
        >>> aplicar_transformacao([3.14159, 2.71828, 1.61803], lambda x: round(x, 2))
        [3.14, 2.72, 1.62]
        >>> aplicar_transformacao([{"nome": "Alice"}, {"nome": "Bob"}], lambda d: d["nome"])
        ['Alice', 'Bob']
    """
    return [funcao(item) for item in dados]

strings = ["maçã", "banana", "laranja"]
strings_maiusculas = aplicar_transformacao(strings, str.upper)
print("Strings em maiúsculas:", strings_maiusculas)
floats = [3.14159, 2.71828, 1.61803]
floats_arredondados = aplicar_transformacao(floats, lambda x: round(x, 2))
print("Floats arredondados:", floats_arredondados)
dicionarios = [{"nome": "Alice"}, {"nome": "Bob"}]
nomes = aplicar_transformacao(dicionarios, lambda d: d["nome"])
print("Nomes extraídos dos dicionários:", nomes)


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
import json
def carregar_dados(caminho: str) -> list[dict]:
   
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)
def normalizar_dados(dados: list[dict]) -> list[dict]:
    for cliente in dados:
        cliente["nome"] = cliente["nome"].strip().title()
        cliente["email"] = cliente["email"].lower()
        cliente["telefone"] = f"({cliente['telefone'][:2]}) {cliente['telefone'][2:7]}-{cliente['telefone'][7:]}"
    return dados    
def enriquecer_dados(dados: list[dict]) -> list[dict]:
    for cliente in dados:
        cliente["dominio_email"] = cliente["email"].split("@")[-1]
    return dados
def exportar_resultado(dados: list[dict], caminho: str) -> None:
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
clientes = carregar_dados("clientes.json")
clientes_normalizados = normalizar_dados(clientes)
clientes_enriquecidos = enriquecer_dados(clientes_normalizados)
exportar_resultado(clientes_enriquecidos, "clientes_tratados.json")




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
import json


def cadastrar_aluno(
    nome: str, email: str, idade: int, notas: list[float]
) -> dict:
    """Cadastra um novo aluno e salva no arquivo JSON.

    Args:
        nome (str): O nome completo do aluno. Deve conter pelo menos 3
          caracteres.
        email (str): O endereço de e-mail do aluno. Deve conter "@" e ".".
        idade (int): A idade do aluno. Deve ser um número inteiro entre 18 e
          120.
        notas (list[float]): Uma lista de notas do aluno, onde cada nota deve
          se um número entre 0 e 10.

    Returns:
        dict: Retorna um dicionário representando o aluno cadastrado, incluindo
        um ID gerado automaticamente.

    Example:
        >>> cadastrar_aluno("Carlos Silva", "carlos.silva@email.com", 20, [8.5,
        9.0, 7.5])
        {'id': 1, 'nome': 'Carlos Silva', 'email': 'carlos.silva@email.com',
        'idade': 20, 'notas': [8.5, 9.0, 7.5], 'ativo': True}
    """
    alunos = listar_alunos()

    novo_id = max([aluno["id"] for aluno in alunos], default=0) + 1
    aluno = {
        "id": novo_id,
        "nome": nome.strip().title(),
        "email": email.lower(),
        "idade": idade,
        "notas": notas,
        "ativo": True,
    }
    alunos.append(aluno)

    with open("alunos.json", "w", encoding="utf-8") as f:
        json.dump(alunos, f, indent=4, ensure_ascii=False)
    return aluno


def listar_alunos() -> list[dict]:
    """Lista todos os alunos cadastrados.

    Returns:
        list[dict]: Retorna uma lista de dicionários, onde cada dicionário
        representa um aluno cadastrado.

    Example:
        >>> listar_alunos()
        [{'id': 1, 'nome': 'Carlos Silva', 'email': 'carlos.silva@email.com',
        'idade': 20, 'notas': [8.5, 9.0, 7.5], 'ativo': True}]
    """
    try:
        with open("alunos.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def buscar_por_nome(nome: str) -> dict | None:
    """Busca um aluno pelo nome.

    Args:
        nome (str): O nome do aluno a ser buscado. A busca é case-insensitive e
          ignora espaços extras.

    Returns:
        dict | None: Retorna um dicionário representando o aluno encontrado ou
        None se nenhum aluno corresponder ao nome fornecido.

    Example:
        >>> buscar_por_nome("Carlos Silva")
        {'id': 1, 'nome': 'Carlos Silva', 'email': 'carlos.silva@email.com',
        'idade': 20, 'notas': [8.5, 9.0, 7.5], 'ativo': True}
    """
    alunos = listar_alunos()
    for aluno in alunos:
        if aluno["nome"].lower() == nome.strip().lower():
            return aluno
    return None


def calcular_media_turma() -> float:
    """Calcula a média geral das notas de todos os alunos ativos.

    Returns:
        float: Retorna a média geral das notas dos alunos ativos. Se não houver
        alunos ativos, retorna 0.0.

    Example:
        >>> calcular_media_turma()
        8.33
    """
    alunos = listar_alunos()
    notas_ativas = [
        nota
        for aluno in alunos
        if aluno["ativo"]
        for nota in aluno["notas"]
    ]
    if notas_ativas:
        return sum(notas_ativas) / len(notas_ativas)
    return 0.0


def exportar_relatorio() -> None:
    """Gera um relatório da turma e salva em 'relatorio_turma.json'.

    O relatório inclui:
        - Total de alunos cadastrados
        - Média geral das notas dos alunos ativos
        - Aluno com a maior média de notas
        - Aluno com a menor média de notas

    Returns:
        None: Esta função não retorna nenhum valor, mas salva o relatório em um
        arquivo JSON.

    Example:
        >>> exportar_relatorio()
        (Gera o arquivo 'relatorio_turma.json' com as informações da turma)
    """
    alunos = listar_alunos()
    total_alunos = len(alunos)
    media_geral = calcular_media_turma()

    aluno_maior_media = max(
        alunos,
        key=lambda a: sum(a["notas"]) / len(a["notas"]) if a["notas"] else 0,
        default=None,
    )
    aluno_menor_media = min(
        alunos,
        key=lambda a: sum(a["notas"]) / len(a["notas"]) if a["notas"] else 0,
        default=None,
    )

    relatorio = {
        "total_alunos": total_alunos,
        "media_geral": media_geral,
        "aluno_maior_media": (
            aluno_maior_media["nome"] if aluno_maior_media else "N/A"
        ),
        "aluno_menor_media": (
            aluno_menor_media["nome"] if aluno_menor_media else "N/A"
        ),
    }

    with open("relatorio_turma.json", "w", encoding="utf-8") as f:
        json.dump(relatorio, f, indent=4, ensure_ascii=False)


with open("alunos.json", "w", encoding="utf-8") as f:
    json.dump([], f)

aluno1 = cadastrar_aluno(
    "Carlos Silva", "carlos.silva@gmail.com", 20, [8.5, 9.0, 7.5]
)
aluno2 = cadastrar_aluno("Ana Costa", "ana.costa@gmail.com", 19, [9.0, 9.5, 10.0])
aluno3 = cadastrar_aluno("João Souza", "joao.souza@gmail.com", 21, [6.0, 7.0, 6.5])
aluno4 = cadastrar_aluno("Maria Lima", "maria.lima@gmail.com", 20, [7.5, 8.0, 8.5])

print("Alunos cadastrados:")
for aluno in listar_alunos():
    print(
        f"ID: {aluno['id']}, Nome: {aluno['nome']}, Email: {aluno['email']}, Idade: {aluno['idade']}, Notas: {aluno['notas']}, Ativo: {aluno['ativo']}"
    )

print("\nBuscando aluno por nome 'Ana Costa':")
aluno_encontrado = buscar_por_nome("Ana Costa")
if aluno_encontrado:
    print(f"Aluno encontrado: {aluno_encontrado['nome']}")
else:
    print("Aluno não encontrado.")

media_turma = calcular_media_turma()
print(f"\nMédia geral da turma: {media_turma:.2f}")

exportar_relatorio()
print("\nRelatório da turma exportado para 'relatorio_turma.json'.")

    
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
