

class Tomato:
    index: int
    ripeness: str
    states: tuple = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')

    def __init__(self, index):
        self.index = index
        self.ripeness = self.states[0]

    def grow(self):
        if self.ripeness != self.states[3]:
            current_stage = self.states.index(self.ripeness)
            print(f'Помидор {self.index} вырастает из стадии {self.states[current_stage]} до стадии {self.states[current_stage + 1]}')
            self.ripeness = self.states[current_stage + 1]
        else:
            return self.ripeness

    def is_ripe(self):
        if self.ripeness == self.states[3]:
            print('Спелый!')
            return True
        else:
            print('Зеленоват ещё')
            return False

#
# a = Tomato(1)
# a.grow()
# a.is_ripe()
# a.grow()
# a.is_ripe()
# a.grow()
# a.is_ripe()
