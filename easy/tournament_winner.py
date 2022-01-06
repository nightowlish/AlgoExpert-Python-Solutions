def tournamentWinner(competitions, results):
    points = {}
    for index, competition in enumerate(competitions):
        winner = competition[0] if results[index] else competition[1]
        try:
            points[winner] += 3
        except:
            points[winner] = 3
    winner_team = None
    winner_points = 0
    for team in points:
        if points[team] > winner_points:
            winner_team = team
            winner_points = points[team]
    return winner_team
