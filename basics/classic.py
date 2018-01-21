class Horse:
    def __init__(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.isAlive = True
        self.children = []

    def die(self):
        self.isAlive = False

    def aging(self):
        self.age += 1

    def having_children(self, child_horse):
        self.children.append(child_horse)


class HorseHospital:

    def __init__(self):
        self.horses = []

    def add_horse(self, horse_to_add):
        self.horses.append(horse_to_add)

    def let_a_horse_die(self, number):
        self.horses.index(number).isAlive = False