from engine.events import entity_events
from engine.hp_bar import HealthBar
from engine.visual import Colors
from entities.entity import Entity, EntityItemTypeError
from entities.entity_data import EntityData
from entities.items import Armor, Weapon


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
    tag, armor, weapon, data = 'Player', get_armor(), get_weapon(), get_entity_data()
    entity = Entity(tag=tag, armor=armor, weapon=weapon, data=data)
    assert hasattr(entity, '_Entity__tag'), "У класса Entity должен быть приватный атрибут __tag"
    assert hasattr(entity, '_Entity__data'), "У класса Entity должен быть приватный атрибут __data"
    assert hasattr(entity, '_is_dead'), "У класса Entity должен быть протектед атрибут _is_dead"
    assert hasattr(entity, '_Entity__weapon'), "У класса Entity должен быть приватный атрибут __weapon"
    assert hasattr(entity, '_Entity__armor'), "У класса Entity должен быть приватный атрибут __armor"
    assert hasattr(entity, '_hp_bar'), "У класса Entity должен быть протектед атрибут _hp_bar"

    assert isinstance(getattr(Entity, 'tag'), property), 'У класса Entity должно быть свойство tag'
    assert isinstance(getattr(Entity, 'data'), property), 'У класса Entity должно быть свойство data'
    assert isinstance(getattr(Entity, 'is_dead'), property), 'У класса Entity должно быть свойство is_dead'
    assert isinstance(getattr(Entity, 'weapon'), property), 'У класса Entity должно быть свойство weapon'
    assert isinstance(getattr(Entity, 'armor'), property), 'У класса Entity должно быть свойство armor'
    assert isinstance(getattr(Entity, 'current_hp'), property), 'У класса Entity должно быть свойство current_hp'

    assert entity.tag == tag, f"При инициализации класса Entity с аргументами 'tag={tag}', 'armor={armor}', 'weapon={weapon}', 'data={data}', свойство tag должно было вернуть '{tag}', фактически вернуло '{entity.tag}'"
    assert entity.data == data, f"При инициализации класса Entity с аргументами 'tag={tag}', 'armor={armor}', 'weapon={weapon}', 'data={data}', свойство data должно было вернуть '{data}', фактически вернуло {entity.data}"
    assert not entity.is_dead, f"При инициализации класса Entity свойство is_dead должно было вернуть False, фактически вернуло {entity.is_dead}"
    assert entity.weapon == weapon, f"При инициализации класса Entity с аргументами 'tag={tag}', 'armor={armor}', 'weapon={weapon}', 'data={data}', свойство weapon должно было вернуть '{weapon}', фактически вернуло {entity.weapon}"
    assert entity.armor == armor, f"При инициализации класса Entity с аргументами 'tag={tag}', 'armor={armor}', 'weapon={weapon}', 'data={data}', свойство armor должно было вернуть '{armor}', фактически вернуло {entity.armor}"
    hp_bar = HealthBar(bar_color=Colors.default, max_health=data.health).draw(data.hp)
    assert entity.current_hp == hp_bar, f"При инициализации класса Entity свойство current_hp должно было вернуть {hp_bar}, фактически вернуло {entity.current_hp}"

    assert entity._Entity__tag == 'Player', f"При инициализации класса Entity с аргументами 'tag={tag}', 'armor={armor}', 'weapon={weapon}', 'data={data}', приватный атрибут __tag должен быть '{tag}', фактически вернул '{entity._Entity__tag}'"
    assert entity._Entity__data == data, f"При инициализации класса Entity с аргументами 'tag={tag}', 'armor={armor}', 'weapon={weapon}', 'data={data}', приватный атрибут __data должен быть {data}, фактически вернул {entity._Entity__data}"
    assert entity._is_dead == False, f"При инициализации класса Entity протектед атрибут _is_dead должен быть False, фактически вернул {entity._is_dead}"
    assert entity._Entity__weapon == weapon, f"При инициализации класса Entity с аргументами 'tag={tag}', 'armor={armor}', 'weapon={weapon}', 'data={data}', приватный атрибут должен быть {weapon}, фактически вернул {entity._Entity__weapon}"
    assert entity._Entity__armor == armor, f"При инициализации класса Entity с аргументами 'tag={tag}', 'armor={armor}', 'weapon={weapon}', 'data={data}', приватный атрибут должен быть {armor}, фактически вернул {entity._Entity__armor}"
    assert entity._hp_bar.draw(data.hp) == hp_bar, f"Метод draw у протектед атрибут _hp_bar должен был вернуть {entity._hp_bar.draw(data.hp)}, фактически вернул {entity._hp_bar.draw(data.hp)}"


