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
        n = mp._list(2 ** 8)
        self.assertEqual(mp._sub(n, [1]), [255])

    def test_int(self):
        mp = MersennePrime(3)
        n = mp._list(2 ** 12)
        self.assertEqual(mp._sub(n, [1]), [255, 15])
        self.assertEqual(mp._sub(n, [0, 1]), [0, 15])
        n = mp._list(2 ** 16)
        self.assertEqual(mp._sub(n, [1]), [255, 255])
    
    def test_int24(self):
        mp = MersennePrime(3)
        n = mp._list(2 ** 20)
        self.assertEqual(mp._sub(n, [1]), [255, 255, 15])
        self.assertEqual(mp._sub(n, [0, 1]), [0, 255, 15])
        n = mp._list(2 ** 24)
        self.assertEqual(mp._sub(n, [1]), [255, 255, 255])

    def test_int32(self):
        mp = MersennePrime(3)
        n = mp._list(2 ** 28)
        self.assertEqual(mp._sub(n, [1]), [255, 255, 255, 15])
        self.assertEqual(mp._sub(n, [0, 1]), [0, 255, 255, 15])
        n = mp._list(2 ** 32)
        self.assertEqual(mp._sub(n, [1]), [255, 255, 255, 255])