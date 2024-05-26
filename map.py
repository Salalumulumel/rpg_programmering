from os import system, name
from random import randint, random
from time import sleep


boss_deafeat = {1: False, 2: False, 3: False, 4: False}

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


monster_list = ['Slime', 'Bat', 'Skeleton', 'Goblin', 'Shadow', 'Witch', 'Zombie']



class Player():
    def __init__(self, name, attack, defense, speed, critchance, statpoints):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.critchance = critchance
        self.statpoints = statpoints
        self.health = 10
        self.maxhealth = 10
        self.lvl = 0
        self.exp = 0
        self.money = 0
        self.potions = 0
        self.monsterskilled = 0
        self.potionsused = 0
    
    def __repr__(self):
        print("You're the fighter {name}.".format(name = self.name))
        print("Here are your current stats:\n\nLevel: {lvl}\nAttack: {attack}\nDefense: {defense}\nSpeed: {speed}\nCrit Chance: {critchance}\nExp : {exp\n}".format(lvl = self.lvl, attack = self.attack, defense = self.defense, speed = self.speed, exp = self.exp))
        print("You have {potions} potions".format(potions = self.potions))
        return ("\nYou have {money} money\n".format(money = self.money))
    
    def train(self):
        if self.lvl >= 30:
            print("\nYou've maxed out your level, which means you won't level up anymore. But don't worry! You'll still gain potions and money for your wonderful feats against monsters!\n")
            input("Press Enter to continue")

        keep_fighting = True
        while keep_fighting == True:
            if self.lvl <= 10:
                monster = spawnmonster(self.attack,self.defense, self.speed, self.critchance, self.maxhealth, 1)
            elif self.lvl > 10 and self.lvl <= 20:
                monster = spawnmonster(self.attack,self.defense, self.speed, self.critchance, self.maxhealth, 2)
            elif self.lvl > 20:
                monster = spawnmonster(self.attack,self.defense, self.speed, self.critchance, self.maxhealth, 3)
            
            clear()
            
            print("You found a {monster}! Get ready to fight!\n".format(monster = monster.name))
            combat = True
            while combat == True:
                try:
                    print(f'{"HP:":7} {"{health}/{maxhealth}"}'.format(health = self.health, maxhealth = self.maxhealth))
                    print(f'{"Potions:":5} {"{potions}"}'.format(potions = self.potions))
                    decision = int(input('\nIt\'s your turn {player}, what do you want to do?\n1. Attack\n2. Use potion\n'.format(player = self.name)))
                    match decision:
                        case 1:
                            clear()
                            combat = self.attack_enemy(monster)

                            if combat == True:
                                print("\nWatch out! {enemy} is attacking now!\n".format(enemy = monster.name))
                                combat = monster.attack_player(self)

                            else:
                                del monster
                                self.monsterskilled += 1
                                self.exp += 5

                                if self.lvl == 30: self.exp = 0
                                self.money += randint(1,3)
                                print("You received {money}$ now.\n".format(money = self.money))
                                
                                if (random()*100 < 25 and self.potions <10):
                                    random_potions = randint (1,2)
                                    print("Oh? It seems like the monster was carrying potions. \n\nYou got {potions} more potion(s)".format(potions = random_potions))
                                    self.potions += random_potions
                                    
                                    if self.potions > 10:
                                        self.potions = 10
                                        print("\n\nYou've got the maximum amount of potions, so you'll have to leave some behind.\n")
                                
                                if self.exp >= 10:
                                    self.level_up()
                        
                        case 2:
                            clear()
                            self.use_potion()
                        
                        case _:
                            print("Please type 1 or 2 on your keyboard to choose an option.")
                            continue
                
                except ValueError:
                    print("My apologies, we didn't get that. Please try again!")
            
            if self.health == 0: break

            while True:

                try:

                    decision = int(input('You have {health}/{maxhealth} HP left and {potions} potions, dop you want to continue trainning or go back to the village?\n1. Continue training\n2. Go back\n'.format(health = self.health, maxhealth = self.maxhealth, potions = self.potions)))
                    match decision:

                        case 1:
                            keep_fighting = True
                            break

                        case 2:

                            keep_fighting = False
                            clear()
                            print("Going back to the village.", flush= True)
                            input("Press Enter to continue.")
                            clear()
                            break

                        case _:
                            print("Please type 1 or 2 on your keyboard to pick an option.")
                            continue

                except ValueError:
                    print("Sorry, we couldn't get that. Please try again.")
    
    def level_up(self):
        while self.exp >= 10:
            self.lvl += 1

            if self.lvl > 30:
                print("You've reached the max level you can get {player}!".format(player = self.name))
                self.lvl = 30
                self.exp = 0
                return 0
            self.health += 3
            self.maxhealth += 5
            self.exp -= 10
            self.statpoints += 1

            print('\nYou leveled up {player}! You are now level {lvl} and you have {statpoints} stat points ready to use when you return to the village.\n\nYou have recovered 3 healthpoints and have 5 more maximum health points!.\n'.format(player = self.name, lvl = self.lvl, statpoints = self.statpoints))

    def use_potion(self):
        if self.potions > 0:
            while True:
                if self.health == self.maxhealth:
                    print('Your HP is already full {name}'.format(name = self.name))
                    return False
                else:
                    self.gainHealth()
                    self.potions -= 1
                    self.potionsused += 1
                    return True
                    break

        else: print('You are out of potions.'); return False

    def gainhealth(self):
        self.health += round(self.maxhealth * 0.2)
        if self.health > self.maxhealth:
            self.health = self.maxhealth
        
        print('You used a potion and now have {health}/{maxhealth} HP'.format(health = self.health, maxhealth = self.maxhealth))
    
    def attack_enemy(self, enemy):
        dodge = enemy.dodge()
        if dodge:
            print("\n{enemy} is faster than you! They dodged your attack\n".format(enemy = enemy.name))
            return True
        else:
            crit = self.crit()
            return (enemy.lose_health(round((self.maxhealth * 0.75 + self.attack) - (enemy.maxhealth * 0.5 + enemy.defense))*crit))
        
    def crit(self):
        if (random()*100 < self.critchance * 5):
            print("\n You landed a critical hit!\n")
            return 2
        return 1

    def dodge(self):
        if ((random()*100) < self.speed*3.3):
            print("You dodged the attack!")
            return True
        return False
    
    def lose_health(self, damage):
        if damage <= 0:
            damage = 1
        print("\nYou take {damage} damage!\n".format(damage = damage))
        self.health -= damage

        if self.health <= 0:
            self.health = 0
            print("\nYou got your ass whooped!\n We will transport you back to the village and take some potions and money as payment.")
            self.potions = 0
            self.money -= round(self.money * 0.25)
            input("\nPress Enter to continue\n")
            clear()
            return False
        
        else:
            print("\nYou have {health}/{maxhealth} left\n".format(health = self.health, maxhealth = self.health))
            return True
        
