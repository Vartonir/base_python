"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) —
2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
(Для ожидания нескольких секунд можно использовать метод стандартной библиотеки time.sleep())
"""

from time import sleep


class TrafficLight:
    __color = "Черный"

    def running(self):
        while True:
            print("Сфетофор сейчас красный")
            sleep(7)
            print("Сфетофор сейчас жёлтый")
            sleep(2)
            print("Сфетофор сейчас зелёный")
            sleep(7)
            print("Сфетофор сейчас жёлтый")
            sleep(2)


trafficlight = TrafficLight()
trafficlight.running()
