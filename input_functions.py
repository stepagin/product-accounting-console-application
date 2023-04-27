import datetime


def string_input(message=""):
    """
    Вводит непустую строку с клавиатуры
    """
    res = ""
    while res == "":
        res = input(message).strip()
    return res


def float_input(message=""):
    """
    Вводит число с клавиатуры
    """
    res = ""
    while res == "":
        buffer = input(message).replace(",", ".").strip()
        try:
            res = float(buffer)
            break
        except ValueError:
            continue
    return res


def date_input():
    """
    Вводит дату с клавиатуры
    """
    date = ""
    while date == "":
        y = int(float_input("Введите год: "))
        m = int(float_input("Введите номер месяца: "))
        d = int(float_input("Введите день: "))
        try:
            date = datetime.datetime(year=y, month=m, day=d).strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Такой даты не существует. Попробуйте ещё раз:")
            continue
    return date
