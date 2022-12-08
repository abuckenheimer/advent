import aocd, pandas as pd


if __name__ == '__main__':
    df = pd.DataFrame(list(l) for l in aocd.get_data(day=8).splitlines()).astype(int)
    v = lambda f: f.rolling(len(f), min_periods=0).max().diff().fillna(1).astype(bool)
    a1 = v(df) | v(df.loc[::-1]).loc[::-1] | v(df.T).T | v(df.T.loc[::-1]).loc[::-1].T

    def d(f: pd.DataFrame) -> pd.DataFrame:
        dist = pd.DataFrame(pd.np.zeros(f.shape), index=f.index, columns=f.columns)
        for c in range(len(f)):
            last_tree = pd.Series({i: 0 for i in range(10)})
            for r in range(len(f)):
                dist.iloc[r, c] = r - last_tree.loc[last_tree.index >= f.iloc[r, c]].max()
                last_tree.loc[f.iloc[r, c]] = r
        return dist

    a2 = d(df) * d(df.loc[::-1]).loc[::-1] * d(df.T).T * d(df.T.loc[::-1]).loc[::-1].T
    print(f"answer 1:{a1}\nanswer 2:{a2}")
