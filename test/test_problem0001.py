#! python3
#-*- coding: utf-8 -*-

import unittest
import scripts

class TestProblem0001(unittest.TestCase):

    def test_computed(self):
        result = scripts.problem0001.compute(10)
        self.assertEqual(result,23)
    
    def test_computed_Result(self):
        result = scripts.problem0001.compute(1000)
        self.assertEqual(result,233168)