def test_entity_weapon_setter():
    tag = "Enemy"
    armor = get_armor()
    weapon = get_weapon()
    data = get_entity_data()

    entity = Entity(tag=tag, armor=armor, weapon=weapon, data=data)

    new_weapon = Weapon(name="Iron Sword", description="A sturdy iron sword.", cost=75, damage=25, hit_chance=80)
    entity.weapon = new_weapon

    assert entity.weapon == new_weapon, "Свойство weapon у класса Entity, после изменения значения на новое с типом Weapon, должно было измениться. Фактически не изменилось."
    entity.weapon = None
    assert entity.weapon is None, "Свойство weapon у класса Entity, после изменения значения на новое с типом None, должно было измениться. Фактически не изменилось."
    try:
        entity.weapon = "Not a weapon"
        assert False, "Установка значения для weapon у класса Entity с неправильным типом должна вызывать EntityItemTypeError"
    except EntityItemTypeError:
        pass


def test_entity_armor_setter():
    tag = "Enemy"
    armor = get_armor()
    weapon = get_weapon()
    data = get_entity_data()

    entity = Entity(tag=tag, armor=armor, weapon=weapon, data=data)

    new_armor = Armor(name="Iron Armor", description="A sturdy iron armor.", cost=100, defence=50)
    entity.armor = new_armor

    assert entity.armor == new_armor, "Свойство armor у класса Entity, после изменения значения на новое с типом Armor, должно было измениться. Фактически не изменилось."
    entity.armor = None
    assert entity.armor is None, "Свойство armor у класса Entity, после изменения значения на новое с типом None, должно было измениться. Фактически не изменилось."
    try:
        entity.armor = "Not an armor"
        assert False, "Установка значения для armor у класса Entity с неправильным типом должна вызывать EntityItemTypeError"
    except EntityItemTypeError:
        pass


def test_entity_draw_info():
    tag = "Enemy"
    armor = get_armor()
    weapon = get_weapon()
    data = get_entity_data()

    entity = Entity(tag=tag, armor=armor, weapon=weapon, data=data)
    hp_bar = HealthBar(bar_color=Colors.default, max_health=data.health).draw(data.hp)
    expected_info = (f'\n[{data.name}] {hp_bar}\n'
                     f'{data.description}\n'
                     f'=======[В руках]=======\n'
                     f'{weapon.get_short_info()}\n'
                     f'=======[Надето]=======\n'
                     f'{armor.get_short_info()}\n')

    assert entity.draw_info() == expected_info, f"Метод draw_info у класса Entity должен возвращать '{expected_info}', фактически вернул '{entity.draw_info()}'"


def test_entity_die():
    tag = "Enemy"
    armor = get_armor()
    weapon = get_weapon()
    data = get_entity_data()

    entity = Entity(tag=tag, armor=armor, weapon=weapon, data=data)

    try:
        entity.die()
        assert False, "Метод die не должен иметь реализации в классе Entity"
    except NotImplementedError:
        pass


def test_entity_calculate_damage_miss():
    tag = "Enemy"
    armor = Armor(name="Leather Armor", description="Light and flexible.", cost=50, defence=10)
    weapon = Weapon(name="Rusty Sword", description="A slightly rusted sword.", cost=30, damage=10, hit_chance=0)
    data = EntityData(name="Goblin", hp=50, description="A small, green creature.", death_description="The goblin lies motionless on the ground.")

    entity = Entity(tag=tag, armor=armor, weapon=weapon, data=data)
    target = Entity(tag="Player", armor=armor, weapon=weapon, data=data)

    damage = entity._Entity__calculate_damage(target)
    assert damage == 0, f"Метод __calculate_damage класса Entity, при промахе, должен вернуть 0, фактически вернул {damage}."


