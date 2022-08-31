def teamsfinder(games: list[str], team1: str, team2: str) -> tuple[list[str], list[str]]:
    team1_list_games = []

    team2_list_games = []

    for game in games:
        if team1 in game:
            team1_list_games.append(game)
            if team1 in game:
                team1_list_games.append(game)

        if team2 in game:
            team2_list_games.append(game)
            if team2 in game:
                team2_list_games.append(game)
    return team1_list_games, team2_list_games

def matching_games(games_orginzed_by_team, team1, team2):
    mutal_oppenents = set()
    team1_team2_intercet = {team1, team2}

    team1_games, team2_games = games_orginzed_by_team
    games_orginzed_by_team = team1_games + team2_games
    for game in games_orginzed_by_team:
        mutal_oppenents.add(game[0])
        mutal_oppenents.add(game[2])

        mutal_oppenents.symmetric_difference(team1_team2_intercet)
    return mutal_oppenents.symmetric_difference(team1_team2_intercet)


def find_team_average(matching_games_set, played_games):
    total_sum = 0
    team1_count = 0
    for game in played_games:
        side_one = game[0:2]
        side_two = game[2:5]

        for team in matching_games_set:

            if team in side_one:
                total_sum += (int(side_two[1]) - int(side_one[1]))
                team1_count += 1

            if team in side_two:
                total_sum += (int(side_one[1]) - int(side_two[1]))
                team1_count += 1
    if team1_count:
        return total_sum / team1_count
    else:
        return 0


def average_dif_oppenents(list_games, team1, team2):
    teams = teamsfinder(list_games, team1, team2)
    interction = matching_games(teams, team1, team2)
    team1_list, team2_list = teams
    average = find_team_average(interction, team1_list)
    average2 = find_team_average(interction, team2_list)
    return average, average2
