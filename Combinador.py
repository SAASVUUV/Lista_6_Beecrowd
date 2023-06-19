n = int(input())
while n > 0:
    f, s = input().split()
    w = []
    if len(f) > len(s):
        for i in range(len(s)):
            w.append(f[i])
            w.append(s[i])
        w.append(f[i+1:])
    else:
        for i in range(len(f)):
            w.append(f[i])
            w.append(s[i])
        w.append(s[i+1:])
    print(''.join(w))
    n -= 1
