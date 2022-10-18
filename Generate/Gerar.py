import random as r


def gerar(n):
    consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 't', 's', 'w', 'x', 'y', 'z']
    vogais = ['a', 'e', 'i', 'o', 'u']
    palavras = ''
    for i in range(n):
        sil = r.choice(consoantes)+r.choice(vogais)
        sil2 = r.choice(consoantes)+r.choice(vogais)
        palavra_dissilaba = sil + sil2
        palavras += palavra_dissilaba + '\n'
    return palavras
