def minimumWaitingTime(queries):
    queries.sort()
    len_queries = len(queries)
    multiplier = 0
    summer = 0
    for i in range(len_queries):
        summer += multiplier * (len_queries - i)
        multiplier = queries[i]
    return summer
