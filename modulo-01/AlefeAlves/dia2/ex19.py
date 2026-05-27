email = "   joao.silva@EMPRESA.com.br   "

print(f"String original: {email}")
emailnovo = email.strip()
print(f"Removendo os espaços extras com strip: {emailnovo}")
emailnovo = email.lower()
print(f"Normalizando para minúsculas: {emailnovo}")
print(f"Extraindo o nome do usuário: {emailnovo[0 : email.index("@")]}")
print(f"Extraindo o domínio: {emailnovo[email.index("@") + 1 :]} ")
