template = 'Мир {}'
template = template.format('Танков. %s')
template = template % 'Наша игра!'

template = f'{template} Присоединяйся к нам!'

if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    expected_result = 'Мир Танков. Наша игра! Присоединяйся к нам!'
    assert template == expected_result, f'Ожидается шаблон "{expected_result}", а был "{template}"'
    # вывод в терминал результата
    print(template)