estoque = ["Teclado", "Mouse", "Webcam", "Monitor", "Headset", "Notebook"]

for es in estoque:
    if es == "Monitor":
        print(f" O indice é {estoque.index(es)}")
        break
    