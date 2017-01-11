import json
import math


def load_data(filepath):
    with open(filepath, "r", encoding='windows-1251') as json_content:
        return json.load(json_content)


def get_biggest_bar(data):
    bar = max(data, key = lambda bar: bar['SeatsCount'])
    return bar['Name']

def get_smallest_bar(data):
    bar = min(data, key = lambda bar: bar['SeatsCount'])
    return bar['Name']

def get_closest_bar(data, longitude, latitude):
    for bar in data:
        horizontal_distance = abs(longitude - float(bar['Longitude_WGS84']))
        vertical_distance = abs(latitude - float(bar['Latitude_WGS84']))
        bar['Distance'] = math.sqrt(horizontal_distance ** 2 + vertical_distance ** 2)
    closest_bar = min(data, key = lambda bar: bar['Distance'])
    return closest_bar['Name']

if __name__ == '__main__':
    json_content = load_data('data-2897-2016-11-23.json')
    print('Самый большой бар -', get_biggest_bar(json_content))
    print('Самый маленький бар -',get_smallest_bar(json_content))
    print('Введите широту и долготу через пробел')
    try:
        latitude, longitude = (float(x) for x in input().split())
        print('Ближайший бар -', get_closest_bar(json_content, longitude, latitude))
    except ValueError:
        print('Ошибка ввода. Программа завершена')
