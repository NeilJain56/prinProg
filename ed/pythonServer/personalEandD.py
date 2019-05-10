def personalEncryption(sentence):
    alpha = [[]] * 6
    alpha[1] = ['a']
    alpha[2] = ['b']
    alpha[3] = ['c']
    alpha[4] = ['d']
    alpha[5] = ['e']
    alpha[0] = ['f']
    final = []
    for x in range(103,123):
        if x % 6 == 0:
            alpha[0].append(chr(x))
        elif x % 6 == 1:
            alpha[1].append(chr(x))
        elif x % 6 == 2:
            alpha[2].append(chr(x))
        elif x % 6 == 3:
            alpha[3].append(chr(x))
        elif x % 6 == 4:
            alpha[4].append(chr(x))
        elif x % 6 == 5:
            alpha[5].append(chr(x))
                # print(alpha)
    words = sentence.split()
    for i in range(0,len(words)):
        word = list(words[i])
        for j in range(0,len(word)):
            index = ord(word[j]) % 6
            for ello in range(0,len(alpha[index])):
                if word[j] == alpha[index][ello]:
                    y = ello - 1
                else:
                    continue
            word[j] = alpha[index][y]
        final.append("".join(word))
    return (" ".join(final))

def personalDecryption(sentence):
    alpha = [[]] * 6
    alpha[1] = ['a']
    alpha[2] = ['b']
    alpha[3] = ['c']
    alpha[4] = ['d']
    alpha[5] = ['e']
    alpha[0] = ['f']
    final = []
    for x in range(103,123):
        if x % 6 == 0:
            alpha[0].append(chr(x))
        elif x % 6 == 1:
            alpha[1].append(chr(x))
        elif x % 6 == 2:
            alpha[2].append(chr(x))
        elif x % 6 == 3:
            alpha[3].append(chr(x))
        elif x % 6 == 4:
            alpha[4].append(chr(x))
        elif x % 6 == 5:
            alpha[5].append(chr(x))
    words = sentence.split()
    for i in range(0,len(words)):
        word = list(words[i])
        for j in range (0,len(word)):
            index = ord(word[j]) % 6
            for ello in range(0, len(alpha[index])):
                if word[j] == alpha[index][ello]:
                   y = ello + 1
                   if y >= len(alpha[index]):
                        y = 0
                else:
                    continue
            word[j] = alpha[index][y]
        final.append("".join(word))
    return (" ".join(final))
