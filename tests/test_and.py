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

class TestMersennePrimeAndCommand(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
    
    def test_byte(self):
        mp = MersennePrime(3)
        self.assertEqual(mp._and([255], [1]), [1])
        self.assertEqual(mp._and([128], [127]), [0])

    def test_int(self):
        mp = MersennePrime(3)
        self.assertEqual(mp._and([255, 15], [100, 100]), [100, 4])
        self.assertEqual(mp._and([255, 15], [0, 0, 1]), [0])
        self.assertEqual(mp._and([255, 255], [1]), [1])
    
    def test_int24(self):
        mp = MersennePrime(3)
        self.assertEqual(mp._and([255, 255, 15], [63]), [63])
        self.assertEqual(mp._and([0, 255, 15], [0, 1]), [0, 1])
        self.assertEqual(mp._and([255, 255, 255], [1]), [1])
        self.assertEqual(mp._and([0, 255, 15], [0, 0, 0, 1]), [0])

    def test_int32(self):
        mp = MersennePrime(3)
        self.assertEqual(mp._and([255, 255, 255, 15], [1]), [1])
        self.assertEqual(mp._and([0, 255, 255, 15], [255, 1]), [0, 1])
        self.assertEqual(mp._and([255, 1], [0, 255, 255, 15]), [0, 1])
        self.assertEqual(mp._and([255, 255, 255, 255], [0, 0, 0, 0, 1]), [0])
