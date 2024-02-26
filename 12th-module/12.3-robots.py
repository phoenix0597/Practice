class Robot:
    def __init__(self, serial_number):
        self.serial_number = serial_number
    
    def operate(self, action):
        print('Этот робот выполняет действие: {}'.format(action))
    
    def __str__(self):
        return '\nДанный робот имеет серийный номер: {}'.format(self.serial_number)


class RobotVacuum(Robot):  # наследование от класса Robot
    def __init__(self, serial_number):
        super().__init__(serial_number)
        self.__bag_fullness = 'пустой'
    
    def operate(self, action):
        super().operate(action)
        print('Заполненность мешка: {}'.format(self.__bag_fullness))
        self.__bag_fullness = 'полный'
    
    def __str__(self):
        return super().__str__() + '\nЗаполненность мешка: {}'.format(self.__bag_fullness)


class MilitaryRobot(Robot):  # наследование от класса Robot
    def __init__(self, serial_number, weapon):
        super().__init__(serial_number)
        self.__weapon = weapon
    
    def operate(self, action):
        super().operate(action)
        print('\nЭтот робот выполняет действие: {}\nс помощью оружия: {}.'.format(action, self.__weapon))
    
    def __str__(self):
        return super().__str__() + '\nЕго оружие: {}'.format(self.__weapon)


class SubmarineRobot(MilitaryRobot):
    def __init__(self, serial_number, weapon, depth=10):
        super().__init__(serial_number, weapon)
        self.__depth = depth
    
    def operate(self, action):
        super().operate(action)
        print('на глубине: {} метров.'.format(self.__depth))
    
    def __str__(self):
        return super().__str__() + '\nГлубина: {}'.format(self.__depth)


robot_vacuum = RobotVacuum('12345')
robot_vacuum.operate('вычистить мусор')
print("\nИнформация о роботе после действия:", robot_vacuum)

mil_robot = MilitaryRobot('67890', 'лазерная пушка')
mil_robot.operate('охраняет важный объект')

sub_robot = SubmarineRobot('54321', 'реактивная торпеда', 100)
sub_robot.operate('охраняет важный объект')

print("\nИнформация о роботе:", sub_robot)
