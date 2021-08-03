from tomato import Tomato


class TomatoBush:
    tomato_list: list = []

    def __init__(self, *args):
        self.tomato_list = list(args)

    def grow_all(self):
        for i in self.tomato_list:
            Tomato.grow(i)

    def all_are_ripe(self):
        for i in self.tomato_list:
            if Tomato.is_ripe(i):
                return True
            else:
                return False

    def give_away_all(self):
        tomato_list_ripe = [i for i in self.tomato_list]
        self.tomato_list.clear()
        return tomato_list_ripe
