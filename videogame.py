import random


class Character:

    defense = 0
    potions = 3

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

    # def special_ability(self, opponent):
    #     print(f"{self.name} has used their special ability against {opponent.name}!")

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
    special_ability1_name = "Rage"
    special_ability2_name = "Double-handed Swing"

    def __init__(self, name):
        super().__init__(name, health=150, attack_power=25)


    def special_ability1(self, opponent):
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

    def special_ability2(self, opponent):
        print(f"\n{self.name} uses Double-handed Swing!")
        print(f"\n{self.name}'s Greatsword is wielded with force and masterful speed!")


        print(f"{opponent.name} has taken {self.attack_power+20} points of damage.")
        opponent.health -= self.attack_power+20

        if opponent.health <= 0:
            print(f"{opponent.name} has fainted.")
        else:
            print(f"{opponent.name} has {opponent.health} hp left.")

class Mage(Character):
    special_ability1_name = "Army of the Undead"
    special_ability2_name = "Secret Weakness"

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

    def special_ability1(self, opponent):
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

    def special_ability2(self, opponent):
        print(f"{self.name} casts Secret Weakness!")
        print(f"{self.name} becomes {opponent.name}'s conscience.")
        
        random_int = random.randint(1,5)
        if random_int == 5:
            print("A Secret Weakness was discovered!")
            print(f"{opponent.name}'s lactase pills float out of his pockets and burst into flames!")
            print(f"{opponent.name} takes {opponent.max_health-20} points of damage.")

            if opponent.health <= 0:
                print(f"{opponent.name} has fainted out of complete embarrassment.")
            else:
                print(f"{opponent.name} has {opponent.health} hp left.")

        else:
            print("Secret Weakness failed!")


class Archer(Character):
    special_ability1_name = "Evade"
    special_ability2_name = "QuickShot"

    def __init__(self, name):
        super().__init__(name, health=80, attack_power=35)
    

    def special_ability1(self, opponent):
        print(f"{self.name} prepares to evade {opponent.name}'s next attack!")
        self.defense = 1

    def special_ability2(self, opponent):
        print(f"{self.name} fires off QuickShot!")
        print(f"Two arrows were released!")

        random_int = random.randint(1,2)

        print(f"{random_int} arrow(s) hit!")
        print(f"{opponent.name} has taken {self.attack_power*random_int} points of damage.")
        opponent.health -= self.attack_power*random_int

        if opponent.health <= 0:
            print(f"{opponent.name} has fainted.")
        else:
            print(f"{opponent.name} has {opponent.health} hp left.")

        while random_int == 2:
            print(f"{self.name} sees another opening!")
            continue



class Paladin(Character):
    special_ability1_name = "Holy Strike"
    special_ability2_name = "Divine Shield"

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

    def special_ability1(self, opponent):
        random_int = random.randint(1,4)
        assist_power = int(self.attack_power/random_int)

        print(f"{self.name} casts Holy Strike on {opponent.name}!")
        print("A blinding light appears as a greater power assists in the attack.")
        print(f"{opponent.name} has taken {self.attack_power + assist_power} points of damage.")
        opponent.health -= self.attack_power + assist_power

    def special_ability2(self, opponent):
        print(f"{self.name} prepares their Divine Shield for {opponent.name}'s next attack!")
        self.defense = 2

class Magical_Girl(Character):
    special_ability1_name = "Nuclear Glitterbomb"
    special_ability2_name = "Heart Impact"

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

    def special_ability1(self, opponent):
        print(f"{self.name} uses Nuclear GlitterBomb on {opponent.name}!")
        print(f"{opponent.name} has taken {self.attack_power*2} points of damage.")
        opponent.health -= self.attack_power*2

        if opponent.health <= 0:
            print(f"{opponent.name} begins to rethink their life choices and faints.")
        else:
            print(f"{opponent.name} has {opponent.health} hp left.")

    def special_ability2(self, opponent):
        print(f"{self.name} uses Heart Impact!")
        print(f"{opponent.name} has taken {self.attack_power*2} points of damage.")
        opponent.health -= self.attack_power*2

        if opponent.health <= 0:
            print(f"{opponent.name} develops a moral compass and feels overwhelming guilt. {opponent.name} tears up and faints.")
        else:
            print(f"{opponent.name} has {opponent.health} hp left.")

        

