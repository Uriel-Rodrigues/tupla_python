#cre uma tupla preenchida com os 15 primeiros colocados da NBA na ordem e depois mostre
# [1] os 5 primeiros times
# [2] os ultimos 4 colocados
# [3] times em ordem alfabetica
# [4] em que posição esta o time TORONTO RAPTORS

times = ('Miami Heat','Boston Celtics','Milwaukee Bucks','Philadelphia 76ers',
         'Toronto Raptors','Chicago Bulls','Brooklyn Nets','Cleveland Cavaliers',
         'Atlanta Hawks','Charlotte Hornets','New York Knicks','Washington Wizards',
         'Indiana Pacers','Detroit Pistons','Orlando Magic')
print('-='*25)
print(f'[1] 5 primeiros colocados da NBA {times[0:5]}')
print('-='*25)
print(f'[2] ultimos 4 colocados da NBA {times[-4:]}')
print('-='*25)
print(f'[3] times em ordem alfabetica {sorted(times)}')
print('-='*25)
print(f'[4] posição do time TORONTO RAPTORS, posição {times.index("Toronto Raptors")+1}ª')