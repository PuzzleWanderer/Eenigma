def Eencode(s, settt, rotors, commutator):
    """
    функция зашифрования/расшифрования

    чтобы расшифровать последовательность важно внести все настройки,
    при которых последовательность была зашифрована

    :param s: строка (открытый текст или шифртекст)
    :param settt: массив положений роторов
    :param rotors: массив с самими роторами
    :param commutator: рефлектор в виде словаря
    :return: строка (открытый текст или шифртекст)
    """
    if not (type(s) is str):
        return ['(ERROR: input is not a string)', '']

    s = s.lower()
    for el in s:
        if not(el in [chr(a+97) for a in range(0,26)]):
            return ["(ERROR: contains not English letter)", '']
    rotor1 = rotors[0]
    rotor2 = rotors[1]
    rotor3 = rotors[2]
    
    sett = settt[0:]
    out = ""
    for el in s:
        s_num = ord(el) - 97

        s_num = rotor1[sett[0]][s_num]
        s_num = rotor2[sett[1]][s_num]
        s_num = rotor3[sett[2]][s_num]

        if s_num in commutator:
            s_num = commutator[s_num]

        s_num = rotor3[(sett[2] + 13) % 26][s_num]
        s_num = rotor2[(sett[1] + 13) % 26][s_num]
        s_num = rotor1[(sett[0] + 13) % 26][s_num]

        out += chr(s_num+97)

        if sett[0] != 25:
            sett[0] += 1
        else:
            sett[0] = 0
            if sett[1] != 25:
                sett[1] += 1
            else:
                sett[1] = 0
                if sett[2] != 25:
                    sett[2] += 1
                else:
                    sett[2] = 0

    return out, sett
