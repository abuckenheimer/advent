"""
1 = rock 2 = paper 3 = scissors

part 1
3 - 1 = 2   loss + 1 % 3 = 0
2 - 1 = 1   win  + 1 % 3 = 2
1 - 1 = 0   tie  + 1 % 3 = 1
1 - 2 = -1  loss + 1 % 3 = 0
1 - 3 = -2  win  + 1 % 3 = 2

1 = loss 2 = draw 3 = win

part 2
3 + 1 = 4  paper    % 3 + 1 = 2
2 + 1 = 3  rock     % 3 + 1 = 1
1 + 1 = 2  scissors % 3 + 1 = 3
1 + 2 = 3  rock     % 3 + 1 = 1
1 + 3 = 4  paper    % 3 + 1 = 2
2 + 2 = 4  paper    % 3 + 1 = 2
3 + 2 = 5  scissors % 3 + 1 = 3
"""

import io
import pandas as pd
import aocd

if __name__ == '__main__':
    df = pd.read_csv(io.StringIO(aocd.get_data(day=2)), sep=' ', names=['you', 'me'])
    df = df.applymap({'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}.get)
    print("score 1:", ((((df.me - df.you + 1) % 3) * 3) + df.me).sum())
    print("score 2:",  (((df.me + df.you) % 3 + 1) + ((df.me - 1) * 3)).sum())

