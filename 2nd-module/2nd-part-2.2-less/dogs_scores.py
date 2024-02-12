# swap max and min elements in list
def swap_max_min(scores):

    if not scores:
        return None

    max_val = min_val = scores[0]
    max_idx = min_idx = 0

    for i in range(len(scores)):
        if scores[i] > max_val:
            max_val = scores[i]
            max_idx = i
        if scores[i] < min_val:
            min_val = scores[i]
            min_idx = i

    scores[max_idx] = min_val
    scores[min_idx] = max_val

    return scores


# Example usage
scores_lst = [5, 3, 8, 1, 9]
swapped_scores = swap_max_min(scores_lst)
print(swapped_scores)
