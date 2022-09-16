# add a test to see if RNG < p, it does the intentional step
import unittest
from unittest.mock import patch
import numpy as np
from io import StringIO
import sys
from walker import Walker

class TestWalker(unittest.TestCase):
    """
    Class to test the Walker() class and all its methods.
    """
    def setUp(self):
        """
        Initialise seed values to test this stochastic process.
        Expected results from three seeds included in the seeds attribute.
        """
        self.seeds = {  1:  ":)_________0\n"+
                            ":)_________1\n"+
                            "_:)________2\n"+
                            ":)_________3\n"+
                            ":)_________4\n"+
                            ":)_________5\n"+
                            ":)_________6\n"+
                            ":)_________7\n"+
                            ":)_________8\n"+
                            ":)_________9\n"+
                            "_:)________10\n",
                        
                        42: ":)_________0\n"+
                            ":)_________1\n"+
                            "_:)________2\n"+
                            "__:)_______3\n"+
                            "___:)______4\n"+
                            "__:)_______5\n"+
                            "_:)________6\n"+
                            ":)_________7\n"+
                            "_:)________8\n"+
                            "__:)_______9\n"+
                            "___:)______10\n",
                        
                        127:":)_________0\n"+
                            "_:)________1\n"+
                            ":)_________2\n"+
                            ":)_________3\n"+
                            "_:)________4\n"+
                            "__:)_______5\n"+
                            "_:)________6\n"+
                            ":)_________7\n"+
                            "_:)________8\n"+
                            "__:)_______9\n"+
                            "_:)________10\n",
                        }

    def test_makeStreet(self):
        randWalker = Walker()
        randWalker.makeStreet()
        self.assertEqual(randWalker.output, [':)', '_', '_', '_', '_', '_', '_', '_', '_', '_', '0'])

    def test_printStreet(self):
        randWalker = Walker()
        randWalker.makeStreet()
        with patch('sys.stdout', new = StringIO()) as fake_out:
            randWalker.printStreet()
            self.assertEqual(fake_out.getvalue(), ':)_________0\n')

    def test_walk(self):
        for seed in self.seeds:
            np.random.seed(seed)
            randWalker = Walker()

            # send console outputes to fake_out
            with patch('sys.stdout', new = StringIO()) as fake_out:
                randWalker.walk()
                self.assertEqual(fake_out.getvalue(), self.seeds[seed])

