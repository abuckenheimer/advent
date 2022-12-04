from string import ascii_letters

import aocd


def score(lines):
    return sum(ascii_letters.index(li) + 1 for li in lines)


lines = aocd.get_data(day=3).splitlines()
a1 = score((set(li[: len(li) // 2]) & set(li[len(li) // 2 :])).pop() for li in lines)
a2 = score(
    (set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2])).pop()
    for i in range(0, len(lines), 3)
)
print("answer 1: {a1}\nanswer2: {a2}")
