# Sistema de Lançamento de Notas 📋

> **Curso de Capacitação em Desenvolvimento Full Stack — Programação em Python**
> Professor: Msc. Hygo Sousa De Oliveira | Instituto ITEAM

---

## Contexto do Problema

Uma escola precisa de um sistema simples para que professores possam **lançar as notas dos alunos por turma**. O sistema deve ser executado via terminal, pedir as informações uma a uma, validar cada entrada e salvar os dados em disco no formato JSON para consulta posterior.

Este projeto é o ponto de partida da sua jornada em desenvolvimento de software. Antes de escrever qualquer linha de código complexo, é fundamental aprender a **organizar o código em responsabilidades separadas** — cada arquivo faz apenas o que é seu papel. Essa ideia, que parece simples aqui, é a mesma que sustenta a Programação Orientada a Objetos que você estudará nos próximos módulos.

---

## Diagrama do Sistema

O diagrama abaixo mostra a **estrutura de pastas** do projeto e o **fluxo completo do programa**, desde a leitura da turma até o salvamento e exibição das notas. Leia-o com atenção antes de começar a codificar.

![Diagrama do Sistema de Lançamento de Notas](./img/diagrama_sistema_notas.png)

> 💡 **Dica:** Sempre que travar em algum `TODO`, volte ao diagrama e localize em qual etapa do fluxo você está. Isso vai ajudar a entender o que a função precisa receber, processar e retornar.

---

## Estrutura de Pastas

```
sistema_notas/
├── main.py              ← ponto de entrada; coordena todo o programa
├── README.md            ← este arquivo
├── funcoes/
│   ├── __init__.py      ← transforma a pasta em um pacote Python
│   ├── validacoes.py    ← funções que validam as entradas do usuário
│   └── arquivo.py       ← funções que salvam e leem os dados em JSON
└── notas/               ← pasta onde os arquivos .json serão criados
```

Cada arquivo tem **uma única responsabilidade**. Isso não é apenas organização — é o primeiro passo para escrever código profissional e reutilizável.

---

## O que o programa deve fazer

Ao ser executado, o programa deve seguir este roteiro:

1. Exibir uma mensagem de boas-vindas.
2. Pedir o **nome da turma** e validá-lo.
3. Entrar em um **loop principal** onde, para cada aluno:
   - Pede o **nome completo** do aluno (mínimo nome e sobrenome).
   - Pede as **3 notas** do aluno (valores entre `0.0` e `10.0`).
   - **Salva** os dados em um arquivo JSON na pasta `/notas`.
   - **Exibe** todos os registros daquela turma até o momento.
4. O programa encerra quando o usuário digitar `sair` em qualquer campo de texto.

### Exemplo de execução esperada

```
=============================================
  Sistema de Lançamento de Notas
  Digite 'sair' a qualquer momento para encerrar
=============================================

Nome da turma: Turma A

Nome do aluno (ou 'sair'): Maria Silva
Nota 1: 8.5
Nota 2: 7.0
Nota 3: 9.5

✔ Nota salva com sucesso!

─── Registros da Turma A ───────────────────
Aluno : Maria Silva
Nota 1: 8.5  |  Nota 2: 7.0  |  Nota 3: 9.5
Média : 8.33
────────────────────────────────────────────

Nome do aluno (ou 'sair'): sair

Encerrando o sistema. Até logo!
```

---

## Regras de Validação

| Campo       | Regras                                                                 |
|-------------|------------------------------------------------------------------------|
| Turma       | Não pode ser vazio. Não pode ser `"sair"`.                            |
| Aluno       | Não pode ser vazio. Não pode ser `"sair"`. Mínimo de 2 palavras.     |
| Nota        | Deve ser um número. Aceita vírgula como separador decimal. Entre `0.0` e `10.0`. |

---

## Sua tarefa: completar os `TODO`s

Os três arquivos de código possuem campos marcados com `# TODO` e instruções detalhadas em português dentro das docstrings. **Você não deve alterar os nomes das funções nem seus parâmetros** — apenas escrever o corpo de cada uma.

A ordem sugerida de implementação é:

### 1. `funcoes/validacoes.py`

Comece por aqui. As funções são independentes e fáceis de testar isoladamente.

- `validar_turma(nome_turma)` — retorna `True` ou `False`
- `validar_aluno(nome_aluno)` — retorna `True` ou `False`
- `validar_nota(valor_digitado)` — retorna `float` ou `None`

**Conceitos praticados:** condicionais `if/elif/else`, método `.strip()`, `.lower()`, `.split()`, bloco `try/except`, conversão de tipos.

### 2. `funcoes/arquivo.py`

Aqui você vai aprender a persistir dados em disco. Leia a docstring de cada função com atenção — a estrutura do JSON esperado está descrita lá.

- `salvar_nota(turma, aluno, nota1, nota2, nota3)` — salva ou atualiza o JSON
- `ler_notas(turma)` — lê o JSON e exibe os dados formatados

**Conceitos praticados:** `open()`, `json.load()`, `json.dump()`, `os.path.exists()`, `os.path.join()`, dicionários, listas.

### 3. `main.py`

Por último, integre tudo. As funções auxiliares `obter_turma()`, `obter_aluno()` e `obter_nota()` fazem loops de entrada com validação. A função `main()` orquestra o programa inteiro.

**Conceitos praticados:** `while True`, `break`, `return`, importação de módulos, fluxo de controle.

---

## Como executar o projeto

> **Pré-requisito:** Python 3.8 ou superior instalado.

Abra o terminal na pasta raiz do projeto (`sistema_notas/`) e execute:

```bash
python main.py
```

A pasta `notas/` já está criada. Os arquivos JSON serão gerados automaticamente dentro dela conforme você cadastrar turmas.

---

## Dica para testar suas funções antes de rodar tudo

Antes de rodar o `main.py` completo, você pode testar cada função individualmente. Por exemplo, abra o terminal Python interativo e faça:

```python
from funcoes.validacoes import validar_nota

print(validar_nota("7,5"))   # esperado: 7.5
print(validar_nota("11"))    # esperado: None
print(validar_nota("abc"))   # esperado: None
```

Isso vai ajudá-lo a encontrar erros mais cedo, sem precisar rodar o programa inteiro.

---

## Conexão com os próximos módulos

Ao completar este projeto, você terá praticado:

- Separação de responsabilidades entre módulos
- Validação de entrada do usuário
- Persistência de dados em JSON
- Controle de fluxo com loops e condicionais

No **nível intermediário**, você reescreverá este mesmo sistema usando **classes e objetos** — transformando `Aluno`, `Turma` e `GerenciadorDeNotas` em entidades do mundo real representadas no código. Você vai perceber que tudo o que aprendeu aqui se encaixa naturalmente dentro da Programação Orientada a Objetos.

---

*Instituto ITEAM — Paixão por Desenvolver Talentos*
