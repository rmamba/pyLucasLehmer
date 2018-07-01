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

class TestMersennePrimeSmallerCommand(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()
    
    def test_byte(self):
        mp = MersennePrime(3)
        self.assertFalse(mp._smaller([0xff], [0x01]))
        self.assertFalse(mp._smaller([0x80], [0x7f]))
        self.assertFalse(mp._smaller([0x7f], [0x7f]))
        self.assertTrue(mp._smaller([0x7e], [0x7f]))
        self.assertTrue(mp._smaller([0x00], [0x7f]))

    def test_int(self):
        mp = MersennePrime(3)
        self.assertFalse(mp._smaller([0x64, 0x64], [0xff, 0x0f]))
        self.assertFalse(mp._smaller([0xff, 0xff], [0x01]))
        self.assertFalse(mp._smaller([0xff, 0x0f], [0xff, 0x0f]))
        self.assertFalse(mp._smaller([0x00, 0x00, 0x01], [0xff, 0x0f]))
        self.assertTrue(mp._smaller([0x01], [0xff, 0xff]))
        self.assertTrue(mp._smaller([0xff, 0x0f], [0x64, 0x64]))
        self.assertTrue(mp._smaller([0xff, 0x0f], [0x00, 0x00, 0x01]))
    
    def test_int24(self):
        mp = MersennePrime(3)
        self.assertFalse(mp._smaller([0xff, 0xff, 0x0f], [0x3f]))
        self.assertFalse(mp._smaller([0x00, 0xff, 0x0f], [0x00, 0x01]))
        self.assertFalse(mp._smaller([0xff, 0xff, 0xff], [0x01]))
        self.assertFalse(mp._smaller([0x01, 0x00, 0x01], [0x00, 0x00, 0x01]))
        self.assertTrue(mp._smaller([0x00, 0xff, 0x0f], [0x00, 0x00, 0x00, 0x01]))
        self.assertTrue(mp._smaller([0x00, 0x00, 0x01], [0x01, 0x00, 0x01]))

    # def test_int32(self):
    #     mp = MersennePrime(3)
    #     self.assertEqual(mp._smaller([0xff, 0xff, 0xff, 0x0f], [0x01]), [0xff, 0xff, 0xff, 0x0f])
    #     self.assertEqual(mp._smaller([0x00, 0xff, 0xff, 0x0f], [0xff, 0x01]), [0x00, 0x01, 0xfe, 0xef, 0x1f])
    #     self.assertEqual(mp._smaller([0xff, 0xff, 0xff, 0xff], [0x00, 0x00, 0x00, 0x00, 0x01]), [0x00, 0x00, 0x00, 0x00, 0xff, 0xff, 0xff, 0xff])
