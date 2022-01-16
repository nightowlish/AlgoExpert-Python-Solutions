def minRewards(scores):
    if len(scores) < 2:
        return len(scores)
    awards = [1 for score in scores]
    for index in range(1, len(scores)):
        if scores[index - 1] < scores[index]:
            awards[index] = awards[index - 1] + 1
    for index in range(len(scores) - 1, 0, -1):
        if scores[index - 1] > scores[index]:
            if awards[index - 1] == 1:
                awards[index - 1] = awards[index] + 1
            else:
                awards[index - 1] = max(awards[index - 1], awards[index] + 1)
    return sum(awards)
