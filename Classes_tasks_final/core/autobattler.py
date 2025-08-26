from engine.animation import TextAnimation
from engine.events import entity_events, game_events
from engine.visual import Colors, Emotion
from entities.enemy import Enemy
from entities.entity import Entity
from entities.player import Player


class AutoBattler:
    def __init__(self, player: Player, enemy: Enemy):
        self.player = player
        self.enemy = enemy
        self.__log = []
        self.__looser = None
        entity_events.Attack += self.__damage
        entity_events.Die += self.__kill_entity

    def __battle_template(self, player_emotion, enemy_emotion, text):
        max_len = 100
        text_len = len(text)
        residual = max_len - text_len
        part_1 = int(residual / 2)
        part_2 = residual - part_1
        text = f'{"-"*part_1}{text}{"-"*part_2}'
        return (f'[{self.player.data.name}]{self.player.current_hp}[{Colors.green}{player_emotion}{Colors.default}] '
                f'{text} '
                f'[{Colors.red}{enemy_emotion}{Colors.default}]{self.enemy.current_hp}[{self.enemy.data.name}]')

    def fight(self):
        self.__log.clear()
        print(f'Вы решительно бросаетесь на противника. Завязался бой:')
        while True:
            self.__log.append(self.__battle_template(Emotion.action, Emotion.confuse, 'Вы наносите удар!'))
            self.player.attack(self.enemy)
            if self.enemy.is_dead:
                break
            self.__log.append(self.__battle_template(
                Emotion.confuse, Emotion.action, f'{self.enemy.data.name} наносит ответный удар. Берегитесь!')
            )
            self.enemy.attack(self.player)
            if self.player.is_dead:
                break
        TextAnimation(self.__log).play()
        if self.player.is_dead:
            game_events.Game_Over(self.player)
        self.destroy()

    def __damage(self, attacker: Entity, target: Entity, damage: int):
        target.taking_damage(damage)
        if damage <= 0:
            player_emotion = Emotion.action if target.tag == 'Player' else Emotion.confuse
            enemy_emotion = Emotion.confuse if target.tag == 'Player' else Emotion.action
            self.__log.append(self.__battle_template(
                player_emotion, enemy_emotion, f'{target.data.name} смог увернулся от удара.')
            )
        else:
            player_emotion = Emotion.confuse if target.tag == 'Player' else Emotion.action
            enemy_emotion = Emotion.action if target.tag == 'Player' else Emotion.confuse
            self.__log.append(self.__battle_template(
                player_emotion, enemy_emotion, f'Удар пришелся точно в цель! {attacker.data.name} наносит "{damage}" урона.')
            )
        if self.__looser:
            if self.__looser.tag == 'Player':
                self.__log.append(self.__battle_template(
                    Emotion.dead, Emotion.winner, f'Вы храбро сражались, но {self.enemy.data.name} оказался сильнее.')
                )
                self.__log.append(self.__battle_template(
                    Emotion.dead, Emotion.winner, self.__looser.data.death_description)
                )
            else:
                self.__log.append(self.__battle_template(
                    Emotion.winner, Emotion.dead, f'Вы одержали победу над {self.enemy.data.name}!')
                )
                self.__log.append(self.__battle_template(
                    Emotion.winner, Emotion.dead, self.__looser.data.death_description)
                )

    def __kill_entity(self, entity: Entity):
        self.__looser = entity
        entity.die()

    def destroy(self):
        entity_events.Attack -= self.__damage
        entity_events.Die -= self.__kill_entity
