#! python3
#-*- coding: utf-8 -*-

import unittest
from scripts import problem0003

class TestProblem0003(unittest.TestCase):

    def test_primeFactors(self):
        self.assertEqual([x for x in problem0003.primeFactors()]
                        ,[5, 7, 13 ,29])
    
    def test_primeFactorsResult(self):
        self.assertEqual(problem0003.compute()
                        ,[71, 839, 1471, 6857])