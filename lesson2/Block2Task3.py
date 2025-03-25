recipient = input()
player_name = recipient[:recipient.index('@'):]
player_ships_count = input()
reward_ships_count = input()


def check_ships_count(ships_count):
    if ships_count % 20 <= 19 and ships_count % 20 >= 5 or ships_count % 20 == 0:
        return "Кораблей"
    elif ships_count % 10 == 1:
        return "Корабль"
    else: return "Корабля"


title = f'[Массовая рассылка] Уважаемый игрок Мира кораблей, {player_name}! '
body = f'''Спасибо, что любите и играете в нашу игру. \
       \nМы заметили, что у вас всего {player_ships_count} {check_ships_count(player_ships_count)}. 
        \nПоэтому, мы дарим вам подарок: {reward_ships_count} {check_ships_count(reward_ships_count)}!'''

total = title + body + 'Ваш промокод: {<вставь промокод>}'

print(total)

