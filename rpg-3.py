class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            return True

    def print_status(self):
        print("The %s has %s health and %s power." % (self.name, self.health, self.power))
    
    def attack(self, enemy):
        enemy.health -= self.power
        if enemy == zombie:
            enemy.health = 10
            print("The %s attacks, but the %s does not take any damage.\n" % (self.name, enemy.name))
        else:
            print("The %s does %s damage to the %s.\n" % (self.name, self.power, enemy.name))
        if not enemy.alive():
            print("The %s is dead.\n" % enemy.name)

class Hero(Character):
    def set_enemy(self, s_enemy):
        if s_enemy == "goblin":
            self.s_enemy = goblin
        elif s_enemy == "zombie":
            self.s_enemy = zombie


hero = Hero('hero', 10, 5)
goblin = Character('goblin', 6, 2)
zombie = Character('zombie', 10, 2)

correct_input = False
while correct_input == False:
    print("Who do you want to fight? goblin or zombie")
    hero.set_enemy(input())

    if hero.s_enemy == goblin or hero.s_enemy == zombie:
        correct_input = True
        while hero.alive() and hero.s_enemy.alive():   
            hero.print_status()
            hero.s_enemy.print_status()

            print()
            print("What do you want to do?")
            print("1. fight %s" % hero.s_enemy.name)
            print("2. do nothing")
            print("3. flee")
            print("> ",)
            user_input = input()

            if user_input == '1':
                hero.attack(hero.s_enemy)
            elif user_input == '2':
                pass
            elif user_input == '3':
                print("Goodbye.")
                break
            else:
                print("Invalid input %s" % user_input)
            
            if hero.s_enemy.alive():
                hero.s_enemy.attack(hero)
    
    else:
        print("Invalid input %s" % hero.s_enemy)
