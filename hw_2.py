"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.

"""


def var_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f" {key}: {value}")
    return kwargs


var_kwargs(name=input("Введите свое имя: "), surname=input("Введите свою фамилию: "),
           birthday=input("Введите свою дату рождения: "), city=input("Введите свой город проживания: "),
           email=input("Введите свой email: "), phone_number=input("Введите свой номер телефона: "))
