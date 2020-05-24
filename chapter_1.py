import time
import random

def act_1(Character,Enemy):

    '''
    Intro to the Game
    '''
    

    intro = f"""
    Chapter 1  - Through the woods: 

    You awaken in the middle of the woods with your memory in pieces and only one thought....

    "How did I get here?" 

    You start to get up and find that your head hurts, You examine it.. 

    (You have a cut on your head!). You think to yourself "I must of hit my head and now I'm here". 

    You cut the sleeves of your shirt and make a bandage. 

    After putting the bandage you remember you were running from something... but what? 

    You collect what belongings you have around which is 

    your trusty sword handed by generations in your family, 

    A mysterious book and a orb that seems to be pulsing...
     
    "What's this book?" "What's this orb?? you ask yourself. 

    Upon opening the book, You are flooded with a lot of information!

    After reading through the book you discover 

    it's a magic book and within it you find a page titled The Shrouded Orb. 

    You start to read the page and half othe page is missing... 

    it reads "The Void Orb is a very powerful orb. 

    It's believed to unlock a really powerful magic ability, 

    According to legends In order to unlock it's full potential you have locate the Shrouded Cave,

    Just north of Lithuea." Just before you reach the torn half it reads " A Deity was...". 

    You also notice there is 3 pages intact "Fire, Water, Lightning" and several pages

    missing with only the beginning letters remaining.... 

    "Ea, Nat, Ice, Air, Light, Da, Aet, and Vo" 

    You close the book gaining 3 new abilties and a question on your mind 

    "What's this about a cave? What's the purpose of this orb?". 

    You find an old map underneath the book you picked up it reads "Map of Leathren". 

    The map points you in the direction of the cave... and you set out on your journey!
    """
    for line in intro.split('\n'):
        print(line.strip())
        time.sleep(0.5)

def deer_encounter():
    '''
    First battle of the game
    '''

    starting_journey = f"""
    You gather your things and head towards a cave shown on the map...   

    You reach a path in the woods.. 

    While traveling on the path..
    """

    for line in starting_journey.split('\n'):
        print(line.strip())
        time.sleep(0.7)

def Reaching_fork_in_road():
    '''
    Fork in the Road first real decision of the game
    '''

    fork_in_road = f"""
    After collecting yourself after your first battle, You continue down the the trail reaching a fork in the road...
    """

    for line in fork_in_road.split('\n'):
        print(line.strip())
        time.sleep(0.7)

def forrest_left_trail(player_name):
    '''
    Left Path
    '''

    left_path = f"""
    You chose the left path.

    After a short walk you reach a small cabin in the woods.

    Mysterious Man: You are greeted by an old man... "Adventurer!!" he shouts.

    You make you way over to him..

    Mysterious Man: You look familiar

    {player_name}: I do?
    """
    for line in left_path.split('\n'):
        print(line.strip())
        time.sleep(0.8)

def elliot(player_name):

    elliot_encounter = True
    left_options = ['1. How did you regonize me?','2. Ask name']
    while elliot_encounter:

        print(*left_options, sep='\n')
        print('')

        left_input = input('Type a number or End Conversation:\n> ')
        if left_input == '1':
            print('Mysterious Man: I saw you running through the woods Yesterday')
            three = '3. Did you see why I was running?'
            if three not in left_options:
                
                elliot_text_4 = '4. How did you end living in the woods?'
                left_options.append(three)
                left_options.append(elliot_text_4)
                
                time.sleep(0.8)
                print('')
            else:
                continue
        
        elif left_input =='2':
            print('My name is Elliot')
            time.sleep(0.8)
            print('')

        elif left_input == '3':
            print('Elliot: You seemed to be running away from something.')
            time.sleep(0.8)
            print('')

        elif left_input == '4':
            text = """
            Elliot: A long time ago I used to be an adventurer just like you..

            Elliot: Unfortunately I had a bad accident and I was forced to retire. 

            Elliot: I then settled down here, and have been here ever since.
            """

            for line in text.split('\n'):
                print(line.strip())
                time.sleep(0.8)

            time.sleep(0.8)
            print('')

        elif left_input.lower().startswith('e'):
            elliot_encounter = False
            print('')



def forrest_right_trail():
    '''
    Right Path
    '''

    right_path = f"""
    You walk down the path,

    It is nearing nightfall

    You see a camp...
    """

    for line in right_path.split('\n'):
        print(line.strip())
        time.sleep(0.7)

def in_camp():

    camp_text_1 = f"""
    You enter the camp and notice its been long abandoned. 

    """

    for line in camp_text_1.split('\n'):
        print(line.strip())
        time.sleep(0.7)
