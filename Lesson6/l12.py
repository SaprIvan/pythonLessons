class EntityData: #name, description, hp, health и death_description
    def __init__(self, name, description, hp, death_description):
        self.__name = name
        self.__description = description
        self.__health = self.__hp = hp
        self.__death_description = death_description

    @property
    def name(self):
        return self.__name
    @property
    def description(self):
        return self.__description
    @property
    def health(self):
        return self.__health
    @property
    def death_description(self):
        return self.__death_description
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, value):
        self.__hp = int(round(value, 0))


if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    name, hp = 'Герман из Ливии', 10
    description = 'Вам за 50 лет, по местным меркам - глубокая старость. Но несбывшиеся мечты молодости толкают вас на авантюры.'
    death_description = 'Ваша кончина была быстрой. Вы даже не поняли, как погибли.'
    ed = EntityData(name=name, description=description, hp=hp, death_description=death_description)
    assert all([
        hasattr(ed, '_EntityData__name'), hasattr(ed, '_EntityData__hp'), hasattr(ed, '_EntityData__health'),
        hasattr(ed, '_EntityData__description'), hasattr(ed, '_EntityData__death_description')
    ]), 'Атрибуты name, description, hp, health и death_description у класса EntityData должны быть приватными.'
    assert all([
        isinstance(getattr(EntityData, 'name'), property), isinstance(getattr(EntityData, 'hp'), property), isinstance(getattr(EntityData, 'health'), property),
        isinstance(getattr(EntityData, 'description'), property), isinstance(getattr(EntityData, 'death_description'), property)
    ]), 'Класс EntityData должен содержать в себе свойства (property) name, description, hp, health и death_description'
    tests_hp = [(8, 8), (8.7, 9), (3.2, 3)]
    errors = []
    for new_hp, expected_hp in tests_hp:
        ed.hp = new_hp
        if ed.hp != expected_hp:
            errors.append(f'Сеттер hp класса EntityData работает некорректно. Ожидалось, '
                          f'что при входящем значении {new_hp}, значение атрибута hp будет {expected_hp}, а было {ed.hp}')
    assert not errors, '\n'.join(errors)
    assert ed.health == hp, 'Атрибут health не должен изменяться при изменении атрибута hp'

    # вывод в терминал результата
    print(f'Все тесты прошли, класс реализован верно.')
    print(f'Ваш персонаж: {ed.name}\nОписание: {ed.description}\n'
          f'Текущее здоровье: {ed.hp}\nВаш персонаж погиб: {ed.death_description}')