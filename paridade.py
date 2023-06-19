s = input()
c = 0
for b in s:
    if b == '1':
        c += 1
if c % 2 == 0:
    print(s+'0')
else:
    print(s+'1')
