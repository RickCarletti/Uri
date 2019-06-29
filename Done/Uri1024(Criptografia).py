def criptografia(text):
    newtext = []                                    # Passo1
    for i in text:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            newtext.append(chr(ord(i)+3))
        else:
            newtext.append(i)
    text = str(''.join(reversed(newtext)))          # Passo2
    newtext = []                                    # Passo3
    for j in range(len(text)):
        if j >= len(text) // 2:
            newtext.append(chr(ord(text[j])-1))
        else:
            newtext.append(text[j])
    return str(''.join(newtext))


for i in range(int(input())):
    text = str(input())
    text = criptografia(text)
    print(text)
