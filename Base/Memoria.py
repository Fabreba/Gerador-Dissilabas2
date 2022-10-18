import Generate.Gerar

def save_base():

    text = Generate.Gerar.gerar(int(input("Quantas dissilabas deseja?")))
    print("Palavras Geradas \n")
    print(f"{text}")
    with open("base_palavras","a+") as arq:
        arq.write(text)

