class Character:
    
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            return True
    

class Hero(Character):

    def __init__(self, health, power):
        super().__init__(health, power)
    
    def attack(self, enemy):
        # Hero attacks goblin
        enemy.health -= self.power
        print("You do %d damage to the goblin.\n" % self.power)
        if not enemy.alive():
            print("The goblin is dead.\n")
    
    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))
       

class Goblin(Character):
    def __init__(self, health, power):
        super().__init__(health, power)

    def attack(self, enemy):
        enemy.health -= self.power
        print("The goblin does %d damage to you.\n" % self.power)
        if not enemy.alive():
            print("You are dead.\n")

    def print_status(self):
        print("The goblin has %d health and %d power." % (self.health, self.power))

hero = Hero(10, 5)
goblin = Goblin(6, 2)

while hero.alive() and goblin.alive():
    hero.print_status()
    goblin.print_status()
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ",)
    user_input = input()

    if user_input == '1':
        hero.attack(goblin)
    elif user_input == '2':
        pass
    elif user_input == '3':
        print("Goodbye.")
        break
    else:
        print("Invalid input %r" % user_input)
    
    if goblin.alive():
        goblin.attack(hero) 

    
