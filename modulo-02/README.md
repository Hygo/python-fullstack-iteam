# 🐍 Módulo 2 – Estruturas de Controle
**Curso de Capacitação em Desenvolvimento Full Stack – ITEAM**  
Professor: Msc. Hygo Sousa De Oliveira

---

## 📌 Como entregar sua solução

> Siga os passos abaixo **antes de começar a resolver os exercícios**.

### 1. Clone o repositório (só na primeira vez)
```bash
git clone https://github.com/Hygo/python-fullstack-iteam.git
cd python-fullstack-iteam
```

### 2. Crie sua pasta dentro de `alunos/`
```bash
# Substitua pelo seu nome, sem espaços e em minúsculas
mkdir -p alunos/seu_nome/modulo-02
```

Exemplo:
```bash
mkdir -p alunos/ana_beatriz/modulo-02
```

### 3. Copie o template para sua pasta
```bash
cp modulo-02/template_aluno.py alunos/seu_nome/modulo-02/exercicios.py
```

### 4. Resolva os exercícios no arquivo copiado

Abra `alunos/seu_nome/modulo-02/exercicios.py` no VS Code ou PyCharm e preencha cada função.

### 5. Suba para o GitHub
```bash
git add alunos/seu_nome/
git commit -m "feat: módulo 2 resolvido - seu_nome"
git push origin main
```

---

## 📊 Níveis dos exercícios

🟢 Básico — conceito direto  
🟡 Intermediário — combinação de conceitos  
🔴 Avançado — raciocínio fora da caixa

---

## 📅 Módulo 2 – Estruturas de Controle

> **Tópicos cobertos:** `if / elif / else` · `for` · `while` · `break / continue / pass` · `try / except / else / finally`

---

### 🟢 Exercício 01 – Classificador de Temperatura

Um sistema de monitoramento climático precisa categorizar temperaturas ambiente.

Escreva um programa que leia uma temperatura em Celsius e classifique conforme a tabela:

| Faixa | Classificação |
|-------|--------------|
| Abaixo de 0°C | ❄️ Congelante |
| 0°C a 14°C | 🥶 Frio |
| 15°C a 24°C | 😊 Agradável |
| 25°C a 34°C | ☀️ Quente |
| 35°C ou mais | 🔥 Muito quente |

**Saída esperada (exemplo):**
```
Temperatura: 28°C
Classificação: ☀️ Quente
```

> 💡 *Use `if / elif / else`. Lembre-se de converter o `input()` para `float()`.*

---

### 🟢 Exercício 02 – Validador de Acesso

Um sistema corporativo precisa validar credenciais antes de liberar acesso.

Implemente uma verificação com as seguintes regras:
- Usuário correto: `"admin"`
- Senha correta: `"iteam2025"`
- Se ambos estiverem corretos → `"✅ Acesso liberado. Bem-vindo!"`
- Se o usuário estiver correto mas a senha errada → `"❌ Senha incorreta."`
- Se o usuário estiver errado → `"❌ Usuário não encontrado."`

> 💡 *Pense na **ordem** das verificações. Testar o usuário antes da senha evita revelar informações desnecessárias.*

---

### 🟢 Exercício 03 – Tabuada Interativa

Escreva um programa que solicite um número inteiro ao usuário e exiba sua tabuada completa (de 1 a 10) usando um laço `for`.

**Saída esperada (para o número 7):**
```
=== Tabuada do 7 ===
7 x  1 =  7
7 x  2 = 14
...
7 x 10 = 70
```

> 💡 *Use f-string com alinhamento: `{resultado:>3}` alinha o número à direita em 3 caracteres.*

---

### 🟢 Exercício 04 – Contador Regressivo

Sistemas de lançamento e cronômetros usam contagem regressiva. Escreva um programa com `while` que:
1. Solicite um número inteiro positivo ao usuário
2. Faça a contagem regressiva até 0, exibindo cada número
3. Ao chegar em 0, exiba `"🚀 Lançamento!"`

**Saída esperada (para 5):**
```
5... 4... 3... 2... 1... 0...
🚀 Lançamento!
```

> 💡 *Tudo pode sair na mesma linha usando `print(n, end=" ")`.*

---

### 🟢 Exercício 05 – Buscador com `break`

Em sistemas de busca, paramos assim que encontramos o que procuramos.

