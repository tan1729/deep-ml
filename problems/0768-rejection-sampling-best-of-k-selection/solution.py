def rejection_sampling_best_of_k(candidates, scores):
    n = len(candidates)
    ans = []

    for i in range(n):
        maxi = scores[i][0]
        ele = candidates[i][0]

        for j in range(1, len(candidates[i])):
            if scores[i][j] > maxi:
                maxi = scores[i][j]
                ele = candidates[i][j]

        ans.append(ele)

    return ans
