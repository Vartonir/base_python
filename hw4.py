"""
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
обязательно использовать генератор.
"""

list_a = [2, 3, 7, 3, 4, 2, 2, 9]

list_b = [el for el in list_a if list_a.count(el) < 2]
print(list_b)

