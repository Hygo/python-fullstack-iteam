def gera_tabuada(numero):
    print(f"=== Tabuada do {numero} ===")
    for i in range(1,10,1):
        print(f"{numero} x  {i} =  {numero * i}")


if __name__ == "__main__":
    valor = int(input("Digite um numero para ver sua tabuada: "))
    gera_tabuada(valor)
