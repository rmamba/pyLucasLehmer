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

class TestMersennePrimeAddCommand(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
    
    def test_byte(self):
        mp = MersennePrime(3)
        self.assertEqual(mp._add([255], [1]), [0, 1])

    def test_int(self):
        mp = MersennePrime(3)
        self.assertEqual(mp._add([255, 15], [1]), [0, 16])
        self.assertEqual(mp._add([255, 15], [0, 1]), [255, 16])
        self.assertEqual(mp._add([255, 255], [1]), [0, 0, 1])
    
    def test_int24(self):
        mp = MersennePrime(3)
        self.assertEqual(mp._add([255, 255, 15], [1]), [0, 0, 16])
        self.assertEqual(mp._add([0, 255, 15], [0, 1]), [0, 0, 16])
        self.assertEqual(mp._add([255, 255, 255], [1]), [0, 0, 0, 1])
        self.assertEqual(mp._add([0, 255, 15], [0, 0, 0, 1]), [0, 255, 15, 1])

    def test_int32(self):
        mp = MersennePrime(3)
        self.assertEqual(mp._add([255, 255, 255, 15], [1]), [0, 0, 0, 16])
        self.assertEqual(mp._add([0, 255, 255, 15], [0, 1]), [0, 0, 0, 16])
        self.assertEqual(mp._add([255, 255, 255, 255], [1]), [0, 0, 0, 0, 1])
