class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x,self.y



if __name__ == '__main__':
	# не обращайте на это внимание, это тесты
	points = [Point(x=0, y=0), Point(x=-3, y=-4), Point(x=5, y=6)]
	assert not [point for point in points if point.get_coordinates() != (point.x, point.y)], 'Проверь очередность координат, которые возвращает метод get_coordinates. Должны быть x, y'
	assert not 'x' in Point.__dict__ and not 'y' in Point.__dict__, 'Атрибуты класса Point должны быть динамическими, а не статическими.'
	# вывод в терминал результата
	print(f'Все тесты прошли, класс  реализован верно.')