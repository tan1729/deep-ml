def quality_filter_rejection_sampling(scores: list, threshold: float, n_select: int = None) -> dict:
    n = len(scores)
    sc = []

    for i in range(n):
        if scores[i] >= threshold:
            sc.append((scores[i], i))

    acceptance_rate = round(len(sc) / n, 4) if n > 0 else 0.0

    sc.sort(reverse=True)

    if n_select is not None:
        sc = sc[:n_select]

    accepted_indices = []
    selected_scores = []

    for i in sc:
        selected_scores.append(i[0])
        accepted_indices.append(i[1])

    mean_quality = round(sum(selected_scores) / len(selected_scores), 4) if selected_scores else 0.0

    return {
        'accepted_indices': accepted_indices,
        'acceptance_rate': acceptance_rate,
        'mean_quality': mean_quality
    }