import Base.Memoria as bm

def main():
    escolha = 21
    while escolha!=0:
        esc = '''
        0 - Parar Programa
        1 - Gerar Palavras
        2 - Consultar Palavras Geradas
        '''
        print(esc)
        escolha = int(input("Escolha uma das opções"))
        if escolha == 1:
            bm.save_base()
        elif escolha == 2:
            with open("base_palavras","r") as arq:
                text = arq.read()
                print(text)

if __name__ == "__main__":
    main()