class Family:
    surname = "Smith"
    money = 100000
    has_a_house = False
    
    def print_info(self):
        print('\nФамилия: {}\nСбережения: {}\nЕсть дом: {}'.format(
            self.surname, self.money, self.has_a_house))
    
    def add_money(self, amount):
        self.money += amount
        print('\nЗаработано: {}\nБаланс сбережений: {}'.format(amount, self.money))
    
    def buy_house(self, price, discount=0):
        price -= price * discount / 100
        if self.money < price:
            print('Недостаточно средств для покупки дома по цене: {}'.format(price))
            return
        self.money -= price
        self.has_a_house = True
        print('\nКуплен дом по цене: {}\nБаланс сбережений: {}'.format(price, self.money))


my_family = Family()
my_family.print_info()
my_family.add_money(1000)
print('\nПытаемся купить дом')
my_family.buy_house(10 ** 6)
