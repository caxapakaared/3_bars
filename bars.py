import json
import math


def load_data(filepath):
	with open(filepath, "r", encoding='windows-1251') as file:
		return json.load(file)


def get_biggest_bar(data):
	name = ''
	maxSeatsCount = 0
	for i in data:
		if i['SeatsCount'] > maxSeatsCount:
			name = i['Name']
			maxSeatsCount = i['SeatsCount']
	return name


def get_smallest_bar(data):
	name = ''
	minSeatsCount = float('Inf')
	for i in data:
		if i['SeatsCount'] < minSeatsCount:
			name = i['Name']
			minSeatsCount = i['SeatsCount']
	return name

def get_closest_bar(data, longitude, latitude):
	name = ''
	min_distance = float('Inf')
	for i in data:
		x = abs(longitude - float(i['Longitude_WGS84']))
		y = abs(latitude - float(i['Latitude_WGS84']))
		distance = math.sqrt(x * x + y * y)
		if distance < min_distance:
			min_distance = distance
			name = i['Name']
			print(x, y, min_distance) 
	return name


if __name__ == '__main__':
	data = load_data('data-2897-2016-11-23.json')
	print('Самый большой бар -', get_biggest_bar(data))
	print('Самый маленький бар -',get_smallest_bar(data))
	print('Введите Вашу долготу и ширину через пробел')
	
	while True:
		try:
			latitude, longitude = (float(x) for x in input().split())
			break
		except ValueError:
			print('Что-то пошло не так, попробуйте еще раз')

	print('Ближайший к вам бар - ', get_closest_bar(data, longitude, latitude))


