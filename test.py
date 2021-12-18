import unittest
from functions import Eencode

rotors = [[[22, 18, 7, 3, 8, 11, 24, 12, 9, 21, 0, 2, 4, 1, 14, 13, 10, 25, 6, 5, 16, 19, 23, 17, 20, 15],
[25, 20, 10, 24, 1, 11, 7, 0, 16, 18, 6, 12, 22, 14, 23, 19, 13, 5, 3, 15, 9, 4, 21, 2, 17, 8],
[1, 9, 19, 13, 22, 11, 7, 0, 14, 5, 6, 25, 16, 23, 10, 21, 3, 17, 4, 20, 2, 18, 8, 12, 15, 24],
[20, 24, 22, 9, 25, 17, 0, 19, 4, 5, 16, 10, 13, 12, 8, 2, 21, 7, 15, 18, 3, 23, 11, 1, 6, 14],
[8, 22, 7, 19, 9, 13, 20, 1, 0, 12, 24, 15, 6, 17, 4, 2, 21, 25, 11, 14, 10, 18, 16, 23, 5, 3],
[10, 23, 1, 13, 8, 18, 0, 21, 17, 25, 11, 14, 4, 16, 19, 6, 5, 9, 24, 2, 3, 20, 22, 7, 12, 15],
[8, 17, 13, 22, 23, 18, 10, 4, 11, 0, 24, 16, 5, 15, 21, 25, 7, 6, 3, 2, 19, 1, 14, 20, 12, 9],
[17, 18, 15, 20, 13, 0, 11, 6, 10, 2, 1, 19, 7, 3, 8, 9, 21, 24, 5, 16, 25, 12, 23, 4, 22, 14],
[13, 1, 8, 24, 20, 10, 15, 4, 22, 14, 11, 25, 0, 18, 7, 23, 19, 12, 6, 5, 21, 17, 3, 9, 16, 2],
[24, 10, 2, 19, 9, 15, 16, 22, 4, 0, 14, 8, 23, 13, 12, 6, 17, 25, 3, 20, 5, 1, 21, 18, 7, 11],
[19, 3, 1, 2, 4, 21, 7, 11, 25, 20, 15, 12, 13, 16, 24, 18, 23, 9, 5, 10, 0, 14, 6, 8, 17, 22],
[25, 24, 2, 13, 0, 15, 4, 11, 3, 1, 7, 5, 12, 23, 21, 10, 14, 6, 17, 19, 8, 22, 16, 20, 9, 18],
[5, 15, 20, 17, 10, 0, 11, 19, 23, 8, 3, 4, 1, 13, 7, 2, 25, 22, 14, 12, 9, 21, 16, 24, 18, 6],
[10, 13, 11, 3, 12, 19, 18, 2, 4, 8, 16, 5, 7, 15, 14, 25, 20, 23, 1, 21, 24, 9, 0, 22, 6, 17],
[7, 4, 23, 18, 21, 17, 10, 6, 25, 20, 2, 5, 11, 16, 13, 19, 8, 24, 9, 15, 1, 22, 12, 14, 3, 0],
[7, 0, 20, 16, 18, 9, 10, 6, 22, 1, 14, 5, 23, 3, 8, 24, 12, 17, 21, 2, 19, 15, 4, 13, 25, 11],
[6, 23, 15, 20, 8, 9, 24, 17, 14, 3, 11, 22, 13, 12, 25, 18, 10, 5, 19, 7, 0, 16, 2, 21, 1, 4],
[8, 7, 15, 25, 14, 24, 12, 2, 0, 4, 20, 18, 9, 5, 19, 11, 22, 13, 21, 3, 6, 16, 1, 23, 10, 17],
[6, 2, 19, 20, 12, 16, 15, 23, 4, 17, 0, 10, 24, 3, 11, 25, 13, 8, 5, 14, 21, 7, 22, 1, 18, 9],
[9, 21, 19, 18, 7, 12, 17, 16, 0, 25, 6, 8, 24, 2, 22, 13, 11, 1, 5, 20, 23, 14, 3, 4, 10, 15],
[5, 10, 9, 13, 23, 18, 7, 12, 14, 15, 8, 6, 21, 4, 25, 2, 19, 0, 1, 11, 3, 16, 24, 22, 17, 20],
[12, 1, 25, 22, 7, 19, 18, 14, 2, 23, 5, 10, 17, 0, 9, 6, 24, 21, 13, 16, 4, 20, 8, 15, 3, 11],
[9, 21, 2, 18, 8, 20, 15, 24, 11, 4, 1, 25, 14, 13, 10, 5, 6, 16, 23, 3, 19, 22, 7, 12, 0, 17],
[20, 2, 3, 1, 4, 18, 22, 6, 23, 17, 19, 7, 11, 12, 21, 10, 13, 24, 15, 0, 9, 5, 25, 16, 14, 8],
[4, 9, 2, 8, 6, 11, 17, 10, 20, 24, 15, 7, 12, 3, 16, 5, 22, 18, 25, 19, 23, 14, 21, 13, 1, 0],
[5, 12, 15, 10, 11, 0, 25, 14, 9, 20, 4, 6, 19, 13, 18, 1, 22, 3, 24, 7, 2, 21, 17, 8, 23, 16]],
[[11, 25, 12, 20, 4, 18, 19, 2, 1, 9, 3, 17, 0, 22, 16, 21, 10, 24, 15, 7, 8, 13, 6, 23, 14, 5],
[5, 19, 23, 16, 6, 22, 17, 25, 3, 4, 7, 9, 21, 13, 24, 10, 11, 18, 20, 1, 8, 0, 2, 12, 15, 14],
[13, 7, 24, 9, 17, 1, 23, 18, 25, 20, 0, 16, 10, 14, 19, 11, 6, 2, 22, 5, 8, 12, 15, 21, 4, 3],
[23, 25, 19, 21, 20, 12, 3, 22, 4, 6, 1, 13, 9, 11, 18, 8, 10, 16, 17, 24, 14, 5, 2, 7, 15, 0],
[14, 25, 20, 8, 15, 22, 7, 1, 10, 16, 23, 5, 24, 21, 19, 3, 6, 12, 2, 4, 11, 9, 17, 0, 18, 13],
[21, 0, 7, 18, 13, 20, 19, 14, 24, 1, 16, 6, 12, 9, 11, 5, 3, 25, 8, 2, 15, 17, 23, 4, 22, 10],
[1, 15, 16, 25, 23, 2, 8, 18, 11, 20, 5, 22, 9, 0, 6, 13, 21, 12, 4, 19, 7, 24, 3, 17, 14, 10],
[11, 25, 13, 6, 8, 4, 20, 10, 0, 21, 18, 23, 5, 24, 15, 22, 17, 16, 1, 19, 3, 2, 12, 7, 14, 9],
[22, 0, 3, 10, 23, 13, 11, 18, 17, 8, 25, 4, 14, 16, 7, 9, 5, 2, 1, 12, 15, 6, 19, 20, 21, 24],
[19, 24, 11, 20, 5, 15, 16, 10, 6, 22, 7, 23, 2, 25, 21, 4, 13, 18, 8, 0, 12, 9, 14, 1, 17, 3],
[8, 4, 23, 21, 22, 14, 18, 9, 16, 6, 12, 24, 7, 10, 2, 11, 19, 1, 25, 3, 13, 17, 15, 20, 0, 5],
[0, 15, 25, 12, 11, 21, 19, 6, 17, 24, 13, 22, 4, 7, 3, 14, 5, 9, 18, 23, 2, 20, 1, 10, 8, 16],
[19, 17, 20, 13, 8, 22, 0, 1, 4, 24, 11, 21, 7, 2, 3, 14, 5, 18, 12, 25, 16, 15, 9, 10, 23, 6],
[12, 8, 7, 10, 4, 25, 22, 19, 20, 9, 16, 0, 2, 21, 24, 18, 14, 11, 5, 6, 3, 15, 13, 23, 17, 1],
[21, 19, 22, 8, 9, 0, 4, 10, 20, 11, 15, 16, 23, 13, 25, 24, 3, 6, 17, 1, 18, 12, 5, 2, 14, 7],
[10, 5, 17, 25, 24, 19, 16, 1, 20, 3, 12, 15, 21, 0, 13, 22, 11, 4, 7, 14, 9, 23, 18, 6, 2, 8],
[25, 10, 22, 6, 8, 21, 9, 23, 15, 12, 16, 13, 5, 11, 20, 24, 17, 18, 14, 2, 4, 3, 7, 0, 19, 1],
[23, 7, 18, 15, 19, 11, 16, 6, 3, 21, 8, 20, 17, 25, 0, 4, 9, 22, 24, 14, 2, 13, 5, 10, 12, 1],
[1, 9, 19, 16, 23, 15, 11, 2, 18, 13, 25, 14, 12, 4, 7, 20, 10, 21, 3, 6, 5, 0, 24, 22, 8, 17],
[13, 0, 5, 22, 18, 10, 14, 20, 6, 12, 25, 8, 17, 15, 24, 1, 2, 23, 7, 19, 9, 16, 11, 4, 21, 3],
[8, 18, 21, 20, 5, 12, 3, 23, 4, 25, 7, 0, 22, 2, 24, 14, 17, 16, 10, 19, 6, 9, 15, 11, 13, 1],
[1, 18, 17, 2, 11, 16, 21, 14, 9, 15, 3, 6, 19, 5, 12, 20, 13, 8, 7, 22, 23, 24, 0, 4, 25, 10],
[19, 23, 12, 25, 15, 4, 8, 10, 18, 21, 7, 2, 20, 16, 22, 5, 6, 24, 17, 0, 3, 14, 9, 11, 1, 13],
[24, 17, 14, 19, 1, 25, 9, 12, 0, 7, 13, 15, 10, 20, 5, 22, 8, 21, 6, 16, 23, 3, 4, 2, 11, 18],
[0, 22, 20, 14, 12, 16, 7, 13, 24, 17, 23, 4, 3, 10, 15, 1, 25, 8, 18, 6, 21, 5, 11, 19, 9, 2],
[6, 7, 13, 14, 8, 16, 25, 12, 4, 22, 23, 10, 18, 3, 15, 21, 20, 1, 17, 0, 2, 11, 5, 24, 9, 19]],
[[10, 18, 13, 22, 12, 1, 21, 15, 7, 17, 0, 9, 2, 19, 20, 6, 3, 23, 8, 16, 5, 11, 14, 24, 25, 4],
[17, 14, 15, 5, 18, 19, 11, 25, 7, 20, 24, 16, 21, 10, 9, 1, 12, 13, 22, 23, 2, 8, 6, 4, 3, 0],
[8, 22, 20, 1, 3, 6, 21, 23, 17, 2, 0, 25, 9, 16, 24, 15, 10, 14, 4, 19, 12, 5, 11, 18, 13, 7],
[12, 18, 8, 4, 2, 3, 25, 16, 15, 11, 6, 22, 23, 17, 1, 20, 5, 9, 13, 0, 21, 10, 19, 7, 24, 14],
[18, 16, 3, 2, 7, 14, 8, 0, 1, 24, 15, 6, 4, 11, 21, 20, 5, 13, 22, 25, 9, 23, 19, 12, 17, 10],
[2, 8, 13, 16, 0, 14, 15, 19, 24, 4, 21, 25, 17, 22, 5, 23, 11, 1, 18, 7, 3, 12, 6, 10, 20, 9],
[5, 24, 8, 3, 13, 18, 22, 17, 25, 0, 10, 12, 16, 6, 14, 21, 9, 4, 20, 19, 15, 23, 2, 11, 1, 7],
[18, 3, 9, 6, 8, 11, 22, 14, 24, 7, 20, 16, 25, 13, 2, 15, 19, 12, 5, 10, 0, 4, 21, 1, 17, 23],
[25, 9, 13, 18, 24, 20, 5, 14, 17, 0, 15, 19, 10, 16, 4, 1, 3, 2, 22, 6, 21, 12, 11, 7, 8, 23],
[3, 12, 20, 21, 25, 10, 13, 15, 8, 5, 17, 6, 16, 0, 4, 2, 24, 7, 1, 22, 9, 18, 14, 11, 23, 19],
[22, 14, 2, 0, 3, 12, 24, 9, 1, 25, 6, 20, 7, 11, 17, 4, 23, 13, 15, 21, 18, 19, 16, 8, 10, 5],
[20, 7, 17, 6, 15, 0, 5, 16, 8, 2, 12, 18, 24, 23, 10, 11, 25, 22, 14, 4, 19, 1, 13, 3, 21, 9],
[0, 20, 10, 15, 11, 12, 3, 22, 4, 24, 14, 16, 2, 5, 8, 17, 7, 21, 6, 18, 19, 9, 13, 23, 1, 25],
[10, 5, 12, 16, 25, 20, 15, 8, 18, 11, 0, 21, 4, 2, 22, 7, 19, 9, 1, 13, 14, 6, 3, 17, 23, 24],
[25, 15, 20, 24, 23, 3, 22, 8, 21, 14, 13, 6, 16, 17, 1, 2, 11, 0, 4, 5, 9, 12, 18, 19, 10, 7],
[10, 3, 9, 4, 18, 21, 5, 25, 0, 12, 16, 22, 20, 24, 17, 15, 13, 8, 23, 19, 2, 6, 1, 7, 14, 11],
[19, 14, 4, 5, 3, 16, 10, 23, 2, 17, 21, 9, 0, 18, 25, 8, 7, 13, 1, 22, 15, 20, 11, 12, 24, 6],
[7, 8, 3, 2, 12, 16, 11, 4, 6, 20, 25, 13, 23, 17, 5, 10, 1, 24, 0, 22, 15, 14, 18, 21, 9, 19],
[4, 17, 0, 20, 9, 14, 22, 19, 1, 25, 23, 16, 21, 2, 5, 6, 3, 12, 18, 7, 24, 10, 13, 15, 8, 11],
[9, 24, 22, 3, 17, 0, 13, 25, 2, 16, 10, 23, 11, 4, 14, 20, 12, 7, 5, 19, 18, 15, 6, 21, 1, 8],
[20, 23, 14, 1, 21, 18, 3, 9, 4, 2, 19, 5, 17, 13, 7, 15, 11, 24, 0, 16, 10, 22, 6, 25, 8, 12],
[9, 15, 17, 16, 14, 6, 19, 23, 24, 1, 12, 22, 21, 2, 7, 10, 13, 8, 3, 11, 5, 20, 18, 25, 4, 0],
[13, 18, 15, 0, 14, 9, 11, 17, 8, 20, 5, 23, 1, 6, 22, 7, 12, 10, 21, 25, 2, 3, 19, 24, 16, 4],
[3, 8, 2, 4, 15, 25, 10, 12, 23, 7, 24, 13, 5, 17, 1, 18, 22, 14, 20, 21, 11, 19, 0, 16, 6, 9],
[5, 21, 9, 23, 19, 6, 3, 1, 8, 25, 14, 15, 10, 22, 18, 4, 7, 2, 11, 20, 0, 24, 17, 13, 12, 16],
[0, 24, 12, 6, 8, 13, 18, 16, 14, 21, 2, 4, 5, 22, 10, 3, 11, 15, 19, 20, 1, 17, 7, 23, 9, 25]]]

