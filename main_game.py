import time
import random
import chapter_1, chapter_2

class Character:

    def __init__(self,name,health,mana,inv={'Family Sword':1,'Spell Book':1,'Shrouded Orb':1,'Map of Leathren':1,'Health Potion':2,'Gold':0}):
        self.name = name
        self.health = health
        self.mana = mana
        self.inv = inv

    def atk_chance(self):
        hit_chance = random.randint(0, 99)
        if hit_chance >= 15:
            return 1
        else:
            return
        
    def accuracy(self):
        accuracy = random.randint(0,99)
        if accuracy >= 50:
            return 1
        else:
            return 0

    def attack(self):
        damage = 10
        if self.atk_chance() == 1:
            crit_chance = random.randint(0, 99)
            if crit_chance >= 50:
                crit_damage = random.randint(2, 3)
                damage = damage * crit_damage
                print(f'You did a x{crit_damage} crit!\n{self.name} did {damage} damage!\n')
                return damage
            else:
                damage = 10
                print(f'{self.name} did {damage} damage!\n')
                return damage
        else:
            print(f'{self.name} missed!\n')
            return 0

    def magic(self):
        book_open = True
        weakness = 0
        resistance = 0
        while book_open:
            spells = ['Fire', 'Water', 'Lightning']
            spell_book = '\n'.join(spells)
            print(spell_book)
            print(f'You have {self.mana} mana left!')
            
            if self.mana >= 15:
                ask_magic = input('Which Spell would you like to use:\n> ')

                if ask_magic.lower() == 'fire':
                    if self.accuracy() == 1:
                        dmg = 15 + weakness - resistance
                        self.mana -= 15
                        book_open = False
                        print(f'You casted a Fire spell that did {dmg}!\n') 
                    else:
                        self.mana -= 15
                        print('You missed!')
                        dmg = 0
                        book_open = False
                        
                elif ask_magic.lower() == 'water':
                    if self.accuracy() == 1:
                        dmg = 15 + weakness - resistance
                        self.mana -= 15
                        book_open = False
                        print(f'You casted a Water spell that did {dmg}!\n') 
                    else:
                        print('You missed!')
                        dmg = 0
                        self.mana -= 15
                        book_open = False
                elif ask_magic.lower() == 'lightning':
                    if self.accuracy() == 1:
                        dmg = 15 + weakness - resistance
                        self.mana -= 15
                        book_open = False
                        print(f'You casted a Lightning spell that did {dmg}!\n') 
                    else:
                        print('You missed!')
                        dmg = 0
                        self.mana -= 15
                        book_open = False        
                else:
                    print('Invalid spell!\n')
                    return 0             
       
            else:
                print('You have no mana!\n')
                book_open = False
                return 0
            return dmg

    def inventory(self):
        inv_open = True
        while inv_open:
            print("Your Inventory:\n")
            for item in self.inv:
                print(f'{item} x{self.inv[item]}')

            print('')
            inventory_ask = input("What would you like to use? or cancel?:\n> ")
            if inventory_ask.lower() == 'cancel':
                inv_open = False

            elif inventory_ask.lower() == 'family Sword':
                print("You inspect the sword, it appears to bare your family's crest.")

            elif inventory_ask.lower() == 'spell Book':
                print("You inspect the book, what did you think to expect?")

            elif inventory_ask.lower() == 'shrouded Orb':
                print('You look into the orb and see your reflection.')
                
            elif inventory_ask.lower() == 'health potion':
                if self.health >= 100:
                    print('You already have max health!')
                else:

                    self.inv['Health Potion'] -=1
                    health_potion = random.randint(10,30)
                    self.health += health_potion
                    if self.health > 100:
                        self.health = 100

                    print(f'You healed {health_potion} health!')
                

            elif inventory_ask.lower() == 'mana potion' and 'Mana Potion' in self.inv:
                self.inv['Mana Potion'] -=1
                mana_potion = random.randint(10,30)
                updated_mana = mana_potion + self.mana
                print(f'You mana is now {updated_mana}!')

            else:
                print('Invalid Item!\n')
                time.sleep(0.5)
            inv_open = False

class LowLevelEnemy():

    def __init__(self,health,attack=0,name='',weakness='',resistance='',run_chance=0):
        self.health = health
        self.attack = attack
        self.name = name
        self.weakness = weakness
        self.resistance = resistance
        self.run_chance = run_chance

    def atk_chance(self):
        hit_chance = random.randint(0, 99)
        if hit_chance >= 5:
            return 1
        else:
            return 0

    def damage(self):
        attack = self.attack
        if self.atk_chance() == 1:
            crit_chance = random.randint(0, 99)
            if crit_chance >= 75:
                crit_damage = random.randint(2, 3)
                attack = crit_damage * self.attack
                print(f'{self.name} got a crit of x{crit_damage}!\n{self.name} did {attack} damage!\n')
                return attack
            else:
                print(f'{self.name} did {self.attack} damage!\n')
                return self.attack
        else:
            print(f'{self.name} missed!\n')
            return 0