def test_entity_calculate_damage_no_damage():
    tag = "Enemy"
    armor = Armor(name="Leather Armor", description="Light and flexible.", cost=50, defence=10)
    weapon = Weapon(name="Rusty Sword", description="A slightly rusted sword.", cost=30, damage=10, hit_chance=100)
    data = EntityData(name="Goblin", hp=50, description="A small, green creature.", death_description="The goblin lies motionless on the ground.")

    entity = Entity(tag=tag, armor=armor, weapon=weapon, data=data)
    target = Entity(tag="Player", armor=Armor(name="Iron Armor", description="A sturdy iron armor.", cost=100, defence=15), weapon=weapon, data=data)

    damage = entity._Entity__calculate_damage(target)
    assert damage == 0, f"Метод __calculate_damage класса Entity, когда урон атакующего и защита атакуемого равны, должен вернуть 0, фактически вернул {damage}"


def test_entity_calculate_damage_partial_damage():
    tag = "Enemy"
    armor = Armor(name="Leather Armor", description="Light and flexible.", cost=50, defence=10)
    weapon = Weapon(name="Rusty Sword", description="A slightly rusted sword.", cost=30, damage=20, hit_chance=100)
    data = EntityData(name="Goblin", hp=50, description="A small, green creature.", death_description="The goblin lies motionless on the ground.")

    entity = Entity(tag=tag, armor=armor, weapon=weapon, data=data)
    target = Entity(tag="Player", armor=Armor(name="Iron Armor", description="A sturdy iron armor.", cost=100, defence=15), weapon=weapon, data=data)

    damage = entity._Entity__calculate_damage(target)
    assert damage == 5, f"Метод __calculate_damage класса Entity, когда урон атакующего 20, а защита атакуемого 15, должен вернуть 5, фактически вернул {damage}"


def test_entity_calculate_damage_full_damage():
    tag = "Enemy"
    armor = Armor(name="Leather Armor", description="Light and flexible.", cost=50, defence=10)
    weapon = Weapon(name="Rusty Sword", description="A slightly rusted sword.", cost=30, damage=30, hit_chance=100)
    data = EntityData(name="Goblin", hp=50, description="A small, green creature.", death_description="The goblin lies motionless on the ground.")

    entity = Entity(tag=tag, armor=armor, weapon=weapon, data=data)
    target = Entity(tag="Player", armor=Armor(name="Leather Armor", description="Light and flexible.", cost=50, defence=0), weapon=weapon, data=data)

    damage = entity._Entity__calculate_damage(target)
    assert damage == 30, f"Метод __calculate_damage класса Entity, когда урон атакующего 30, а защита атакуемого 0, должен вернуть 30, фактически вернул {damage}"


def __damage(self, target: Entity, damage: int):
    target.taking_damage(damage)


def test_entity_attack_miss():
    tag = "Enemy"
    armor = Armor(name="Leather Armor", description="Light and flexible.", cost=50, defence=10)
    weapon = Weapon(name="Rusty Sword", description="A slightly rusted sword.", cost=30, damage=10, hit_chance=0)
    data = EntityData(name="Goblin", hp=50, description="A small, green creature.", death_description="The goblin lies motionless on the ground.")

    entity = Entity(tag=tag, armor=armor, weapon=weapon, data=data)
    target = Entity(tag="Player", armor=armor, weapon=weapon, data=data)
    entity_events.Attack += __damage
    entity.attack(target)
    entity_events.Attack -= __damage
    assert target.data.hp == 50, f'При промахе атакуемого, hp цели меняться не должен. Сверьте реализацию методов taking_damage и __calculate_damage с заданием.'


def test_entity_attack_partial_damage():
    tag = "Enemy"
    armor = Armor(name="Leather Armor", description="Light and flexible.", cost=50, defence=10)
    weapon = Weapon(name="Rusty Sword", description="A slightly rusted sword.", cost=30, damage=20, hit_chance=100)
    data = EntityData(name="Goblin", hp=50, description="A small, green creature.", death_description="The goblin lies motionless on the ground.")

    entity = Entity(tag=tag, armor=armor, weapon=weapon, data=data)
    target = Entity(tag="Player", armor=Armor(name="Iron Armor", description="A sturdy iron armor.", cost=100, defence=15), weapon=weapon, data=data)
    entity_events.Attack += __damage
    entity.attack(target)
    entity_events.Attack -= __damage
    assert target.data.hp == 45, (f'Ожидалось, при уроне оружия атакующего 20 и защиты цели 15, у цели, после нанесения '
                                  f'урона, из 50 hp останется 45 hp, а осталось {target.data.hp}. Сверьте реализацию методов taking_damage и __calculate_damage с заданием.')


