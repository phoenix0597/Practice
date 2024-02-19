class Student:
    def __init__(self, name, group_num, score):
        self.name = name
        self.group = group_num
        self.score = score
    
    def average_score(self):
        if len(self.score) == 0:
            raise ValueError('Список оценок пуст')
        return sum(self.score) / len(self.score)
    
    def print_info(self):
        print(f"Имя: {self.name}\n"
              f"Номер группы: {self.group}\n"
              f"Успеваемость: {self.score}\n"
              f"Средний балл: {self.average_score()}")
