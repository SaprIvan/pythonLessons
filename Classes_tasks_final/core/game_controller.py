import os
import time
from typing import Optional

from core.autobattler import AutoBattler
from core.dungeon_generator import DungeonGenerator
from data.settings import ALL_MAP
from dungeon.cell_entity import Cell
from engine.animation import TextAnimation
from engine.events import game_events, entity_events
from engine.geometry import Direction
from engine.visual import DefaultAnimation, CellType
from entities.items import BaseItem, Weapon, Armor
from entities.player import Player


class ActionsStorage:
    def __init__(self, player):
        self.player = player
        self.enemy = None

    @property
    def actions(self):
        return {
            "Пойти на Север": lambda: self.player.move(self.player.location.get_neighbour(Direction.N)),
            "Пойти на Восток": lambda: self.player.move(self.player.location.get_neighbour(Direction.E)),
            "Пойти на Запад": lambda: self.player.move(self.player.location.get_neighbour(Direction.W)),
            "Пойти на Юг": lambda: self.player.move(self.player.location.get_neighbour(Direction.S)),
            "Атаковать": lambda: AutoBattler(self.player, self.enemy).fight(),
            'Выйти из подземелья': lambda: game_events.Game_Over(self.player),
            'Поднять предмет': lambda: self.player.lift_item(),
            'Обыскать поверженного врага': lambda: self.player.looting_dead_enemy(),
        }


