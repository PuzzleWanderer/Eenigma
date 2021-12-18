import random as r

def generate_rotor_layer():
    rotor_layer = [0 for i in range(26)]
    used = []
    for i in range(26):
        err = 1
        while err == 1:
            r_num = r.randint(0,25)
            if not(r_num in used):
                err = 0
                rotor_layer[i] = r_num
                used.append(r_num)
    return rotor_layer


def generate_rotor():
    layers = [generate_rotor_layer() for i in range(13)]
    layers_second_part = [[0 for i in range(26)] for j in range(13)]
    for i in range(len(layers)):
        for j in range(len(layers[i])):
            layers_second_part[i][layers[i][j]] = j

    for layer in layers_second_part:
        layers.append(layer)

    return layers


def generate_commutator():
    commutator = dict()
    used = []
    for i in range(10):
        err1 = 1
        while err1 == 1:
            r_num1 = r.randint(0,25)
            if not(r_num1 in used):
                err1 = 0
                err2 = 1
                used.append(r_num1)
                while err2 == 1:
                    r_num2 = r.randint(0,25)
                    if not(r_num2 in used):
                        err2 = 0
                        used.append(r_num2)
                        commutator[r_num1] = r_num2
                        commutator[r_num2] = r_num1
    return commutator
            

#для вывода рандомного коммутатора
"""
print(generate_commutator())
"""

#для вывода рандомного ротора
"""
rotor = generate_rotor()
for elem in rotor:
    print(elem, end="")
    print(", ")
"""
