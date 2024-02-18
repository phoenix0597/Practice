class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
    
    def attack(self, enemy):
        if self.health > 0:
            print(f'Воин {self.name} атакует воина {enemy.name}!')
            enemy.health -= 20
            print(f'{enemy.name} осталось здоровья: {enemy.health}')
            if enemy.health <= 0:
                print(f'Воин {self.name} одержал победу!')
                raise Exception('Игра окончена')
        else:
            print('Атака невозможна. Воин {} мертв.'.format(self.name))
            raise Exception('Игра окончена')