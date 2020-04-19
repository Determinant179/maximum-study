import random

class Tank():
    #Здесь будем описывать наш танк
    def __init__(self, model, armor, min_damage, max_damage, health):
        self.model = model
        self.armor = armor
        self.damage = random.randint(min_damage, max_damage)
        self.health = health

    def health_down(self, enemy_damage):
        self.health = self.health - enemy_damage
        print('\n' + self.model + ": ")
        print("Осталось " + str(self.health) + " здоровья")

    def print_info(self):
        print('\n')
        print("Модель: " + self.model)
        print("Броня: " + str(self.armor))
        print("Урон: " + str(self.damage))
        print("Здоровье: " + str(self.health))

    def shot(self, enemy):
        if self.damage >= enemy.health:
            enemy.health = 0
            print('\n' + "Танк " + enemy.model + " уничтожен")
        if self.damage < enemy.health:
            enemy.health_down(self.damage)
            print('\n' + self.model + ": ")
            print("Попали!!! У танка " + enemy.model + " осталось " + str(enemy.health) + " здоровья!")


class superTank(Tank):
    def __init__(self, model, armor, min_damage, max_damage, health, force_armor):
        self.model = model
        self.armor = armor
        self.damage = random.randint(min_damage, max_damage)
        self.health = health
        self.force_armor = force_armor

    def health_down(self, enemy_damage):
        if self.force_armor == True:
            self.health = self.health - (enemy_damage/2)
        if self.force_armor == False:
            self.health = self.health - enemy_damage
        print('\n' + self.model + ": ")
        print("Осталось " + str(self.health) + " здоровья")
