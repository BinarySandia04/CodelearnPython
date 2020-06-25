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

def new_alphabet(alp, p):
    alpha = list(alp) # PUTO PYTHON OSTIAAAAAA AIXO ES MOLT LLEIG
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

def encrypt_monoalfabetic(s, kw, alphabet):
    newalpha = new_alphabet(alphabet, kw)
    result = ""
    for c in s:
        result += newalpha[alphabet.index(c)]
    return result

def decrypt_monoalfabetic(s, kw, alphabet):
    newalpha = new_alphabet(alphabet, kw)
    result = ""
    for c in s:
        result += alphabet[newalpha.index(c)]
    return result
    # M'HA COSTAT LA VIDA DIOOOOOOS

def displaced_alphabet(alphabet, i):
    return alphabet[i:] + alphabet[:i] # Bastant facil

def create_displaced_alphabet_list(alphabet):
    r = []
    for i in range(len(alphabet)):
        r.append(displaced_alphabet(alphabet, i))
    return r
    # Casi em moro aixo es molt molt molt dificil

def create_dictionary(l1, l2):
    dic = {}

    #Ambdues son de la mateixa longitud?
    if(len(l1) != len(l2)):
        return

    for i in range(len(l1)):
        dic[l1[i]] = l2[i]
    return dic

    # M'he tirat anys per fer aixo

def create_encrypt_alphabets_dictionary(l1, l2):
    dic = {}
    for i in range(len(l1)):
        dic[l1[i]] = create_dictionary(l1, l2[i])
    return dic

    # He estat més temps escribint el nom de la funcio xDDDD