Dada a lista abaixo, escreva um `for` que percorra os produtos e pare (usando `break`) assim que encontrar `"Monitor"`, exibindo em qual posição ele foi encontrado:

```python
estoque = ["Teclado", "Mouse", "Webcam", "Monitor", "Headset", "Notebook"]
```

Se não encontrar, exiba `"Produto não encontrado no estoque."`.

> 💡 *Use uma variável `encontrado = False` antes do loop e altere-a quando achar o item.*

---

### 🟡 Exercício 06 – Filtro de Dados com `continue`

Em pipelines de dados, é comum ignorar registros inválidos durante o processamento.

Dada a lista abaixo (que mistura números e `None`), use `continue` para pular os valores `None` e calcule:
- A **soma** dos valores válidos
- A **média** dos valores válidos
- O **total de registros ignorados**

```python
leituras = [12.5, None, 8.3, None, 15.0, 9.7, None, 11.2, 6.8, None]
```

---

### 🟡 Exercício 07 – Validação de Entrada com `while`

Sistemas robustos não aceitam dados inválidos silenciosamente — eles continuam pedindo até receber uma entrada válida.

Escreva um programa que solicite a nota de um aluno repetidamente até que o valor seja válido (entre 0.0 e 10.0), depois exiba o conceito:

| Nota | Conceito |
|------|---------|
| 9.0 a 10.0 | A – Excelente |
| 7.0 a 8.9 | B – Bom |
| 5.0 a 6.9 | C – Regular |
| Abaixo de 5.0 | D – Insuficiente |

> 💡 *O `while True` com `break` quando a entrada for válida é um padrão clássico para validação.*

---

### 🟡 Exercício 08 – Calculadora com `try/except`

Escreva uma calculadora simples que:
1. Solicite dois números e uma operação (`+`, `-`, `*`, `/`)
2. Trate os seguintes erros:
   - `ValueError`: se o usuário digitar algo que não é número
   - `ZeroDivisionError`: se tentar dividir por zero
   - Operação inválida: se o símbolo não for um dos quatro aceitos
3. Use o bloco `else` para exibir o resultado (executado só quando não há exceção)
4. Use `finally` para sempre exibir `"Calculadora encerrada."`

> 💡 *O bloco `else` do `try` é executado apenas quando **nenhuma** exceção ocorre — ideal para separar o resultado do tratamento de erro.*

---

### 🟡 Exercício 09 – Padrão Numérico com `for` aninhado

Escreva um programa que gere o padrão abaixo usando dois `for` aninhados:

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

**Desafio extra 🔴:** gere também o triângulo invertido logo abaixo:
```
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
```

> 💡 *Use `print(..., end=" ")` dentro do loop interno e `print()` vazio para quebrar a linha ao final de cada linha do padrão.*

---

### 🟡 Exercício 10 – Jogo de Adivinhação

Implemente um mini-jogo onde o computador "pensa" em um número entre 1 e 100 e o usuário tenta adivinhar:

- A cada tentativa errada, diga se o número secreto é maior ou menor
- Limite as tentativas a **7 rounds** (use `while` com contador)
- Se acertar: `"🎉 Parabéns! Você acertou em X tentativas."`
- Se esgotar as tentativas: `"💀 Game over! O número era Y."`

```python
import random
numero_secreto = random.randint(1, 100)
```

> 💡 *7 tentativas não é aleatório — é o número mínimo necessário para encontrar qualquer número entre 1 e 100 com busca binária. Pesquise sobre isso!*

---

### 🔴 Exercício 11 – Verificador de Número Primo

Um número primo é divisível apenas por 1 e por ele mesmo. Escreva um programa que:
1. Solicite um número inteiro positivo
2. Verifique se é primo
3. Use `break` para sair do loop assim que encontrar um divisor
4. Trate com `try/except` a entrada de valores não numéricos ou negativos

**Dica de otimização:** você só precisa verificar divisores até `√n` (use `n ** 0.5`). Por quê? Pense nisso!

**Saída esperada:**
```
Digite um número: 17
17 é um número primo. ✅

Digite um número: 18
18 não é primo. Divisível por 2. ❌
```

---

### 🔴 Exercício 12 – Analisador de Senha Forte

Sistemas de segurança exigem senhas robustas. Escreva um verificador que analise uma senha e retorne um relatório completo.

