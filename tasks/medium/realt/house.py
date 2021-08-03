

class House:
    address: str
    area: float
    cost: float

    def __init__(self, address, cost, area):
        self.address = address
        self.area = area
        self.cost = cost

    def increase_cost(self, value: float):
        self.cost += value

    def decrease_cost(self, value: float):
        self.cost -= value

    def __repr__(self):
        return f'{__name__} {self.address}'
