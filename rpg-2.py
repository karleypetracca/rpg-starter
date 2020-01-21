class Character:
    
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

    def alive(self):
        if self.health > 0:
            return True

    def print_status(self):
        print("The %s has %d health and %d power." % (self.name, self.health, self.power))
    
    def attack(self, enemy):
        enemy.health -= self.power
        print("The %s does %d damage to the %s.\n" % (self.name, self.power, enemy.name))
        if not enemy.alive():
            print("The %s is dead.\n" % enemy.name)

hero = Character(10, 5, 'hero')
goblin = Character(6, 2, 'goblin')
zombie = Character(10, 2, 'zombie')

correct_input = False
while correct_input == False:
    print("Who do you want to fight? goblin or zombie")
    fight_input = input()
    if fight_input == 'goblin':
        correct_input = True
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
    elif fight_input == 'zombie':
        correct_input = True
        while hero.alive() and zombie.alive():
            zombie.health = 10
            hero.print_status()
            zombie.print_status()
            print()
            print("Can the hero beat the zombie?")
            print("What do you think fool?")
            print("1. fight zombie")
            print("2. do nothing")
            print("3. flee")
            print("> ",)
            user_input = input()

            if user_input == '1':
                hero.attack(zombie)
                print("Zombie does not take any damage.")
            elif user_input == '2':
                pass
            elif user_input == '3':
                print("Goodbye.")
                break
            else:
                print("Invalid input %r" % user_input)
            
            if zombie.alive():
                zombie.attack(hero)

    else:
        print("Invalid input %r" % fight_input)
