n = int(input())
while n > 0:
    nutrientes = input()
    cafe = input()
    almoco = input()
    if nutrientes == '' and cafe != '':
        print('CHEATER')
        n -= 1
        continue
    elif nutrientes =='' and almoco != '':
        print('CHEATER')
        n -=1
        continue
    if nutrientes == '':
        print()
        n -= 1
        continue
    if cafe == '' == almoco:
        nu = []
        for nut in nutrientes:
            nu.append(nut)
        nu.sort()
        print(''.join(nu))
        n -= 1
        continue
    r = []
    T = True
    for i in nutrientes:
        if i in cafe:
            continue
        else:
            r.append(i)
    for k in almoco:
        if k not in nutrientes or k in cafe:
            T = False
            break
        elif k in r:
            r.remove(k)
    for j in cafe:
        if j not in nutrientes:
            T = False
            break
    if T == False:
        print('CHEATER')
        n -= 1
        continue
    r.sort()
    print(''.join(r))
    n -= 1
