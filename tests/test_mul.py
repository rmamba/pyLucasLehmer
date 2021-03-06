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

class TestMersennePrimeMulCommand(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
    
    def test_byte(self):
        mp = MersennePrime(3)
        self.assertEqual(mp._mul([0xff], [0x01]), [0xff])
        self.assertEqual(mp._mul([0x80], [0x7f]), [0x80, 0x3f])

    def test_int(self):
        mp = MersennePrime(3)
        self.assertEqual(mp._mul([0xff, 0x0f], [0x64, 0x64]), [0x9c, 0xdb, 0x45, 0x06])
        self.assertEqual(mp._mul([0xff, 0x0f], [0x00, 0x00, 0x01]), [0x00, 0x00, 0xff, 0x0f])
        self.assertEqual(mp._mul([0xff, 0xff], [0x01]), [0xff, 0xff])
    
    def test_int24(self):
        mp = MersennePrime(3)
        self.assertEqual(mp._mul([0xff, 0xff, 0x0f], [0x3f]), [0xc1, 0xff, 0xef, 0x03])
        self.assertEqual(mp._mul([0x00, 0xff, 0x0f], [0x00, 0x01]), [0x00, 0x00, 0xff, 0x0f])
        self.assertEqual(mp._mul([0xff, 0xff, 0xff], [0x01]), [0xff, 0xff, 0xff])
        self.assertEqual(mp._mul([0x00, 0xff, 0x0f], [0x00, 0x00, 0x00, 0x01]), [0x00, 0x00, 0x00, 0x00, 0xff, 0x0f])

    def test_int32(self):
        mp = MersennePrime(3)
        self.assertEqual(mp._mul([0xff, 0xff, 0xff, 0x0f], [0x01]), [0xff, 0xff, 0xff, 0x0f])
        self.assertEqual(mp._mul([0x00, 0xff, 0xff, 0x0f], [0xff, 0x01]), [0x00, 0x01, 0xfe, 0xef, 0x1f])
        self.assertEqual(mp._mul([0xff, 0xff, 0xff, 0xff], [0x00, 0x00, 0x00, 0x00, 0x01]), [0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff])
