# coding:utf-8
"""
00. 文字列の逆順

文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"""

def swing00(str):
    return str[::-1]


if __name__ == "__main__":
    str = "stressed"
    print(swing00(str))