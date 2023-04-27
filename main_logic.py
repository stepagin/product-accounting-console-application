import datetime
import pickle
from random import randint

from input_functions import string_input


class Product:
    """
    Объект продукта.
    Поля экземпляра: id, name, price, category, date
    """
    _products_created = 0

    def __init__(self, name, price, category):
        buffer = self._products_created + 1
        while buffer in CollectionManager.get_id_list():
            buffer = randint(1, 2 * self._products_created + 10)
        self.id = buffer
        self.name = name
        self.price = price
        self.category = category
        self.date = datetime.date.today().strftime("%Y-%m-%d")
        self._products_created += 1


class Interpreter:
    """
    Считывает команды с консоли и выполняет их.
    """
    _working_flag = True

    def run(self):
        print("Добро пожаловать в программу для контроля денежных средств!")
        print("Введите команду, чтобы начать взаимодействие с программой.")
        print("Для вывода доступных команд введите help.")
        while self._working_flag:
            self._read_and_execute_command()

    def _read_and_execute_command(self):
        cn = string_input(">")
        if cn == "exit":
            self._working_flag = False
            return
        CommandManager.execute_command_by_name(cn)


class CollectionManager:
    """
    Хранит коллекцию и содержит всю логику по работе с ней.
    """
    _products = []
    _id_list = []

    @staticmethod
    def get_products():
        return CollectionManager._products.copy()

    @staticmethod
    def get_id_list():
        return CollectionManager._id_list.copy()

    @staticmethod
    def add_product(name, price, category):
        p = Product(name, price, category)
        CollectionManager._products.append(p)
        CollectionManager._id_list.append(p.id)

    @staticmethod
    def delete_product_by_id(id):
        for p in CollectionManager._products:
            if p.id == id:
                CollectionManager._products.remove(p)
                return True
        return False

    @staticmethod
    def get_columns():
        return ["id", "name", "price", "category", "date"]

    @staticmethod
    def sort_products(ascending=False):
        CollectionManager._products = sorted(CollectionManager._products, key=lambda p: p.price, reverse=ascending)

    @staticmethod
    def save_collection():
        with open("product_collection.pickle", "wb") as f:
            pickle.dump([CollectionManager.get_products(), CollectionManager.get_id_list()], f)

    @staticmethod
    def load_collection():
        with open("product_collection.pickle", "rb") as f:
            CollectionManager._products, CollectionManager._id_list = pickle.load(f)
            Product._products_created = len(CollectionManager.get_id_list())


class CommandManager:
    """
    Содержит в себе команды и их названия
    """
    _command_names = []
    _command_funcs = []

    @staticmethod
    def register_command(name, func):
        """
        Зарегистрировать команду.
        name - имя команды при работе в консоли
        func - функция команды без скобок
        """
        CommandManager._command_names.append(name)
        CommandManager._command_funcs.append(func)

    @staticmethod
    def execute_command_by_name(name):
        """
        Выполняет команду с заданным именем.
        """
        for t in range(len(CommandManager._command_names)):
            if CommandManager._command_names[t] == name:
                CommandManager._command_funcs[t]()
                return
        print("Команда не найдена. Введите help для просмотра доступных команд")
