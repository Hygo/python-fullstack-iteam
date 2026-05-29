### 🔴 Exercício 19 – Manipulação de Strings no Mundo Real
# E-mail mal formatado recebido: "   joao.silva@EMPRESA.com.br   "
# 1. Remova espaços extras (.strip())
# 2. Normalize para minúsculas (.lower())
# 3. Extraia o usuário (parte antes do @)
# 4. Extraia o domínio (parte depois do @)
# 5. Exiba cada resultado com uma label clara

email_bruto = "   joao.silva@EMPRESA.com.br   "

email_sem_espacos = email_bruto.strip()
email_normalizado = email_sem_espacos.lower()
usuario = email_normalizado.split("@")[0]
dominio = email_normalizado.split("@")[1]

print(f"E-mail original  : '{email_bruto}'")
print(f"Sem espaços      : '{email_sem_espacos}'")
print(f"Normalizado      : '{email_normalizado}'")
print(f"Usuário          : '{usuario}'")
print(f"Domínio          : '{dominio}'")
