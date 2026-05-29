### 🔴 Exercício 06 – Explorando Tipos com `type()`
# Escreva um script que crie **6 variáveis** com os seguintes valores e tipos:
# - Um número inteiro representando o ano atual - ✅
# - Um número de ponto flutuante representando uma temperatura em Celsius
# - Uma string com o nome de uma cidade brasileira
# - Um booleano indicando se está chovendo
# - O valor especial `None` atribuído a uma variável chamada `previsao`
# - Uma string vazia
# Para cada variável, exiba o **valor** e seu **tipo** com `type()`.
# Formato de saída esperado:
# ```
# 2025 → <class 'int'>
# 28.5 → <class 'float'>
# ...
# ```

from datetime import date

ano_atual = date.today().year
print(f"{ano_atual} → {type(ano_atual)}") # Vai retornar 2026

print("-------------------------------------------------------------------")
temperatura_celsius = 28.5
print(f"{temperatura_celsius}°C → {type(temperatura_celsius)}")

print("-------------------------------------------------------------------")
cidade_brasileira = "Boa Vista"
print(f"{cidade_brasileira} → {type(cidade_brasileira)}")

print("-------------------------------------------------------------------")
está_chovendo = False
print(f"Temos chuva? {está_chovendo} → {type(está_chovendo)}")

print("-------------------------------------------------------------------")
previsao = None
print(f"{previsao} → {type(previsao)}")

print("-------------------------------------------------------------------")
string_vazia = ""
print(f"{string_vazia} → {type(string_vazia)}")
