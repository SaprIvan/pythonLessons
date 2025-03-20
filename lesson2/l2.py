a = 2
b = 2

c = int(str(a) + str(b))  # используй в этой строке явное приведение типов

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert a is not None and b is not None and c is not None
    assert isinstance(c, int), 'Переменная "с" должна иметь целочисленный тип данных (int)'
    assert c == 22, f'В переменной "с" должно находится значение 22, а было {c}'
    # вывод в терминал результата
    print(c)