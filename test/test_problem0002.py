#! python3
#-*- coding: utf-8 -*-

import unittest
import scripts

class TestProblem0002(unittest.TestCase):

    def test_fibonacci(self):
        result = scripts.problem0002.fibonacci()
        self.assertEqual(result,[1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
    
    def test_fibComputed(self):
        # result = scripts.problem0002.compute(0)
        # self.assertEqual(result,231)
        result = scripts.problem0002.compute(4000000)
        self.assertEqual(result,4613732)
    

