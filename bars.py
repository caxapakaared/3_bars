import json
import math


def load_data(filepath):
    with open(filepath, "r", encoding='windows-1251') as json_content:
        return json.load(json_content)


def get_biggest_bar(data):
    bar_name = ''
    max_seats_count = 0
    for bar in data:
        if bar['SeatsCount'] > max_seats_count:
            bar_name = bar['Name']
            max_seats_count = bar['SeatsCount']
    return bar_name


def get_smallest_bar(data):
    bar_name = ''
    min_seats_countn = float('Inf')
    for bar in data:
        if bar['SeatsCount'] < min_seats_countn:
            bar_name = bar['Name']
            min_seats_countn = bar['SeatsCount']
    return bar_name

def get_closest_bar(data, longitude, latitude):
    bar_name = ''
    min_distance = float('Inf')
    for bar in data:
        horizontal_distance = abs(longitude - float(bar['Longitude_WGS84']))
        vertical_distance = abs(latitude - float(bar['Latitude_WGS84']))
        distance = math.sqrt(horizontal_distance ** 2 + vertical_distance ** 2)
        if distance < min_distance:
            min_distance = distance
            bar_name = bar['Name']
    return bar_name


if __name__ == '__main__':
    json_content = load_data('data-2897-2016-11-23.json')
    print('Самый большой бар -', get_biggest_bar(json_content))
    print('Самый маленький бар -',get_smallest_bar(json_content))
    print('Введите широту и долготу через пробел')

    while True:
        try:
            latitude, longitude = (float(x) for x in input().split())
            break
        except ValueError:
            print('Что-то пошло не так, попробуйте еще раз')

    print('Ближайший бар -', get_closest_bar(json_content, longitude, latitude))
