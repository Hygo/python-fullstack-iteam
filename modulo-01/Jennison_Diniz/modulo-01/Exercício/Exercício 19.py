# E-mail original mal formatado
email_bruto = "   joao.silva@EMPRESA.com.br   "

# 1. Removendo espaços extras no início e no fim
email_limpo = email_bruto.strip()

# 2. Convertendo todo o texto para letras minúsculas
email_normalizado = email_limpo.lower()

# 3. Extraindo o usuário e o domínio
# O método .split("@") divide a string em duas partes onde estiver o caractere "@"
# gerando uma lista: ['joao.silva', 'empresa.com.br']
partes = email_normalizado.split("@")
usuario = partes[0]
dominio = partes[1]

# 4. Exibindo os resultados com etiquetas claras
print("========== ANÁLISE DE E-MAIL ==========")
print(f"E-mail Original   : '{email_bruto}'")
print(f"E-mail Limpo      : '{email_limpo}'")
print(f"E-mail Normalizado: '{email_normalizado}'")
print("-" * 39)
print(f"Usuário Extraído  : {usuario}")
print(f"Domínio Extraído  : {dominio}")
print("=======================================")