def contador_palavras (palavra):
    s = palavra
    while s != '':
        print (s)
        s = s [: -1]
    return
         
palavra = input('Digite sua palavra:  ')
contador_palavras (palavra)