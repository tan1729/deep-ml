
def balance_undersample(data: list) -> list:
    if len(data) == 0:
        return []

    d = {}

    for i in data:
        d[i[1]] = d.get(i[1], 0) + 1

    mini = min(d.values())

    count = {}
    ans = []

    for label in d:
        count[label] = 0

    for i in data:
        label = i[1]

        if count[label] < mini:
            ans.append(i)
            count[label] += 1

    return ans
