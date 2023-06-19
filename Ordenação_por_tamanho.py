n = int(input())
while n > 0:
    frase = list(input().split())
    lens = []
    for i in range(len(frase)):
        lens.append(len(frase[i]))
    ff = []
    lens.sort(reverse = True)
    for l in lens:
        for k in range(len(frase)):
            if l == len(frase[k]):
                ff.append(frase[k])
                frase.remove(frase[k])
                break
    print(' '.join(ff))
    n -= 1
