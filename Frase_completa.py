n = int(input())
for q in range(n):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    frase = input().split()
    for palavra in frase:
        for letra in palavra:
            if letra in alfabeto:
                alfabeto.remove(letra)
    if alfabeto == []:
        print('frase completa')
    elif len(alfabeto) <= 13:
        print('frase quase completa')
    else:
        print('frase mal elaborada')
    
