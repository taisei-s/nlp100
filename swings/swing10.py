# coding:utf-8
"""
10．行数のカウント

行数をカウントせよ．確認にはwcコマンドを用いよ．

command:
$wc -l hightemp.txt
"""

import sys

def swing10():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        lines = f.readlines()

    print(len(lines))


if __name__ == "__main__":
    swing10()