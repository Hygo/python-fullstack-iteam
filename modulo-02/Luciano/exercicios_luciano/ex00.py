while True:
    texto = input("Digite alguma coisa: ")
    texto = texto.lower()
    if texto == "sair":
        print("Fim!")
        break
    elif len(texto) < 2:
        print("Texto muito curto")
        continue
    elif texto == "admin":
        pass
    print(f"A processar: {texto}")
    