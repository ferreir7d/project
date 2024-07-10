times = 'Corinthians', 'São Paulo','Palmeiras' , 'Grêmio', 'Botafogo', 'Vasco', 'Bragantino', 'Internacional', 'Flamengo', 'Cruzeiro', 'Bahia', 'Atlético Mineiro', 'Atlético Paranaênse', 'Juventude', 'Criciuma', 'Cuiabá', 'Fortaleza', 'Vitória', 'Atĺetico GO', 'Fluminense'

for time in times:
    print(time)
print('---------------' * 15)
print(f'Os 5 primeiros times do brasileirão são {times[0:5]}')
print('---------------' * 15)
print(f'Os últimos 4 colocados são {times[16:20]}')
print('---------------' * 15)
print('Os times em ordem são:')
print(sorted(times))



