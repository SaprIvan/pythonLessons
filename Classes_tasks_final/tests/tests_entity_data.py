from engine.visual import Colors
from entities.entity_data import EntityData


def get_test_entity_data():
    name, hp = 'Герман из Ливии', 10
    description = 'Вам за 50 лет, по местным меркам - глубокая старость. Но несбывшиеся мечты молодости толкают вас на авантюры.'
    death_description = 'Ваша кончина была быстрой. Вы даже не поняли, как погибли.'
    return EntityData(name=name, description=description, hp=hp, death_description=death_description)


def test_initialize():
    ed = get_test_entity_data()
    assert all([
        hasattr(ed, '_EntityData__name'), hasattr(ed, '_EntityData__hp'), hasattr(ed, '_EntityData__health'),
        hasattr(ed, '_EntityData__description'), hasattr(ed, '_EntityData__death_description')
    ]), 'Атрибуты name, description, hp, health и death_description у класса EntityData должны быть приватными.'
    assert all([
        isinstance(getattr(EntityData, 'name'), property), isinstance(getattr(EntityData, 'hp'), property), isinstance(getattr(EntityData, 'health'), property),
        isinstance(getattr(EntityData, 'description'), property), isinstance(getattr(EntityData, 'death_description'), property)
    ]), 'Класс EntityData должен содержать в себе свойства (property) name, description, hp, health и death_description'


def test_hp():
    ed = get_test_entity_data()
    tests_hp = [(8, 8), (8.7, 9), (3.2, 3)]
    errors = []
    for new_hp, expected_hp in tests_hp:
        ed.hp = new_hp
        if ed.hp != expected_hp:
            errors.append(f'Сеттер hp класса EntityData работает некорректно. Ожидалось, '
                          f'что при входящем значении {new_hp}, значение атрибута hp будет {expected_hp}, а было {ed.hp}')
    assert not errors, '\n'.join(errors)
    assert ed.health == 10, 'Атрибут health не должен изменяться при изменении атрибута hp'


def run_entity_data_tests():
    print(f'{Colors.yellow}===Тестируем класс EntityData==={Colors.default}')
    test_initialize()
    test_hp()
    ed = get_test_entity_data()
    print(f'{Colors.green}+++Все тесты прошли, класс EntityData реализован верно.+++{Colors.default}')
    print(f'Ваш персонаж: {ed.name}\nОписание: {ed.description}\n'
          f'Текущее здоровье: {ed.hp}\nВаш персонаж погиб: {ed.death_description}')
    print('====================')