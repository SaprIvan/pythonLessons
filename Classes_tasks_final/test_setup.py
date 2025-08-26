from tests.tests_entity_data import run_entity_data_tests
from tests.tests_event import run_event_tests
from tests.tests_hp_bar import run_hp_bar_tests
from tests.tests_inventory import run_inventory_tests
from tests.tests_items import run_items_tests
from tests.tests_vector import run_vector_tests


if __name__ == '__main__':
    run_entity_data_tests()
    run_event_tests()
    run_hp_bar_tests()
    run_inventory_tests()
    run_items_tests()
    run_vector_tests()