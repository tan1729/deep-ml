def prefix_cache_hit_rate(prompts: list, cache: list) -> dict:
    cached_tokens = 0
    total_tokens = 0

    for i in range(len(prompts)):
        total_tokens += len(prompts[i])
        longest = 0

        for j in range(len(cache)):
            if prompts[i][:len(cache[j])] == cache[j]:
                longest = max(longest, len(cache[j]))

        cached_tokens += longest

    hit_rate = round(cached_tokens / total_tokens, 4) if total_tokens > 0 else 0.0

    return {
        'hit_rate': hit_rate,
        'cached_tokens': cached_tokens,
        'total_tokens': total_tokens
    }