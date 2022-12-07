# can express this as a regex with backrefs but I cant get python to do this right
# something about the dialect
# re.match(r"([a-z])((?!\1).)((?!(?:\1|\2)).)((?!(?:\1|\2|\3)).)", data)
import collections, aocd

if __name__ == '__main__':
    q, min_dist = collections.deque(), {}
    for i, c in enumerate(aocd.get_data(day=6), 1):
        if c in q:
            for i in range(q.index(c) + 1): q.popleft()
        q.append(c)
        if len(q) not in min_dist:
            min_dist[len(q)] = i
    print(f"answer 1: {min_dist[4]}\nanswer 2: {min_dist[14]}")
