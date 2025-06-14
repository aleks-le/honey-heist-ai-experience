from ai import call_gpt
from graphics import Canvas
import random
import time

'''
Endless game of Dragons and Dungeons campaign using AI. 
Instructions:
https://www.docdroid.net/KJzmn5k/honey-heist-by-grant-howitt-pdf
'''

# Player's character setup
BEARTYPE = ['Grizzly','Polar','Panda','Black','Sun','Honey Badger']
USERS_BEARTYPE = random.choice(BEARTYPE).lower()
DESCRIPTOR = ['Rookie','Washed-Up','Retired','Unhinged','Slick','Incompetent']
USERS_DESCRIPTOR = random.choice(DESCRIPTOR).lower()
ROLE = ['Muscle','Brains','Driver','Hacker','Thief','Face']
USERS_ROLE = random.choice(ROLE).lower()

# Setting the scene
ORGANIZER_LIST = ['Cunning and Sly','Greedy and Wicked','Clueless and Exploitable','Ruthless and Corrupt']
ORGANIZER = random.choice(ORGANIZER_LIST)
ADJECTIVE_LIST = ['Creepy','Busy','Run-down','Beautiful','Dangerous','Lavish']
ADJECTIVE = random.choice(ADJECTIVE_LIST).lower()
LOCATION_LIST = ['Lakeside Camp','Fishing Village','Metropolitan City','Convention Centre','Truck Convoy','Wilderness Retreat']
LOCATION = random.choice(LOCATION_LIST).lower()
PRIZE_LIST = ['ultradense megahoney from especially posh bees','a briefcase of pure manuka extract worth $5m','The Queen of All Bees, Once Exiled, Now Returned','Black Orchid Honey, which turns anyone who eats it into a goth','Abraham Lincoln\'s beehive, thought to be haunted by his ghost','Miss Universe 2017–an especially attractive Bee']
PRIZE = random.choice(PRIZE_LIST)
SECURITY_FEATURES_LIST = ['Armed Guards','Electronically locked doors','Laser tripwire grids','CCTV network','"Impenetrable” Vault','Poison Gas']
SECURITY_FEATURE1 = random.choice(SECURITY_FEATURES_LIST)
SECURITY_FEATURES_LIST.remove(SECURITY_FEATURE1)
SECURITY_FEATURE1 = SECURITY_FEATURE1.lower()
SECURITY_FEATURE2 = random.choice(SECURITY_FEATURES_LIST).lower()

# Save file of what is happening:
SAVEFILE = []

def main():
    print('Welcome to Honey Heist!')

    # Setting the character's name
    bear_name = ''
    incorrect_input = True
    while incorrect_input == True:
        name_or_not = input('Do you want to name your bear?(yes/no) ')
        if len(name_or_not) <= 3:
            if name_or_not.lower() == 'no':
                bear_name = call_gpt('Generate a random name for a bear that would be in a Honey Heist campaign for DnD. Give me just the name.')
                print(f'Your bear\'s name is {bear_name}.')
                incorrect_input = False
            elif name_or_not.lower() == 'yes':
                bear_name = input('What is your bear\'s name? ')
                incorrect_input = False
            else:
                print('Incorrect input')
                incorrect_input = True
        else:
            print('Incorrect input')
            incorrect_input = True

    # Introduction
    time.sleep(1)
    print('------------------')
    time.sleep(1)
    players_character = f'{bear_name} is a {USERS_BEARTYPE} bear, who is {USERS_DESCRIPTOR} and whose role in the heist team is the {USERS_ROLE}.'
    print(players_character)
    time.sleep(4)
    print('------------------')
    time.sleep(1)
    print('It\'s Honeycon 2017. You are going to undertake the greatest heist the world has ever seen. Two Things –')
    time.sleep(5)
    print('One: You have a complex plan that requires precise timing.')
    time.sleep(4)
    print('Two: You are a GODDAMN BEAR.')
    time.sleep(1)
    print('------------------')
    time.sleep(3)
    
    # Informing the player about the game-world
    scene = f'You investigated Honeycon 2017 and you find out that convention organizer is infamous "{ORGANIZER} Corp" and it\'s being held in {ADJECTIVE} {LOCATION}.'
    print(scene)
    time.sleep(7)
    prize = f'You got a tip from the insider spy that aside from loads of honey, the prize of the heist is {PRIZE}.'
    print(prize)
    time.sleep(1)
    print('------------------')
    time.sleep(7)
    print(f'Rumour says that "{ORGANIZER} Corp" has these security features:')
    time.sleep(4)
    print('1. ',SECURITY_FEATURE1)
    time.sleep(2)
    print('2. ',SECURITY_FEATURE2)
    time.sleep(2)
    # Tools to be used in game
    users_tool1 = input('Which tool will you take with you to help with the heist? ')
    time.sleep(1)
    users_tool2 = input('You can take one more tool. Which one will you take? ')
    time.sleep(1)
    print('------------------')
    time.sleep(3)

    # Start of the game. Using AI to generate scenarios
    base_scenario = f'It\'s Honeycon 2017. You are going to undertake the greatest heist the world has ever seen. {players_character}. User is the bear and works in a team of 5 heister-bears. {scene}. {prize}. The conference will have these security features: {SECURITY_FEATURE1},{SECURITY_FEATURE2}. Player selected these tools to take with them: {users_tool1},{users_tool2}.'
    SAVEFILE.append(base_scenario)
    generated_scenario = call_gpt(f'DnD game instructions: {base_scenario}. Generate a consecutive scenario (up to 2 sentences) and a question for the player. Give me just the scenario and question.')
    users_answer = input(f'{generated_scenario} ')
    SAVEFILE.append(f'Scenario :{generated_scenario}; users answer: {users_answer}.')
    print('*****')
    time.sleep(3)
    while True:
        generated_scenario = call_gpt(f'DnD campaign storyline: {SAVEFILE}. Generate a consecutive scenario (up to 2 sentences, keep it short, don\'t repeat old information and previous scenarios and make scenario closer to the player winning) and a question for the player. Give me just the scenario and question.')
        users_answer = input(f'{generated_scenario} ')
        SAVEFILE.append(f'Scenario :{generated_scenario}; users answer: {users_answer}.')
        print('*****')
        time.sleep(3)
        

if __name__ == '__main__':
    main()