commutator = {0: 10, 10: 0, 13: 12, 12: 13, 16: 4, 4: 16, 14: 8, 8: 14, 2: 17, 17: 2, 19: 20, 20: 19, 25: 6, 6: 25, 22: 5, 5: 22, 18: 3, 3: 18, 24: 7, 7: 24, 11: 9, 9: 11, 1: 15, 15: 1, 23: 21, 21: 23}

class EenigmaTest(unittest.TestCase):
    def test_1_base(self):
        self.assertEqual(Eencode('enigma', [5-1,14-1,18-1], rotors, commutator)[0], 'yxkrpz')

    def test_2_base(self):
        self.assertEqual(Eencode('yxkrpz', [5-1,14-1,18-1], rotors, commutator)[0], 'enigma')

    def test_3_register(self):
        self.assertEqual(Eencode('ReGiStEr', [5-1,14-1,18-1], rotors, commutator)[0], 'faaorhym')

    def test_4_register(self):
        self.assertEqual(Eencode('FaAorhYm', [5-1,14-1,18-1], rotors, commutator)[0], 'register')

    def test_5_ERR_not_only_eng(self):
        self.assertEqual(Eencode('3534', [5-1,14-1,18-1], rotors, commutator)[0], '(ERROR: contains not English letter)')

    def test_4_ERR_not_str(self):
        self.assertEqual(Eencode([1,2], [5-1,14-1,18-1], rotors, commutator)[0], '(ERROR: input is not a string)')
    


if __name__ == "__main__":
    unittest.main()
