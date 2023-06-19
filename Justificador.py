n = int(input())
nw = []
while 0 < 1:
    if n == 0:
        break
    w = []
    lens = []
    for h in range(n):
        p = input()
        w.append(p)
        lens.append(len(p))
    for q in w:
        nw.append((max(lens) - len(q))*' ' + q)
    nw.append('')
    n = int(input())
for t in nw[:-1]:
    print(t)
