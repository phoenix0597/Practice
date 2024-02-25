class Potato:
    states = {0: "Отсутствует", 1: "Росток", 2: "Зеленая", 3: "Зрелая"}
    
    def __init__(self, index):
        self.index = index
        self.state = 0
    
    def grow(self):
        if self.state < 3:
            self.state += 1
            self.print_state()
    
    def is_ripe(self):
        if self.state == 3:
            return True
        return False
    
    def print_state(self):
        print("Картошка No{} - {}".format(self.index, self.states[self.state]))


class PotatoGarden:
    def __init__(self, count):  # count - количество посаженной картошки
        self.potatoes = [Potato(index) for index in range(1, count + 1)]
    
    def grow_all(self):
        print('Картошка подрастает:')
        for potato in self.potatoes:
            potato.grow()
    
    def print_state_all(self):
        for i_potato in self.potatoes:
            i_potato.print_state()
    
    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print("Картошка еще не созрела!\n")
        else:
            print("Вся картошка созрела. Можно собирать!\n")