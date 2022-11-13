from data import matches

print(matches)

print('/'*100)

print(f'Total of matches {len(matches)}')

print('/'*100)

team_wins = list(filter(lambda item: item['home_team_result'] == 'Win', matches))
print(team_wins)

print('/'*100)

print(f'Total of matches {len(team_wins)}')
