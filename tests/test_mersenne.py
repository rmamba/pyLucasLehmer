try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import os
import sys
import unittest

module_path = os.path.abspath(os.getcwd())
if module_path not in sys.path:
    sys.path.append(module_path)

from MersennePrime import MersennePrime

class TestMersenneIsPrimeCommand(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
    
    def test_true(self):
        mp = MersennePrime(3)
        self.assertTrue(mp.isPrime())
        self.assertEqual(mp._P, [7])

        mp = MersennePrime(5)
        self.assertTrue(mp.isPrime())
        self.assertEqual(mp._P, [31])

        mp = MersennePrime(7)
        self.assertTrue(mp.isPrime())
        self.assertEqual(mp._P, [127])

        mp = MersennePrime(13)
        self.assertTrue(mp.isPrime())
        self.assertEqual(mp._P, [255, 31])

        mp = MersennePrime(17)
        self.assertTrue(mp.isPrime())
        self.assertEqual(mp._P, [255, 255, 1])

        mp = MersennePrime(19)
        self.assertTrue(mp.isPrime())
        self.assertEqual(mp._P, [255, 255, 7])

        mp = MersennePrime(31)
        self.assertTrue(mp.isPrime())
        self.assertEqual(mp._P, [255, 255, 255, 127])

    def test_false(self):
        mp = MersennePrime(9)
        # self.assertFalse(mp.isPrime())
        # throw error

        mp = MersennePrime(11)
        self.assertFalse(mp.isPrime())
        self.assertEqual(mp._P, [255, 7])

    # def test_medium(self):


mp = MersennePrime(89)
print(mp.isPrime())
print(mp.speed)
