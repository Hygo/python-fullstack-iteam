email_bruto = "   joao.silva@EMPRESA.com.br   "

email_limpo = email_bruto.strip().lower()

partes = email_limpo.split('@')
usuario = partes[0]
dominio = partes[1]

print(f"E-mail limpo: {email_limpo}")
print(f"Usuário: {usuario}")
print(f"Domínio: {dominio}")
