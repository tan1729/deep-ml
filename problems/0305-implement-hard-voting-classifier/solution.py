def hard_voting_classifier(predictions: list[list[int]]) -> list[int]:
    n = len(predictions[0])
    ans = []

    for i in range(n):
        votes = []
        for j in range(len(predictions)):
            votes.append(predictions[j][i])

        winner = votes[0]
        for x in set(votes):
            if votes.count(x) > votes.count(winner):
                winner = x
            elif votes.count(x) == votes.count(winner) and x < winner:
                winner = x
        ans.append(winner)

    return ans