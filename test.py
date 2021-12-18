import unittest
from settings import *
from functions import Eencode
from functions import Edecode


class EenigmaTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Eencode('enigma', [4,13,17], [rotor1, rotor2, rotor3], commutator), 'vjggli')

    def test_2(self):
        self.assertEqual(Edecode('vjggli', [4,13,17], [rotor1, rotor2, rotor3], commutator), 'enigma')

    def test_3(self):
        self.assertEqual(Eencode('moznodesyat', [4,13,17], [rotor1, rotor2, rotor3], commutator), 'dxvarxmtqoz')

    def test_4(self):
        self.assertEqual(Edecode('dxvarxmtqoz', [4,13,17], [rotor1, rotor2, rotor3], commutator), 'moznodesyat')
    


if __name__ == "__main__":
    unittest.main()
