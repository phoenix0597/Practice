class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._children = []
    
    def print_info(self):
        print(f"Информация о родителе:\nИмя: {self.name} \nВозраст: {self.age}")
        if self.children:
            print("Дети:")
            for child in self.children:
                child.print_info()
    
    @property
    def children(self):
        return self._children
    
    @children.setter
    def children(self, new_children):
        if new_children.age + 16 > self.age:
            self._children = self._children.append(new_children)
        else:
            print('')
        return self._children
    
    def calm_child(self, child):
        child.calm()
    
    def feed_child(self, child):
        child.feed()


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calmness = "неспокоен/неспокойна"
        self.hunger = "голоден/голодна"
    
    def print_info(self):
        print(f"Имя: {self.name}, \nВозраст: {self.age}, \nСпокойствие: {self.calmness}, \nГолод: {self.hunger}")
    
    def calm(self):
        self.calmness = "спокоен/спокойна"
        print(f"{self.name} теперь {self.calmness}.")
    
    def feed(self):
        self.hunger = "не голоден/голодна"
        print(f"{self.name} теперь {self.hunger}.")


# Создание родителя и детей
parent = Parent("Иван", 40)
child1 = Child("Алиса", 10)
child2 = Child("Игорь", 8)

# Добавление детей в список детей родителя
parent.children.extend([child1, child2])

# Взаимодействие между родителем и детьми
parent.print_info()
print("")

parent.calm_child(child1)
parent.feed_child(child2)

print("\nПосле взаимодействия:")
parent.print_info()
