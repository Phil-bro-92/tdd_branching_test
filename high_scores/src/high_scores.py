def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_three_scores = []
    remove_duplicates = []
    [
        remove_duplicates.append(score)
        for score in scores
        if score not in remove_duplicates
    ]

    remove_duplicates.sort()
    if len(scores) == 1:
        top_three_scores.append(remove_duplicates[-1])
    elif len(scores) < 3:
        top_three_scores.append(remove_duplicates[-1])
        top_three_scores.append(remove_duplicates[-2])
    else:
        top_three_scores.append(remove_duplicates[-1])
        top_three_scores.append(remove_duplicates[-2])
        top_three_scores.append(remove_duplicates[-3])
    
    return top_three_scores


def sort_high_to_low(scores):
    scores.sort()
    scores.reverse()
    return scores
