from engine.visual import Colors
from entities.enemy import Enemy
from entities.entity_data import EntityData
from entities.items import Weapon, Armor


def get_armor():
    name, description = 'Легкий кожаный доспех', 'Сшитый из крыс кожанный доспех. Пахнет ужасно, но вроде бы защищает от урона.'
    cost, defence = 10, 2
    return Armor(name=name, cost=cost, description=description, defence=defence)


def get_weapon():
    name, description = 'Опасная дубина', 'Крепкая сосновая ветка с вбитым ржавым гвоздем на конце.'
    cost, damage, hit_chance = 4, 5, 75
    return Weapon(name=name,cost=cost, description=description, damage=damage, hit_chance=hit_chance)


def get_entity_data():
    name, hp = 'Герман из Ливии', 10
    description = 'Вам за 50 лет, по местным меркам - глубокая старость. Но несбывшиеся мечты молодости толкают вас на авантюры.'
    death_description = 'Ваша кончина была быстрой. Вы даже не поняли, как погибли.'
    return EntityData(name=name, description=description, hp=hp, death_description=death_description)


def test_initialize():
    armor = get_armor()
    weapon = get_weapon()
    data = get_entity_data()
    enemy = Enemy(armor=armor, weapon=weapon, data=data)

    assert hasattr(enemy, '_Entity__tag'), "Класс Enemy должен наследоваться от Entity"

    assert isinstance(getattr(Enemy, 'tag'), property), 'Для класса Enemy должно быть доступно свойство tag родительского класса Entity'
    assert isinstance(getattr(Enemy, 'data'), property), 'Для класса Enemy должно быть доступно свойство data родительского класса Entity'
    assert isinstance(getattr(Enemy, 'is_dead'), property), 'Для класса Enemy должно быть доступно свойство is_dead родительского класса Entity'
    assert isinstance(getattr(Enemy, 'weapon'), property), 'Для класса Enemy должно быть доступно свойство weapon родительского класса Entity'
    assert isinstance(getattr(Enemy, 'armor'), property), 'Для класса Enemy должно быть доступно свойство armor родительского класса Entity'
    assert isinstance(getattr(Enemy, 'current_hp'), property), 'Для класса Enemy должно быть доступно свойство current_hp родительского класса Entity'

    assert enemy.tag == 'Enemy', f"При инициализации класса Enemy, свойство tag должно было вернуть 'Enemy', фактически вернуло '{enemy.tag}'"
    assert enemy.data == data, f"При инициализации класса Enemy с аргументами 'armor={armor}', 'weapon={weapon}', 'data={data}', свойство data должно было вернуть '{data}', фактически вернуло {enemy.data}"
    assert not enemy.is_dead, f"При инициализации класса Enemy свойство is_dead должно было вернуть False, фактически вернуло {enemy.is_dead}"
    assert enemy.weapon == weapon, f"При инициализации класса Enemy с аргументами 'armor={armor}', 'weapon={weapon}', 'data={data}', свойство weapon должно было вернуть '{weapon}', фактически вернуло {enemy.weapon}"
    assert enemy.armor == armor, f"При инициализации класса Enemy с аргументами 'armor={armor}', 'weapon={weapon}', 'data={data}', свойство armor должно было вернуть '{armor}', фактически вернуло {enemy.armor}"
    assert enemy._hp_bar.bar_color == Colors.red, f'Для bar_color класса HealthBar, который хранится в атрибуте _hp_bar класса Entity, при создании класса Enemy должен был быть установлен цвет {Colors.red}ЦВЕТ{Colors.default}, фактически был {enemy._hp_bar.bar_color}ЦВЕТ{Colors.default}'


def test_enemy_die():
    armor = get_armor()
    weapon = get_weapon()
    data = get_entity_data()
    enemy = Enemy(armor=armor, weapon=weapon, data=data)
    enemy.die()
    assert enemy.is_dead, 'После вызова метода die класса Enemy, атрибут is_dead должен был измениться на True.'


def run_enemy_tests():
    print(f'{Colors.yellow}===Тестируем класс Enemy==={Colors.default}')
    test_initialize()
    test_enemy_die()
    print(f'{Colors.green}+++Все тесты прошли, класс Enemy реализован верно.+++{Colors.default}')
    print('====================')
