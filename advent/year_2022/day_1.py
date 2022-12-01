import aocd
import pandas as pd

if __name__ == '__main__':
    body = aocd.get_data(day=1, year=2022)
    df = pd.DataFrame({"calories": pd.to_numeric(body.splitlines())})
    df['elf'] = df.isnull().cumsum()
    elf_totals = df.groupby('elf').calories.sum().sort_values()
    print("answer 1:", elf_totals.tail(1).sum())
    print("answer 2:", elf_totals.tail(2).sum())
