def modify_team_statistic(goals_scored, goals_conceded, line):
    line[0] += 1
    if goals_scored > goals_conceded:
        line[1] += 1
        line[4] += 3
    elif goals_scored == goals_conceded:
        line[2] += 1
        line[4] += 1
    else:
        line[3] += 1


def main():
    n = int(input())

    table = {}

    for i in range(n):
        row = input().split(';')
        team1 = row[0]
        goals1 = int(row[1])
        team2 = row[2]
        goals2 = int(row[3])

        if team1 not in table:
            table[team1] = [0, 0, 0, 0, 0]

        modify_team_statistic(goals1, goals2, table[team1])

        if team2 not in table:
            table[team2] = [0, 0, 0, 0, 0]

        modify_team_statistic(goals2, goals1, table[team2])

    for team, statistic in table.items():
        line_str = ' '.join([str(i) for i in statistic])
        print(f'{team}:{line_str}')


main()