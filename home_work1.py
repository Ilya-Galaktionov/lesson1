climate = {
    'city': 'Москва',
    'temperature': 20,
}
print(climate['city'])
climate['temperature'] = climate['temperature'] - 5
print(climate)
print(climate.get('country'))
climate['country'] = 'Россия'
climate['date'] = '27.05.2019'
print(len(climate))