from main_logic import *
from prettytable import PrettyTable
from input_functions import *


def _print_table(condition=lambda p: True):
    """
    Печатает на экран таблицу с продуктами

    Параметр condition: условие по которому выводить строки
    По умолчанию выводит все строки
    """
    th = CollectionManager.get_columns()
    table = PrettyTable(th)
    products = CollectionManager.get_products()
    for p in products:
        if condition(p):
            table.add_row([p.id, p.name, p.price, p.category, p.date])

    print(table)


def help_command():
    s = """Список команд:
    help - вывести команды
    add - добавить покупку
    delete - удалить покупку
    show - просмотреть все покупки
    category - показать покупки из заданной категории
    date - вывести покупки по заданной дате
    sort - отсортировать покупки по стоимости
    save - сохранить коллекцию в файл
    load - загрузить коллекцию из файла
    exit - выйти из программы без сохранения\n"""
    print(s)


def show_command():
    _print_table()


def add_command():
    name = string_input("Введите наименование: ")
    price = float_input("Введите стоимость: ")
    category = string_input("Введите категорию: ")
    CollectionManager.add_product(name, price, category)
    print("Продукт успешно добавлен")


def delete_command():
    p_id = int(float_input("Введите id продукта: "))
    print(p_id)
    if CollectionManager.delete_product_by_id(p_id):
        print("Элемент успешно удалён")
    else:
        print("Элемент с заданным id не найден")


def category_command():
    category = string_input("Введите категорию: ")
    print('Продукты из категории "' + category + '":')
    _print_table(lambda p: p.category == category)


def date_command():
    date = date_input()
    print('Продукты в эту дату:')
    _print_table(lambda p: p.date == date)


def sort_command():
    print("Сортировка продуктов по возрастанию стоимости.")
    print("Если хотите отсортировать по убыванию, введите yes, иначе оставьте поле пустым:")
    how = input()
    if how == "yes":
        CollectionManager.sort_products(ascending=True)
    else:
        CollectionManager.sort_products()
    print("Успешно отсортировано")


def save_command():
    try:
        CollectionManager.save_collection()
        print("Коллекция сохранена в файл product_collection.pickle")
    except Exception:
        print("Произошла ошибка при сохранении в файл")


def load_command():
    try:
        CollectionManager.load_collection()
        print("Коллекция успешно загружена")
    except Exception:
        print("Произошла ошибка при загрузке коллекции")
