class Cursor:
    def __init__(self):
        self.is_closed = False

    @staticmethod
    def execute(sql: str):
        print(f'Выполняем SQL скрипт: {sql}')

    def close(self):
        self.is_closed = True
        print('Закрываем курсор')


class DataBase:
    def __init__(self):
        self.__config = None
        self.__cursors = []

    def commit(self):
        print('Сделали коммит в базе данных.')

    def connect(self, config: dict):
        self.__config = config
        print(f'Подключились к базе данных. Конфигурация: {self.__config}')
        return self

    def cursor(self):
        cursor = Cursor()
        self.__cursors.append(cursor)
        return cursor

    def close(self):
        for c in self.__cursors:
            if not c.is_closed:
                c.close()
        self.__cursors = []
        print('Закрываем подключение к базе данных')


class UseDatabase:
    def __init__(self, config):
        self.config = config

    def __enter__(self):
        self.connect = DataBase().connect(self.config)
        self.cursor = self.connect.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connect.commit()
        self.connect.close()


if __name__ == '__main__':
    # не обращайте на это внимание, это тесты
    db_config = {
        'host': '127.0.0.1',
        'user': 'admin',
        'password': 'admin',
        'database': 'LAD_DB'
    }
    ud = UseDatabase(db_config)
    assert 'config' in ud.__dict__, f'Класс UseDatabase должен иметь динамический атрибут config'
    assert '__enter__' in dir(UseDatabase) and '__exit__' in dir(UseDatabase), \
        f'Класс UseDatabase должен иметь переопределенные методы __enter__ и __exit__.'
    from  contextlib import redirect_stdout
    import io
    f = io.StringIO()
    with redirect_stdout(f):
        assert isinstance(ud.__enter__(), Cursor), f'Метод __enter__ класса UseDatabase должен возвращать экземпляр класса Cursor. Фактически вернул: {type(ud.__enter__())}'

    f = io.StringIO()
    with redirect_stdout(f):
        with UseDatabase(db_config) as cursor:
            sql = 'SHOW TABLE'
            cursor.execute(sql)
    actual_printed_str = f.getvalue()
    expected_printed_str = """\
Подключились к базе данных. Конфигурация: {'host': '127.0.0.1', 'user': 'admin', 'password': 'admin', 'database': 'LAD_DB'}
Выполняем SQL скрипт: SHOW TABLE
Сделали коммит в базе данных.
Закрываем курсор
Закрываем подключение к базе данных
"""
    assert expected_printed_str == actual_printed_str, f"""\
Ожидалось, что при вызове:
    with UseDatabase(db_config) as cursor:
    sql = 'SHOW TABLE'
    cursor.execute(sql)
будет вывод сообщений такой:
{expected_printed_str}
А был такой:
{actual_printed_str}
    """
    print(actual_printed_str)
    # вывод в терминал результата
    print(f'Все тесты прошли, контекстный менеджер реализован верно.')