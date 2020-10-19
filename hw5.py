"""
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод
для каждого экземпляра.
"""

class Stationery:
    def __init__(self, title="Тем чем будем рисовать"):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки! {self.title}))")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Начинает рисовать ручкой {self.title}!")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Начинает рисовать карандашом {self.title} !")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Начинает рисовать маркером {self.title}!")


stat = Stationery()
stat.draw()
pen = Pen("Parker")
pen.draw()
pencil = Pencil("Комус")
pencil.draw()
handle = Handle("Erich-Krause")
handle.draw()
