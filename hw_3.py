"""
3. Реализовать функцию my_func(), которая принимает
три позиционных аргумента, и возвращает сумму наибольших
двух аргументов.

 """


def my_func(one, two, three):
    list_numbers = [one, two, three]
    try:
        list_numbers.pop(list_numbers.index(min(list_numbers)))
        return sum(list_numbers)
    except TypeError:
        return "Только числа нужно вводить!!!"


print(f'Сумма наибольших чисел: {my_func(2, 3, 3)}')
