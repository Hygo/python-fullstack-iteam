email_bruto = "   joao.silva@EMPRESA.com.br   "

email_limpo = email_bruto.strip()
email_normal = email_limpo.lower()
usuario = email_normal.split("@")[0]
dominio = email_normal.split("@")[1]

print(f"Original  : '{email_bruto}'")
print(f"Sem espaços: '{email_limpo}'")
print(f"Minúsculas : '{email_normal}'")
print(f"Usuário   : '{usuario}'")
print(f"Domínio   : '{dominio}'")
