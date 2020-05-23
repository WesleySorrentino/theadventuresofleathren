import time
import random

#Town has Tavern, Merchant, Blacksmith

def intro():
    intro_text = f"""
    Chapter 2: The Cave Monster

    After defeating Pinky, You are finally able to get a much needed rest.

    It is now the morning, You pack up your stuff and head towards the cave on the map.

    Peaking through the trees in the distance you see what looks to be a town!

    You look at the map and you notice it doesn't show a town.

    You think to yourself "Maybe someone in the town can point me in the right direction."

    You finally reach a sign that says "Town of Lithuea"
    """

    for line in intro_text.split('\n'):
        print(line.strip())
        time.sleep(0.8)

def town_intro():
    town_text = f"""
    You pass the sign and enter a busseling city,

    Mechants, Villagers all living their lives.

    You reach the town square.....
    """

    for line in town_text.split('\n'):
        print(line.strip())
        time.sleep(0.8)


def tavern_intro():
    tavern_text = f"""
    You enter the tavern

    Its a busy atmosphere

    You see a man standing in the corner by himself who looks like he has information or You can get a drink..
    """

    for line in tavern_text.split('\n'):
        print(line.strip())
        time.sleep(0.8)

def tavern_man(player_name):
    tavern_man_text = f"""
    Mysterious Man: You walk over the man, he says "What are you looking at!?" in a loud tone.
    """

    insult_text = f"""
    You call him a bich boy...

    Mysterious Man: He smirks "I like you kid" Names Leroy.

    Leroy: I'm a Bounter Collector, I go to different towns looking for people who need help.

    Leroy: What can I help you with?
    """

    three_text = f"""
    Leroy: Let me take a look..

    Leroy: I see, Do you know what's in the cave?

    {player_name}: "in the cave??? What do you mean"

    Leroy: Around the the world, According to legends there is Mysterious Monsters inside them.

    Leroy: I've never had the need to enter them. So I don't know if its true but you are more than welcome to.

    {player_name}: How do I get to the cave?

    Leroy: Once you Leave the tavern you head Northeast a little ways you will see it.

    {player_name}: Thank you Leroy.
    """

    for line in tavern_man_text.split('\n'):
        print(line.strip())
        time.sleep(0.8)

    leroy_encounter = True
    talk_options = ['1. Insult','2. Obviously you']
    while leroy_encounter:
        print(*talk_options,sep='\n')
        print('')

        three = '3. I am looking for a cave (Show map)'

        player_input = input('Type a number or End Conversation:\n> ')
        if player_input == '1':
            for line in insult_text.split('\n'):
                print(line.strip())
                time.sleep(0.8)

            if three not in talk_options:
                talk_options.append(three)

        elif player_input == '2':
            print(
                "Leroy: I'm a Bounter Collector, I go to different towns looking for people who need help.\n\n"
                "Leroy: What can I help you with?\n"
            )
            if three not in talk_options:
                talk_options.append(three)
        elif player_input == '3':
            for line in three_text.split('\n'):
                print(line.strip())
                time.sleep(0.8)
        elif player_input.lower().startswith('e'):
            leroy_encounter = False
            print('')