def test_entity_attack_full_damage():
    tag = "Enemy"
    armor = Armor(name="Leather Armor", description="Light and flexible.", cost=50, defence=10)
    weapon = Weapon(name="Rusty Sword", description="A slightly rusted sword.", cost=30, damage=30, hit_chance=100)
    data = EntityData(name="Goblin", hp=50, description="A small, green creature.", death_description="The goblin lies motionless on the ground.")

    entity = Entity(tag=tag, armor=armor, weapon=weapon, data=data)
    target = Entity(tag="Player", armor=Armor(name="Leather Armor", description="Light and flexible.", cost=50, defence=0), weapon=weapon, data=data)

    entity_events.Attack += __damage
    entity.attack(target)
    entity_events.Attack -= __damage
    assert target.data.hp == 20, (f'Ожидалось, при уроне оружия атакующего 30 и защиты цели 0, у цели, после нанесения'
                                  f' урона, из 50 hp останется 20 hp, а осталось {target.data.hp}. Сверьте реализацию методов taking_damage и __calculate_damage с заданием.')


def test_entity_attack_no_damage():
    tag = "Enemy"
    armor = Armor(name="Leather Armor", description="Light and flexible.", cost=50, defence=10)
    weapon = Weapon(name="Rusty Sword", description="A slightly rusted sword.", cost=30, damage=10, hit_chance=100)
    data = EntityData(name="Goblin", hp=50, description="A small, green creature.", death_description="The goblin lies motionless on the ground.")

    entity = Entity(tag=tag, armor=armor, weapon=weapon, data=data)
    target = Entity(tag="Player", armor=Armor(name="Iron Armor", description="A sturdy iron armor.", cost=100, defence=15), weapon=weapon, data=data)

    entity_events.Attack += __damage
    entity.attack(target)
    entity_events.Attack -= __damage
    assert target.data.hp == 50, (f'Ожидалось, при уроне оружия атакующего 10 и защиты цели 10, у цели, после нанесения'
                                  f' урона, из 50 hp останется 50 hp, а осталось {target.data.hp}. Сверьте реализацию методов taking_damage и __calculate_damage с заданием.')


def __die(entity: Entity):
    entity.die()


def test_entity_event_die():
    tag = "Enemy"
    armor = Armor(name="Leather Armor", description="Light and flexible.", cost=50, defence=10)
    weapon = Weapon(name="Rusty Sword", description="A slightly rusted sword.", cost=30, damage=50, hit_chance=100)
    data = EntityData(name="Goblin", hp=50, description="A small, green creature.", death_description="The goblin lies motionless on the ground.")

    entity = Entity(tag=tag, armor=armor, weapon=weapon, data=data)
    target = Entity(tag="Player", armor=Armor(name="Iron Armor", description="A sturdy iron armor.", cost=100, defence=0), weapon=weapon, data=data)

    try:
        entity_events.Attack += __damage
        entity_events.Die += __die
        entity.attack(target)
        assert False, 'Ожидалось, что при hp цели ниже или равном 0, вызовется событие Die.'
    except NotImplementedError:
        pass
    finally:
        entity_events.Attack -= __damage
        entity_events.Die -= __die


def run_entity_tests():
    print(f'{Colors.yellow}===Тестируем класс Entity==={Colors.default}')
    test_initialize()
    test_entity_weapon_setter()
    test_entity_armor_setter()
    test_entity_draw_info()
    test_entity_die()

    test_entity_calculate_damage_miss()
    test_entity_calculate_damage_no_damage()
    test_entity_calculate_damage_partial_damage()
    test_entity_calculate_damage_full_damage()

    test_entity_attack_miss()
    test_entity_attack_partial_damage()
    test_entity_attack_full_damage()
    test_entity_attack_no_damage()

    test_entity_event_die()

    print(f'{Colors.green}+++Все тесты прошли, класс Entity реализован верно.+++{Colors.default}')
    print('====================')