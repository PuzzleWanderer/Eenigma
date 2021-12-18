from settings import *
from functions import *

#начальные положения роторов(0-25)
settt = [4,13,17]
rotors = [rotor1, rotor2, rotor3]

while(1):
    todo = input("Decode(d) or Encode(e): ")
    if todo.lower() == "d":
        s = input("Encoded string: ")
        s = s.lower()
        de = Edecode(s, settt, rotors, commutator)
        print("String: "+de)
    elif todo.lower() == "e":
        s = input("String: ")
        s = s.lower()
        en = Eencode(s, settt, rotors, commutator)
        print("Encoded string: "+en)

