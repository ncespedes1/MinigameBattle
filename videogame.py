import random


class Character:

    defense = 0

    def __init__(self, name, health, attack_power): 

        self.name = name 
        self.health = health
        self.attack_power = attack_power
        self.max_health = health


    def attack(self, opponent):
        print(f"{self.name} has attacked {opponent.name}!")
        print(f"{opponent.name} has taken {self.attack_power} points of damage.")
        opponent.health -= self.attack_power

        if opponent.health <= 0:
            print(f"{opponent.name} has fainted.")
        else:
            print(f"{opponent.name} has {opponent.health} hp left.")

    def special_ability(self, opponent):
        print(f"{self.name} has used their special ability against {opponent.name}!")

    def heal(self):
        print(f"{self.name} drinks a potion to heal!")
        self.health += 15
        if self.health >= self.max_health:
            self.health = self.max_health
            print(f"{self.name} has fully recovered to {self.max_health} points.")
        else:
            print(f"{self.name} has regained 15 hp. {self.name} has {self.health} hp left.")

    def display_stats(self):
        print(f"""
        {self.name}'s Stats:
        ==============
        Health: {self.health}
        Attack Power: {self.attack_power}""")


    

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=25)
    
    def attack(self, opponent):
        print(f"\n{self.name} swings his Greatsword!")
        print(f"{opponent.name} has taken {self.attack_power} points of damage.")
        opponent.health -= self.attack_power

        if opponent.health <= 0:
            print(f"{opponent.name} has fainted.")
        else:
            print(f"{opponent.name} has {opponent.health} hp left.")

    def special_ability(self, opponent):
        print(f"\n{self.name} activates their Rage and is engulfed in flames!")
        print(f"{self.name} attacks {opponent.name} while enraged!")
        opponent.health -= self.attack_power*3

        print(f"{opponent.name} has taken {self.attack_power*3} points of damage.")
        if opponent.health <= 0:
            print(f"{opponent.name} has fainted.")
        else:
            print(f"{opponent.name} has {opponent.health} hp left.")
        
        print(f"{self.name} takes 10 hp recoil damage while attacking enraged.")
        self.health -= 10
        if self.health <= 0:
            print(f"{self.name} has fainted.")
        else:
            print(f"{self.name} has {self.health} hp left.")


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health = 90, attack_power=75)

    def attack(self, opponent):
        print(f"{self.name} casts meteor strike!")
        print(f"{opponent.name} has taken {self.attack_power} points of damage.")
        opponent.health -= self.attack_power

        if opponent.health <= 0:
            print(f"{opponent.name} has fainted.")
        else:
            print(f"{opponent.name} has {opponent.health} hp left.")

    def special_ability(self, opponent):
        print(f"{self.name} sacrifices 5 hp and casts Army of the Undead!")
        self.health -= 5

        random_int = random.randint(1,5)
        print(f"{random_int} Undead allies have risen to help.")
        print(f"{random_int} Undead attack {opponent.name}!")

        while random_int > 0 and opponent.health > 0:
            print(f"{opponent.name} has taken 40 points of damage.")
            opponent.health -= 40
            random_int -= 1
            print("An Undead ally returns to their underground rest.")

        if opponent.health <= 0:
            print(f"{opponent.name} has fainted.")
        else:
            print(f"{opponent.name} has {opponent.health} hp left.")

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=35)
    
    def attack(self, opponent):
        print(f"{self.name} fires a QuickShot!")
        print(f"Two arrows were released!")

        random_int = random.randint(1,2)

        print(f"{random_int} arrow(s) hit!")
        print(f"{opponent.name} has taken {self.attack_power*random_int} points of damage.")
        opponent.health -= self.attack_power*random_int

        if opponent.health <= 0:
            print(f"{opponent.name} has fainted.")
        else:
            print(f"{opponent.name} has {opponent.health} hp left.")

    def special_ability(self, opponent):
        print(f"{self.name} prepares to evade {opponent.name}'s next attack!")
        self.defense = 1
        if opponent.attack(self):
            pass



class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=60)
    
    def attack(self, opponent):
        print(f"{self.name} casts Smite!")
        print(f"{opponent.name} has taken {self.attack_power} points of damage.")
        opponent.health -= self.attack_power

        if opponent.health <= 0:
            print(f"{opponent.name} has fainted.")
        else:
            print(f"{opponent.name} has {opponent.health} hp left.")

    def special_ability(self, opponent):
        print(f"{self.name} prepares their Divine Shield for {opponent.name}'s next attack!")
        self.defense = 2

