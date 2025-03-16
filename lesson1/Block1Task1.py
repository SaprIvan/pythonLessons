year = int(input('Введите год для проверки на високосность: '))

is_leap_year = year % 400 == 0 or year % 4 == 0 and year % 100 > 0

print(is_leap_year)
