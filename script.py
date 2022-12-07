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
        potion = input("Do you want to use a potion? y/n ")
        if potion == "y":
            self.use_potion()
        # Checks to see if Hero is alive
        if self.health == 0:
            print("Your hero is dead, sorry!")
            return
        # Check to see if your attack crits
        if self.crit > random.randint(1, 100):
            print("You CRIT {enemy} and hit for {attack} health".format(enemy=enemy.name, attack=(self.stregth * 1.5)))
            enemy.health -= self.strength * 1.5
        else:
            attack_value = random.randint(self.strength -2, self.strength +2)
            print("You attack {enemy} and hit for {attack} health".format(enemy=enemy.name, attack=attack_value))
            enemy.health -= attack_value
        if enemy.health <= 0:
            enemy.is_knocked_out = True