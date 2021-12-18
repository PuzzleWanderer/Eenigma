from settings import *
from functions import *

"""
основная идея взята из видео: https://www.youtube.com/watch?v=eJXmdi41Z2U
коммутатор в программе отсутствует, но количество пар в 
рефлекторе(который в программе я назвал коммутатором) может быть меньше 13(не все символы связаны в пары)
таким образом символы могут кодировать сами себя
"""

#начальные положения роторов(0-25 для функции, но от 1 до 26 в программе)
settt = [5,14,18]
rotors_nums = [1,2,3]
commutator_num = 1

print('_____________________')
while(1):
    print("Decode or Encode(e)")
    print("Change  settings(c)")
    #0 не используется, поэтому может быть использован в качестве символа для выхода
    print("note:  to exit  (0)")
    todo = input(": ").lower()
    print('_____________________')
    if todo == "e":
        while (1):
            s = input("String: ")
            if s == '0':
                break
            en = Eencode(s, [settt[0]-1,settt[1]-1,settt[2]-1], [rotors[rotors_nums[0]-1], rotors[rotors_nums[1]-1], rotors[rotors_nums[2]-1]], commutator[commutator_num-1])
            if en[0][1:5] != 'ERROR':
                settt = en[1]
            print("Output: "+en[0])

    elif todo == 'c':
        while(1):
            print('view    settings (v)')
            print('change  position (p)')
            print('change   rotors  (r)')
            print('change commutator(c)')
            s = input(': ')
            print('_____________________')
            if s == '0':
                break

            s = s.lower()
            if s == 'v':
                print('rotor     position : ', end='')
                print(*settt)
                print('selected   rotors  : ', end='')
                print(*rotors_nums)
                print('selected commutator: ', end='')
                print(commutator_num)
                print('number  of  rotors : ', end='')
                print(len(rotors))
                print('number  of  comms  : ', end='')
                print(len(commutator))
                print('_____________________')

            elif s == 'p':
                while (1):
                    print('enter 3 nums from 1 to 26')
                    s = input(': ')

                    if s == '0':
                        break

                    s = s.split()
                    if len(s) != 3:
                        print('ERROR: not 3 nums')
                    else:
                        digits = s[0].isdigit() and s[1].isdigit() and s[2].isdigit()
                        if digits:
                            if int(s[0]) in range(1, 26+1) and int(s[1]) in range(1, 26+1) and int(
                                    s[2]) in range(1, 26+1):
                                print('Success')
                                settt = [int(s[0]), int(s[1]), int(s[2])]
                                break
                            else:
                                print("ERROR: not in range")
                        else:
                            print("ERROR: not nums")

                    print('_____________________')

            elif s == 'r':
                while(1):
                    print('enter 3 nums from 1 to '+str(len(rotors)))
                    s = input(': ')

                    if s == '0':
                        break

                    s = s.split()
                    if len(s) != 3:
                        print('ERROR: not 3 nums')
                    else:
                        digits = s[0].isdigit() and s[1].isdigit() and s[2].isdigit()
                        if digits:
                            if int(s[0]) in range(1,len(rotors)+1) and int(s[1]) in range(1,len(rotors)+1) and int(s[2]) in range(1,len(rotors)+1):
                                print('Success')
                                rotors_nums = [int(s[0]), int(s[1]), int(s[2])]
                                break
                            else:
                                print("ERROR: not in range")
                        else:
                            print("ERROR: not nums")

                    print('_____________________')

            elif s == 'c':
                while(1):
                    print('enter 1 num from 1 to ' + str(len(commutator)))
                    s = input(': ')

                    if s == '0':
                        break

                    if not s.isdigit():
                        print("ERROR: not a num")
                    elif not int(s) in range(len(commutator)+1):
                        print("ERROR: not in range")
                    else:
                        print("Success")
                        commutator_num = int(s)
                        break