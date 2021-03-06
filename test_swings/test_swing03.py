# coding:utf-8
"""
03. 円周率

"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""

import unittest
import sys, os
path = os.path.join(os.path.dirname(__file__), "../swings")
sys.path.append(path)
from swing03 import swing03

class TestSwings(unittest.TestCase):

    def test_swing03(self):
        str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
        expected = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
        actual = swing03(str)

        self.assertEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()