class Monster():
    def __init__(self, name, attack, defense, speed, critchance, health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.critchane = critchance
        self.health = health
        self.maxhealth = health
    def __repr__(self):
        return("This monster is a {name}, Attack: {attack}, Defense: {defense}, Speed: {speed}, CritChance: {critchance}, HP: {hp}, Max HP: {maxhp}".format(name = self.name, attack = self.attack, defense = self.defense, speed = self.speed, critchance = self.critchance, hp = self.health, maxhp = self.maxhealth))
    def dodge(self):
        if ((random()*100) < self.speed*3.3):
            return True
        return False
    
    def lose_health(self, damage):
        if damage <= 0:
            damage = 1
        print("\n{monster} takes {damage} damage!\n".format(monster = self.name, damage = damage))
        self.health -= damage

        if self.health <= 0:
            self.health = 0
            print("\nYou slayed the {enemy}!\n".format(enemy = self.name))
            return False
        else:
            print ("\n{enemy} has {health}/{maxhealth} HP left\n",format(enemy = self.name, health = self.health, maxhealth = self.maxhealth))
            return True
    
    def crit(self):
             if (random()*100 < self.critchane * 5):
                 print("\{monster} lands a critical hit!\n".format(monster = self.name))
                 return 2
             return 1
    
    def attack_player(self, player):
        dodge = player.dodge()
        if dodge:
            print("You dodged {enemy}'s attack!\n".format(enemy = self.name))
            return True
        else:
            crit = self.crit()
            return ( player.lose_health(round((self.maxhealth * 0.75 + self.attack) - (player.maxhealth * 0.5 + player.defense))*crit))
        

def spawnmonster(attack, defense, speed, critchance, maxhealth, lvl):
        match lvl:
            case 1:
                index = randint(0,6)
                lower_stats = randint(75,80)
                percentage_lower_stats = lower_stats/100
                return Monster(monster_list[index], round(attack*percentage_lower_stats), round(defense*percentage_lower_stats), round(speed * percentage_lower_stats), round(critchance * percentage_lower_stats), round(maxhealth * percentage_lower_stats))     
            case 2:
                index = randint(7,13)
                lower_stats = randint(80,85)
                percentage_lower_stats = lower_stats/100
                return Monster(monster_list[index], round(attack*percentage_lower_stats), round(defense*percentage_lower_stats), round(speed * percentage_lower_stats), round(critchance * percentage_lower_stats), round(maxhealth * percentage_lower_stats))
            case 3:
                index = randint(14,20)
                lower_stats = randint(85,90)
                percentage_lower_stats = lower_stats/100
                return Monster(monster_list[index], round(attack*percentage_lower_stats), round(defense*percentage_lower_stats), round(speed * percentage_lower_stats), round(critchance * percentage_lower_stats), round(maxhealth * percentage_lower_stats))
            case 4:
                percentage_lower_stats = 95/100
                return Monster('Immigrant mother', round(attack*percentage_lower_stats), round(defense*percentage_lower_stats), round(speed * percentage_lower_stats), round(critchance * percentage_lower_stats), round(maxhealth * percentage_lower_stats))
            case 5:
                percentage_lower_stats = 1
                return Monster('Sandal', round(attack*percentage_lower_stats), round(defense*percentage_lower_stats), round(speed * percentage_lower_stats), round(critchance * percentage_lower_stats), round(maxhealth * percentage_lower_stats))
            case 6:
                percentage_lower_stats = 105/100
                return Monster('The belt', round(attack*percentage_lower_stats), round(defense*percentage_lower_stats), round(speed * percentage_lower_stats), round(critchance * percentage_lower_stats), round(maxhealth * percentage_lower_stats))
            case 7:
                percentage_lower_stats = 110/100
                return Monster('Satan himself', round(attack*percentage_lower_stats), round(defense*percentage_lower_stats), round(speed * percentage_lower_stats), round(critchance * percentage_lower_stats), round(maxhealth * percentage_lower_stats))
            

     