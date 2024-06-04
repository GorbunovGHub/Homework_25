team_1 = 'Мастера кода'
team_2 = 'Волшебники данных'

team1_num = 5
team2_num = 6

score_1 = 40
score_2 = 42

team1_time = 180.2
team2_time = 196.3

task_total = score_1 + score_2
time_avg = team1_time + team2_time / task_total

challenge_result = 'победа команды Мастера кода!'

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

print('В команде %s' % team_1, 'участников: %s' % team1_num)
print('В команде %s' % team_2, 'участников: %s' % team2_num)
print('Итого сегодня в командах участников: %s' % team1_num, 'и %s' % team2_num)
print('Команда {} решила задач: {}'.format(team_1, score_1))
print('{} решили задачи за {} c!'.format(team_1, team1_time))
print('Команда {} решила задач: {}'.format(team_2, score_2))
print('{} решили задачи за {} c!'.format(team_2, team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {result}')
print(f'Сегодня было решенно {task_total} задач, в среднем по {time_avg:.2f} секунды на задачу!.')
