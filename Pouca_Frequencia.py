T = int(input())
for t in range(T):
    n = int(input())
    l = list(input().split())
    p = list(input().split())
    R =[]
    for a in range(n):
        g = 0
        u = len(p[a])
        for f in p[a]:
            if f == 'P':
                g += 1
            elif f == 'A':
                continue
            else:
                u -= 1
        if (g/u) < 0.75:
            R.append(l[a])
    print(*R)
            
