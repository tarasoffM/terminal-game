import random

class Hero:
  # To create a hero give him/her a name.  You get 3 rolls to accept the base attributes.  
  # If you don't pick the first or second, then the third roll is automatically assigned to your character.
    def __init__(self, name, strength, crit, max_health=20, level = 1):
        self.name = name
        self.strength = strength
        self.crit = crit
        self.max_health = max_health
        self.health = max_health
        self.level = level
        self.potion = 1
        self.experience = 0
        self.is_knocked_out = False
    
    def __repr__(self):
        # Printing your character will tell you its name and health along with the stats.
        return """
        {name} has {health} health remaining.
        Strength    : {strength}
        Crit        : {crit}
        Max Health  : {max_health}
        Potions     : {potion}
        """.format(name=self.name, health=self.health, strength=self.strength, crit=self.crit, max_health=self.max_health, potion=self.potion)

    def attack(self, enemy):
        # Do you want a use a potion first?
        potion = input("Do you want to use a potion? y/n \n")
        if potion == "y":
            self.use_potion()
        # Checks to see if Hero is alive
        if self.health == 0:
            print("Your hero is dead, sorry!")
            return
        # Check to see if your attack crits
        if self.crit > random.randint(1, 100):
            print("You CRIT {enemy} and hit for {attack} health".format(enemy=enemy.name, attack=(self.strength * 1.5)))
            enemy.health -= self.strength * 1.5
        else:
            attack_value = random.randint(self.strength -2, self.strength +2)
            print("You attack {enemy} and hit for {attack} health".format(enemy=enemy.name, attack=attack_value))
            enemy.health -= attack_value
        if enemy.health <= 0:
            enemy.is_knocked_out = True

    def use_potion(self):
        # First checks to see if you have potions
        if self.potion > 0:
            self.potion -= 1
            self.health += 20
        # Adds 20 health and ensures you don't go over your max health
        if self.health > self.max_health:
            self.health = self.max_health
            print("You use a potion.  Your health is now {health}".format(health=self.health))
        else:
            print("You do not have any potions")

    # Level up function.  This will occur when your experience is a multiple of 10
    def lvl_up(self):
        # Increases your stats and brings your health to max
        self.strength += 4
        self.crit += 5
        # Caps your max crit at 80 percent
        if self.crit > 80:
            self.crit = 80
        self.max_health += 10
        self.health = self.max_health

class Enemy:
  
    def __init__(self, health, strength, name="The Boss"):
        self.name = name
        self.health = health
        self.strength = strength
        self.is_knocked_out = False
        self.loot = random.randint(0,2)
        self.experience = random.randint(1, 10)

    def __repr__(self):
        return """
        {name} has {health} health remaining.
        Strength    : {strength}
        """.format(name=self.name, health=self.health, strength=self.strength)

    def attack(self, hero):
        attack_value = random.randint(self.strength -2, self.strength +2)
        print("{enemy} attacks you for {attack} health".format(enemy=self.name, attack=attack_value))
        hero.health -= attack_value
        if hero.health <= 0:
            hero.is_knocked_out = True

# Character Creation Function
def create_character():
    choice = ""
    while choice != "y":
        name = input("Please enter your characters name : ")
        choice = input("Your characters name is {name}.  Is this correct? y/n : ".format(name=name))
    rolls = 2
    while rolls > -1:
        strength = random.randint(1,10)
        crit = random.randint(1,10)
        print("""
        Stregnth : {strength}
        Crit     : {crit}
        """.format(strength=strength, crit=crit))
        print("You can roll " + str(rolls) + " more times")
        accept = input("Do you accept? y/n ")
        if accept == "y" or accept == "n":
            if accept == "y":
                print("Character created")
                return Hero(name, strength, crit)
            elif accept == "n":
                rolls -= 1
                continue
    return Hero(name, strength, crit)

# Enemy Creation Function
def create_enemy():
    health = hero.max_health * 1.5
    strength = random.randint(hero.strength -3, hero.strength +3)
    return Enemy(health, strength)

# Create a hero to start the game
hero = create_character()

# The battle starts here
# This loop continues as long as the hero is alive
while hero.is_knocked_out == False:
    enemy = create_enemy()
    while enemy.is_knocked_out == False:
        print(enemy)
        print(hero)
        hero.attack(enemy)
        if enemy.is_knocked_out == True:
            hero.potion += enemy.loot
            hero.experience += enemy.experience
            if hero.experience % 10 == 0:
                hero.lvl_up()
            continue
        enemy.attack(hero)
        if hero.is_knocked_out == True:
            break

print("You have been slain!.")