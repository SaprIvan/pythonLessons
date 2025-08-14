
import math
# место для вашей реализации

class Vector2:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Geometry:
	def get_vector_length(self, vector1):
		return math.sqrt(pow(vector1.x, 2) + pow(vector1.y, 2))

	def add(self, vector1, vector2):
		return vector1.x + vector2.x + vector1.y + vector2.y
	def get_segment_length(self, segment):
		return math.sqrt((segment.end.x - segment.begin.x) ** 2 + (segment.end.y - segment.begin.y) ** 2)

class Segment:
	def __init__(self, begin,  end):
		self.begin = begin
		self.end = end


if __name__ == '__main__':
	# не обращайте на это внимание, это тесты
	from random import randint
	x_1, y_1, x_2, y_2 = randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)
	vector_1 = Vector2(x_1, y_1)
	vector_2 = Vector2(x_2, y_2)
	segment = Segment(begin=vector_1, end=vector_2)
	g = Geometry()
	assert getattr(g, 'get_vector_length', None) and getattr(g, 'get_segment_length', None) and getattr(g, 'add', None), \
		'Класс Geometry должен иметь методы "get_vector_length", "get_segment_length" и "add"'
	assert g.get_segment_length(segment) == math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2), 'Длина отрезка считается неверно'
	assert getattr(segment.begin, 'x', None) and getattr(segment.begin, 'y', None), 'Класс Vector2 должен иметь атрибуты "x" и "y"'
	assert not 'x' in Vector2.__dict__ and not 'y' in Vector2.__dict__, 'Атрибуты класса Vector2 должны быть динамическими, а не статическими'
	assert not 'begin' in Segment.__dict__ and not 'end' in Segment.__dict__, 'Атрибуты класса Segment должны быть динамическими, а не статическими'

	# вывод в терминал результата
	print(f'Все тесты прошли, классы реализованы верно.')