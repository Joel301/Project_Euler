#! python3
#-*- coding: utf-8 -*-

import unittest
import scripts

class TestProblem0001(unittest.TestCase):

    def test_computed(self):
        result = scripts.problem0001.compute()
        self.assertEqual(result,23)