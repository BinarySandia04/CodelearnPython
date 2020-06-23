def alphabet_list():
    res = []
    for i in range(ord('a'), ord('z') + 1):
        res.append(chr(i))
    return res

def new_pos(a, b, c):
    return (a + b) % c


def old_pos(a, b, c):
    return (c + a - b) % c

def encrypt_cesar(s, n, alphabet):
    res = ""
    for c in s:
        res += alphabet[new_pos(alphabet.index(c), n, len(alphabet))]
    return res

def decrypt_cesar(s, n, alphabet):
    res = ""
    for c in s:
        res += alphabet[old_pos(alphabet.index(c), n, len(alphabet))]
    return res

def new_alphabet(l, p):
    alpha = alphabet_list()
    result = []
    if p == "" or len(p) > len(alpha):
        return alpha
    else:
        lastchar = "a"
        for c in p:
            theindex = alpha.index(c)
            result.append(c)
            alpha.remove(c)
            lastchar = alpha[(theindex) % len(alpha)]
        for r in range(len(alpha)):
            thein = (r + alpha.index(lastchar)) % len(alpha)
            result.append(alpha[thein])
        return result


print(new_alphabet("wtf", "epsilon")  )