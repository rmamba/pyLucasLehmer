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

class TestMersennePrimeListCommand(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
    
    def test_byte(self):
        mp = MersennePrime(3)
        self.assertEqual(mp._list(2), [2])
        self.assertEqual(mp._list(127), [127])
        self.assertEqual(mp._list(255), [255])

    def test_int(self):
        mp = MersennePrime(3)
        self.assertEqual(mp._list(256), [0, 1])
        self.assertEqual(mp._list(24931), [99, 97])
        self.assertEqual(mp._list(65535), [255, 255])

    def test_int24(self):
        mp = MersennePrime(3)
        self.assertEqual(mp._list(3152070), [198, 24, 48])
        self.assertEqual(mp._list(4718404), [68, 255, 71])
        self.assertEqual(mp._list(13329713), [49, 101, 203])

    def test_int32(self):
        mp = MersennePrime(3)
        self.assertEqual(mp._list(67821966), [142, 225, 10, 4])
        self.assertEqual(mp._list(68027874), [226, 5, 14, 4])
        self.assertEqual(mp._list(81023199), [223, 80, 212, 4])
