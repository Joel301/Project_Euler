#! python3
# -*- coding: utf-8 -*-

import unittest
from scripts import problem0004


class TestProblem0002(unittest.TestCase):

    def test_largestPalindrome(self):
        self.assertEqual(problem0004.largestPalindrome(2), 9009)

    # def test_largestPalindrome_OneDigit(self):
    #     self.assertEqual(problem0004.largestPalindrome(1), 9)

    def test_largestPalindrome_OneDigit(self):
        self.assertEqual(problem0004.largestPalindrome(3), 906609)