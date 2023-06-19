n = int(input())
for lines in range(n):
    word = input()
    neword = []
    for letter in word:
        if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
            l = ord(letter) + 3
            neword.append(chr(l))
        else:
            neword.append(letter)
    neword = neword[::-1]
    neword2 = neword[:int(len(neword)/2)]
    for letter in neword[(int(len(neword)/2)):]:
        l = ord(letter) - 1
        neword2.append(chr(l))
    print(''.join(neword2))
