sum_from_cash_receipt = int(input('Введите сумму чека игрока: '))

discount = None

if (sum_from_cash_receipt < 1001):
    discount = 5
elif (sum_from_cash_receipt < 2501):
    discount = 10
elif (sum_from_cash_receipt < 5001):
    discount = 15
else:
    discount = 20


if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert discount is not None, 'Размер скидки нужно положить в переменную discount'
    assert isinstance(sum_from_cash_receipt, (int, float)) and isinstance(discount, (
    int, float)), 'Переменные sum_from_cash_receipt и discount должны иметь числовой тип данных'

    # вывод в терминал результата
    print(f'Персональная скидка игрока: {discount}')