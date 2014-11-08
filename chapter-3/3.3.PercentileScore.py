scores = [56, 58, 98, 34, 58, 50, 78, 72, 67, 69, 12, 90, 89, 83, 70, \
        91, 99, 57, 50, 61, 62, 69, 88, 81, 82, 80, 67, 88, 91, 95]

def Percentile_rank(scores, given_score):
    """
    Returns the Percentile rank for the given score

    Args:
    scores - list of scores
    given_score - the score for which the Percentile is to be computed

    Returns:
    The Percentile rank for the given score
    """
    count = 0
    for score in scores:
        if score <= given_score:
            count += 1
    percentile = float(count) / len(scores) * 100
    return percentile

def Percentile_score(scores, percentile_rank):
    """
    Returns the score having the given percentile rank

    Args:
    scores - list of scores
    percentile_rank - the percentile rank for which the score has to be found

    Returns:
    The score corresponding to the given percentile
    """
    sorted_scores = sorted(scores)
    score_index = int((percentile_rank / 100) * len(sorted_scores)) - 1
    return sorted_scores[score_index]

def main():
    your_score = 67 
    your_percentile = Percentile_rank(scores, your_score)
    print "Score %d has %.2f percentile rank" % (your_score, your_percentile) 
    assert your_score == Percentile_score(scores, your_percentile)

if __name__ == "__main__":
    main()

