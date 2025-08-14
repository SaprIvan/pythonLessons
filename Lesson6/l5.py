
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

if __name__ == '__main__':
	# не обращайте на это внимание, это тесты
	from random import randint
	x_1, y_1, x_2, y_2 = randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)
	vector_1 = Vector2(x_1, y_1)
	vector_2 = Vector2(x_2, y_2)
	g = Geometry()
	vectors_sum = g.add(vector_1, vector_2)
	assert isinstance(vectors_sum, int), f'Результат выполнения метода сложения векторов должен иметь тип int, а был {type(vectors_sum)}'
	assert vectors_sum == x_1 + x_2 + y_1 + y_2, 'Сумма векторов считается неверно'
	assert g.get_vector_length(vector_1) == math.sqrt(x_1**2 + y_1**2), 'Длина вектора считается неверно'
	assert not 'x' in Vector2.__dict__ and not 'y' in Vector2.__dict__, 'Атрибуты класса Vector2 должны быть динамическими, а не статическими'

	# вывод в терминал результата
	print(f'Все тесты прошли, классы реализованы верно.')