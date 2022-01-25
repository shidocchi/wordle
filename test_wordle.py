# coding:utf-8

import unittest
from wordle import Wordle

class WordleTest(unittest.TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_ishitblow(self):
    """validate hitblow"""
    w = Wordle()
    self.assertTrue(w.ishitblow('-H-B-'))
    self.assertFalse(w.ishitblow('-X-B-'))
    self.assertFalse(w.ishitblow('-H-O-'))
    self.assertFalse(w.ishitblow('=H=B='))

  def test_hitblow1(self):
    """all hits"""
    w = Wordle()
    self.assertEqual(w.hitblow('abort', 'abort'), 'HHHHH')

  def test_hitblow2(self):
    """all blows"""
    w = Wordle()
    self.assertEqual(w.hitblow('abort', 'tabor'), 'BBBBB')

  def test_hitblow3(self):
    """same letters hit twice"""
    w = Wordle()
    self.assertEqual(w.hitblow('robot', 'cocoa'), '-H-H-')

  def test_hitblow4(self):
    """same letters hit and blow"""
    w = Wordle()
    self.assertEqual(w.hitblow('robot', 'taboo'), 'B-HHB')

  def test_hitblow5(self):
    """same letters hit and not blow"""
    w = Wordle()
    self.assertEqual(w.hitblow('tacos', 'cocoa'), '--HHB')

if __name__ == "__main__":
    unittest.main()