class Magical_Girl(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=100)
    
    def attack(self, opponent):
        print(f"{self.name} uses the Power of Friendship!")
        print(f"{opponent.name} has taken {self.attack_power} points of damage.")
        opponent.health -= self.attack_power

        if opponent.health <= 0:
            print(f"{opponent.name} has a flashback of a childhood friend and faints.")
        else:
            print(f"{opponent.name} has {opponent.health} hp left.")

    def special_ability(self, opponent):
        print(f"{self.name} uses Nuclear GlitterBomb on {opponent.name}!")
        print(f"{opponent.name} has taken {self.attack_power*2} points of damage.")
        opponent.health -= self.attack_power*2

        if opponent.health <= 0:
            print(f"{opponent.name} begins to rethink their life choices and faints.")
        else:
            print(f"{opponent.name} has {opponent.health} hp left.")

        

class EvilWizard(Character):
    def __init__(self):
        super().__init__(name = "Evil Wizard", health = 150, attack_power=40)

    def regenerate(self):
        self.health += 5
        print(f"\n{self.name} regenerated 5 health! Current Health: {self.health}")

    def attack(self, opponent):
        if opponent.defense == 1:
            print(f"{opponent.name} evaded the attack!")

        elif opponent.defense == 2:
            deflected_hit = int(self.attack_power/3)

            print(f"{opponent.name} shielded against the attack!")
            print(f"{self.name}'s attack was partially deflected back!")
            print(f"{self.name} has taken {deflected_hit} points of damage.")
            opponent.health -= deflected_hit
            
        else:
            print(f"{self.name} has attacked {opponent.name}!")
            print(f"{opponent.name} has taken {self.attack_power} points of damage.")
            opponent.health -= self.attack_power
        
        opponent.defense = 0

        if opponent.health <= 0:
            print(f"{opponent.name} has fainted.")
        else:
            print(f"{opponent.name} has {opponent.health} hp left.")


def create_character():
    name = input("What is your name adventurer? ")
    print(""" 
        Choose Your Character 
        ======================= 
        1. Warrior 
        2. Mage
        3. Archer
        4. Paladin
        """)
    choice = input("Insert Class choice number: ")

    if choice == "1":
        return Warrior(name)
    elif choice == "2":
        return Mage(name)
    elif choice == "3":
        return Archer(name)
    elif choice == "4":
        return Paladin(name)
    else:
        print("Invalid answer.")
        print("Secret Character Unlocked. Beginning Magical Girl Transformation.")
        return Magical_Girl(name)
    
    
def battle(player,boss):
    while boss.health > 0 and player.health > 0:
        print(f""" 
        {player.name}'s Turn 
        ============== 
        1. Attack 
        2. Use Special Ability
        3. Heal
        4. View their Stats
        """)

        choice = input("Insert choice number: ")

        if choice == "1":
            player.attack(boss)
        elif choice == "2":
            player.special_ability(boss)
        elif choice == "3":
            player.heal()
        elif choice == "4":
            player.display_stats()
            continue


        if boss.health > 0:
            boss.regenerate();
            boss.attack(player)
        else:
            print(f"\n====== ♪♬ ====== ♪♬ ==== CONGRATULATIONS!!!! ==== ♪♬ ====== ♪♬ ======\n")
            print("(ノ°▽°)ノ  ♪♬ （〜^∇^ )〜  ♪♬  ᕕ( >_<)ᕗ  ♪♬  ╰(^o^ )╮  ♪♬  ~(˘▾˘ ~) \n")
            print(f"You have defeated {boss.name} and saved the land!")
            print(f"You won 20% off on your next ice-cream order.")
            break

def main():
    print("Welcome to blahblahblah!")
    print("There is an Evil Wizard terrorizing our town! They'll stop at nothing to drink all of our sodas!")
    print("Please help us and save our fizzy goods.")
    player = create_character()

    wizard = EvilWizard()
    battle(player, wizard)

main()


# player_1 = Warrior("BigBox")
# player_2 = Mage("Gandolf")
# goblin = Character("LilCircle", 500, 100)
# boss = EvilWizard()

# player_1.attack(boss)
# player_2.attack(boss)
# boss.regenerate()
# goblin.attack(player_1)
