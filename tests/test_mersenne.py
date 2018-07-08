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

if __name__ == "__main__":
    # {
    #     'and': 0, 
    #     'add': 0, 
    #     'smaller': 6.139833450317383, 
    #     'square': 0, 
    #     'sub': 279.0928645133972, 
    #     'mul': 1321.333925485611, 
    #     'total': 1615.8498299121857, 
    #     'mod': 294.17711067199707
    # }
    debug=False
    # mp = MersennePrime(17, debug=debug)
    # mp = MersennePrime(19, debug=debug)
    # mp = MersennePrime(31, debug=debug)
    # mp = MersennePrime(61, debug=debug)
    # mp = MersennePrime(89, debug=debug)
    # mp = MersennePrime(107, debug=debug)
    mp = MersennePrime(127, debug=debug)
    # mp = MersennePrime(521, debug=debug)
    # mp = MersennePrime(607, debug=debug)
    # mp = MersennePrime(1279, debug=debug)
    print(mp.isPrime())
    print(mp.speed)
    # print mp._and([255, 15], [100, 100]), [100, 4]
    # print mp._and([100, 100], [255, 15]), [100, 4]
    # print mp._and([255, 15], [1, 1]), [1, 1]
    # print mp._and([255, 15], [1]), [1]
    # print mp._and([255, 15], [0, 0, 1]), [0]
