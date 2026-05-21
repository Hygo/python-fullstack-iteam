def classificar_temperatura(temperatura: float):
    if temperatura < 0:
        print(f"Temperatura: {temperatura}\nClassificação: Congelante❄️")
    elif temperatura >= 0 and temperatura <= 14:
        print(f"Temperatura: {temperatura}\nClassificação: Frio⛄")
    elif temperatura > 14 and temperatura <= 24:
        print(f"Temperatura: {temperatura}\nClassificação: Agradavel😊")
    elif temperatura > 24 and temperatura <= 34:
        print(f"Temperatura: {temperatura}\nClassificação:  Quente🥵")
    else:
        print(f"Temperatura: {temperatura}\nClassificação: Muito quente🔥")


if __name__ == "__main__":
    temperatura = float(input("Digite a temperatura para podemos classificala: "))
    classificar_temperatura(temperatura)