**Critérios obrigatórios:**
- Mínimo de 8 caracteres
- Pelo menos 1 letra maiúscula
- Pelo menos 1 letra minúscula  
- Pelo menos 1 dígito numérico
- Pelo menos 1 caractere especial: `!@#$%^&*`

Use `for` para percorrer os caracteres e variáveis booleanas para rastrear cada critério. Exiba quais critérios foram atendidos e quais não foram.

**Saída esperada (para `"Python@2025"`):**
```
Analisando: Python@2025
✅ Comprimento adequado (11 caracteres)
✅ Contém maiúscula
✅ Contém minúscula
✅ Contém número
✅ Contém caractere especial
🔒 Senha FORTE!
```

---

### 🔴 Exercício 13 – Simulador de Caixa Eletrônico

Simule o saque de um caixa eletrônico que trabalha com cédulas de R$200, R$100, R$50, R$20 e R$10.

O programa deve:
1. Solicitar o valor do saque (múltiplo de 10, máximo R$3.000)
2. Usar `while` e `//` para calcular o menor número de cédulas
3. Tratar com `try/except` valores não numéricos
4. Tratar com `if/else` valores que não são múltiplos de 10 ou excedem o limite

**Saída esperada (para R$380):**
```
💵 Saque: R$ 380
Cédulas utilizadas:
  R$200 → 1 cédula(s)
  R$100 → 1 cédula(s)
  R$50  → 1 cédula(s)
  R$20  → 1 cédula(s)
  R$10  → 1 cédula(s)
Total de cédulas: 5
```

---

### 🔴 Exercício 14 – Leitura de Múltiplos Dados com Tratamento de Erros

Escreva um programa que leia as notas de uma turma com as seguintes regras:
1. O usuário digita as notas uma por uma (entre 0 e 10)
2. Para encerrar, digita `"fim"` (use `break`)
3. Notas inválidas (fora do intervalo ou não numéricas) devem ser ignoradas com `continue` e uma mensagem de aviso
4. Use `try/except` para tratar entradas não numéricas
5. Ao encerrar, exiba: total de notas válidas, média, maior nota e menor nota

**Dica:** use `pass` para estruturar o bloco de tratamento de erro enquanto está desenvolvendo.

---

### 🔴 Exercício 15 – Desafio Final: Simulador de Menu de Sistema

Crie um sistema de menu interativo completo que permaneça ativo até o usuário escolher sair:

```
=============================
   SISTEMA ITEAM - MENU    
=============================
[1] Conversor de temperatura
[2] Verificador de número primo
[3] Analisador de senha
[4] Calculadora segura
[0] Sair
=============================
```

**Requisitos técnicos:**
- `while True` para manter o menu ativo
- `if/elif/else` para rotear as opções
- `try/except` em toda entrada do usuário
- `break` para encerrar quando o usuário escolher `0`
- `continue` para ignorar opções inválidas com mensagem de aviso
- Cada funcionalidade pode ser simplificada (não precisa reimplementar tudo dos exercícios anteriores)

> 🏆 *Este exercício integra todos os conceitos do Módulo 2. Um menu bem implementado é a base de qualquer CLI (Command Line Interface) profissional.*

---

## 📊 Tabela Resumo

| # | Conceito Principal | Nível |
|---|--------------------|-------|
| 01 | `if / elif / else` | 🟢 |
| 02 | `if` aninhado, lógica de validação | 🟢 |
| 03 | `for` + `range()` | 🟢 |
| 04 | `while` + contador | 🟢 |
| 05 | `for` + `break` | 🟢 |
| 06 | `for` + `continue` + `None` | 🟡 |
| 07 | `while True` + validação de entrada | 🟡 |
| 08 | `try/except/else/finally` | 🟡 |
| 09 | `for` aninhado + padrões | 🟡 |
| 10 | `while` + `random` + lógica de jogo | 🟡 |
| 11 | `for` + `break` + `try/except` + otimização | 🔴 |
| 12 | `for` + booleanos + análise de string | 🔴 |
| 13 | `while` + `if/else` + `try/except` | 🔴 |
| 14 | `while` + `break` + `continue` + `try/except` | 🔴 |
| 15 | Integração completa do Módulo 2 | 🔴 |

---

*Bons estudos! Lembre-se: errar faz parte — o `try/except` existe exatamente pra isso. 🐍*