def merchant_intro(player_name,player_inv):
    merchant_text = f"""
    You hear a man shouting..

    Merchant: FRESH CABBAGE, FRESH BREAD COME AND GET IT

    You walk up to him.
    """

    for line in merchant_text.split('\n'):
        print(line.strip())
        time.sleep(0.8)
    
    talk_options = ['1. Buy','2. Sell','3. Ask about cave']
    merchant_inventory = {'Cabbage':4,'Bread':5}
    food_cost = random.randint(1,10)
    merchant_encounter = True
    while merchant_encounter:
        print(*talk_options,sep='\n')
        print('')

        player_input = input('Type a number or End Conversation:\n> ')
        if player_input == '1':
            print('What would you like to buy?:\n> ')
            print('')

            for item in merchant_inventory:
                print(f'{item} x{merchant_inventory[item]} costs {food_cost} Gold')
            print('')

            current_gold = player_inv['Gold']
            print(f'You have {current_gold} gold!\n')

            ask_user = input('Type item or Go back:\n> ')
            print('')
            if player_inv['Gold'] >= 1:
                if ask_user.lower().startswith('c'):
                    merchant_inventory['Cabbage'] -=1
                    player_inv['Gold'] -=10
                    player_inv['Cabbage'] =1
                    print(f'Added cabbage to inventory!\n')
                
                elif ask_user.lower().startswith('b'):
                    merchant_inventory['Bread'] -=1
                    player_inv['Gold'] -=10
                    player_inv['Bread'] =1
                    print(f'Added Bread to inventory!\n')
                
                elif ask_user.lower().startswith('g'):
                    continue

            else:
                print("You don't have enough gold!\n")

        elif player_input == '2':
            print('What would you liek to sell?:\n> ')
            print('')

            for item in player_inv:
                print(f'{item} x{player_inv[item]}')
            print('')
        
            ask_user = input('Type item or End Conversation:\n> ')
            

            if ask_user.lower().startswith('h'):
                if 'Health Potion' in player_inv:
                    print(f"You sold 1 Health Potion for 15 Gold!\n")
                    player_inv['Health Potion'] -=1
                    player_inv['Gold'] +=15
                else:
                    print("You don't have that item!")
                

            elif ask_user.lower().startswith('m'):
                if 'Mana Potion' in player_inv:

                    print(f"You sold 1 Mana Potion for 15 Gold!\n")
                    player_inv['Mana Potion'] -=1
                    player_inv['Gold'] +=15
                
                else:
                    print("You don't have that item!")
            
            elif ask_user.lower() == 'family sword' or 'spell book' or 'shrouded orb' or 'gold':
                print(f"You can't sell {ask_user}!\n")
            
            elif ask_user.lower().startswith('e'):
                continue

            else:
                print('Invalid Command\n')
        
        elif player_input == '3':
            print('Merchant: A cave? If its around here I never seen one\n')
        
        else:
            print('Invalid Command\n')

def journey_to_cave():
    journey_text = f"""
    After talking to the locals,

    You are now able to go this cave since you woke up.

    Just before you reach the trail, You look back on Lithuea and think to your self

    What a journey I have gone through.

    You are now back in the woods, it is starting to look a little familiar...

    You reach a sign..

    On the the top sign it shows a cave sign... and just below it says.... 
    
    DANGER DO NOT GO THIS WAY!
    
    Regardless what the sign says you proceed towards the cave....

    After a long hike, You have finally reached the cave.........
    """

    for line in journey_text.split('\n'):
        print(line.strip())
        time.sleep(0.8)

def cave_entrance(player_name):
    cave_entrance_text = f"""
    As you approach the cave...

    You see dead bodies and blood everywhere....

    {player_name}: What happend here? you think to yourself.

    You are still determined to enter the cave...
    """

    for line in cave_entrance_text.split('\n'):
        print(line.strip())
        time.sleep(0.8)

def inside_cave(player_name):
    cave_text = f"""
    You light your torch and proceed to enter the cave..

    You can barely see 2 feet in front of you.

    In the distance you hear a very feint what sound like a growl....

    You contine to march forward..

    The growl sounds closer...

    You reach a giant open room and all you can is say... 

    {player_name}: I'm...HERE!

    You look a above you and see a Giant golem like monster drop down!!

    You draw you sword, and say..

    {player_name}: Let's do this.
    """

    for line in cave_text.split('\n'):
        print(line.strip())
        time.sleep(0.8)

def abdul_death(player_name):
    death_text = f"""
    You pull you sword from abdul's corpse, Feeling victorius!

    As you begin to gather yourself, You feel something in your backpack shaking... 
    
    It's the book!!

    You open it and flings open to one of the torn pages!

    It starts to repair the page Earth!

    You now have learned how to do earth spells!!

    You put the book away and notice an exit behind the corpse..

    You make your way through the exit, you start to see some light...

    {player_name}: Ah.. Finally some fresh air..

    TO BE CONTINUED?

    Thanks for playing my game {player_name}!
    """

    for line in death_text.split('\n'):
        print(line.strip())
        time.sleep(0.8)