class EvilWizard(Character):

    def __init__(self):
        super().__init__(name = "Evil Wizard", health = 150, attack_power=40)

    def regenerate(self):
        self.health += 5
        # If it regenerates to full health
        if self.health >= self.max_health:
            self.health = self.max_health
            print(f"\n{self.name} regenerated to full health! Current Health: {self.health}")
        else:
            print(f"\n{self.name} regenerated 5 health! Current Health: {self.health}")

    def attack(self, opponent):
        print(f"\n{self.name} attacks {opponent.name}!")
        random_int = random.randint(1,5)
        current_attack = self.attack_power

        if random_int == 5:
            current_attack = self.attack_power*2
            print(f"{self.name} locked in!")
            print(f"{self.name} takes out two stolen Growth Spurt Shakes and scarfs them down.")
            print(f"{self.name} doubles in size for this turn! {self.name}'s attack power is doubled.")

        if opponent.defense == 1:
            print(f"{opponent.name} evaded the attack!")

        elif opponent.defense == 2:
            deflected_hit = int(current_attack/3)

            print(f"{opponent.name} shielded against the attack!")
            print(f"{self.name}'s attack was partially deflected back!")
            print(f"{self.name} has taken {deflected_hit} points of damage.")
            self.health -= deflected_hit
            
        else:
            print(f"{opponent.name} has taken {current_attack} points of damage.")
            opponent.health -= current_attack
        
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
        2. Use a Special Ability
        3. Heal (Potions Left: {player.potions})
        4. View their Stats
        """)

        choice = input("Insert choice number: ")

        if choice == "1":
            player.attack(boss)
        elif choice == "2":
            
            print(f""" 
        1. {player.special_ability1_name}
        2. {player.special_ability2_name}
        3. Return to previous choices.
                  """)
            sp_choice = input("Choose your special ability: ")
            if sp_choice == "1":
                player.special_ability1(boss)
            elif sp_choice == "2":
                player.special_ability2(boss)
            else:
                continue

        elif choice == "3":
            if player.potions > 0:
                player.heal()
                player.potions -= 1
            else:
                print("There are no potions left!")
                continue
        elif choice == "4":
            player.display_stats()
            continue
        else:
            print("Invalid Answer. Please choose again.")
            continue


        if boss.health > 0:
            if boss.health != boss.max_health:
                boss.regenerate()
            boss.attack(player)


    if player.health <= 0 and boss.health > 0:
        print(f"""
        
        ====== You have been defeated. ======
        
        The nefarious, pint-sized Evil Wizard has triumphed, and our milk reserves are dwindling.
        The streets remain steeped in fear. It's a creamy catastrophe.
              
        Come back and try again.
        """)
            
    elif boss.health <= 0 and player.health <=0:
        print(f"\n====== ♪♬ ====== ♪♬ ==== CONGRATU-dolences.. ==== ♪♬ ====== ♪♬ ======\n")
        print(" (Ｔ▽Ｔ)   o(〒﹏〒)o  (ಥ﹏ಥ)  (¬､¬)\n")
        print(f"You have defeated {boss.name} but you're not around to celebrate!")
        print("The people of Moo York raise a statue of you (without much likeness) in the main plaza.")
        print("\nTry again?")

    else:
            print(f"\n====== ♪♬ ====== ♪♬ ==== CONGRATULATIONS!!!! ==== ♪♬ ====== ♪♬ ======\n")
            print("(ノ°▽°)ノ  ♪♬ （〜^∇^ )〜  ♪♬  ᕕ( >_<)ᕗ  ♪♬  ╰(^o^ )╮  ♪♬  ~(˘▾˘ ~) \n")
            print(f"You have defeated {boss.name} and saved the creamy exports!")
            print(f"You won 20% off on your next Moo York ice-cream order.")

def main():
    print("\n \n============== WELCOME TO MOO YORK CITY ==============\n")
    print("     ~~ Home to the famous Growth Spurt Shake! ~~\n")

    print("""
    Unfortunately it's not the best time to visit. \n
    A short Evil Wizard, no taller than a pint of cream, has unleashed a creamy chaos upon our beloved town!
    He'll drink all the milk he can get his hands on. The Moo York's dairy supply is in danger!
    The citizens are desperate, with empty refrigerators and dry breakfast cereals.\n
    Please help us and save our lactose goods.\n""")
    # print("There is a short Evil Wizard terrorizing our town! They'll stop at nothing to drink all of our milk!")
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