class Boss:

    def __init__(self,health,attack,name,weakness,resistance):
        self.health = health
        self.attack = attack
        self.name = name
        self.weakness = weakness
        self.resistance =resistance
    
    def atk_chance(self):
        hit_chance = random.randint(0, 99)
        if hit_chance >= 15:
            return 1
        else:
            return 0

    def damage(self):
        if self.atk_chance() == 1:
            crit_chance = random.randint(0, 99)
            crit_damage = random.randint(2, 3)
            #Moves: Slam, Punch, Crush
            moves = random.choice(['Slam','Punch','Crush'])

            if moves == 'Slam':
                attack = 20
                if crit_chance >=85:
                    attack = crit_damage * self.attack
                    print(f'{self.name} got a crit of x{crit_damage}!\n{self.name} slams for {attack} damage!\n')
                    return self.attack

                else:
                    print(f'{self.name} slams for {self.attack} damage!\n')
                    return attack

            elif moves =='Punch':
                attack = 10
                if crit_chance >=25:
                    attack = crit_damage * self.attack
                    print(f'{self.name} got a crit of x{crit_damage}!\n{self.name} punched for {attack} damage!\n')
                    return self.attack

                else:
                    print(f'{self.name} punched for {self.attack} damage!\n')
                    return attack

            elif moves == 'Crush':
                attack = 15
                if crit_chance >=75:
                    attack = crit_damage * self.attack
                    print(f'{self.name} got a crit of x{crit_damage}!\n{self.name} crushes for {attack} damage!\n')
                    return attack

                else:
                    print(f'{self.name} crushes for {self.attack} damage!\n')
                    return self.attack
        else:
            print(f'{self.name} missed!\n')
            return 0
        

