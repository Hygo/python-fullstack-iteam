def login(user, password):
    usuario = "admin"
    senha = "iteam2025"
    if usuario == user and senha == password:
        print("✅ Acesso liberado. Bem-vindo!")
    elif usuario == user and senha != password:
        print("❌ Senha incorreta.")
    else:
        print("❌ Usuário não encontrado.")


if __name__ == "__main__":
    user = input("Digite o usuario: ")
    password = input("Digite a senha: ")
    login(user, password)
