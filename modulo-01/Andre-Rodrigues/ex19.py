emailSujo = "   joao.silva@EMPRESA.com.br   "

emailLimpo = emailSujo.strip().lower()
usuario, dominio = emailLimpo.split("@")

print(f"E-mail normalizado: '{emailLimpo}'")
print(f"Usuário: '{usuario}'")
print(f"Domínio: '{dominio}'")