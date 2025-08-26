from core.game_controller import GameController
from engine.visual import Colors
from tests.tests_animation import run_animation_tests
from tests.tests_cell import run_cell_tests
from tests.tests_configs import run_configs_tests
from tests.tests_enemy import run_enemy_tests
from tests.tests_entities_loader import run_entities_loader_tests
from tests.tests_entity import run_entity_tests
from tests.tests_entity_data import run_entity_data_tests
from tests.tests_event import run_event_tests
from tests.tests_hp_bar import run_hp_bar_tests
from tests.tests_inventory import run_inventory_tests
from tests.tests_items import run_items_tests
from tests.tests_player import run_player_tests
from tests.tests_vector import run_vector_tests

if __name__ == '__main__':
    try:
        run_entity_data_tests()
        run_event_tests()
        run_hp_bar_tests()
        run_inventory_tests()
        run_items_tests()
        run_vector_tests()
        run_entity_tests()
        run_cell_tests()
        run_configs_tests()
        run_animation_tests()
        run_enemy_tests()
        run_player_tests()
        run_entities_loader_tests()
        print(f'{Colors.green}ВСЕ ТЕСТЫ ПРОЙДЕНЫ. ЗАПУСКАЕМ ИРГУ.{Colors.default}')
    except AssertionError as e:
        print(f'{Colors.red}Все тесты должны быть пройдены, перед запуском игры.{Colors.default}')
        raise e
    game = GameController()