def Game_Start():

    def play_again():
        ask_player = input('Would you like to play again? y or n:\n> ')
        if ask_player.lower().startswith('y'):
            Game_Start()
        elif ask_player.lower().startswith('n'):
            print('Thanks for playing my game!')
            time.sleep(1.5)
            quit()
    game_on = True
    while game_on:
        print('')
        player = Character('Adventurer',100,50)
        print(f'Welcome to The Fresh Adventurer of Leathren!\nMade by: Wesley Sorrentino\n')
        while True:

            main_menu_input = input("Start | Help:\n> ")
            if main_menu_input.startswith('s'):
                print('')
                break
            elif main_menu_input.lower().startswith('h'):
                help_text = f"""
                How to play:

                This is a simple text based rpg! The console will relay some commands you can type, 

                You can either enter them Capitalized or Lowercase its totally up to you!

                General Info:

                After every battle you gain all your health and Mana back, 
                
                so you don't have to worry about using potions outside of battle.

                IF YOU DIE! You will have to start the game over! Except the boss battle! (Save points to be added in a later update)
                """
                for text in help_text.split('\n'):
                    print(text.strip())
                    time.sleep(0.4)
            
                continue

        ask_name = input('What is your name? or Leave blank:\n> ')
        player.name = ask_name

        if ask_name == '':
            player.name = 'Adventurer'
        print('')
        #CHAPTER 1
        ask_intro = True
        while ask_intro:
            ask_user = input('Skip Intro? y/n:\n> ')
            if ask_user.lower().startswith('y'):
                print('')
                ask_intro = False
                chapter_1.deer_encounter()
            elif ask_user.lower().startswith('n'):
                chapter_1.act_1(Character,LowLevelEnemy)
                

            else:
                print('Invalid Command\n')
                continue
        
        deer = LowLevelEnemy(45,10,'Big boy the Buck','','',90)
        print(f'You encountered a deer named {deer.name}\n')
        deer_encounter = True
        while  deer_encounter:
            if player.health > 0:
                print(f'{deer.name} has {deer.health}\n{player.name} has {player.health} hp\n\n')
                ask_user = input('Attack | Magic | Items | Run:\n> ')
                if ask_user.lower().startswith('a'):
                    deer.health -= player.attack()
                elif ask_user.lower().startswith('m'):
                    deer.health -= player.magic()
                elif ask_user.lower().startswith('i'):
                    player.inventory()
                else:
                    print('Invalid Command\n')
                if deer.health >= 0:
                    player.health -= deer.damage()
                else:
                    print(f'{deer.name} has been defeated!')
                    player.health = 100
                    player.mana = 100
                    player.inv['Venison'] = 1
                    print('Added Venison x1 to Inventory\n')
                    deer_encounter = False
            else:
                print(f'Really? Did you just die to the first enenmy?\n')
                game_on =False
                
                play_again()
            
        chapter_1.Reaching_fork_in_road()
        forrest_fork = True
        while forrest_fork:

            player_input = input('Left Path | Right Path:\n> ')
            if player_input.lower().startswith('l'):
                #Left Trail
                chapter_1.forrest_left_trail(player.name)
                chapter_1.elliot(player.name)
                while True:
                    player_input = input('Talk to Elliot | Go back:\n> ')
                    if player_input.lower().startswith('t'):
                        chapter_1.elliot()
                    elif player_input.lower().startswith('g'):
                        print('')
                        print('You walk back towards that fork in the trail..\n\nbut instead you take the right path.')
                        chapter_1.forrest_right_trail()
                        forrest_fork = False
                        break

                    else:
                        print('Invalid Command!\n')
            elif player_input.lower().startswith('r'):
                chapter_1.forrest_right_trail()
                forrest_fork = False

            else:
                print('Invalid Command\n')

        def pinky_the_bandit():
            pinky = LowLevelEnemy(100,10,'Pinky the Bandit','','',50)
            print(f'You encountered {pinky.name}!\n')
            pinky_combat = True
            while  pinky_combat:
                if player.health > 0:
                    print(f'{pinky.name} has {pinky.health}\n{player.name} has {player.health} hp\n\n')
                    ask_user = input('Attack | Magic | Items | Run:\n> ')
                    if ask_user.lower().startswith('a'):
                        pinky.health -= player.attack()
                    elif ask_user.lower().startswith('m'):
                        pinky.health -= player.magic()
                    elif ask_user.lower().startswith('i'):
                        player.inventory()
                    else:
                        print('Invalid Command\n')

                    if pinky.health > 0 or player.health == 0:
                        player.health -= pinky.damage()
                    else:
                        print(f'{pinky.name} has been defeated!\n')
                        player.health = 100
                        player.mana = 100
                        player.inv['Health Potion'] = 2
                        print('Added Health Potions x2 to Inventory\n')
                        pinky_combat = False
                        break
                        
                else:
                    print(f'You have been killed by {pinky.name}\n')
                    play_again()
        #Right Path
        right_trail = True
        print("""I'm getting a little hungry" You say to yourself\n""")
        while right_trail:
            ask_user = input('Enter camp | Keep walking:\n> ')

            if ask_user.lower().startswith('e'):
                
                
                ask_camp = True
                chapter_1.in_camp()
                while ask_camp:
                    camp_activities = input('Cook Food | Sleep:\n> ')
                    if camp_activities.lower().startswith('c'):
                        print('')
                        if 'Venison' in player.inv:
                            del player.inv['Venison']
                            print(f'You cook the Venison you harvested from {deer.name}\n')
                            continue
                        else:
                            print('You have no food to cook!\n')
                            continue
                    
                    elif camp_activities.lower().startswith('s'):
                        sleep_text = f"""
                        You noticed a not broken tent at the end of the camp 

                        You have decided to take shelter there for the night.

                        As you were about to fall asleep for the night

                        You hear a voice...
                        """

                        for line in sleep_text.split('\n'):
                            print(line.strip())
                            time.sleep(0.7)
                            
                        ask_camp =False

                    else:
                        print('Invalid Command!\n')
                        continue

                    pinky_encounter = True
                    while pinky_encounter:

                        ask_user = input('Stay Quiet | Step Outside:\n> ')
                        if ask_user.lower() == 'stay quiet':
                            stay_quiet_text = f"""
                            You hear footsteps coming closer to your tent

                            You then see a shadowy figure standing in the entrance of tent

                            The man shouts "I see you, Show yourself!"
                            """

                            for line in stay_quiet_text.split('\n'):
                                print(line.strip())
                                time.sleep(0.7)

                            pinky_the_bandit()
                            right_trail = False
                            break
                        elif ask_user.lower() == 'step outside':
                            print('You step outside the tent and see a shadowy figure...')
                            ask_user = input('Engage | Run:/n> ')
                            if ask_user.lower().startswith('e'):
                                print('You shout at the man... "HEY!!"\n\nThe man runs to you....')
                                pinky_the_bandit()
                            elif ask_user.lower().startswith('r'):
                                run_text = f"""
                                You slowly make you way out of the camp 

                                but as you were trying to leave you 

                                step on a stick and it snaps alerting the man!
                                """

                                for line in run_text.split('\n'):
                                    print(line.strip())
                                    time.sleep(0.7)

                                pinky_the_bandit()
                                right_trail = False
                                break
                            else:
                                print('Invalid command\n')
                        else:
                            print('Invaliid Command\n')

                    
            elif ask_user.lower().startswith('k'):
                keep_walking_text = f"""
                You completely walk passed the camp..

                As You continue down the trail, it is almost pitch black outside.

                You see a man walking towards you holding a torch...               
                """

                for line in keep_walking_text.split('\n'):
                    print(line.strip())
                    time.sleep(0.7)

                
                pinky_the_bandit()
                right_trail = False
                break
            else:
                print('Invalid command\n')

        chapter_2.intro()
        chapter_2.town_intro()
        def town_sqauare():
            in_town = True
            while in_town:
                print('Where would you like to go?\n')
                ask_user = input('Tavern | Merchant | Leave Town:\n> ')
                if ask_user.lower().startswith('t'):
                    chapter_2.tavern_intro()
                    in_tavern = True
                    while in_tavern:
                        print('Talk | Drink | Leave')
                        ask_user = input('What would you like to do?:\n> ')
                        if ask_user.lower().startswith('t'):
                            
                            chapter_2.tavern_man(player.name)
                            in_tavern = False
                        elif ask_user.lower().startswith('d'):
                            if player.inv['Gold'] == 0:
                                print('You have no money!\n')
                            else:
                                print('You grab a drink!\n')
                                continue

                        elif ask_user.lower().startswith('l'):
                            in_tavern = False
                            print('')

                        else:
                            print('Invalid Command!\n')

                elif ask_user.lower().startswith('m'):
                    chapter_2.merchant_intro(player.name,player.inv)

                elif ask_user.lower().startswith('l'):
                    ask_user = input('Are you sure you want leave the Town?:\n> ')
                    if ask_user.lower().startswith('y'):
                        in_town = False
                        break
                    elif ask_user.lower().startswith('n'):
                        in_town = True
                    else:
                        print('Invalid Comand')
                else:
                    print('Invalid Command')
        town_sqauare()
        chapter_2.journey_to_cave()
        chapter_2.cave_entrance(player.name)
        print('Just before you enter the cave you see a backpack...\n\n')
        
        in_cave = True
        while in_cave:
            ask_user = input('Loot | Contine on:\n> ')
            if ask_user.lower().startswith('l'):
                text = f"""
                You open the backpack...

                You find a torch, and some rope!

                added Torch x1 to Inventory

                added Rope x1 to Inventory
                """

                player.inv['Rope'] = 1
                player.inv['Torch'] = 1

                for line in text.split('\n'):
                    print(line.strip())
                    time.sleep(0.8)
                continue

            elif ask_user.lower().startswith('c'):
                print('You continue into the cave its completly dark...\n')
                ask_user = input('Do you want to go back? y/n:\n> ')    
                if ask_user.lower().startswith('y'):
                    print('You exit the cave...\n')

                    for line in text.split('\n'):
                        print(line.strip())
                        time.sleep(0.8)
                    continue
            else:
                print('Invalid Command\n')

            chapter_2.inside_cave(player.name)

            def abdul():
                player = Character('Adventurer',100,50)
                abdul = Boss(150,10,'Abul The Earth Golem','Water','Earth')
                print(f'You encountered {abdul.name}!\n')
                abdul_combat = True
                while  abdul_combat:
                    if player.health > 0:
                        print(f'{abdul.name} has {abdul.health}\n{player.name} has {player.health} hp\n\n')
                        ask_user = input('Attack | Magic | Items:\n> ')
                        if ask_user.lower().startswith('a'):
                            abdul.health -= player.attack()
                        elif ask_user.lower().startswith('m'):
                            abdul.health -= player.magic()
                        elif ask_user.lower().startswith('i'):
                            player.inventory()
                        else:
                            print('Invalid Command\n')

                        if abdul.health > 0 or player.health == 0:
                            player.health -= abdul.damage()

                        else:
                            print(f'{abdul.name} has been defeated!\n')
                            player.health = 100
                            player.mana = 100
                            player.inv['Health Potion'] += 2
                            print('Added Health Potions x2 to Inventory\n')
                            abdul_combat = False
                            break
                            
                    else:
                        print(f'You have been killed by {abdul.name}\n')
                        ask_user = input(f'Would you like to try again {player.name}? y/n:\n>')
                        if ask_user.lower().startswith('y'):
                            abdul = Boss(150,10,'Abul The Earth Golem','Water','Earth')
                            player.health = 100
                            player.mana = 100
                            abdul_combat = True
                            print('')
                        
                        elif ask_user.lower().startswith('n'):
                            quit()

                        else:
                            print('Invalid Command!\n')
            abdul()
            break
        chapter_2.abdul_death(player.name)
        break

Game_Start()