class GameController:
    def __init__(self):
        self.dungeon_generator: Optional[DungeonGenerator] = None
        self.actions_storage: Optional[ActionsStorage] = None
        self.__is_running = True
        game_events.Game_Over += self.stop_game
        entity_events.Lift_Item += self.describe_item
        self.__create()

    @staticmethod
    def describe_item(item: BaseItem):
        print(f'Вы нашли:\n{item.get_info()}')
        time.sleep(3)

    def stop_game(self, player: Player):
        self.__is_running = False
        msg = 'Игра окончена... '
        if player.is_dead:
            msg += ('Ваш персонаж погиб. Никто даже не узнает, что вы были в подземелье, т.к. вы отправились в путь в тайне от всех.'
                    '\nТо немногое добро, что вам удалось получить в ходе приключения, останется в подземелье и будет ждать более удачливого героя.')
        if player.location.is_end_cell:
            msg += (f'Уставший, потрёпанный и грязный, вы добрались до выхода из подземелья.\nЭто был сложный путь и вы можете гордиться собой.'
                    f'\nВаша добыча:\n{player.inventory.draw_all_items()}')
        if player.location.is_start_cell:
            msg += 'Страх толкает людей на необдуманные поступки, такие, как например, отказ от прохождения подземелья...'
        print(msg)

    def __create(self):
        self.__clear_cmd()
        create_msg = 'Добро пожаловать в игру.\n'
        for _map in ALL_MAP:
            create_msg += f'[{ALL_MAP.index(_map)}] {_map}\n'
        create_msg += 'Выберите размер карты: '
        answer = self.__input_handler(create_msg)
        self.dungeon_generator = DungeonGenerator(ALL_MAP[answer])
        self.actions_storage = ActionsStorage(self.dungeon_generator.player)
        TextAnimation(DefaultAnimation.loader, 1, 0.25).play()
        time.sleep(0.5)
        self.__clear_cmd()
        print('Создана карта:')
        self.dungeon_generator.draw_map()
        print('Добро пожаловать в подземелье, приключенец!\n'
              'У вас нет возможности выбрать персонажа, но не сомневайтесь, '
              'созданный герой взял в этот поход самое лучшее снаряжение, что у него было...')
        print(f'\nВаш персонаж:{self.dungeon_generator.player.draw_info()}\n')
        msg = 'Вы можете:\n\t[1] Начать приключение\n\t[2] Выйти из игры\n\tВаши действия: '
        answer_mapper = {
            1: lambda: self.__play(),
            2: lambda: game_events.Game_Over(self.dungeon_generator.player)
        }
        answer = self.__input_handler(msg)
        answer_mapper[answer]()

    def __play(self):
        self.__clear_cmd()
        while self.__is_running:
            msg, answer_mapper = self.__lore_maker()
            answer = self.__input_handler(msg)
            try:
                answer_mapper[answer]()
            except KeyError:
                print('Выбирать можно только из доступных действий. Никаких пасхалок тут нет. Попробуйте выбрать действие еще раз.')
                self.__clear_cmd()

    def __change_armor(self):
        self.__clear_cmd()
        answer_mapper = dict()
        msg = '[Замена снаряжения]\nДоступное снаряжение:\n\t'
        items = [item for item in self.dungeon_generator.player.inventory.items if isinstance(item, Armor)]
        index = 0
        answer_mapper.update({index: lambda: self.__play()})
        if items:
            for item in items:
                index = items.index(item) + 1
                msg += f'[{index}] {item.get_short_info()}\n\t'
                answer_mapper.update({index: lambda: entity_events.Change_Armor(items[answer - 1])})
        msg += f'[{index + 1}] Назад\n'
        msg += 'Выберите действие: '
        answer = self.__input_handler(msg)
        answer_mapper[answer]()

    def __change_weapon(self):
        self.__clear_cmd()
        answer_mapper = dict()
        msg = '[Замена оружия]\nДоступное оружие:\n\t'
        items = [item for item in self.dungeon_generator.player.inventory.items if isinstance(item, Weapon)]
        index = 0
        answer_mapper.update({index: lambda: self.__play()})
        if items:
            for item in items:
                index = items.index(item) + 1
                msg += f'[{index}] {item.get_short_info()}\n\t'
                answer_mapper.update({index: lambda: entity_events.Change_Weapon(items[answer - 1])})
        msg += f'[{index + 1}] Назад\n'
        msg += 'Выберите действие: '
        answer = self.__input_handler(msg)
        answer_mapper[answer]()

    def __lore_maker(self):
        self.__clear_cmd()
        self.dungeon_generator.draw_map()
        print(f'[{self.dungeon_generator.player.data.name}] {self.dungeon_generator.player.current_hp}\t'
              f'[Предметов в инвентаре] {self.dungeon_generator.player.inventory.items_count}\t'
              f'[Стоимость предметов в инвентаре] {self.dungeon_generator.player.inventory.calculate_items_costs()}\t')
        print(f'[В руках] {self.dungeon_generator.player.weapon.get_short_info()}\n[Надето] {self.dungeon_generator.player.armor.get_short_info()}')
        current_room: Cell = self.dungeon_generator.player.location
        answer_mapper = dict()
        msg = '\n================================================\n'
        msg += f'Перед вами: {current_room.description}.\n'

        if current_room.cell_type == CellType.player:
            if current_room.entity and not current_room.entity.is_dead:
                self.actions_storage.enemy = current_room.entity
                msg += (f'Сквозь тусклый свет, вы замечаете, что в центре комнаты кто-то находится...\n'
                        f'{current_room.entity.draw_info()}')
                msg += f'\nВы можете:\n\t1. Атаковать\n\t'
                answer_mapper.update({
                    1: self.actions_storage.actions['Атаковать']
                })
            else:
                if current_room.entity and current_room.entity.is_dead:
                    msg += f'{current_room.entity.data.death_description}\n'
                if current_room.item:
                    msg += ('В сумраке комнаты вы замечаете любопытный силуэт, это нечто неодушевленное '
                            '- артефакт давно забытой эпохи.\n')
                msg += f'Вы можете:\n\t'
                move_directions = [Direction.direction_from_int(current_room.neighbours.index(neighbour))
                                   for neighbour in current_room.neighbours
                                   if neighbour and current_room.neighbours.index(neighbour) % 2 == 0
                                   and neighbour.cell_type != CellType.wall]
                action_number = 1
                msg += f'[{action_number}] Сменить оружие\n\t'
                answer_mapper.update({action_number: lambda: self.__change_weapon()})
                action_number += 1
                msg += f'[{action_number}] Сменить броню\n\t'
                answer_mapper.update({action_number: lambda: self.__change_armor()})
                action_number += 1
                for direction in move_directions:
                    msg += f'[{action_number}] Пойти на {direction}\n\t'
                    answer_mapper.update({action_number: self.actions_storage.actions[f'Пойти на {direction}']})
                    action_number += 1
                if (current_room.entity and current_room.entity.is_dead
                        and current_room.entity.weapon and current_room.entity.armor):
                    msg += f'[{action_number}] Обыскать поверженного врага\n\t'
                    answer_mapper.update({action_number: self.actions_storage.actions['Обыскать поверженного врага']})
                if current_room.item:
                    msg += f'[{action_number}] Поднять предмет\n\t'
                    answer_mapper.update({action_number: self.actions_storage.actions['Поднять предмет']})
                if current_room.is_end_cell:
                    msg += f'[{action_number}] Выйти из подземелья\n\t'
                    answer_mapper.update({action_number: self.actions_storage.actions['Выйти из подземелья']})
            msg += 'Ваше действие: '

        return msg, answer_mapper

    @staticmethod
    def __clear_cmd():
        os.system('cls')

    @staticmethod
    def __input_handler(msg: str):
        try:
            return int(input(msg))
        except ValueError:
            print('Нужно ввести номер действия, например: 1 для действия "1. Пойти дальше".')
            return -1