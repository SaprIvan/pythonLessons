import statistics


class Statistics:
    @staticmethod
    def mean(data):
        return sum(data) / len(data) if len(data) > 0 else 0
    @staticmethod
    def median(data):
        return statistics.median(data) if data else 0


if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    assert not Statistics().__dict__, 'Класс Statistics не должен содержать в себе динамических атрибутов'

    mean_tests_data = [([0, 1, 2, 3, 4], 2), ([], 0), ([10], 10), ([1, 3, 5, 10], 19 / 4)]
    median_tests_data = [([0, 1, 2, 3, 4], 2), ([], 0), ([10], 10), ([1, 3, 5, 10], 4)]

    mean_errors = []
    for test_data, expected_result in mean_tests_data:
        mean = Statistics.mean(test_data)
        if mean != expected_result:
            mean_errors.append(f'Среднее для числового набора: {test_data}, рассчитывается неверно, ожидалось "{expected_result}", а было "{mean}"')
    median_errors = []
    for test_data, expected_result in median_tests_data:
        median = Statistics.median(test_data)
        if median != expected_result:
            median_errors.append(f'Медиана для числового набора: {test_data}, рассчитывается неверно, ожидалось "{expected_result}", а было "{mean}"')

    assert not mean_errors, '\n'.join(mean_errors)
    assert not median_errors, '\n'.join(median_errors)

    # вывод в терминал результата
    print(f'Все тесты прошли, класс реализован верно.')