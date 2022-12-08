import pandas as pd
import pathlib


if __name__ == '__main__':
    r = pd.Series(aocd.get_data(day=7).splitlines())
    d = ('/' + r.str.extract(r"^\$ cd (.*)")[0]).fillna('').cumsum().apply(pathlib.Path)
    d = d.apply(pathlib.Path.resolve).apply(str)
    s = pd.to_numeric(r.str.extract(r"^(\d+) [\w.]+")[0])
    s.index = d
    f = pd.Series({k, s.loc[d.str.startswith(d)].sum() for d in d.unique()})
    a2 = f.loc[f  > 30_000_000 - (70_000_000 - s.sum())].sort_values().head(1)
    print(f"answer 1: {f.sum()}\nanswer 2: {a2}")
