import io

import aocd
import pandas as pd

df = pd.read_csv(io.StringIO(aocd.get_data(day=4)), names=["l", "r"])
l, r = [c.str.split("-", expand=True).astype(int) for _, c in df.items()]
is_subset = ((l[0] <= r[0]) & (l[1] >= r[1])) | ((l[0] >= r[0]) & (l[1] <= r[1]))
has_overlap = ((l[0] >= r[0]) & (l[0] <= r[1])) | ((r[0] >= l[0]) & (r[0] <= l[1]))
print(f"answer 1: {is_subset.sum()}\nanswer 2: {has_overlap.sum()}")
