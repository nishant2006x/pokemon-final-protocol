import sys, os

# this is here to quickly link to the file path to the main folder instead of scripts
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)


import install_requirements
# use the function from the helper file install_requirements
install_requirements.Install_Reqs()

print("Loading... (This game has 5000+ lines of code!)\n")
import time
from in_game_data.colortext import *
import json
import random
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import base64
import pygame
pygame.init()
try:
  my_sound = pygame.mixer.Sound('sound.mp3')
except:
  pass
from storymode import storymode
is_storymode = False
# Define popular Pokemon data
global coins, inventory, yourPokemon_NAMEpre, yourPokemon_DATA, settingsAndcodes, scene, storyinventory, storyyouPokemon_NAME, storyyourPokemon_DATA, yourWins, yourLosses, storyNAME, TRAINERLEVEL, storyBagpack


from in_game_data.allpokemon import *
coins = 200  # OK BRO I KNOW YOU ARE GONNA CHEAT, BUT IT IS MORE FUN TO GRIND INSTEAD!
scene = 0
yourWins = 0
yourLosses = 0
TRAINERLEVEL = 0
storyBagpack = []
storyinventory = []
storyyouPokemon_NAME = None
storyyourPokemon_DATA = None
storyNAME = ''

inventory = ["Pikachu"] # Player's initial Pokemon 
yourPokemon_NAMEpre = Pokemon["Pikachu"]['name'] # Starting with Pikachu, PRE JUST MEANS PRE BATTLE CUZ I WANTED TO DIFFER IT
yourPokemon_DATA = Pokemon["Pikachu"]

# ART AND OTHER VARS
settingsAndcodes = {

  "ASCII": True,
  "GigachadMode": False,
  "TypeSpeed": 0.01,

}


Pikachu =  yellow + '''                                                                 
 ''' +black+ ''' @@                                                        
  ''' +black+ ''' @@@@@@                                        ''' +black+ ''' @@        
  ''' +black+ '''  @@@   @@          ''' +yellow+ '''                    ''' +black+ '''  @@ @@@@@        
     @@   ''' +yellow+ '''    @                          @@   ''' +black+ ''' @@@@   ''' +yellow+ '''      
      @@       @                      @@       @@           
        @       @@                  @@        @@            
         @@       @  @@@@@@@@@@@@  @        @@     @@@@@ @  
           @@                             @    @@        @  
              @@@@                   @@@  @@@            @  
               @                      @@@               @   
              @@                       @                @   
              @@  ''' +black+ '''@@@   ''' +black+ '''         @@@ '''+yellow+'''  @               @@   
              @@''' +black+ ''' @@@''' +white+ '''@''' +black+ '''@    ''' +black+ '''      @''' +white+ '''@''' +black+ '''@@@''' +yellow+ '''  @             @ @    
              @  ''' +black+ ''' @@@@  ''' +yellow+ '''   @   ''' +black+ '''  @@@    ''' +yellow+ ''' @      @@@@@@        
             ''' +red+ '''@@@                     @ @ ''' +yellow+ ''' @@@ 
             ''' +red+ '''@@@@@@    ''' +yellow+ '''@@     @@''' +red+ '''    @@@@@  ''' +yellow+ '''  @              
              ''' +red+ '''@@@@@@   ''' +yellow+ '''  @@@@@     ''' +red+ ''' @@@@@@  ''' +yellow+ '''   @@            
              ''' +red+ ''' @@@                  @@@ ''' +yellow+ '''@@      @           
               ''' +red+ ''' @ @                  @@ ''' +yellow+ ''' @@     @@          
               @    @@           @@@   @    @@              
               @        @@@@@@         @ @@@                
              @         @     @         @@           
            @@           @    @          @                  
           @@            @   @         @  @                 
           @   @         @   @        @    @                
       @@@ @   @         @   @        @    @@@@             
        @@@@    @        @@@@@       @   @   @@             
         @@@@@   @       @@@@@      @    @@@@               
           @@@@@@@@      @@@@@     @@@@@@@@@                
             @@@@@@@@ @@@@   @ @@@@@@@@@@@                  



    ''' + resetlol





Charizard = red + '''             

                :*-''' +Orange+ '''..  ''' +red+ '''                             
            .****:-''' +Orange+ '''.. ''' +red+ '''                           
           ***:''' +Orange+ '''......    ''' +red+ '''                        
            =+**..                               
              .**:.                              
                  +.''' + Orange + ''' :%%=.                       
         ''' +blue+ ''' =-  ''' +Orange+ '''      . @@@=.     ''' +blue+ '''   .-            
       ''' +blue+ '''.:=+-   ''' +Orange+ '''       #@@+:=    ''' +blue+ '''    ==+          
      ''' +blue+ ''':%%%@%- ''' +Orange+ '''       -%+#+'''+blue+'''=''' +White+ '''=    '''+blue+'''   .+%%=         
   ''' +blue+ ''' :*%%%#@%*. ''' +Orange+ '''      *%+*+: :.    ''' +blue+ ''' +%#%%+=       
   ''' +blue+ ''' =%%%##@%%=  ''' +Orange+ '''       ++=       ''' +blue+ ''' -%%@#%%%*-.    
  ''' +blue+ ''' =%%%%##@%%+::.''' +Orange+ '''      ===.    ''' +blue+ ''' ::#%%@##%%%%#.   
  ''' +blue+ '''-#%%%####:%*%%%=:''' +Orange+ '''   .===.:=.''' +blue+ '''=%%%%%%%%##%%%%+   
''' +blue+ ''' :#%%%%###.+''' +Orange+ ''' ==''' +blue+ '''%%%%@''' +Orange+ '''===-===++*''' +blue+ '''%%%%%%#%%@**#%%%%+. 
''' +blue+ '''.*%%%%%*:*%*''' +Orange+ '''==''' +blue+ '''+#%%''' +Orange+ '''-+==========''' +blue+ '''%%%''' +Orange+ '''==''' +blue+ '''***@#*..%%%%*.''' +Orange+ '''
''' +blue+ ''':%%%#     .%%''' +Orange+ '''=====''' +Orange+ '''===:...''' +Orange+ '''-=====..===''' +blue+ '''+%%*=.:.-%%* 
''' +blue+ '''.%%     ''' +Orange+ '''    =     =''' +yellow+ '''........''' +Orange+ '''-=- +=++ .=.+.:+-''' +blue+ ''' %# 
 ''' +blue+ '''+#  ''' +Orange+ '''     ..-=====''' +yellow+ '''..........''' +Orange+ '''-=       =.:....  ''' +blue+ ''':+ 
 ''' +blue+ ''' *   ''' +Orange+ '''  .....-..=*''' +yellow+ '''..........:''' +Orange+ '''=...     =+ .   ''' +blue+ '''  . ''' +Orange+ '''
       =====..-==+''' +yellow+ '''..........''' +Orange+ '''====-:=====          
       .-==+===+++*''' +yellow+ ''':.......''' +Orange+ '''=+====+-:..           
        .:..:+*++*:..:-.  :*+++++.               
           .:=-=++.        +===:-.                  

'''
SystemFixer = 'Ik1hZGUgYnkgQGNvbXB1dGVyZXJtYW4gKEZvbGxvdyBtZSBvbiBYOiBATmlzaGFudFRoZUcpXG5cbkdhbWUgTG9hZGVkISBQcmVzcyBFbnRlcjogIg=='

Nothing = rainbow_text('>>> Pokemon Final Protocol <<<\n\n')




def print2(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(float(settingsAndcodes['TypeSpeed']))  # Adjust the delay (in seconds) as needed
    print()  # Add a newline character at the end


def clear():
    if os.name == 'posix':
        os.system('clear')  # For Unix/Linux
    elif os.name == 'nt':
        os.system('cls')  # For Windows


global type_effectiveness
type_effectiveness = {
    'Normal': {'Ghost': 0.5, 'Steel': 0.5, 'Grass': 2.0, 'Rock': 0.5, 'Delta-Dragon': 0.75,'Cosmic':0.5,'Wonder-Gaurd':0.0},
    'Fire': {'Water': 0.5, 'Grass': 2.0, 'Ice': 2.0, 'Bug': 2.0, 'Rock': 0.5, 'Steel': 2.0, 'Dragon': 0.5, 'Delta-Dragon': 2.0, 'Delta-Fire':0.5, 'Delta-Water': 0.5,'Cosmic':0.5,'Wonder-Gaurd':2.0},
    'Water': {'Fire': 2.0, 'Electric': 0.5, 'Ice': 0.5, 'Steel': 2.0, 'Rock': 2.0, 'Ground': 2.0, 'Dragon': 0.5, 'Delta-Dragon': 0.55, 'Delta-Fire':2.0, 'Delta-Water': 0.5,'Cosmic':0.5,'Wonder-Gaurd':0.0},
    'Electric': {'Water': 2.0, 'Grass': 0.5, 'Ground': 0.5, 'Flying': 2.0, 'Steel': 2.0, 'Dragon': 0.5, 'Delta-Dragon': 2.0,'Cosmic':2.0,'Wonder-Gaurd':0.0},
    'Grass': {'Water': 2.0, 'Fire': 0.5, 'Ground': 2.0, 'Flying': 0.5, 'Bug': 0.5, 'Rock': 2.0, 'Steel': 0.5, 'Delta-Dragon': 0.86, 'Delta-Water': 2.0,'Cosmic':2.0,'Wonder-Gaurd':2.0},
    'Ice': {'Fire': 0.5, 'Water': 0.5, 'Grass': 2.0, 'Ground': 2.0, 'Flying': 2.0, 'Steel': 0.5, 'Dragon': 2.0, 'Delta-Dragon': 1.6, 'Delta-Water': 1.5,'Cosmic':0.5, 'Bug': 2.0, 'Delta-Fire': 0.8,'Wonder-Gaurd':0.0},
    'Fighting': {'Ice': 2.0, 'Flying': 0.5, 'Psychic': 0.5, 'Bug': 0.5, 'Rock': 2.0, 'Ghost': 0.5, 'Dark': 2.0, 'Steel': 2.0, 'Fairy': 2.0, 'Delta-Dragon': 0.58,'Wonder-Gaurd':0.0},
    'Poison': {'Grass': 2.0, 'Poison': 0.5, 'Bug': 2.0, 'Rock': 0.5, 'Steel': 0.5, 'Fairy': 2.0, 'Water': 2.0, 'Delta-Dragon': 0.75, 'Delta-Water': 0.5,'Wonder-Gaurd':0.0},
    'Ground': {'Fire': 2.0, 'Electric': 2.0, 'Grass': 0.5, 'Flying': 0.5, 'Rock': 2.0, 'Steel': 2.0, 'Delta-Dragon': 0.75, 'Delta-Fire': 2.0,'Cosmic':0.5,'Wonder-Gaurd':0.0},
    'Flying': {'Electric': 0.5, 'Grass': 2.0, 'Fighting': 2.0, 'Bug': 2.0, 'Rock': 2.0, 'Steel': 0.5, 'Delta-Dragon': 0.75,'Cosmic':0.5,'Wonder-Gaurd':2.0},
    'Psychic': {'Ground': 2.0,'Fighting': 2.0, 'Poison': 2.0, 'Bug': 2.0, 'Ghost': 0.5, 'Dark': 0.5, 'Steel': 0.5, 'Rock': 0.5, 'Delta-Dragon': 0.49,'Cosmic':2.0,'Wonder-Gaurd':0.0},
    'Bug': {'Grass': 2.0, 'Ground': 2.0, 'Flying': 0.5, 'Fire': 0.5, 'Fairy': 2.0, 'Bug': 2.0, 'Delta-Dragon': 0.56,'Cosmic':0.5,'Wonder-Gaurd':0.0},
    'Rock': {'Fire': 2.0, 'Ice': 2.0, 'Fighting': 0.5, 'Ground': 0.5, 'Steel': 0.5, 'Flying': 2.0, 'Dragon': 2.0, 'Electric': 2.0, 'Delta-Dragon': 0.65, 'Delta-Water': 0.5,'Bug':2.0,'Wonder-Gaurd':2.0,'Wonder-Gaurd':2.0},
    'Ghost': {'Normal': 0.5, 'Psychic': 2.0, 'Fighting': 2.0, 'God': 0.5, 'Dark': 0.5, 'Poison': 2.0, 'Delta-Dragon': 0.75,'Cosmic':2.0,'Wonder-Gaurd':2.0},
    'Dragon': {'Dragon': 2.0, 'Steel': 0.5, 'Fairy': 0.5, 'Fire': 2.0, 'Water': 2.0, 'Grass': 2.0, 'Electric': 0.5, 'Delta-Dragon': 0.87, 'Delta-Water': 0.5, 'Delta-Fire':2.0,'Cosmic':0.5,'Wonder-Gaurd':0.0},
    'Dark': {'Fighting': 0.5, 'Psychic': 2.0, 'Ghost': 2.0, 'Fairy': 0.5, 'Ground': 2.0, 'Bug': 2.0, 'Poison': 0.5, 'Delta-Dragon': 0.66,'Cosmic':0.5,'Wonder-Gaurd':2.0},
    'Steel': {'Ice': 2.0, 'Rock': 2.0, 'Steel': 0.5, 'Fairy': 2.0, 'Fire': 0.5, 'Fighting': 0.5, 'Dark': 2.0, 'Delta-Dragon': 0.75,'Cosmic':0.5,'Wonder-Gaurd':0.0},
    'Fairy': {'Fighting': 2.0, 'Poison': 0.5, 'Bug': 0.5, 'Steel': 0.5, 'Dragon': 2.0, 'Dark': 2.0, 'Fire': 0.5, 'Delta-Dragon': 0.66,'Cosmic':2.0,'Wonder-Gaurd':2.0},
    'Cosmic': {'Flying': 0.5, 'Steel': 2.0, 'Rock': 2.0, 'Dragon': 0.5, 'Fairy': 2.0, 'Ghost': 2.0,'Ground':0.5, 'Delta-Dragon': 2.0, 'Delta-Water': 2.0, 'Delta-Fire': 2.0, 'Psychic':0.5, 'Electric': 0.5,'Wonder-Gaurd':2.0},

    'God': {'Normal': 2.0, 'Fighting': 2.0, 'Fire': 2.0, 'Water': 2.0, 'Electric': 2.0, 'Grass': 2.0, 'Ice': 2.0, 'Poison': 2.0, 'Ground': 2.0, 'Flying': 2.0, 'Psychic': 2.0, 'Bug': 2.0, 'Rock': 2.0, 'Ghost': 2.0, 'Dragon': 2.0, 'Dark': 2.0, 'Steel': 2.0, 'Fairy': 2.0, 'God': 2.0, 'Delta-Dragon': 2.0,'Delta-Water':2.0, 'Delta-Fire': 2.0,'Cosmic': 2.0,'Wonder-Gaurd':2.0}, 
    'Delta-Dragon': {'Normal': 1.3, 'Fighting': 1.3, 'Fire': 0.5, 'Water': 0.5, 'Electric': 2.0, 'Grass': 0.5, 'Ice': 1.3, 'Poison': 1.3, 'Ground': 1.6, 'Flying': 1.2, 'Psychic': 2.0, 'Bug': 1.3, 'Rock': 1.3, 'Ghost': 1.2, 'Dragon': 1.3, 'Dark': 1.3, 'Steel': 0.5, 'Fairy': 1.3, 'God': 1.3, 'Delta-Fire':2.0, 'Delta-Water': 2.0,'Cosmic':0.5,'Wonder-Gaurd':0.0},
    'Delta-Fire': {'Water': 2.0, 'Grass': 0.5, 'Ice': 0.5, 'Bug': 2.0, 'Rock': 1.3, 'Steel': 2.0, 'Delta-Dragon': 0.5, 'Normal': 1.2, 'Fighting': 1.3, 'Fire': 0.5, 'Electric': 1.1, 'Ghost': 2.0, 'Dark': 1.1,'Fairy': 1.2, 'God': 1.1, 'Psychic': 1.1, 'Poison': 1.1, 'Ground': 1.1, 'Flying': 1.2, 'Delta-Water': 0.5, 'Cosmic':0.5,'Wonder-Gaurd':2.0},
    'Delta-Water': {'Water': 0.5, 'Grass': 2.0, 'Ice': 1.2, 'Bug': 1.1, 'Rock': 1.1, 'Steel': 1.1, 'Dragon': 1.1, 'Delta-Dragon': 0.5, 'Fire': 2.0, 'Electric': 1.2, 'Ghost': 1.21, 'Dark': 1.1,'Fairy': 1.2, 'God': 1.1, 'Psychic': 1.1, 'Poison': 1.2, 'Ground': 2.0, 'Flying': 0.5, 'Delta-Fire': 0.5,'Cosmic':0.5,'Wonder-Gaurd':0.0},
    'Wonder-Gaurd': {'Psychic': 2.0, 'Dark': 0.5, 'Grass': 0.5, 'Ground': 0.5, 'Flying': 0.5, 'Fire': 0.5, 'Fairy': 2.0, 'Bug': 2.0,'Wonder-Gaurd':2.0,'Cosmic':2.0},

}

def type_damage_multiplier(attacking_type, defending_type):
    damage_multiplier = 1.0

    if attacking_type in type_effectiveness and defending_type in type_effectiveness[attacking_type]:
      damage_multiplier = type_effectiveness[attacking_type][defending_type]
    return float(damage_multiplier)




def battle(odds, enemyPokemon_Selected, OpponentName, yourPokemonSTORYONLY, coins):
      NEWVARcoinsWILD = coins
      try:
        my_sound.play(-1)
      except:
        pass
      clear()
      if enemyPokemon_Selected == False:
            if odds < 60:
                while True:
                  enemyPokemon_Selected = random.choice(list(Pokemon.keys()))
                  if Pokemon[enemyPokemon_Selected]['price'] >= 250:
                    continue
                  else:
                    break
            else:
                while True:
                  enemyPokemon_Selected = random.choice(list(Pokemon.keys()))
                  if Pokemon[enemyPokemon_Selected]['price'] >= 250:
                    break
                  else:
                    continue



      enemyPokemon_NAME = Pokemon[enemyPokemon_Selected]['name']
      yourPokemon = yourPokemon_DATA.copy() if yourPokemonSTORYONLY == False else yourPokemonSTORYONLY.copy()
      REFERENCE_YOUR_POKEMONDATA = yourPokemon_DATA.copy() if yourPokemonSTORYONLY == False else yourPokemonSTORYONLY.copy()
      yourPokemon_NAME = yourPokemon_NAMEpre if yourPokemonSTORYONLY == False else yourPokemonSTORYONLY['name']
      enemyPokemon = Pokemon[enemyPokemon_Selected].copy()
      yourHP = yourPokemon["max_hp"]
      enemyHP = enemyPokemon["max_hp"]

      if OpponentName == False:
        def generate_random_player_name():
          prefixes = ["Bug Catcher", "Pokemon Lover", "Pokemon Trainer", "Team Rocket Grunt", "Grunt", "Rival", "Professor", "Dr.", "Lady", "Nurse", "Officer", "Robber", "Bird Keeper", "Cameraman", "Dancer", "Scientist", "Boxer", "Baley Dancer", "Corp. CEO", "Corp. President", "Pokemon Fan", "Sleepy", "Typical NPC", "Schoolboy", "Schoolgirl", "Convicted Felon", "Kalos Queen", "Psycho Murderer", "Anonnying Baby", "Tree Lover", "Black Belt", "BJJ Fan", "ESports Gamer", "Strict Cop", "Currupt Politician", "Monk", "Evalangelist", "Gangster", "Escaped Prisoner", "Typical Earthling", "Swimmer", "Athlete", "Super Nerd", "Egoticial Snob", "Typical Bro", "Planter", "Gardener", "Doctor", "City Governer", "Nomad", "Kind Humanitarian", "Angryman", "Angrywoman", "Sweetheart", "Guru", "Archeologist", "Scholar", "Newbie Trainer", "Poketrainer", "Gym Leader", "Elite Trainer", "Digimon Trainer", "Professor", "Ace Trainer", "Battle Legend", "Team Leader", "Gym Challenger", "Pokemon Breeder", "Pokemon Coordinator", "Safari Zone Warden", "Frontier Brain", "Pokemon Ranger", "Pokemon Researcher", "Pokemon Collector", "Team Rocket Grunt", "Team Quasar Grunt", "Colonel"
]
          specialPrefixes = ["Pokemon Master", "Regional Champion", "Global Champion", "Elite Four", "Leader", "Admin", "Ohio Final Boss", "Youtuber", "Creator", "Former Champion", "Florida Man", "Australia Final Boss", "President", "King", "Aura Farmer", "Top Dogg", "Queen", "Environmental Activist", "Greek God", "Greek Goddess", "Average Enjoyer", "The Rizzler", "Multiverse Champion", "Pokemon Creator", "Developer", "Last Trainer", "Light-Year Traveler", "Time Traveler", "Final Sakura", "Esports Champion", "Supreme Leader", "Martian", ]
          suffixes = ["Lan", "Green", "Austin", "Carter", "Iyer", "Ivor", "James", "Jacob", "Felipe", "Scott", "Aarav", "Yashmail", "Freon", "Jesse", "Ithica", "Mary", "Luna", "Maria", "Nishant", "Ken", "Farid", "Alexis", "Luciana", "Edwards", "Sakura", "Imran", "Alferd", "Vladmir", "Singh", "Joe", "Jenny", "Shea", "Matt", "Chad", "Tyson", "Mike", "Jordan", "Lebron", "Kobe", "Lee-Hung", "Mohammad", "Hussien", "Byung-Hun", "Yamada", "Joeseph", "Cornelius", "Vide", "Natasha", "Ben", "Matep", "Zorga", "Salman", "Solomon", "Thomas", "Hesus", "William", "Bill", "Yetus", "Alan", "Mary", "Ella", "Sarah", "Eugene", "Edwards", "Dan", "Ashley", "Vlodemhir", "Georgia", "Luciana", "Lucy", "Pearl", "Diamond", "Scarlet", "Pearl", "Ruby", "Sapphire", "Karen", "Emerald", "Aseenee", "Pocoman", "Bella", "Fukumina", "Sumatra", "Ruby", "Artep", "Mansinlla", "Artilah", "Kaur", "Asli", "Elif", "Said", "Roxelana", "Zehra", "Mustafa", "Kemal", "Akio", "Emi", "Ravi", "Anjali", "Santiago", "Amara", "Yasir", "Mariam", "Zain", "Amina", "Ramon", "Nina", "Faisal", "Farida", "Luca", "Giulia", "Satoshi", "Hanah", "Arjun", "Priya", "Nabil", "Amina", "Luigi", "Giovanna", "Hassan", "Fatima", "Ibrahim", "Leila", "Javier", "Elena", "Kenta", "Yuki", "Mikhail", "Svetlana", "Raul", "Carmen", "Aditya", "Aishwarya", "Gabriel", "Isabel", "Hiroshi", "Yui", "Anton", "Natalia", "Fadi", "Layla", "Renato", "Giulia", "Vikram", "Connor", "Emma", "Liam", "Olivia", "Mason", "Ava", "Noah", "Sophia", "Ethan", "Isabella", "Caleb", "Mia", "Logan", "Amelia", "Aiden", "Harper", "Jackson", "Evelyn", "Lucas", "Abigail", "Jack", "Emily", "Carter", "Charlotte", "William", "Scarlett", "Henry", "Grace", "Owen", "Lily", "Wyatt", "Chloe", "James", "Avery", "Benjamin", "Ella", "Samuel", "Madison", "Alexander", "Elizabeth", "Michael", "Layla", "Elijah", "Nora", "Daniel", "Hannah", "Matthew", "Addison", "Oliver", "Lillian", "Sebastian", "Victoria", "Joseph", "Aubrey", "David", "Paisley", "Andrew", "Brooklyn", "John", "Zoey", "Gabriel", "Natalie", "Jonathan", "Hazel", "Nicholas", "Aria", "Dylan", "Aurora", "Ryan", "Stella", "Nathan", "Nova", "Isaac", "Penelope", "Thomas", "Claire", "Luke", "Luna", "Christopher", "Eleanor", "Julian", "Skylar", "Isaiah", "Sadie", "Christian", "Allison", "Levi", "Lucy","Ling", "Xiu", "Mei", "Yan", "Li", "Hui", "Ying", "Jing", "Fang", "Qian", "Xia", "Wei", "Rui", "Jia", "Yun", "Xinyi", "Lin", "Zhen", "Hong", "Lan", "Qing", "Xiaoli", "Yujie", "Yue", "Lihua", "Lena", "Mia", "Sophie", "Emma", "Hannah", "Anna", "Laura", "Lea", "Lina", "Julia", "Clara", "Emilia", "Charlotte", "Mila", "Marie", "Johanna", "Paula", "Amelie", "Fiona", "Alina", "Isabella", "Eva", "Lara", "Lisa", "Victoria", "Felix", "Lukas", "Maximilian", "Leon", "Luca", "Benjamin", "Paul", "Jonas", "Elias", "Simon", "Nico", "Anton", "Mats", "Fabian", "Tim", "Philipp", "Moritz", "Johannes", "Julian", "David", "Noah", "Eric", "Tom", "Alexander", "Daniel","Aarav", "Rohan", "Arjun", "Vikram", "Ravi", "Kiran", "Aniket", "Arya", "Amit", "Ishaan", "Zayn", "Imran", "Aadil", "Amitabh", "Rajat", "Vivek", "Rajiv", "Kunal", "Dev", "Aarush", "Varun", "Rahul", "Harish", "Nikhil", "Siddharth","Aisha", "Priya", "Ananya", "Kavya", "Ishita", "Pooja", "Neha", "Sakshi", "Meera", "Diya", "Zara", "Nina", "Sanjana", "Trisha", "Riya", "Sara", "Jiya", "Lavanya", "Swara", "Ayesha", "Amara", "Nidhi", "Aruna", "Ishika", "Shreya", "Emre", "Enes", "Arda", "Kaan", "Alp", "Batu", "Burak", "Ege", "Cem", "Can", "Deniz", "Eren", "Umut", "Kerem", "Ozan", "Baran", "Doruk", "Tolga", "Yusuf", "Mert", "Selim", "Uğur", "Metin", "Onur", "Orhan","Elif", "Zeynep", "Aslı", "Melis", "Ezgi", "Ceren", "Naz", "Ayşe", "Dilara", "Ece", "Yasmin", "Deniz", "Ela", "Simge", "Selin", "Yagmur", "Beyza", "Hazal", "Pelin", "Sevgi", "Sude", "Gizem", "İrem", "Damla", "Rabia", "Amir", "Laila", "Zayd", "Amina", "Tariq", "Fatima", "Khalid", "Sana", "Ahmed", "Leila", "Jamal", "Nadia", "Yasin", "Yasmin", "Omar", "Zahra", "Ali", "Hana", "Rami", "Farida", "Rashid", "Layla", "Hassan", "Aisha", "Nasir","Kwame", "Nia", "Chijioke", "Amani", "Sekou", "Zara", "Jabari", "Nala", "Sefu", "Ayana", "Oluwaseun", "Kwesi", "Ngozi", "Kofi", "Imani", "Jelani", "Adanna", "Kwabena", "Kamaria", "Jengo", "Zuri", "Kwaku", "Nia", "Jelani", "Asha", "Adidan", "Graden", "Grace", "Ayman", "Armenia",
]
          specialSuffixes = ["Red","Gary", "Cynthia", "Lance", "Scaryan", "Ash", "Oak", "Serena", "Satoyu", "Rajih", "Ghandi", "Ali", "Pewdiepie", "Misty", "Blue", "Gold", "Diantha", "Wallace", "Mehmet", "Hesus", "Nemona", "Steven", "Iris", "Leon", "Khamzat", "Seneca", "Socrates", "Andrew", "Trumpet", "Obrahom", "Nas", "Nish", "Obama", "Greta", "Zyzz", "Chestbrah", "Gigachad", "Adonis", "Tristah", "Austin", "Carter", "Elon", "Musk", "MrBeast", "VSauce", "Satya", "Katrina", "Bruce", "Bezos", "Jung", "Jimping", "Khan", "Ishten", "Sasuke", "Yotoshi", "???", "Misty", "Jet"]

          name = random.choice(prefixes) + " " + random.choice(suffixes)
          Specialname = random.choice(specialPrefixes) + " " + random.choice(specialSuffixes)

          if odds < 60:
            return name
          else:
            return Specialname

        OpponentName = generate_random_player_name()


      # Calculate speed for both Pokémon
      yourSpeed = yourPokemon["speed"]
      enemySpeed = enemyPokemon["speed"]

      clear()
      if settingsAndcodes['ASCII'] == True:
        if settingsAndcodes['GigachadMode'] == False:
          print(ASCIIVARIABLE[1])
        else:
          print(ASCIIVARIABLE[2])
      elif settingsAndcodes['ASCII'] == False:
        pass
      if OpponentName == Pokemon[enemyPokemon_Selected]['name']:
        print2(Red + f">>> Wild {OpponentName}{Red} has appeared! <<<\n")
      else:
        print2(Red + f">>> {OpponentName}{Red} would like to battle! <<<\n")
        print2(Red + f">> {OpponentName} sends out {enemyPokemon_NAME}{Red}!")
      print2(Green + f">> Go {yourPokemon_NAME}{Green}!\n")
      if yourPokemon['ability'] == 'Speed Drain (Pokemon steals 25% of enemy Speed for itself.)':
          yourSpeed += int(enemySpeed*0.25)
          enemySpeed = int(enemySpeed*0.75)
          print2(Blue + f">> {yourPokemon_NAME}" + Blue +" stole 25% of the enemy's speed for itself!\n")
      if enemyPokemon['ability'] == 'Speed Drain (Pokemon steals 25% of enemy Speed for itself.)':
          enemySpeed += int(yourSpeed*0.25)
          yourSpeed = int(yourSpeed*0.75)
          print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" stole 25% of the your Pokemon's speed for itself!\n")

      if yourPokemon['ability'] == 'Super Imposter (Clones itself into enemy Pokemon with all stats, type, HP, and abiliity!)':
          yourPokemon['ability'] = enemyPokemon['ability']
          yourPokemon['type'] = enemyPokemon["type"]
          yourPokemon['power'] = enemyPokemon["power"]
          yourPokemon['max_hp'] = enemyPokemon["max_hp"]
          yourHP = enemyHP
          yourPokemon['speed'] = enemyPokemon["speed"]
          yourSpeed = enemySpeed
          print2(Blue + f">> {yourPokemon_NAME}" + Blue +" has copied foe Pokemon!\n")
      if enemyPokemon['ability'] == 'Super Imposter (Clones itself into enemy Pokemon with all stats, type, HP, and abiliity!)':
          enemyPokemon['ability'] = yourPokemon['ability']
          enemyPokemon['type'] = yourPokemon["type"]
          enemyPokemon['power'] = yourPokemon["power"]
          enemyPokemon['max_hp'] = yourPokemon["max_hp"]
          enemyHP = yourHP
          enemyPokemon['speed'] = yourPokemon["speed"]
          enemySpeed = yourSpeed
          print2(Blue + f">> {enemyPokemon_NAME}" + Blue +" has copied your Pokemon!\n")
      if yourPokemon['ability'] == 'Nutrifier (Disables enemy ability and turns type to normal.)':

        enemyPokemon['ability'] = None

        enemyPokemon['type'] = 'Normal'
        print2(Blue + f">> {yourPokemon_NAME}" + Blue +" has disabled the enemy Pokemon's ability and type!\n")
      if enemyPokemon['ability'] == 'Nutrifier (Disables enemy ability and turns type to normal.)':

        yourPokemon['ability'] = None

        yourPokemon['type'] = 'Normal'
        print2(Blue + f">> {enemyPokemon_NAME}" + Blue +" has disabled the your Pokemon's ability!\n")

      if yourPokemon['ability'] == 'Truantifier (Enemy ability becomes taunt.)' or yourPokemon['ability'] == 'Cute Charm (Enemy becomes attracted to this Pokemon & moves every other turn!)':

        enemyPokemon['ability'] = 'Truant (Pokemon is too lazy, disobeys every third turn.)'

        print2(Blue + f">> {yourPokemon_NAME}" + Blue +" has turned the enemy Pokemon's ability into truant!\n")
      if enemyPokemon['ability'] == 'Truantifier (Enemy ability becomes taunt.)' or enemyPokemon['ability'] == 'Cute Charm (Enemy becomes attracted to this Pokemon & moves every other turn!)':

        yourPokemon['ability'] = 'Truant (Pokemon is too lazy, disobeys every third turn.)'

        print2(Blue + f">> {enemyPokemon_NAME}" + Blue +" has turned your Pokemon's ability into truant!\n")


      if yourPokemon['ability'] == 'Magic Maid (Steals Pokemon Ability)':
              yourPokemon['ability'] = enemyPokemon['ability']
              enemyPokemon['ability'] = None
              print2(Blue + f">> {yourPokemon_NAME}" + Blue +" has stolen enemy Pokemon's ability!\n")
      if enemyPokemon['ability'] == 'Magic Maid (Steals Pokemon Ability)':
              enemyPokemon['ability'] = yourPokemon['ability']
              yourPokemon['ability'] = None
              print2(Blue + f">> {enemyPokemon_NAME}" + Blue +" has stolen your Pokemon's ability!\n")



      if yourPokemon['ability'] == 'Genetic Stealer (Steals 1he enemy Pokemon type & ability for itself, enemy type changes to Normal and does not have ability anymore)':
          yourPokemon['ability'] = enemyPokemon['ability']
          enemyPokemon['ability'] = None
          yourPokemon['type'] = enemyPokemon["type"]
          enemyPokemon['type'] = 'Normal'
          print2(Blue + f">> {yourPokemon_NAME}" + Blue +" has stolen enemy Pokemon's ability and type!\n")
      if enemyPokemon['ability'] == 'Genetic Stealer (Steals 1he enemy Pokemon type & ability for itself, enemy type changes to Normal and does not have ability anymore)':
          enemyPokemon['ability'] = yourPokemon['ability']
          yourPokemon['ability'] = None
          enemyPokemon['type'] = yourPokemon["type"]
          yourPokemon['type'] = 'Normal'
          print2(Blue + f">> {enemyPokemon_NAME}" + Blue +" has stolen your Pokemon's ability and type!\n")


      if yourPokemon['ability'] == 'Luck of Ohio (Pokemon HP is tripled in battle!)':
          yourPokemon["max_hp"] = yourPokemon["max_hp"] * 3
          yourHP = yourHP * 3
          print2(Blue + f">> The luck of Ohio has tripled your Pokemon's HP due, average Ohio moment 💀\n")
      if enemyPokemon['ability'] == 'Luck of Ohio (Pokemon HP is tripled in battle!)':
          enemyPokemon["max_hp"] = enemyPokemon["max_hp"] * 3
          print2(Blue + f">> The luck of Ohio has tripled enemy Pokemon's HP, what is bro gon do now 💀\n")
          enemyHP = enemyHP*3



      if yourPokemon['ability'] == 'Ultimate Defense (HP is doubled!)':
        yourPokemon["max_hp"] = yourPokemon["max_hp"] * 2
        yourHP = yourHP * 2
        print2(Blue + f">> {yourPokemon_NAME}" + Blue +" doubled its HP due to its ability!\n")
      if enemyPokemon['ability'] == 'Ultimate Defense (HP is doubled!)':
        enemyPokemon["max_hp"] = enemyPokemon["max_hp"] * 2
        enemyHP = enemyHP*2
        print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" doubled its HP due to its ability!\n")


      if yourPokemon['ability'] == 'Super Power (Power is doubled!)':
          yourPokemon["power"] = yourPokemon["power"] * 2
          print2(Blue + f">> {yourPokemon_NAME}" + Blue +" doubled its power due to its ability!\n")
      if enemyPokemon['ability'] == 'Super Power (Power is doubled!)':
          enemyPokemon["power"] = enemyPokemon["power"] * 2
          print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" doubled its power due to its ability!\n")

      if yourPokemon['ability'] == 'STAB (Power boosted by 50%)':
            yourPokemon["power"] = yourPokemon["power"] * 1.5
            print2(Blue + f">> {yourPokemon_NAME}" + Blue +" increased its power due to its ability!\n")
      if enemyPokemon['ability'] == 'STAB (Power boosted by 50%)':
            enemyPokemon["power"] = enemyPokemon["power"] * 1.5
            print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" increased its power due to its ability!\n")



      if yourPokemon['ability'] == 'Intimidation (Reduces enemy power by 25%!)':
        enemyPokemon["power"] = enemyPokemon["power"] * (7.5/10)
        print2(Blue + f">> {yourPokemon_NAME}" + Blue +" lowered enemy power due to its intimidating energy!\n")
      if enemyPokemon['ability'] == 'Intimidation (Reduces enemy power by 25%!)':
        yourPokemon["power"] = yourPokemon["power"] * (7.5/10)
        print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" lowered your power due to its intimidating energy!\n")







      if yourPokemon['ability'] == 'Undisguise (Intimidation + Disguise Combined.)':
        enemyPokemon["power"] = enemyPokemon["power"] * (7.5/10)
        yourPokemon['ability'] ='Disguise (Nullifies the first enemy attack.)'
        print2(Blue + f">> {yourPokemon_NAME}" + Blue +" lowered enemy power due to its sheer creepyness!\n")
      if enemyPokemon['ability'] == 'Undisguise (Intimidation + Disguise Combined.)':
        yourPokemon["power"] = yourPokemon["power"] * (7.5/10)
        enemyPokemon['ability'] = 'Disguise (Nullifies the first enemy attack.)'
        print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" lowered your power due to its sheer creepyness!\n")

      if yourPokemon['ability'] == 'Aura System (If enemy Pokemon is Fairy or Dark typed, their power and speed are cut in half.)' and (enemyPokemon['type'] == 'Fairy' or enemyPokemon['type'] == 'Dark'):
        enemyPokemon["power"] = enemyPokemon["power"] * (5/10)
        enemySpeed = enemySpeed * (5/10)
        print2(Blue + f">> {yourPokemon_NAME}" + Blue +" halved enemy power and speed due to its anti fairy/dark ability!\n")
      if enemyPokemon['ability'] == 'Aura System (If enemy Pokemon is Fairy or Dark typed, their power and speed are cut in half.)' and (yourPokemon['type'] == 'Fairy' or yourPokemon['type'] == 'Dark'):
        yourPokemon["power"] = yourPokemon["power"] * (5/10)
        yourSpeed = yourSpeed * (5/10)
        print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" halved your power due to its anti fairy/dark ability!\n")




      if yourPokemon['ability'] == 'Blaze Intimidation (Reduces enemy power by 50%!)':
          enemyPokemon["power"] = enemyPokemon["power"] * (5/10)
          print2(Blue + f">> {yourPokemon_NAME}" + Blue +" halved enemy power due to its intimidating blaze!\n")
      if enemyPokemon['ability'] == 'Blaze Intimidation (Reduces enemy power by 50%!)':
          yourPokemon["power"] = yourPokemon["power"] * (5/10)
          print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" halved your power due to its intimidating blaze!\n")

      if yourPokemon['ability'] == 'Brain Drain (Pokemon steals 25% of enemy Power for itself.)':
          yourPokemon["power"] += int(enemyPokemon["power"]*0.25)
          enemyPokemon["power"] = int(enemyPokemon["power"]*0.75)
          print2(Blue + f">> {yourPokemon_NAME}" + Blue +" stole 25% of the enemy's power for itself!\n")
      if enemyPokemon['ability'] == 'Brain Drain (Pokemon steals 25% of enemy Power for itself.)':
          enemyPokemon["power"] += int(yourPokemon["power"]*0.25)
          yourPokemon["power"] = int(yourPokemon["power"]*0.75)
          print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" stole 25% of the your Pokemon's power for itself!\n")



      if yourPokemon['ability'] == "Delta Stream (Pokemon is Delta typed, more damage and better defense, though effectivness depends on enemy typing.)":
          print2(Blue + f">> An odd stream has appeared and the weather is behaving weirdly with thunderstorms, droughts, rainfall, heavy wind...all at the same time! Everyone is confused and Pokemon are behaving differently!\n")
      if enemyPokemon['ability'] == "Delta Stream (Pokemon is Delta typed, more damage and better defense, though effectivness depends on enemy typing.)":
        print2(Blue + f">> An odd stream has appeared and the weather is behaving weirdly with thunderstorms, droughts, rainfall, heavy wind...all at the same time! Everyone is confused and Pokemon are behaving differently!\n")


      if yourPokemon['ability'] =='God Typing (Pokemon is God typed, supereffective to all.)':
          print2(Blue + f">> Time and dimension are suddenly breaking, destruction is happening everywhere and unidentifable objects are falling from the sky. The multiverse is unstable and every entity is afraid. What the hell is happening???.\n")
      elif enemyPokemon['ability'] == 'God Typing (Pokemon is God typed, supereffective to all.)':
          print2(Blue + f">> Time and dimension are suddenly breaking, destruction is happening everywhere and unidentifable objects are falling from the sky. The multiverse is unstable and every entity is afraid. What the hell is happening???.\n")
      if yourPokemon['ability'] =='Ultra Amplifier (Recoverer + Unleashed Combined)':
        print2(Blue + f">> The dimensions have been Amplified for {yourPokemon['name']} via the gods!\n")
      elif enemyPokemon['ability'] == 'Ultra Amplifier (Recoverer + Unleashed Combined)':
        print2(Blue + f">> The dimensions have been Amplified for foe {enemyPokemon['name']} via the gods!\n")

      if yourPokemon['ability'] =='Speed of Light (This Pokemon moves at the speed of light.)':
          print2(Blue + f">> Your Pokemon has caused a disturbance in the dimension due to its sheer speed!\n")
      if enemyPokemon['ability'] == 'Speed of Light (This Pokemon moves at the speed of light.)':
          print2(Blue + f">> Foe Pokemon has caused a disturbance in the dimension due to its sheer speed!\n")
      if yourPokemon['ability'] =='Wonder Guard (Supereffective moves only or some other shenanigans)':
        print2(Blue + f">> Your Pokemon possesses the wonder guard, oh yes!\n")
      if enemyPokemon['ability'] == 'Wonder Guard (Supereffective moves only or some other shenanigans)':
        print2(Blue + f">> Foe Pokemon possesses the wonder guard, oh no!\n")

      time.sleep(1)
      #START
      int(yourHP)
      int(yourPokemon["max_hp"])
      int(yourPokemon['power'])
      int(yourSpeed)
      int(yourPokemon['speed'])
      int(enemyHP)
      int(enemyPokemon["max_hp"])
      int(enemyPokemon['power'])
      int(enemySpeed)
      int(enemyPokemon['speed'])

      yourProtectTurnTotal = 2
      enemyProtectTurnTotal = 2
      slakingYOUTURN = 1
      slakingENEMYTURN = 1
      totalturns = 0
      while yourHP > 0 and enemyHP > 0:

          if yourPokemon['ability'] == 'Soul Stealer (Steals 15% of Power, HP, and Speed from the enemy each turn)':
            enemyPokemon['power'] -= int(enemyPokemon["power"] * 0.15)
            enemyPokemon['max_hp'] -= int(enemyPokemon["max_hp"] * 0.15)
            enemyHP -= int(enemyHP* 0.15)
            enemyPokemon['speed'] -= int(enemyPokemon["speed"]* 0.15)
            enemySpeed -= int(enemySpeed*0.15)

            yourPokemon['power'] += int(enemyPokemon["power"] * 0.15)
            yourPokemon['max_hp'] += int(enemyPokemon["max_hp"] * 0.15)
            yourHP += int(enemyHP* 0.15)
            yourPokemon['speed']+= int(enemyPokemon["speed"]* 0.15)
            yourSpeed += int(enemySpeed*0.15)




            print2(Blue + f">> {yourPokemon_NAME}" + Blue +" has stolen 15% of enemy Pokemon's Power, HP, and Speed!\n")
          if enemyPokemon['ability'] == 'Soul Stealer (Steals 15% of Power, HP, and Speed from the enemy each turn)':
            enemyPokemon['power'] += int(yourPokemon["power"] * 0.15)
            enemyPokemon['max_hp'] += int(yourPokemon["max_hp"] * 0.15)
            enemyHP += int(yourHP* 0.15)
            enemyPokemon['speed'] += int(yourPokemon["speed"]* 0.15)
            enemySpeed += int(yourSpeed*0.15)

            yourPokemon['power'] -= int(yourPokemon["power"]* 0.15)
            yourPokemon['max_hp'] -= int(yourPokemon["max_hp"]* 0.15)
            yourHP -= int(yourHP* 0.15)
            yourPokemon['speed'] -= int(yourPokemon["speed"]* 0.15)
            yourSpeed -= int(yourSpeed* 0.15)

            print2(Blue + f">> {enemyPokemon_NAME}" + Blue +" has stolen 15% of your Pokemon's Power, HP, and Speed!\n")

          if yourPokemon['ability'] =='Speed Boost (Pokemon doubles speed each turn.)':
              yourSpeed *= 2
              yourPokemon['speed'] *= 2
              print2(Blue + f">> Your Pokemon has gained 2x speed due to its ability!\n")

          if enemyPokemon['ability'] == 'Speed Boost (Pokemon doubles speed each turn.)':
              enemySpeed *= 2
              enemyPokemon['speed'] *= 2
              print2(Blue + f">> Foe Pokemon has gained 2x speed due to its ability!\n")


          if yourPokemon['ability'] =='Moody (Each turn, 2x random stat, 0.75x random stat)':
            randomstatincrease = random.randint(1,3)
            randomstatdecrease = random.randint(1,3)

            if randomstatincrease == 1:
              yourHP *= 2
              yourPokemon["max_hp"] *= 2
              print2(Blue + f">> Your Pokemon has gained 2x HP due to its ability!\n")
            elif randomstatincrease == 2:
              yourSpeed *= 2
              yourPokemon['speed'] *= 2
              print2(Blue + f">> Your Pokemon has gained 2x speed due to its ability!\n")
            elif randomstatincrease == 3:
              yourPokemon['power'] *= 2
              print2(Blue + f">> Your Pokemon has gained 2x power due to its ability!\n")

            if randomstatdecrease == 1:
              yourHP *= 0.75
              yourPokemon["max_hp"] *= 0.75

              print2(Blue + f">> Your Pokemon has now 0.75x HP due to its ability!\n")
            elif randomstatdecrease == 2:
              yourSpeed *= 0.75
              yourPokemon['speed'] *= 0.75
              print2(Blue + f">> Your Pokemon has now 0.75x Speed due to its ability!\n")
            elif randomstatdecrease == 3:
              yourPokemon['power'] *= 0.75
              print2(Blue + f">> Your Pokemon has now 0.75x power due to its ability!\n")

          if enemyPokemon['ability'] == 'Moody (Each turn, 2x random stat, 0.75x random stat)':
            randomstatincrease = random.randint(1,3)
            randomstatdecrease = random.randint(1,3)
            if randomstatincrease == 1:
              enemyHP *= 2
              enemyPokemon["max_hp"] *= 2
              print2(Blue + f">> Foe Pokemon has gained 2x HP due to its ability!\n")
            elif randomstatincrease == 2:
              enemySpeed *= 2
              enemyPokemon['speed'] *= 2
              print2(Blue + f">> Foe Pokemon has gained 2x speed due to its ability!\n")
            elif randomstatincrease == 3:
              enemyPokemon['power'] *= 2
              print2(Blue + f">> Foe Pokemon has gained 2x power due to its ability!\n")
            if randomstatdecrease == 1:
              enemyHP *= 0.75
              enemyPokemon["max_hp"] *= 0.75
              print2(Blue + f">> Foe Pokemon has now 0.75x HP due to its ability!\n")
            elif randomstatdecrease == 2:
              enemySpeed *= 0.75
              enemyPokemon['speed'] *= 0.75
              print2(Blue + f">> Foe Pokemon has now 0.75x speed due to its ability!\n")
            elif randomstatdecrease == 3:
              enemyPokemon['power'] *= 0.75
              print2(Blue + f">> Foe Pokemon has now 0.75x power due to its ability!\n")


          if yourPokemon['ability'] =='Ultra Moody (Each turn, 1.5x random stat)':
            randomstatincrease = random.randint(1,3)
            print2(Blue + f">> The gods seem to be gifting energy to {yourPokemon_NAME}")
            if randomstatincrease == 1:
              yourHP *= 1.5
              yourPokemon["max_hp"] *= 1.5
              print2(Blue + f">> Your Pokemon has gained 1.5x HP due to its ability!\n")
            elif randomstatincrease == 2:
              yourSpeed *= 1.5
              yourPokemon['speed'] *= 1.5
              print2(Blue + f">> Your Pokemon has gained 1.5x speed due to its ability!\n")
            elif randomstatincrease == 3:
              yourPokemon['power'] *= 1.5
              print2(Blue + f">> Your Pokemon has gained 1.5x power due to its ability!\n")

          if enemyPokemon['ability'] == 'Ultra Moody (Each turn, 2x random stat)':
            randomstatincrease = random.randint(1,3)
            print2(Blue + f">> The gods seem to be gifting energy to for {enemyPokemon_NAME}")
            if randomstatincrease == 1:
              enemyHP *= 1.5
              enemyPokemon["max_hp"] *= 2
              print2(Blue + f">> Foe Pokemon has gained 1.5x HP due to its ability!\n")
            elif randomstatincrease == 2:
              enemySpeed *= 1.5
              enemyPokemon['speed'] *= 2
              print2(Blue + f">> Foe Pokemon has gained 1.5x speed due to its ability!\n")
            elif randomstatincrease == 3:
              enemyPokemon['power'] *= 1.5
              print2(Blue + f">> Foe Pokemon has gained 1.5x power due to its ability!\n")

          if yourPokemon['ability'] == 'Leftovers (Recovers 10% HP each turn)':
            yourHP = yourHP + int(yourPokemon["max_hp"] * 0.1)
            if yourHP > yourPokemon["max_hp"]:
                yourHP = yourPokemon["max_hp"]
            print2(Blue + f">> {yourPokemon_NAME}" + Blue +" gained some HP due to its ability!\n")
          if enemyPokemon['ability'] == 'Leftovers (Recovers 10% HP each turn)':

              print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" gained some HP due to its ability!\n")
              enemyHP = enemyHP + int(enemyPokemon["max_hp"] * 0.1)
              if enemyHP > enemyPokemon["max_hp"]:
                enemyHP = enemyPokemon["max_hp"]

          if yourPokemon['ability'] == 'Life Aura (Recovers 20% HP each turn + Nullifies Enemy Ability)':
            yourHP = yourHP + int(yourPokemon["max_hp"] * 0.2)
            enemyPokemon['ability'] = None
            if enemyPokemon['type'] == 'Wonder-Gaurd':
              print2(Blue + f">> Foe Wonder Guard is destroyed!\n")
              enemyPokemon['type'] == 'Bug'
            if yourHP > yourPokemon["max_hp"]:
                yourHP = yourPokemon["max_hp"]
            print2(Blue + f">> {yourPokemon_NAME}" + Blue +" gained HP back due to the gods! Foe Pokemon ability is suppressed.\n")
          if enemyPokemon['ability'] == 'Life Aura (Recovers 20% HP each turn + Nullifies Enemy Ability)':
              yourPokemon['ability'] = None
              if yourPokemon['type'] == 'Wonder-Gaurd':
                print2(Blue + f">> Your Pokemon's Wonder Guard is destroyed!\n")
                yourPokemon['type'] == 'Bug'
              print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" gained HP back due to the gods! Your Pokemon ability is suppressed.\n")
              enemyHP = enemyHP + int(enemyPokemon["max_hp"] * 0.2)
              if enemyHP > enemyPokemon["max_hp"]:
                enemyHP = enemyPokemon["max_hp"]

          if yourPokemon['ability'] == 'Z-Power Construct (If HP is less than 50%, doubles all stats, then this ability becomes Leftovers.)' and int((yourHP/yourPokemon['max_hp'])*100) <= 50:
              yourHP *= 2
              yourPokemon["max_hp"] *= 2
              yourSpeed *= 2
              yourPokemon['speed'] *= 2
              yourPokemon['power'] *= 2
              yourPokemon['ability'] = 'Leftovers (Recovers 10% HP each turn)'
              if yourHP > yourPokemon["max_hp"]:
                  yourHP = yourPokemon["max_hp"]
              print2(Blue + f">> {yourPokemon_NAME}" + Blue +" has gained its full legendary potiential via the gods! FAISONS CELA!\n")
          if enemyPokemon['ability'] == 'Z-Power Construct (If HP is less than 50%, doubles all stats, then this ability becomes Leftovers.)' and int((enemyHP/enemyPokemon['max_hp'])*100) <= 50:
              enemyHP *= 2
              enemyPokemon["max_hp"] *= 2
              enemySpeed *= 2
              enemyPokemon['speed'] *= 2
              enemyPokemon['power'] *= 2
              enemyPokemon['ability'] = 'Leftovers (Recovers 10% HP each turn)'
              if enemyHP > enemyPokemon["max_hp"]:
                enemyHP = enemyPokemon["max_hp"]
              print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" has gained its full legendary potiential via the gods! FAISONS CELA!\n")


          if yourPokemon['ability'] == 'Ultimate Contrary (Inverts Stat Changes + Leftovers + Resets Enemy Stat Changes)':

            yourHP = yourHP + int(yourPokemon["max_hp"] * 0.1)
            if yourHP > yourPokemon["max_hp"]:
                yourHP = yourPokemon["max_hp"]

            if yourSpeed < yourPokemon_DATA['speed'] or yourPokemon['power'] < yourPokemon_DATA['power'] or yourPokemon['speed'] < yourPokemon_DATA['speed']:
              yourSpeed = yourPokemon_DATA['speed'] * (2-(yourSpeed/yourPokemon_DATA['speed']))
              yourPokemon['speed'] = yourPokemon_DATA['speed'] * (2-(yourPokemon['speed']/yourPokemon_DATA['speed']))
              yourPokemon['power'] = yourPokemon_DATA['power'] * (2-(yourPokemon['power']/yourPokemon_DATA['power']))

              enemySpeed = Pokemon[enemyPokemon_Selected]['speed']
              enemyPokemon['speed'] = Pokemon[enemyPokemon_Selected]['speed']
              enemyPokemon['power'] = Pokemon[enemyPokemon_Selected]['power']

            print2(Blue + f">> {yourPokemon_NAME}" + Blue +" has been helped by Contrary via the gods! Enemy stats are reset.\n")

          if enemyPokemon['ability'] == 'Ultimate Contrary (Inverts Stat Changes + Leftovers + Resets Enemy Stat Changes)':

            enemyHP = enemyHP + int(enemyPokemon["max_hp"] * 0.1)
            if enemyHP > enemyPokemon["max_hp"]:
                enemyHP = enemyPokemon["max_hp"]

            if enemySpeed < Pokemon[enemyPokemon_Selected]['speed'] or enemyPokemon['power'] < Pokemon[enemyPokemon_Selected]['power'] or enemyPokemon['speed'] < Pokemon[enemyPokemon_Selected]['speed']:  
              enemySpeed = Pokemon[enemyPokemon_Selected]['speed'] * (2-(enemySpeed/Pokemon[enemyPokemon_Selected]['speed']))
              enemyPokemon['speed'] = Pokemon[enemyPokemon_Selected]['speed'] * (2-(enemyPokemon['speed']/Pokemon[enemyPokemon_Selected]['speed']))
              enemyPokemon['power'] = Pokemon[enemyPokemon_Selected]['power'] * (2-(enemyPokemon['power']/Pokemon[enemyPokemon_Selected]['power']))

            yourSpeed = yourPokemon_DATA['speed']
            yourPokemon['speed'] = yourPokemon_DATA['speed']
            yourPokemon['power'] = yourPokemon_DATA['power']
            print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" has been helped by Contrary via the gods! Your Pokemon's stats are reset.\n")

          print(White + f">>> Your {yourPokemon_NAME}" + White + f" HP: {yourHP}/{yourPokemon['max_hp']}"+f" ({int((yourHP/yourPokemon['max_hp'])*100)}%)" + resetlol + f" [Type: {yourPokemon['type']}] <<<" + resetlol + "\n")
          print(White + f">>> Foe {enemyPokemon_NAME}" + White + f" HP: {enemyHP}/{enemyPokemon['max_hp']}"+f" ({int((enemyHP/enemyPokemon['max_hp'])*100)}%)" + resetlol + f" [Type: {enemyPokemon['type']}] <<<" + resetlol + "\n")

          # MOVES
          int(yourHP)
          int(yourPokemon["max_hp"])
          int(yourPokemon['power'])
          int(yourSpeed)
          int(yourPokemon['speed'])
          int(enemyHP)
          int(enemyPokemon["max_hp"])
          int(enemyPokemon['power'])
          int(enemySpeed)
          int(enemyPokemon['speed'])
          moves = {
              1: {"name": Red+"Attack", "power": f"{int(yourPokemon['power']/2)} To {int(yourPokemon['power'])} Damage"},
              2: {"name": Purple+"Recover", "power": f"{int(yourPokemon['max_hp']/3)} To {int(yourPokemon['max_hp']/2)} HP"},
              3: {"name": Cyan+"Protect", "power": "Every Other Turn"},
              4: {"name": cyan+"Compare", "power": "You vs Enemy"},
              5: {"name": green+"Forfeit", "power": "No Coin Loss"} if OpponentName != Pokemon[enemyPokemon_Selected]['name'] else {"name": Green+"Run Away", "power": "No Coin Loss"}
          }  

          if OpponentName == Pokemon[enemyPokemon_Selected]['name']:
            moves = {
                1: {"name": Red+"Attack", "power": f"{int(yourPokemon['power']/2)} To {int(yourPokemon['power'])} Damage"},
                2: {"name": Purple+"Recover", "power": f"{int(yourPokemon['max_hp']/3)} To {int(yourPokemon['max_hp']/2)} HP"},
                3: {"name": Cyan+"Protect", "power": "Every Other Turn"},
                4: {"name": cyan+"Compare", "power": "You vs Enemy"},
                5: {"name": green+"Forfeit", "power": "No Coin Loss"} if OpponentName != Pokemon[enemyPokemon_Selected]['name'] else {"name": Green+"Run Away", "power": "No Coin Loss"},
                6: {"name": yellow+"Catch", "power": f"{int((Pokemon[enemyPokemon_Selected]['price'])*0.25)} To {Pokemon[enemyPokemon_Selected]['price']} Coins"}
            }  


          global enemyChoice
          global yourChoice

          print(White + "\nAvailable Options:")
          for move_num, move_info in moves.items():
              print(White + f"> [{move_num}] {move_info['name']} ({move_info['power']})")
          try:
            yourChoice = int(input(White + "\n>> Enter your choice: "))
            if yourChoice > 6 or yourChoice < 1:
              print2(red + "Invalid choice, autopicked move!" + resetlol)
              yourChoice = random.randint(1, 3)
              time.sleep(1)
          except:
            print2(red + "Invalid choice, autopicked move" + resetlol)
            yourChoice = random.randint(1, 3)
            time.sleep(1)
          clear()
          if settingsAndcodes['ASCII'] == True:
            if settingsAndcodes['GigachadMode'] == False:
              print(ASCIIVARIABLE[1])
            else:
              print(ASCIIVARIABLE[2])
          elif settingsAndcodes['ASCII'] == False:
            pass

          if yourChoice == 5:  
            print2(blue + f"You forfeited the battle, no coins lost...\n{resetlol}") if OpponentName != Pokemon[enemyPokemon_Selected]['name'] else print2(blue + f"You ran away, no coins lost...\n{resetlol}")

            yourHP = 0
            break
            clear()
          if yourChoice == 4:
                clear()
                if settingsAndcodes['ASCII'] == True:
                  if settingsAndcodes['GigachadMode'] == False:
                    print(ASCIIVARIABLE[1])
                  else:
                    print(ASCIIVARIABLE[2])
                elif settingsAndcodes['ASCII'] == False:
                  pass
                print(blue + f"Stat Comparison:\n\n\n{white}Your {REFERENCE_YOUR_POKEMONDATA['name']}: \n\nPower: {REFERENCE_YOUR_POKEMONDATA['power']} \nHP: {REFERENCE_YOUR_POKEMONDATA['max_hp']} \nSpeed: {REFERENCE_YOUR_POKEMONDATA['speed']}\nType: {REFERENCE_YOUR_POKEMONDATA['type']}\nAbility: {REFERENCE_YOUR_POKEMONDATA['ability']}\n" + resetlol)
                print()
                print(blue + f"{white}Foe {Pokemon[enemyPokemon_Selected]['name']}:\n\nPower: {Pokemon[enemyPokemon_Selected]['power']} \nHP: {Pokemon[enemyPokemon_Selected]['max_hp']} \nSpeed: {Pokemon[enemyPokemon_Selected]['speed']}\nType: {Pokemon[enemyPokemon_Selected]['type']}\nAbility: {Pokemon[enemyPokemon_Selected]['ability']}\n\n" + resetlol)
                input('\n[Enter] To Close: \n')
                clear()
                if settingsAndcodes['ASCII'] == True:
                  if settingsAndcodes['GigachadMode'] == False:
                    print(ASCIIVARIABLE[1])
                  else:
                    print(ASCIIVARIABLE[2])
                elif settingsAndcodes['ASCII'] == False:
                  pass
                continue
          if yourChoice == 6:
              if OpponentName == Pokemon[enemyPokemon_Selected]['name']:
                clear()
                if settingsAndcodes['ASCII'] == True:
                  if settingsAndcodes['GigachadMode'] == False:
                    print(ASCIIVARIABLE[1])
                  else:
                    print(ASCIIVARIABLE[2])
                elif settingsAndcodes['ASCII'] == False:
                  pass
                print2(blue + f"Which ball would you like to use? (Price varies by Pokemon) \n\n1. Pokeball ({int((Pokemon[enemyPokemon_Selected]['price'])*0.25)} Coins) - 25%\n2. Greatball ({int((Pokemon[enemyPokemon_Selected]['price'])*0.50)} Coins) - 50%\n3. Ultraball ({int((Pokemon[enemyPokemon_Selected]['price'])*0.75)} Coins) - 75%\n4. Masterball ({(Pokemon[enemyPokemon_Selected]['price'])} Coins) - 100%\n5. Exit\n\n" + resetlol)
                print2(white+f"Coins: {coins}")
                ballchoice = input('Enter Choice: ')
                print()
                if ballchoice == '1':
                  if coins >= int((Pokemon[enemyPokemon_Selected]['price'])*0.25):
                    coins -= int((Pokemon[enemyPokemon_Selected]['price'])*0.25)
                    NEWVARcoinsWILD = coins
                    oddball = random.randint(0,100)
                    if oddball <= 25:
                      print2("You threw a pokeball at the wild Pokemon.")
                      input()
                      print2("...")
                      input()
                      print2("...")
                      input()
                      print2("...")
                      input()
                      print2(f"Gotcha! You caught {Pokemon[enemyPokemon_Selected]['name']}!")
                      if yourPokemonSTORYONLY != False and OpponentName == Pokemon[enemyPokemon_Selected]['name']:
                        storyinventory.append(enemyPokemon_Selected)
                      else:
                        inventory.append(enemyPokemon_Selected)
                      break
                    else:
                      print2("You threw a pokeball at the wild Pokemon.")
                      input()
                      print2("...")
                      input()
                      print2(f"Noooo! It broke free.")
                      input()
                      clear()
                      if settingsAndcodes['ASCII'] == True:
                        if settingsAndcodes['GigachadMode'] == False:
                          print(ASCIIVARIABLE[1])
                        else:
                          print(ASCIIVARIABLE[2])
                      elif settingsAndcodes['ASCII'] == False:
                        pass
                  else:
                    print2(red + "You don't have enough coins to buy this ball." + resetlol)
                    input()
                    clear()
                    if settingsAndcodes['ASCII'] == True:
                      if settingsAndcodes['GigachadMode'] == False:
                        print(ASCIIVARIABLE[1])
                      else:
                        print(ASCIIVARIABLE[2])
                    elif settingsAndcodes['ASCII'] == False:
                      pass
                    continue
                elif ballchoice == '2':
                    if coins >= int((Pokemon[enemyPokemon_Selected]['price'])*0.50):
                      coins -= int((Pokemon[enemyPokemon_Selected]['price'])*0.50)
                      NEWVARcoinsWILD = coins
                      oddball = random.randint(0,100)
                      if oddball <= 50:
                        print2("You threw a greatball at the wild Pokemon.")
                        input()
                        print2("...")
                        input()
                        print2("...")
                        input()
                        print2("...")
                        input()
                        print2(f"Gotcha! You caught {Pokemon[enemyPokemon_Selected]['name']}!")
                        if yourPokemonSTORYONLY != False and OpponentName == Pokemon[enemyPokemon_Selected]['name']:
                          storyinventory.append(enemyPokemon_Selected)
                        else:
                          inventory.append(enemyPokemon_Selected)
                        break
                      else:
                        print2("You threw a greatball at the wild Pokemon.")
                        input()
                        print2("...")
                        input()
                        print2(f"Noooo! It broke free.")
                        input()
                        clear()
                        if settingsAndcodes['ASCII'] == True:
                          if settingsAndcodes['GigachadMode'] == False:
                            print(ASCIIVARIABLE[1])
                          else:
                            print(ASCIIVARIABLE[2])
                        elif settingsAndcodes['ASCII'] == False:
                          pass
                    else:
                      print2(red + "You don't have enough coins to buy this ball." + resetlol)
                      input()
                      clear()
                      if settingsAndcodes['ASCII'] == True:
                        if settingsAndcodes['GigachadMode'] == False:
                          print(ASCIIVARIABLE[1])
                        else:
                          print(ASCIIVARIABLE[2])
                      elif settingsAndcodes['ASCII'] == False:
                        pass
                      continue
                elif ballchoice == '3':
                    if coins >= int((Pokemon[enemyPokemon_Selected]['price'])*0.75):
                      coins -= int((Pokemon[enemyPokemon_Selected]['price'])*0.75)
                      NEWVARcoinsWILD = coins
                      oddball = random.randint(0,100)
                      if oddball <= 75:
                        print2("You threw an ultraball at the wild Pokemon.")
                        input()
                        print2("...")
                        input()
                        print2("...")
                        input()
                        print2("...")
                        input()
                        print2(f"Gotcha! You caught {Pokemon[enemyPokemon_Selected]['name']}!")
                        if yourPokemonSTORYONLY != False and OpponentName == Pokemon[enemyPokemon_Selected]['name']:
                          storyinventory.append(enemyPokemon_Selected)
                        else:
                          inventory.append(enemyPokemon_Selected)
                        break
                      else:
                        print2("You threw an ultraball at the wild Pokemon.")
                        input()
                        print2("...")
                        input()
                        print2(f"Noooo! It broke free.")
                        input()
                        clear()
                        if settingsAndcodes['ASCII'] == True:
                          if settingsAndcodes['GigachadMode'] == False:
                            print(ASCIIVARIABLE[1])
                          else:
                            print(ASCIIVARIABLE[2])
                        elif settingsAndcodes['ASCII'] == False:
                          pass
                    else:
                      print2(red + "You don't have enough coins to buy this ball." + resetlol)
                      input()
                      clear()
                      if settingsAndcodes['ASCII'] == True:
                        if settingsAndcodes['GigachadMode'] == False:
                          print(ASCIIVARIABLE[1])
                        else:
                          print(ASCIIVARIABLE[2])
                      elif settingsAndcodes['ASCII'] == False:
                        pass
                      continue
                elif ballchoice == '4':
                    if coins >= int((Pokemon[enemyPokemon_Selected]['price'])):
                        coins -= int((Pokemon[enemyPokemon_Selected]['price']))
                        NEWVARcoinsWILD = coins
                        print2("You threw an masterball at the wild Pokemon.")
                        input()
                        print2("...")
                        input()
                        print2("...")
                        input()
                        print2("...")
                        input()
                        print2(f"Gotcha! You caught {Pokemon[enemyPokemon_Selected]['name']}!")
                        if yourPokemonSTORYONLY != False and OpponentName == Pokemon[enemyPokemon_Selected]['name']:
                          storyinventory.append(enemyPokemon_Selected)
                        else:
                          inventory.append(enemyPokemon_Selected)
                        break
                    else:
                      print2(red + "You don't have enough coins to buy this ball." + resetlol)
                      input()
                      clear()
                      if settingsAndcodes['ASCII'] == True:
                        if settingsAndcodes['GigachadMode'] == False:
                          print(ASCIIVARIABLE[1])
                        else:
                          print(ASCIIVARIABLE[2])
                      elif settingsAndcodes['ASCII'] == False:
                        pass
                      continue

                else:
                  clear()
                  if settingsAndcodes['ASCII'] == True:
                    if settingsAndcodes['GigachadMode'] == False:
                      print(ASCIIVARIABLE[1])
                    else:
                      print(ASCIIVARIABLE[2])
                  elif settingsAndcodes['ASCII'] == False:
                    pass
                  continue

              else:   
                print2(red + "Invalid choice, autopicked move!" + resetlol)
                yourChoice = random.randint(1, 3)
                time.sleep(1)

          totalturns += 1
          print(f"{white}Turn {totalturns}:{resetlol}\n")

           # Determine who goes first based on speed

          if yourSpeed > enemySpeed:
              yourTurn = True
              enemyTurn = False
              print(Blue + f">> {yourPokemon_NAME}" + Blue+ f" is faster! ({yourSpeed}) > ({enemySpeed})\n")
          elif yourSpeed < enemySpeed:
              yourTurn = False
              enemyTurn = True
              print(Blue + f">> Foe {enemyPokemon_NAME}" + Blue+ f" is faster! ({enemySpeed}) > ({yourSpeed})\n")
          else:
              # If speeds are equal, randomly determine who goes first
              randomTurnNumber = random.randint(1,2)
              if randomTurnNumber == 1:
                  yourTurn = True
                  enemyTurn = False
              else:
                  yourTurn = False
                  enemyTurn = True         
              print(Blue + f">> Same speed! Faster Pokemon is randomly choosen!\n")

          if enemyTurn == True and yourTurn == False: # ENEMY IS FASTER
              # Opponent's turn --------------------------------------------------------------------------------------------------------
              if yourPokemon['ability'] == 'Truant (Pokemon is too lazy, disobeys every third turn.)' and (slakingYOUTURN == 0):
                yourChoice = 83250987
              if enemyPokemon['ability'] == 'Truant (Pokemon is too lazy, disobeys every third turn.)' and (slakingENEMYTURN == 0):
                enemyChoice = 83250987

              if enemyPokemon['ability'] != 'Truant (Pokemon is too lazy, disobeys every third turn.)' or (slakingENEMYTURN == 1 or slakingENEMYTURN == 2):

                if slakingENEMYTURN == 1:
                  slakingENEMYTURN = 2  
                else:
                  slakingENEMYTURN = 0

                if enemyProtectTurnTotal == 2:
                  enemyChoice = random.choice([1, 2, 3])  # 1 for Attack, 2 for Recover
                elif enemyHP <= enemyPokemon['max_hp']/2:
                  enemyChoice = random.choice([1, 2, 2])
                else:
                  enemyChoice = random.choice([1, 1, 2])  # 1 for Attack, 2 for Recover


                if yourChoice == 3:
                  if yourProtectTurnTotal == 2 and enemyPokemon['ability'] != 'Hyperspace Hole (Ignores protect.)':
                    yourProtectTurnTotal = 11
                    if enemyChoice == 1:
                      enemyChoice = 235325
                      print2(Green + "You protected yourself this turn.\n")
                      if yourPokemon['ability'] == 'Regenerator (Recovers 25% HP when protect is used.)':
                        yourHP += int((yourPokemon['max_hp']/4))
                        if yourHP > yourPokemon['max_hp']:
                          yourHP = yourPokemon['max_hp']

                        print2(Blue + f">> The gods regenerated HP for {yourPokemon_NAME}.\n")
                    elif enemyChoice == 2 or enemyChoice ==3:
                      print2(Green + "You protected yourself this turn.\n")
                      if yourPokemon['ability'] == 'Regenerator (Recovers 25% HP when protect is used.)':
                        yourHP += int((yourPokemon['max_hp']/4))
                        if yourHP > yourPokemon['max_hp']:
                          yourHP = yourPokemon['max_hp']

                        print2(Blue + f">> The gods regenerated HP for {yourPokemon_NAME}.\n")
                  else:
                    yourChoice == 53532
                    if enemyPokemon['ability'] != 'Hyperspace Hole (Ignores protect.)':
                      print2(Red + "You tried to use protect, but it failed!\n")
                    else:
                      print2(Blue + ">> You tried to use protect, but the black holes prevented it!\n" + resetlol) 
                    yourProtectTurnTotal = 2
                elif yourChoice != 3:
                    yourProtectTurnTotal = 2

                if enemyChoice == 2 or enemyChoice == 4:
                    if enemyHP >= enemyPokemon["max_hp"] / 1.25 and yourChoice != 3:
                        enemyChoice = 1
                    else:
                        if yourPokemon['ability'] == 'Pikachu Clause (60% chance enemy turn is skipped due to paralysis)':
                          attackmisser = random.randint(0,100)
                        else:
                          attackmisser = 100
                        if attackmisser >= 60:
                            randomHPGain = random.randint(int(enemyPokemon["max_hp"]/3), int(enemyPokemon["max_hp"]/2)) 
                            if enemyPokemon['ability'] == 'Recoverer (Will always recover to max HP)' or enemyPokemon['ability'] == 'Ultra Amplifier (Recoverer + Unleashed Combined)':                          
                              randomHPGain = enemyPokemon["max_hp"]
                            if yourPokemon['ability'] == 'Evil Mist (Steals 20% of HP Enemy Recovers)':
                              randomHPGain = randomHPGain * 0.8 
                              yourHP += randomHPGain * 0.2
                              if yourHP > yourPokemon["max_hp"]:
                                yourHP = yourPokemon["max_hp"]
                              print(Blue + f">> Recover HP was stolen due to evil mist!")
                            enemyHP += int(randomHPGain)
                            if enemyHP > enemyPokemon["max_hp"]:
                              enemyHP = enemyPokemon["max_hp"]
                            print2(Red + f"Foe {enemyPokemon_NAME}" + Red + f" used Recover and healed {randomHPGain} HP!\n")

                        else:
                          print2(Blue + f">> Enemy Turn skipped due to {yourPokemon_NAME}" + blue + "'s ability!\n")

                if enemyChoice == 1:

                  if yourPokemon['ability'] == 'Disguise (Nullifies the first enemy attack.)' or yourPokemon['ability'] == 'Dark Hypnosis (Enemy is asleep on the first attack. After this ability is used, it becomes Devil Aura.)' or yourPokemon['ability'] == 'Ninja Substitution (Nullifies the first enemy attack.)':
                    if yourPokemon['ability'] == 'Disguise (Nullifies the first enemy attack.)' or yourPokemon['ability'] == 'Ninja Substitution (Nullifies the first enemy attack.)':
                      print2(red + f">> {enemyPokemon_NAME}{Green} tried an attack on {yourPokemon_NAME}.\n")
                      print2(Blue + f">> {yourPokemon_NAME}{Blue}'s disguise served as a decoy and it was busted!\n")
                      yourPokemon['ability'] = None

                    elif yourPokemon['ability'] == 'Dark Hypnosis (Enemy is asleep on the first attack. After this ability is used, it becomes Devil Aura.)':

                        print2(Blue + f">> {enemyPokemon_NAME}{Blue} is asleep this turn!\n")
                        yourPokemon['ability'] = 'Devil Aura (Steals 10% of enemy HP for self each turn + Nullifies Enemy Ability)'
                  else:

                    if yourPokemon['ability'] == 'Pikachu Clause (60% chance enemy turn is skipped due to paralysis)':
                        attackmisser = random.randint(0,100)
                    else:
                        attackmisser = 100

                    if attackmisser >= 60:
                      enemy_damage = int(random.randint(int(enemyPokemon["power"]/2),int(enemyPokemon["power"])) * type_damage_multiplier(enemyPokemon['type'], yourPokemon['type'])) if enemyPokemon['ability'] != 'Unleashed (Does the max damage possible.)' or enemyPokemon['ability'] != 'Ultra Amplifier (Recoverer + Unleashed Combined)' else (int(enemyPokemon["power"]) * type_damage_multiplier(enemyPokemon["type"], yourPokemon["type"]))
                      if yourPokemon['ability'] == 'Tidal Shield (When HP is full, halves enemy damage.)' and yourHP == yourPokemon['max_hp']:
                        enemy_damage = enemy_damage/2
                        print2(Blue + f">> The tidal shield blocked some of the incoming attack for {yourPokemon_NAME}.\n")
                      yourHP -= enemy_damage
                      print2(Red + f"Foe {enemyPokemon_NAME}" + Red + f" dealt {enemy_damage} damage to your {yourPokemon_NAME}!\n")

                      if type_damage_multiplier(enemyPokemon['type'], yourPokemon['type']) < 1.0:
                          print2(Red + f">> It is not very effective!\n")
                      elif type_damage_multiplier(enemyPokemon['type'], yourPokemon['type']) > 1.0:
                          print2(Red + f">> It is super effective!\n")
                      if yourHP <= 0:
                          print("\n" + White + f">> Foe {enemyPokemon_NAME}" + White + f" defeated your {yourPokemon_NAME}." + White + f" You lost the battle to {OpponentName}. You lost 5 coins!\n")
                          if yourPokemon['ability'] == "Magikarp Clause (You lose nothing after a defeat, instead get 20 coins.)":
                            print2(Blue + ">> Your Magikarp sacrified some of its soul to cover up your losses and instead you recieved 20 coins and lost nothing!")
                            coins += 20
                            if coins < 0:
                              coins = 0


                            break
                          else:

                            coins -= 5
                            if coins < 0:
                              coins = 0


                            break
                          if yourPokemon['ability'] == 'Brokie Magikarp Clause (You lose nothing after a defeat, instead get 10 coins.)':
                            print2(Blue + ">> Your Magikarp sacrified some of its soul to cover up your losses and instead you recieved 10 coins and lost nothing!")
                            coins += 10
                            if coins < 0:
                              coins = 0


                            break
                          else:

                            coins -= 5
                            if coins < 0:
                              coins = 0


                            break
                    else:
                        print2(Blue + f">> Enemy Turn skipped due to {yourPokemon_NAME}" + blue + "'s ability!\n")
                    if enemyPokemon['ability'] == 'Type Wheel (Pokemon type randomly changes each turn)':
                      enemyPokemon['type'] = random.choice(list(type_effectiveness.keys()))

                      print2(Blue + f">> Foe {enemyPokemon_NAME}'s" + Blue +" type has been decided by the gods!\n")
                    if enemyPokemon['ability'] == 'Heal Aura (Pokemon heals 20% of max HP every turn)':

                      print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" gained some HP due to its ability!\n")
                      enemyHP = enemyHP + int(enemyPokemon["max_hp"] * 0.2)
                      if enemyHP > enemyPokemon["max_hp"]:
                        enemyHP = enemyPokemon["max_hp"]

                    if enemyPokemon['ability'] == 'Confusifier (30% chance enemy loses 1/3 of HP)':
                      luck = random.randint(0,100)
                      if luck <= 30:
                        yourHP = yourHP - int(yourPokemon["max_hp"] * 1/3)
                        print2(Blue + f">> Your Pokemon hurt itself in confusion.\n")
                        if yourHP <= 0:
                          print("\n" + White + f">> Foe {enemyPokemon_NAME}" + White + f" defeated your {yourPokemon_NAME}." + White + f" You lost the battle to {OpponentName}. You lost 5 coins!\n")
                          if yourPokemon['ability'] == "Magikarp Clause (You lose nothing after a defeat, instead get 20 coins.)":
                              print2(Blue + ">> Your Magikarp sacrified some of its soul to cover up your losses and instead you recieved 20 coins and lost nothing!")
                              coins += 20
                              if coins < 0:
                                coins = 0

                          else:

                              coins -= 5
                              if coins < 0:
                                coins = 0


                          if yourPokemon['ability'] == 'Brokie Magikarp Clause (You lose nothing after a defeat, instead get 10 coins.)':
                            print2(Blue + ">> Your Magikarp sacrified some of its soul to cover up your losses and instead you recieved 10 coins and lost nothing!")
                            coins += 10
                            if coins < 0:
                              coins = 0


                          else:

                            coins -= 5
                            if coins < 0:
                              coins = 0



                          break
                      else:
                        pass


                    if enemyPokemon['ability'] == 'Lethal Toxic (Each turn, enemy stats and HP are decreased by 10%)' or enemyPokemon['ability'] == '9,000,000 Celcius Burn (Each turn, enemy stats and HP are decreased by 10%)':

                      yourPokemon['power'] = yourPokemon['power'] - int(yourPokemon['power'] * 0.1)
                      yourHP = yourHP - int(yourPokemon["max_hp"] * 0.1)
                      yourSpeed = yourSpeed - int(yourPokemon["speed"] * 0.1)
                      print2(Blue + f">> Your Pokemon is slowly dying of foe Pokemon's lethal poison!\n") if enemyPokemon['ability'] == 'Lethal Toxic (Each turn, enemy stats and HP are decreased by 10%)' else print2(Blue + f">> Your Pokemon is slowly getting cooked of foe Pokemon's lethal burn!\n")

                      if yourHP <= 0:
                        print("\n" + White + f">> Foe {enemyPokemon_NAME}" + White + f" killed your Pokemon via Poison, wait as the developer I ain't trynna get sued by this player for losing his Pokemon he grinded so much for, here bro I resurrected your Pokemon with the help of the gods." + White + f" But you still lost the battle to {OpponentName}. You lost 5 coins!\n") if enemyPokemon['ability'] == 'Lethal Toxic (Each turn, enemy stats and HP are decreased by 10%)' else print("\n" + White + f">> Foe {enemyPokemon_NAME}" + White + f" killed your Pokemon through burn and cooked your pokemon and ate it, wait as the developer I ain't trynna get sued by this player for losing his Pokemon he grinded so much for, here bro I resurrected your Pokemon with the help of the gods." + White + f" But you still lost the battle to {OpponentName}. You lost 5 coins!\n") 
                        if yourPokemon['ability'] == "Magikarp Clause (You lose nothing after a defeat, instead get 20 coins.)":
                          print2(Blue + ">> Your Magikarp sacrified some of its soul to cover up your losses and instead you recieved 20 coins and lost nothing!")
                          coins += 20
                          if coins < 0:
                            coins = 0


                          break
                        else:

                          coins -= 5
                          if coins < 0:
                            coins = 0


                          break
                        if yourPokemon['ability'] == 'Brokie Magikarp Clause (You lose nothing after a defeat, instead get 10 coins.)':
                          print2(Blue + ">> Your Magikarp sacrified some of its soul to cover up your losses and instead you recieved 10 coins and lost nothing!")
                          coins += 10
                          if coins < 0:
                            coins = 0


                          break
                        else:

                          coins -= 5
                          if coins < 0:
                            coins = 0


                          break
                      if enemyHP > enemyPokemon["max_hp"]:
                        enemyHP = enemyPokemon["max_hp"]

                    if enemyPokemon['ability'] == 'Leech Seed (Steals 20% of enemy HP for self.)' or enemyPokemon['ability'] == 'Devil Aura (Steals 10% of enemy HP for self each turn + Nullifies Enemy Ability)' or enemyPokemon['ability'] == 'Rocky Helmet (Enemy loses 20% HP per turn)':

                      if enemyPokemon['ability'] == 'Devil Aura (Steals 10% of enemy HP for self each turn + Nullifies Enemy Ability)':
                        print2(Blue+">> The Devil's Aura is suppressing its victims ability in the battlefield!\n")
                        yourPokemon['ability'] = None
                        if yourPokemon['type'] == 'Wonder-Gaurd':
                          print2(Blue + f">> Your Wonder Guard is destroyed!\n")
                          yourPokemon['type'] == 'Bug'
                        enemyHP = enemyHP + int(yourPokemon["max_hp"] * 0.1)
                        yourHP = yourHP - int(yourPokemon["max_hp"] * 0.1)
                      else:
                        if enemyPokemon['ability'] != 'Rocky Helmet (Enemy loses 20% HP per turn)':
                          enemyHP = enemyHP + int(yourPokemon["max_hp"] * 0.2)
                        yourHP = yourHP - int(yourPokemon["max_hp"] * 0.2)

                      if yourHP <= 0:
                        print("\n" + White + f">> Foe {enemyPokemon_NAME}" + White + f" defeated your {yourPokemon_NAME}." + White + f" You lost the battle to {OpponentName}. You lost 5 coins!\n")
                        if yourPokemon['ability'] == "Magikarp Clause (You lose nothing after a defeat, instead get 20 coins.)":
                          print2(Blue + ">> Your Magikarp sacrified some of its soul to cover up your losses and instead you recieved 20 coins and lost nothing!")
                          coins += 20
                          if coins < 0:
                            coins = 0


                          break
                        else:

                          coins -= 5
                          if coins < 0:
                            coins = 0


                          break
                        if yourPokemon['ability'] == 'Brokie Magikarp Clause (You lose nothing after a defeat, instead get 10 coins.)':
                          print2(Blue + ">> Your Magikarp sacrified some of its soul to cover up your losses and instead you recieved 10 coins and lost nothing!")
                          coins += 10
                          if coins < 0:
                            coins = 0


                          break
                        else:

                          coins -= 5
                          if coins < 0:
                            coins = 0


                          break
                      if enemyHP > enemyPokemon["max_hp"]:
                          enemyHP = enemyPokemon["max_hp"]
                      print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" stole your Pokemon's HP due to its ability!\n") if enemyPokemon['ability'] != 'Rocky Helmet (Enemy loses 20% HP per turn)' else print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" hurted your Pokemon due to its rocky helmet!\n")
              else:
                  slakingENEMYTURN = 1
                  print2(Blue + f">> {enemyPokemon_NAME}" + Blue +" is loafing around!\n")


               # Your turn --------------------------------------------------------------------------------------------------------

              if yourPokemon['ability'] != 'Truant (Pokemon is too lazy, disobeys every third turn.)' or (slakingYOUTURN == 1 or slakingYOUTURN == 2):
                if slakingYOUTURN == 1:
                  slakingYOUTURN = 2  
                elif slakingYOUTURN == 2:
                  slakingYOUTURN = 0
                try:
                  if enemyChoice == 3:
                    if enemyProtectTurnTotal == 2 and yourPokemon['ability'] != 'Hyperspace Hole (Ignores protect.)':
                      enemyProtectTurnTotal = 11
                      if yourChoice == 1:
                        yourChoice = 444
                        print2(Red + "Enemy protected itself this turn.\n")
                        if enemyPokemon['ability'] == 'Regenerator (Recovers 25% HP when protect is used.)':
                          enemyHP += int((enemyPokemon['max_hp']/4))
                          if enemyHP > yourPokemon['max_hp']:
                            enemyHP = yourPokemon['max_hp']

                          print2(Blue + f">> The gods regenerated HP for {enemyPokemon_NAME}.\n")
                      elif yourChoice == 2 or yourChoice == 3:
                        print2(Red + "Enemy protected itself this turn.\n")
                        if enemyPokemon['ability'] == 'Regenerator (Recovers 25% HP when protect is used.)':
                          enemyHP += int((enemyPokemon['max_hp']/4))
                          if enemyHP > yourPokemon['max_hp']:
                            enemyHP = yourPokemon['max_hp']
                          print2(Blue + f">> The gods regenerated HP for {enemyPokemon_NAME}.\n")
                    else:
                      if yourPokemon['ability'] != 'Hyperspace Hole (Ignores protect.)':
                        print2(Green + "Enemy failed to protect itself.\n")
                      else:
                        print2(Blue + ">> The black holes prevented the enemy from using protect!\n")
                      enemyProtectTurnTotal = 2

                  elif enemyChoice != 3:
                      enemyProtectTurnTotal = 2

                  if yourChoice == 1:


                    if enemyPokemon['ability'] == 'Disguise (Nullifies the first enemy attack.)' or enemyPokemon['ability'] ==  'Dark Hypnosis (Enemy is asleep on the first attack. After this ability is used, it becomes Devil Aura.)':
                      if enemyPokemon['ability'] == 'Disguise (Nullifies the first enemy attack.)':
                        print2(Green + f">> {yourPokemon_NAME}{Green} tried an attack on {enemyPokemon_NAME}.\n")
                        print2(Blue + f">> {enemyPokemon_NAME}{Blue}'s disguise served as a decoy and it was busted!\n")
                        enemyPokemon['ability'] = None

                      elif enemyPokemon['ability'] == 'Dark Hypnosis (Enemy is asleep on the first attack. After this ability is used, it becomes Devil Aura.)':

                          print2(Blue + f">> {yourPokemon_NAME}{Blue} is asleep this turn!\n")
                          enemyPokemon['ability'] = 'Devil Aura (Steals 10% of enemy HP for self each turn + Nullifies Enemy Ability)'




                    else:

                        if enemyPokemon['ability'] == 'Pikachu Clause (60% chance enemy turn is skipped due to paralysis)':
                          attackmisser = random.randint(0,100)
                        else:
                          attackmisser = 100    

                        if attackmisser > 60:
                          your_damage = int(random.randint(int(yourPokemon["power"]/2),int(yourPokemon["power"])) * type_damage_multiplier(yourPokemon["type"], enemyPokemon["type"])) if yourPokemon['ability'] != 'Unleashed (Does the max damage possible.)' or yourPokemon['ability'] != 'Ultra Amplifier (Recoverer + Unleashed Combined)' else (int(yourPokemon["power"]) * type_damage_multiplier(yourPokemon["type"], enemyPokemon["type"]))
                          if enemyPokemon['ability'] == 'Tidal Shield (When HP is full, halves enemy damage.)' and enemyHP == enemyPokemon['max_hp']:
                            your_damage = your_damage/2
                            print2(Blue + f">> The tidal shield blocked some of the incoming attack for {enemyPokemon_NAME}.\n")
                          enemyHP -= your_damage
                          print2(Green + f"{yourPokemon_NAME}" + Green + f" dealt {your_damage} damage to foe {enemyPokemon_NAME}!\n")



                          if type_damage_multiplier(yourPokemon["type"], enemyPokemon["type"]) < 1.0:
                              print2(Green + f">> It is not very effective!\n")
                          elif type_damage_multiplier(yourPokemon["type"], enemyPokemon["type"]) > 1.0:
                              print2(Green + f">> It is super effective!\n")

                          if enemyHP <= 0:
                              if odds < 60:
                                newvar = random.randint(30,60)
                                coins += newvar
                              else:
                                newvar = random.randint(80, 160)
                                coins += newvar

                              print("\n" + White + f">> Your {yourPokemon_NAME}" + White + f" defeated foe {enemyPokemon_NAME}." + White + f" You defeated {OpponentName} and earned {newvar} coins!\n")


                              break
                        else:
                            print2(Blue + f">> Your Turn skipped due to foe {enemyPokemon_NAME}" + blue + "'s ability!\n")
                  elif yourChoice == 2:
                      if enemyPokemon['ability'] == 'Pikachu Clause (60% chance enemy turn is skipped due to paralysis)':
                            attackmisser = random.randint(0,100)
                      else:
                            attackmisser = 100    
                      if attackmisser > 60:
                          randomHPGain = random.randint(int(yourPokemon["max_hp"]/3), int(yourPokemon["max_hp"]/2)) 
                          if  yourPokemon['ability'] == 'Recoverer (Will always recover to max HP)' or yourPokemon['ability'] == 'Ultra Amplifier (Recoverer + Unleashed Combined)':                          
                            randomHPGain = yourPokemon["max_hp"]
                          if enemyPokemon['ability'] == 'Evil Mist (Steals 20% of HP Enemy Recovers)':
                            randomHPGain = randomHPGain * 0.8 
                            enemyHP += randomHPGain * 0.2
                            if enemyHP > enemyPokemon["max_hp"]:
                              enemyHP = enemyPokemon["max_hp"]
                            print(Blue + f">> Recover HP was stolen due to evil mist!")
                          yourHP += int(randomHPGain)
                          if yourHP > yourPokemon["max_hp"]:
                              yourHP = yourPokemon["max_hp"]

                          print2(Green + f"{yourPokemon_NAME}" + Green + f" used Recover and healed {randomHPGain} HP!\n")


                      else:
                            print2(Blue + f">> Your Turn skipped due to {enemyPokemon_NAME}" + blue + "'s ability!\n")
                except:
                    print2(Red + "Your turn skipped!\n" + resetlol)
                if yourPokemon['ability'] == 'Type Wheel (Pokemon type randomly changes each turn)':
                  yourPokemon['type'] = random.choice(list(type_effectiveness.keys()))

                  print2(Blue + f">> {yourPokemon_NAME}'s" + Blue +" type has been decided by the gods!\n")
                if yourPokemon['ability'] == 'Heal Aura (Pokemon heals 20% of max HP every turn)':
                  yourHP = yourHP + int(yourPokemon["max_hp"] * 0.2)
                  if yourHP > yourPokemon["max_hp"]:
                      yourHP = yourPokemon["max_hp"]
                  print2(Blue + f">> {yourPokemon_NAME}" + Blue +" gained some HP due to its ability!\n")



                if yourPokemon['ability'] == 'Confusifier (30% chance enemy loses 1/3 of HP)':
                  luck = random.randint(0,100)
                  if luck <= 30:
                    enemyHP = enemyHP - int(enemyPokemon["max_hp"] * 1/3)
                    print2(Blue + f">> Foe Pokemon hurt itself in confusion.\n")
                    if enemyHP <= 0:
                      if odds < 60:
                        newvar = random.randint(30,60)
                        coins += newvar
                      else:
                        newvar = random.randint(80, 160)
                        coins += newvar

                      print("\n" + White + f">> Your {yourPokemon_NAME}" + White + f" defeated foe {enemyPokemon_NAME}." + White + f" You defeated {OpponentName} and earned {newvar} coins!\n")


                      break
                  else:
                    pass




                if yourPokemon['ability'] == 'Lethal Toxic (Each turn, enemy stats and HP are decreased by 10%)' or yourPokemon['ability'] == '9,000,000 Celcius Burn (Each turn, enemy stats and HP are decreased by 10%)':
                  enemyPokemon['power'] = enemyPokemon['power'] - int(enemyPokemon['power'] * 0.1)
                  enemyHP = enemyHP - int(enemyPokemon["max_hp"] * 0.1)
                  enemySpeed = enemySpeed - int(enemyPokemon["speed"] * 0.1)
                  print2(Blue + f">> Foe Pokemon is slowly dying of your Pokemon's lethal poison!\n") if yourPokemon['ability'] == 'Lethal Toxic (Each turn, enemy stats and HP are decreased by 10%)' else print2(Blue + f">> Foe Pokemon is slowly getting cooked of your Pokemon's lethal burn!\n")
                  if enemyHP <= 0:
                    if odds < 60:
                      newvar = random.randint(30,60)
                      coins += newvar
                    else:
                      newvar = random.randint(80, 160)
                      coins += newvar

                    print("\n" + White + f">> Foe {enemyPokemon_NAME} died of lethal poison, wait I thought this was a kids game???" + White + f" Well anyways, pretend that didn't happen. You defeated {OpponentName} and earned {newvar} coins!\n") if yourPokemon['ability'] == 'Lethal Toxic (Each turn, enemy stats and HP are decreased by 10%)' else  print("\n" + White + f">> Foe {enemyPokemon_NAME} died of lethal burn, and ur pokemon ate it since it is now cooked, wait I thought this was a kids game???" + White + f" Well anyways, pretend that didn't happen. You defeated {OpponentName} and earned {newvar} coins!\n")


                    break
                  if yourHP > yourPokemon["max_hp"]:
                      yourHP = yourPokemon["max_hp"]
                if yourPokemon['ability'] == 'Leech Seed (Steals 20% of enemy HP for self.)' or yourPokemon['ability'] == 'Devil Aura (Steals 10% of enemy HP for self each turn + Nullifies Enemy Ability)' or yourPokemon['ability'] == 'Rocky Helmet (Enemy loses 20% HP per turn)':

                  if yourPokemon['ability'] == 'Devil Aura (Steals 10% of enemy HP for self each turn + Nullifies Enemy Ability)':
                    print2(Blue+">> The Devil's Aura is suppressing its victims ability in the battlefield!\n")
                    enemyPokemon['ability'] = None
                    if enemyPokemon['type'] == 'Wonder-Gaurd':
                      print2(Blue + f">> Foe Wonder Guard is destroyed!\n")
                      enemyPokemon['type'] == 'Bug'
                    if yourPokemon['ability'] != 'Rocky Helmet (Enemy loses 20% HP per turn)':
                      yourHP = yourHP + int(enemyPokemon["max_hp"] * 0.2)
                    enemyHP = enemyHP - int(enemyPokemon["max_hp"] * 0.2)
                  else:
                    if yourPokemon['ability'] != 'Rocky Helmet (Enemy loses 20% HP per turn)':
                      yourHP = yourHP + int(enemyPokemon["max_hp"] * 0.2)
                    enemyHP = enemyHP - int(enemyPokemon["max_hp"] * 0.2)

                  if enemyHP <= 0:
                    if odds < 60:
                      newvar = random.randint(30,60)
                      coins += newvar
                    else:
                      newvar = random.randint(80, 160)
                      coins += newvar
                    print("\n" + White + f">> Your {yourPokemon_NAME}" + White + f" defeated foe {enemyPokemon_NAME}." + White + f" You defeated {OpponentName} and earned {newvar} coins!\n")


                    break
                  if yourHP > yourPokemon["max_hp"]:
                      yourHP = yourPokemon["max_hp"]
                  print2(Blue + f">> {yourPokemon_NAME}" + Blue +" stole enemy HP due to its ability!\n") if yourPokemon['ability'] != 'Rocky Helmet (Enemy loses 20% HP per turn)' else print2(Blue + f">> {yourPokemon_NAME}" + Blue +" hurted foe Pokemon due to its rocky helmet!\n")

              else:
                slakingYOUTURN = 1
                print2(Blue + f">> {yourPokemon_NAME}" + Blue +" is loafing around!\n")

          if enemyTurn == False and yourTurn == True: #YOU ARE FASTER (Below)
              # Your turn --------------------------------------------------------------------------------------------------------
              if enemyProtectTurnTotal == 2:
                enemyChoice = random.choice([1, 2, 3])  # 1 for Attack, 2 for Recover
              elif enemyHP <= enemyPokemon['max_hp']/2:
                enemyChoice = random.choice([1, 2, 2])
              else:
                enemyChoice = random.choice([1, 1, 2])  # 1 for Attack, 2 for Recover



              if yourPokemon['ability'] == 'Truant (Pokemon is too lazy, disobeys every third turn.)' and (slakingYOUTURN == 0):
                yourChoice = 83250987
              if enemyPokemon['ability'] == 'Truant (Pokemon is too lazy, disobeys every third turn.)' and (slakingENEMYTURN == 0):
                enemyChoice = 83250987

              if yourPokemon['ability'] != 'Truant (Pokemon is too lazy, disobeys every third turn.)' or (slakingYOUTURN == 1 or slakingYOUTURN == 2):

                if slakingYOUTURN == 1:
                  slakingYOUTURN = 2  
                else:
                  slakingYOUTURN = 0

                try:
                    if enemyChoice == 3:
                          if enemyProtectTurnTotal == 2 and yourPokemon['ability'] != 'Hyperspace Hole (Ignores protect.)':
                            enemyProtectTurnTotal = 11
                            if yourChoice == 1:
                              yourChoice = 444
                              print2(Red + "Enemy protected itself this turn.\n")
                              if enemyPokemon['ability'] == 'Regenerator (Recovers 25% HP when protect is used.)':
                                enemyHP += int((enemyPokemon['max_hp']/4))
                                if enemyHP > yourPokemon['max_hp']:
                                  enemyHP = yourPokemon['max_hp']
                                print2(Blue + f">> The gods regenerated HP for {enemyPokemon_NAME}.\n")
                            elif yourChoice == 2 or yourChoice == 3:
                              print2(Red + "Enemy protected itself this turn.\n")
                              if enemyPokemon['ability'] == 'Regenerator (Recovers 25% HP when protect is used.)':
                                enemyHP += int((enemyPokemon['max_hp']/4))
                                if enemyHP > yourPokemon['max_hp']:
                                  enemyHP = yourPokemon['max_hp']
                                print2(Blue + f">> The gods regenerated HP for {enemyPokemon_NAME}.\n")
                          else:
                            if yourPokemon['ability'] != 'Hyperspace Hole (Ignores protect.)':
                              print2(Green + "Enemy failed to protect itself.\n")
                            else:
                              print2(Blue + ">> The black holes prevented the enemy from using protect!\n")

                            enemyProtectTurnTotal = 2

                    elif enemyChoice != 3:
                            enemyProtectTurnTotal = 2
                    if yourChoice == 1:

                      if enemyPokemon['ability'] == 'Disguise (Nullifies the first enemy attack.)' or enemyPokemon['ability'] == 'Dark Hypnosis (Enemy is asleep on the first attack. After this ability is used, it becomes Devil Aura.)':
                        if enemyPokemon['ability'] == 'Disguise (Nullifies the first enemy attack.)':
                          print2(Green + f">> {yourPokemon_NAME}{Green} tried an attack on {enemyPokemon_NAME}.\n")
                          print2(Blue + f">> {enemyPokemon_NAME}{Blue}'s disguise served as a decoy and it was busted!\n")
                          enemyPokemon['ability'] = None

                        elif enemyPokemon['ability'] == 'Dark Hypnosis (Enemy is asleep on the first attack. After this ability is used, it becomes Devil Aura.)':

                            print2(Blue + f">> {yourPokemon_NAME}{Blue} is asleep this turn!\n")
                            enemyPokemon['ability'] = 'Devil Aura (Steals 10% of enemy HP for self each turn + Nullifies Enemy Ability)'


                      else:

                        if enemyPokemon['ability'] == 'Pikachu Clause (60% chance enemy turn is skipped due to paralysis)':
                          attackmisser = random.randint(0,100)
                        else:
                          attackmisser = 100     

                        if attackmisser > 60:
                          your_damage = int(random.randint(int(yourPokemon["power"]/2),int(yourPokemon["power"])) * type_damage_multiplier(yourPokemon["type"], enemyPokemon["type"])) if yourPokemon['ability'] != 'Unleashed (Does the max damage possible.)' or yourPokemon['ability'] != 'Ultra Amplifier (Recoverer + Unleashed Combined)' else (int(yourPokemon["power"]) * type_damage_multiplier(yourPokemon["type"], enemyPokemon["type"]))
                          if enemyPokemon['ability'] == 'Tidal Shield (When HP is full, halves enemy damage.)' and enemyHP == enemyPokemon['max_hp']:
                            your_damage = your_damage/2
                            print2(Blue + f">> The tidal shield blocked some of the incoming attack for {enemyPokemon_NAME}.\n")
                          enemyHP -= your_damage
                          print2(Green + f"{yourPokemon_NAME}" + Green + f" dealt {your_damage} damage to foe {enemyPokemon_NAME}!\n")


                          if type_damage_multiplier(yourPokemon["type"], enemyPokemon["type"]) < 1.0:
                              print2(Green + f">> It is not very effective!\n")
                          elif type_damage_multiplier(yourPokemon["type"], enemyPokemon["type"]) > 1.0:
                              print2(Green + f">> It is super effective!\n")

                          if enemyHP <= 0:
                            if odds < 60:
                              newvar = random.randint(30,60)
                              coins += newvar
                              print("\n" + White + f">> Your {yourPokemon_NAME}" + White + f" defeated foe {enemyPokemon_NAME}." + White + f" You defeated {OpponentName} and earned {newvar} coins!\n")


                              break
                            else:
                              newvar = random.randint(80, 160)
                              coins += newvar
                              print("\n" + White + f">> Your {yourPokemon_NAME}" + White + f" defeated foe {enemyPokemon_NAME}." + White + f" You defeated {OpponentName} and earned {newvar} coins!\n")


                              break


                        else:
                            print2(Blue + f">> Your Turn skipped due to foe {enemyPokemon_NAME}" + blue + "'s ability!\n")
                    elif yourChoice == 2:
                      if enemyPokemon['ability'] == 'Pikachu Clause (60% chance enemy turn is skipped due to paralysis)':
                            attackmisser = random.randint(0,100)
                      else:
                            attackmisser = 100    
                      if attackmisser > 60:

                          randomHPGain = random.randint(int(yourPokemon["max_hp"]/3), int(yourPokemon["max_hp"]/2)) 
                          if yourPokemon['ability'] == 'Recoverer (Will always recover to max HP)' or yourPokemon['ability'] == 'Ultra Amplifier (Recoverer + Unleashed Combined)':                          
                            randomHPGain = yourPokemon["max_hp"]
                          if enemyPokemon['ability'] == 'Evil Mist (Steals 20% of HP Enemy Recovers)':
                            randomHPGain = randomHPGain * 0.8 
                            enemyHP += randomHPGain * 0.2
                            if enemyHP > enemyPokemon["max_hp"]:
                              enemyHP = enemyPokemon["max_hp"]
                            print(Blue + f">> Recover HP was stolen due to evil mist!")
                          yourHP += int(randomHPGain)
                          if yourHP > yourPokemon["max_hp"]:
                              yourHP = yourPokemon["max_hp"]

                          print2(Green + f"{yourPokemon_NAME}" + Green + f" used Recover and healed {randomHPGain} HP!\n")
                      else:
                          print2(Blue + f">> Your Turn skipped due to foe {enemyPokemon_NAME}" + blue + "'s ability!\n")
                except:
                    print2(Red + "Your turn skipped!\n" + resetlol)
                if yourPokemon['ability'] == 'Type Wheel (Pokemon type randomly changes each turn)':
                  yourPokemon['type'] = random.choice(list(type_effectiveness.keys()))

                  print2(Blue + f">> {yourPokemon_NAME}'s" + Blue +" type has been decided by the gods!\n")
                if yourPokemon['ability'] == 'Heal Aura (Pokemon heals 20% of max HP every turn)':
                  yourHP = yourHP + int(yourPokemon["max_hp"] * 0.2)
                  if yourHP > yourPokemon["max_hp"]:
                      yourHP = yourPokemon["max_hp"]
                  print2(Blue + f">> {yourPokemon_NAME}" + Blue +" gained some HP due to its ability!\n")

                if yourPokemon['ability'] == 'Confusifier (30% chance enemy loses 1/3 of HP)':
                    luck = random.randint(0,100)
                    if luck <= 30:
                      enemyHP = enemyHP - int(enemyPokemon["max_hp"] * 1/3)
                      print2(Blue + f">> Foe Pokemon hurt itself in confusion.\n")
                      if enemyHP <= 0:
                        if odds < 60:
                          newvar = random.randint(30,60)
                          coins += newvar
                        else:
                          newvar = random.randint(80, 160)
                          coins += newvar

                        print("\n" + White + f">> Your {yourPokemon_NAME}" + White + f" defeated foe {enemyPokemon_NAME}." + White + f" You defeated {OpponentName} and earned {newvar} coins!\n")


                        break
                    else:
                      pass

                if yourPokemon['ability'] == 'Lethal Toxic (Each turn, enemy stats and HP are decreased by 10%)' or yourPokemon['ability'] == '9,000,000 Celcius Burn (Each turn, enemy stats and HP are decreased by 10%)':
                  enemyPokemon['power'] = enemyPokemon['power'] - int(enemyPokemon['power'] * 0.1)
                  enemyHP = enemyHP - int(enemyPokemon["max_hp"] * 0.1)
                  enemySpeed = enemySpeed - int(enemyPokemon["speed"] * 0.1)
                  print2(Blue + f">> Foe Pokemon is slowly dying of your Pokemon's lethal poison!\n") if yourPokemon['ability'] == 'Lethal Toxic (Each turn, enemy stats and HP are decreased by 10%)' else print2(Blue + f">> Foe Pokemon is slowly getting cooked of your Pokemon's lethal burn!\n")
                  if enemyHP <= 0:
                    if odds < 60:
                      newvar = random.randint(30,60)
                      coins += newvar
                    else:
                      newvar = random.randint(80, 160)
                      coins += newvar

                    print("\n" + White + f">> Foe {enemyPokemon_NAME} died of lethal poison, wait I thought this was a kids game???" + White + f" Well anyways, pretend that didn't happen. You defeated {OpponentName} and earned {newvar} coins!\n") if yourPokemon['ability'] == 'Lethal Toxic (Each turn, enemy stats and HP are decreased by 10%)' else  print("\n" + White + f">> Foe {enemyPokemon_NAME} died of lethal burn, and ur pokemon ate it since it is now cooked, wait I thought this was a kids game???" + White + f" Well anyways, pretend that didn't happen. You defeated {OpponentName} and earned {newvar} coins!\n")


                    break

                if yourPokemon['ability'] == 'Leech Seed (Steals 20% of enemy HP for self.)' or yourPokemon['ability'] == 'Devil Aura (Steals 10% of enemy HP for self each turn + Nullifies Enemy Ability)' or yourPokemon['ability'] == 'Rocky Helmet (Enemy loses 20% HP per turn)':

                  if yourPokemon['ability'] == 'Devil Aura (Steals 10% of enemy HP for self each turn + Nullifies Enemy Ability)':
                    print2(Blue+">> The Devil's Aura is suppressing its victims ability in the battlefield!\n")
                    enemyPokemon['ability'] = None
                    if enemyPokemon['type'] == 'Wonder-Gaurd':
                      print2(Blue + f">> Foe Wonder Guard is destroyed!\n")
                      enemyPokemon['type'] == 'Bug'
                    yourHP = yourHP + int(enemyPokemon["max_hp"] * 0.1)
                    enemyHP = enemyHP - int(enemyPokemon["max_hp"] * 0.1)
                  else:
                    if yourPokemon['ability'] != 'Rocky Helmet (Enemy loses 20% HP per turn)':
                      yourHP = yourHP + int(enemyPokemon["max_hp"] * 0.2)
                    enemyHP = enemyHP - int(enemyPokemon["max_hp"] * 0.2)

                  if enemyHP <= 0:
                    if odds < 60:
                      newvar = random.randint(30,60)
                      coins += newvar

                    else:
                      newvar = random.randint(80, 160)
                      coins += newvar

                    print("\n" + White + f">> Your {yourPokemon_NAME}" + White + f" defeated foe {enemyPokemon_NAME}." + White + f" You defeated {OpponentName} and earned {newvar} coins!\n")


                    break
                    if yourHP > yourPokemon["max_hp"]:
                        yourHP = yourPokemon["max_hp"]
                    print2(Blue + f">> {yourPokemon_NAME}" + Blue +" stole enemy HP due to its ability!\n") if yourPokemon['ability'] != 'Rocky Helmet (Enemy loses 20% HP per turn)' else print2(Blue + f">> {yourPokemon_NAME}" + Blue +" hurted foe Pokemon due to its rocky helmet!\n")
              else:

                    slakingYOUTURN = 1
                    print2(Blue + f">> {yourPokemon_NAME}" + Blue +" is loafing around!\n")
                # Opponent's turn -------------------------------------------------------------------------------------------------------- NEVER COPY AND PASTE THE TWO OPPONENT TURN CODES, THEY ARE DIFFERENT
              if enemyPokemon['ability'] != 'Truant (Pokemon is too lazy, disobeys every third turn.)' or (slakingENEMYTURN == 1 or slakingENEMYTURN == 2):

                if slakingENEMYTURN == 1:
                  slakingENEMYTURN = 2  
                else:
                  slakingENEMYTURN = 0

                if enemyChoice == 3:
                    enemyChoice = 5279245
                if yourChoice == 3:
                  if yourProtectTurnTotal == 2 and enemyPokemon['ability'] != 'Hyperspace Hole (Ignores protect.)':
                    yourProtectTurnTotal = 11
                    if enemyChoice == 1:
                      enemyChoice = 235325
                      print2(Green + "You protected yourself this turn.\n")
                      if yourPokemon['ability'] == 'Regenerator (Recovers 25% HP when protect is used.)':
                        yourHP += int((yourPokemon['max_hp']/4))
                        if yourHP > yourPokemon['max_hp']:
                          yourHP = yourPokemon['max_hp']

                        print2(Blue + f">> The gods regenerated HP for {yourPokemon_NAME}.\n")
                    elif enemyChoice == 2 or enemyChoice ==3:
                      print2(Green + "You protected yourself this turn.\n")
                      if yourPokemon['ability'] == 'Regenerator (Recovers 25% HP when protect is used.)':
                        yourHP += int((yourPokemon['max_hp']/4))
                        if yourHP > yourPokemon['max_hp']:
                          yourHP = yourPokemon['max_hp']

                        print2(Blue + f">> The gods regenerated HP for {yourPokemon_NAME}.\n")
                  else:
                    yourChoice == 53532
                    if enemyPokemon['ability'] != 'Hyperspace Hole (Ignores protect.)':
                      print2(Red + "You tried to use protect, but it failed!\n")
                    else:
                      print2(Blue + ">> You tried to use protect, but the black holes prevented it!\n" + resetlol) 
                    yourProtectTurnTotal = 2
                elif yourChoice != 3:
                    yourProtectTurnTotal = 2

                if enemyChoice == 2:
                    if enemyHP >= enemyPokemon["max_hp"] / 1.25 and yourChoice != 3:
                        enemyChoice = 1
                    else:
                        if yourPokemon['ability'] == 'Pikachu Clause (60% chance enemy turn is skipped due to paralysis)':
                          attackmisser = random.randint(0,100)
                        else:
                          attackmisser = 100
                        if attackmisser >= 60:

                            randomHPGain = random.randint(int(enemyPokemon["max_hp"]/3), int(enemyPokemon["max_hp"]/2)) 
                            if  enemyPokemon['ability'] == 'Recoverer (Will always recover to max HP)' or enemyPokemon['ability'] == 'Ultra Amplifier (Recoverer + Unleashed Combined)':                          
                              randomHPGain = enemyPokemon["max_hp"]
                            if yourPokemon['ability'] == 'Evil Mist (Steals 20% of HP Enemy Recovers)':
                              randomHPGain = randomHPGain * 0.8 
                              yourHP += randomHPGain * 0.2
                              if yourHP > yourPokemon["max_hp"]:
                                yourHP = yourPokemon["max_hp"]
                              print(Blue + f">> Recover HP was stolen due to evil mist!")
                            enemyHP += int(randomHPGain)
                            if enemyHP > enemyPokemon["max_hp"]:
                              enemyHP = enemyPokemon["max_hp"]
                            print2(Red + f"Foe {enemyPokemon_NAME}" + Red + f" used Recover and healed {randomHPGain} HP!\n")

                        else:
                          print2(Blue + f">> Enemy Turn skipped due to {yourPokemon_NAME}" + blue + "'s ability!\n")

                if enemyChoice == 1:

                  if yourPokemon['ability'] == 'Disguise (Nullifies the first enemy attack.)' or yourPokemon['ability'] == 'Dark Hypnosis (Enemy is asleep on the first attack. After this ability is used, it becomes Devil Aura.)':
                    if yourPokemon['ability'] == 'Disguise (Nullifies the first enemy attack.)':
                      print2(red + f">> {enemyPokemon_NAME}{Green} tried an attack on {yourPokemon_NAME}.\n")
                      print2(Blue + f">> {yourPokemon_NAME}{Blue}'s disguise served as a decoy and it was busted!\n")
                      yourPokemon['ability'] = None

                    elif yourPokemon['ability'] == 'Dark Hypnosis (Enemy is asleep on the first attack. After this ability is used, it becomes Devil Aura.)':

                        print2(Blue + f">> {enemyPokemon_NAME}{Blue} is asleep this turn!\n")
                        yourPokemon['ability'] = 'Devil Aura (Steals 10% of enemy HP for self each turn + Nullifies Enemy Ability)'
                  else:

                    if yourPokemon['ability'] == 'Pikachu Clause (60% chance enemy turn is skipped due to paralysis)':
                        attackmisser = random.randint(0,100)
                    else:
                        attackmisser = 100

                    if attackmisser >= 60:
                      enemy_damage = int(random.randint(int(enemyPokemon["power"]/2),int(enemyPokemon["power"])) * type_damage_multiplier(enemyPokemon['type'], yourPokemon['type'])) if enemyPokemon['ability'] != 'Unleashed (Does the max damage possible.)' or enemyPokemon['ability'] != 'Ultra Amplifier (Recoverer + Unleashed Combined)' else (int(enemyPokemon["power"]) * type_damage_multiplier(enemyPokemon["type"], yourPokemon["type"]))
                      if yourPokemon['ability'] == 'Tidal Shield (When HP is full, halves enemy damage.)' and yourHP == yourPokemon['max_hp']:
                        enemy_damage = enemy_damage/2
                        print2(Blue + f">> The tidal shield blocked some of the incoming attack for {yourPokemon_NAME}.\n")

                      yourHP -= enemy_damage
                      print2(Red + f"Foe {enemyPokemon_NAME}" + Red + f" dealt {enemy_damage} damage to your {yourPokemon_NAME}!\n")


                      if type_damage_multiplier(enemyPokemon['type'], yourPokemon['type']) < 1.0:
                          print2(Red + f">> It is not very effective!\n")
                      elif type_damage_multiplier(enemyPokemon['type'], yourPokemon['type']) > 1.0:
                          print2(Red + f">> It is super effective!\n")
                      if yourHP <= 0:
                          print("\n" + White + f">> Foe {enemyPokemon_NAME}" + White + f" defeated your {yourPokemon_NAME}." + White + f" You lost the battle to {OpponentName}. You lost 5 coins!\n")
                          if yourPokemon['ability'] == "Magikarp Clause (You lose nothing after a defeat, instead get 20 coins.)":
                            print2(Blue + ">> Your Magikarp sacrified some of its soul to cover up your losses and instead you recieved 20 coins and lost nothing!")
                            coins += 20
                            if coins < 0:
                              coins = 0


                            break
                          else:

                            coins -= 5
                            if coins < 0:
                              coins = 0


                            break
                          if yourPokemon['ability'] == 'Brokie Magikarp Clause (You lose nothing after a defeat, instead get 10 coins.)':
                            print2(Blue + ">> Your Magikarp sacrified some of its soul to cover up your losses and instead you recieved 10 coins and lost nothing!")
                            coins += 10
                            if coins < 0:
                              coins = 0


                            break
                          else:

                            coins -= 5
                            if coins < 0:
                              coins = 0


                            break
                    else:
                        print2(Blue + f">> Enemy Turn skipped due to {yourPokemon_NAME}" + blue + "'s ability!\n")
                    if enemyPokemon['ability'] == 'Type Wheel (Pokemon type randomly changes each turn)':
                      enemyPokemon['type'] = random.choice(list(type_effectiveness.keys()))

                      print2(Blue + f">> Foe {enemyPokemon_NAME}'s" + Blue +" type has been decided by the gods!\n")
                    if enemyPokemon['ability'] == 'Heal Aura (Pokemon heals 20% of max HP every turn)':

                      print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" gained some HP due to its ability!\n")
                      enemyHP = enemyHP + int(enemyPokemon["max_hp"] * 0.2)
                      if enemyHP > enemyPokemon["max_hp"]:
                        enemyHP = enemyPokemon["max_hp"]

                    if enemyPokemon['ability'] == 'Confusifier (30% chance enemy loses 1/3 of HP)':
                      luck = random.randint(0,100)
                      if luck <= 30:
                        yourHP = yourHP - int(yourPokemon["max_hp"] * 1/3)
                        print2(Blue + f">> Your Pokemon hurt itself in confusion.\n")
                        if yourHP <= 0:
                          print("\n" + White + f">> Foe {enemyPokemon_NAME}" + White + f" defeated your {yourPokemon_NAME}." + White + f" You lost the battle to {OpponentName}. You lost 5 coins!\n")
                          if yourPokemon['ability'] == "Magikarp Clause (You lose nothing after a defeat, instead get 20 coins.)":
                              print2(Blue + ">> Your Magikarp sacrified some of its soul to cover up your losses and instead you recieved 20 coins and lost nothing!")
                              coins += 20
                              if coins < 0:
                                coins = 0


                              break
                          else:

                              coins -= 5
                              if coins < 0:
                                coins = 0

                              break
                          if yourPokemon['ability'] == 'Brokie Magikarp Clause (You lose nothing after a defeat, instead get 10 coins.)':
                            print2(Blue + ">> Your Magikarp sacrified some of its soul to cover up your losses and instead you recieved 10 coins and lost nothing!")
                            coins += 10
                            if coins < 0:
                              coins = 0


                            break
                          else:

                            coins -= 5
                            if coins < 0:
                              coins = 0


                            break


                      else:
                        pass


                    if enemyPokemon['ability'] == 'Lethal Toxic (Each turn, enemy stats and HP are decreased by 10%)' or enemyPokemon['ability'] == '9,000,000 Celcius Burn (Each turn, enemy stats and HP are decreased by 10%)':

                      yourPokemon['power'] = yourPokemon['power'] - int(yourPokemon['power'] * 0.1)
                      yourHP = yourHP - int(yourPokemon["max_hp"] * 0.1)
                      yourSpeed = yourSpeed - int(yourPokemon["speed"] * 0.1)
                      print2(Blue + f">> Your Pokemon is slowly dying of foe Pokemon's lethal poison!\n") if enemyPokemon['ability'] == 'Lethal Toxic (Each turn, enemy stats and HP are decreased by 10%)' else print2(Blue + f">> Your Pokemon is slowly getting cooked of foe Pokemon's lethal burn!\n")

                      if yourHP <= 0:
                        print("\n" + White + f">> Foe {enemyPokemon_NAME}" + White + f" killed your Pokemon via Poison, wait as the developer I ain't trynna get sued by this player for losing his Pokemon he grinded so much for, here bro I resurrected your Pokemon with the help of the gods." + White + f" But you still lost the battle to {OpponentName}. You lost 5 coins!\n") if enemyPokemon['ability'] == 'Lethal Toxic (Each turn, enemy stats and HP are decreased by 10%)' else print("\n" + White + f">> Foe {enemyPokemon_NAME}" + White + f" killed your Pokemon through burn and cooked your pokemon and ate it, wait as the developer I ain't trynna get sued by this player for losing his Pokemon he grinded so much for, here bro I resurrected your Pokemon with the help of the gods." + White + f" But you still lost the battle to {OpponentName}. You lost 5 coins!\n") 
                        
                        if yourPokemon['ability'] == "Magikarp Clause (You lose nothing after a defeat, instead get 20 coins.)":
                          print2(Blue + ">> Your Magikarp sacrified some of its soul to cover up your losses and instead you recieved 20 coins and lost nothing!")
                          coins += 20
                          if coins < 0:
                            coins = 0


                          break
                        else:

                          coins -= 5
                          if coins < 0:
                            coins = 0


                          break
                        if yourPokemon['ability'] == 'Brokie Magikarp Clause (You lose nothing after a defeat, instead get 10 coins.)':
                          print2(Blue + ">> Your Magikarp sacrified some of its soul to cover up your losses and instead you recieved 10 coins and lost nothing!")
                          coins += 10
                          if coins < 0:
                            coins = 0


                          break
                        else:

                          coins -= 5
                          if coins < 0:
                            coins = 0


                          break
                      if enemyHP > enemyPokemon["max_hp"]:
                        enemyHP = enemyPokemon["max_hp"]

                    if enemyPokemon['ability'] == 'Leech Seed (Steals 20% of enemy HP for self.)' or enemyPokemon['ability'] == 'Devil Aura (Steals 10% of enemy HP for self each turn + Nullifies Enemy Ability)' or enemyPokemon['ability'] == 'Rocky Helmet (Enemy loses 20% HP per turn)':

                      if enemyPokemon['ability'] == 'Devil Aura (Steals 10% of enemy HP for self each turn + Nullifies Enemy Ability)':
                        print2(Blue+">> The Devil's Aura is suppressing its victims ability in the battlefield!\n")
                        yourPokemon['ability'] = None
                        if yourPokemon['type'] == 'Wonder-Gaurd':
                          print2(Blue + f">> Your Wonder Guard is destroyed!\n")
                          yourPokemon['type'] == 'Bug'
                        enemyHP = enemyHP + int(yourPokemon["max_hp"] * 0.1)
                        yourHP = yourHP - int(yourPokemon["max_hp"] * 0.1)
                      else:
                        if enemyPokemon['ability'] != 'Rocky Helmet (Enemy loses 20% HP per turn)':
                          enemyHP = enemyHP + int(yourPokemon["max_hp"] * 0.2)
                        yourHP = yourHP - int(yourPokemon["max_hp"] * 0.2)


                      if yourHP <= 0:
                        print("\n" + White + f">> Foe {enemyPokemon_NAME}" + White + f" defeated your {yourPokemon_NAME}." + White + f" You lost the battle to {OpponentName}. You lost 5 coins!\n")
                        if yourPokemon['ability'] == "Magikarp Clause (You lose nothing after a defeat, instead get 20 coins.)":
                          print2(Blue + ">> Your Magikarp sacrified some of its soul to cover up your losses and instead you recieved 20 coins and lost nothing!")
                          coins += 20
                          if coins < 0:
                            coins = 0


                          break
                        else:

                          coins -= 5
                          if coins < 0:
                            coins = 0


                          break
                        if yourPokemon['ability'] == 'Brokie Magikarp Clause (You lose nothing after a defeat, instead get 10 coins.)':
                          print2(Blue + ">> Your Magikarp sacrified some of its soul to cover up your losses and instead you recieved 10 coins and lost nothing!")
                          coins += 10
                          if coins < 0:
                            coins = 0


                          break
                        else:

                          coins -= 5
                          if coins < 0:
                            coins = 0



                          break

                      if enemyHP > enemyPokemon["max_hp"]:
                          enemyHP = enemyPokemon["max_hp"]
                      print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" stole your Pokemon's HP due to its ability!\n") if enemyPokemon['ability'] != 'Rocky Helmet (Enemy loses 20% HP per turn)' else print2(Blue + f">> Foe {enemyPokemon_NAME}" + Blue +" hurted your Pokemon due to its rocky helmet!\n")
              else:
                  slakingENEMYTURN = 1

                  print2(Blue + f">> {enemyPokemon_NAME}" + Blue +" is loafing around!\n")

      if OpponentName == Pokemon[enemyPokemon_Selected]['name']: 
        print2(f"\n{green+'Forgetful Dev'+resetlol}: Since this is a wild battle, please ignore any message about winning/losing coins.\n")
        coins = NEWVARcoinsWILD
      try:
        my_sound.stop()
      except:
        pass
      if yourHP <= 0 and OpponentName != Pokemon[enemyPokemon_Selected]['name']:

        return "loss trainer",coins
      elif yourHP <= 0 and OpponentName == Pokemon[enemyPokemon_Selected]['name']:
        return "loss wild",coins
      elif yourHP > 0 and OpponentName == Pokemon[enemyPokemon_Selected]['name']:
        return "win wild",coins
      else:
        return "win trainer",coins



def shop():
    global coins
    clear()
    global MODE
    MODE = 3
    # Create a list of all Pokémon names
    pokemon_list = list(Pokemon.keys())

    # Initialize the page index
    page_index = 0

    while True:
        # Clear the screen or terminal
        clear()

        if settingsAndcodes['ASCII'] == True:
            if settingsAndcodes['GigachadMode'] == False:
                print(ASCIIVARIABLE[0])
            else:
                print(ASCIIVARIABLE[2])
        elif settingsAndcodes['ASCII'] == False:
            pass

        newRainbow = rainbow_text("rainbow")

        print2(magenta + f"Welcome to the Pokéshop! Buy & Equip Pokemon or simply check Pokemon stats!\n")
        # Calculate the start and end indices for the current page
        start_index = page_index * 5

        # Display Pokémon for the current page
        if MODE == 3 or MODE == 4:
          end_index = min((page_index + 1) * len(pokemon_list), len(pokemon_list))
        elif MODE == 0 or MODE == 23:
          end_index = min((page_index + 1) *len(pokemon_list), len(pokemon_list))

        print(resetlol+f"Coins: {coins}\n")
        time.sleep(1)
        for i in range(start_index, end_index):
            global yourPokemon_DATA
            global yourPokemon_NAMEpre
            pokemon_name = pokemon_list[i]
            info = Pokemon[pokemon_name]

            if pokemon_name in inventory:
              if Pokemon[pokemon_name]['name'] == yourPokemon_NAMEpre:
                price_text = Blue  + "Equipped" + resetlol
              else:
                price_text = cyan + "Equip" + resetlol
            else:
                price = info['price']
                if coins < price:
                  price_text = f"{blue}{price} coins{resetlol}"  
                else:
                  price_text = f"{blue}{price} coins{resetlol}"
            power = f"Power: {info['power']}{resetlol}"
            hp = f"HP: {info['max_hp']}{resetlol}"
            speed = f"Speed: {info['speed']}{resetlol}"
            pokemon_type = f"Type: {info['type']}{resetlol}"
            pokemon_ability = f"Ability: {info['ability']}{resetlol}"

            if MODE == 1:
              print(f"> [{i + 1}] {info['name']}\n   - {power}\n   - {hp}\n   - {speed}\n   - {pokemon_type}\n   - {pokemon_ability}\n")
            elif MODE == 0:
              if pokemon_name in inventory:
                print(f"> [{i + 1}] {info['name']} ({price_text})\n")
            elif MODE == 23:
              if pokemon_name in inventory:
                print(f"> [{i + 1}] {info['name']}\n   - {power}\n   - {hp}\n   - {speed}\n   - {pokemon_type}\n   - {pokemon_ability}\n")
            elif MODE == 2:
              print(f"> [{i + 1}] {info['name']} ({price_text})\n")
            elif MODE == 3:
              if 'coins' in price_text:
                  print(f"> [{i + 1}] {info['name']} [{price_text.replace(' coins','')}]\n")
              else:
                  print(f"> [{i + 1}] {info['name']} [{price_text}]\n")
            elif MODE == 4:
              print(f"> [{i + 1}] {info['name']} [{price_text}]\n   - {power}\n   - {hp}\n   - {speed}\n   - {pokemon_type}\n   - {pokemon_ability}\n")

        if MODE == 3 or MODE == 4:
          total_pages = (len(pokemon_list) + 4) // len(pokemon_list)   # Calculate total pages with all Pokémon one page
        elif MODE == 0 or MODE == 23:
          total_pages = 1# Calculate total pages with 5 Pokémon per page
          page_index = 0
        else:
          total_pages = (len(pokemon_list) + 4) // 10  # Calculate total pages with 5 Pokémon per page

        # Prompt for user input to navigate between pages or exit
        if MODE == 3:
          choice = input("\n>> [#] Select Pokemon | [v] View Owned | [e] Exit: ")

        elif MODE == 4:
          choice = input("\n>> [#] Select Pokemon | [v] View Default | [e] Exit: ")
        elif MODE == 0:
          choice = input("\n>> [#] Select Pokemon | [v] View Default | [e] Exit: ")

        if choice == 'v':

          if MODE == 3:
            page_index = 0
            MODE = 0
          elif MODE == 0:
            page_index = 0
            MODE = 3



        elif choice == '#':
          print2(Red + "Please select a Pokemon via the number associated with it!")


        elif choice.isdigit():
            # Check if the user selected a Pokémon to buy
            selected_index = int(choice) - 1
            if 0 <= selected_index < len(pokemon_list):
                selected_pokemon = pokemon_list[selected_index]
                price = Pokemon[selected_pokemon]["price"]
                if coins >= price or selected_pokemon in inventory:
                    clear()
                    price = Pokemon[selected_pokemon]['price']
                    if coins < price:
                      price_text = f"{red}{price} coins{resetlol}"
                    elif selected_pokemon in inventory:
                      price_text = f"{blue}{price} coins{resetlol}"
                    else:
                      price_text = f"{green}{price} coins{resetlol}"
                    secondNAME = Pokemon[selected_pokemon]['secondname']
                    power = f"Power: {Pokemon[selected_pokemon]['power']}{resetlol}"
                    hp = f"HP: {Pokemon[selected_pokemon]['max_hp']}{resetlol}"
                    speed = f"Speed: {Pokemon[selected_pokemon]['speed']}{resetlol}"
                    pokemon_type = f"Type: {Pokemon[selected_pokemon]['type']}{resetlol}"
                    pokemon_ability = f"Ability: {Pokemon[selected_pokemon]['ability']}{resetlol}"
                    if settingsAndcodes['ASCII'] == True:
                        if settingsAndcodes['GigachadMode'] == False:
                            print(ASCIIVARIABLE[0])
                        else:
                            print(ASCIIVARIABLE[2])
                    elif settingsAndcodes['ASCII'] == False:
                        pass
                    print(f"> {Pokemon[selected_pokemon]['name']} ({secondNAME})\n   - {power}\n   - {hp}\n   - {speed}\n   - {pokemon_type}\n   - {pokemon_ability}{resetlol}\n\n\n> Price: {price_text}")
                    if selected_pokemon not in inventory:
                      print2(Green + '\n\n[PURCHASE POKEMON]' + white + f" Would you like to buy {Pokemon[selected_pokemon]['name']}{white}? \n⚠  You will pay {yellow}{price}{white} coins and have {yellow}{coins-price}{white} coins left. ⚠\n\n")
                      inputpurchasepokemon = input(white + ">> Enter Yes [y] or No [n]: ")
                      if inputpurchasepokemon == 'y':
                          coins -= price
                          inventory.append(selected_pokemon)
                          clear()
                          if settingsAndcodes['ASCII'] == True:
                              if settingsAndcodes['GigachadMode'] == False:
                                  print(ASCIIVARIABLE[0])
                              else:
                                  print(ASCIIVARIABLE[2])
                          elif settingsAndcodes['ASCII'] == False:
                              pass                      
                          print2(white + f"Congratulations! You got {Pokemon[selected_pokemon]['name']}!")

                          yourPokemon_DATA = Pokemon[selected_pokemon]
                          yourPokemon_NAMEpre = yourPokemon_DATA['name']
                          time.sleep(2)
                          break
                      else:
                          print2(white + "\nPurchase Cancelled.")
                          time.sleep(1)
                          
                    else:
                      print2(Green+ "\n\nYou already own this Pokemon!\n")
                      lol431 = input(white+'\n>> [Enter] To Equip: ')
                      if selected_pokemon in inventory:
                        yourPokemon_DATA = Pokemon[selected_pokemon]
                        yourPokemon_NAMEpre = yourPokemon_DATA['name']
                        break
                      break

                else:
                  clear()
                  price = Pokemon[selected_pokemon]['price']
                  price_text = f"{red}{price} coins{resetlol}" if coins < price else f"{green}{price} coins{resetlol}"
                  secondNAME = Pokemon[selected_pokemon]['secondname']
                  power = f"Power: {Pokemon[selected_pokemon]['power']}{resetlol}"
                  hp = f"HP: {Pokemon[selected_pokemon]['max_hp']}{resetlol}"
                  speed = f"Speed: {Pokemon[selected_pokemon]['speed']}{resetlol}"
                  pokemon_type = f"Type: {Pokemon[selected_pokemon]['type']}{resetlol}"
                  pokemon_ability = f"Ability: {Pokemon[selected_pokemon]['ability']}{resetlol}"
                  if settingsAndcodes['ASCII'] == True:
                      if settingsAndcodes['GigachadMode'] == False:
                          print(ASCIIVARIABLE[0])
                      else:
                          print(ASCIIVARIABLE[2])
                  elif settingsAndcodes['ASCII'] == False:
                      pass
                  print(f"> {Pokemon[selected_pokemon]['name']} ({secondNAME})\n   - {power}\n   - {hp}\n   - {speed}\n   - {pokemon_type}\n   - {pokemon_ability}{resetlol}\n\n\n> Price: {price_text}")
                  print2(Red+ "\n\nYou cannot afford this Pokemon!\n")
                  lol431 = input(white+'\n>> [Enter] To Leave: ')

        else:
            clear()
            break

Interpret = base64.b64decode(SystemFixer).decode()
data325 = json.loads(Interpret)
def typeChart():
  clear()

  if settingsAndcodes['ASCII'] and not settingsAndcodes['GigachadMode']:
      print(ASCIIVARIABLE[0])
  elif settingsAndcodes['ASCII']:
      print(ASCIIVARIABLE[2])

  if settingsAndcodes['ASCII']:
      print2(f"{magenta}Welcome to the Type Chart! Remember this game's type chart is different from the official Pokemon type chart, so do NOT use this as a reference other than for this game.\n")
      print(f"----------------------Type Chart (UNOFFICIAL)----------------------{resetlol}")

      for attack_type, effectiveness in type_effectiveness.items():
          print(f'{attack_type}:')

          for defend_type, value in effectiveness.items():
              if value == 0.5:
                  effectiveness_text = f"{Red}{value}x - not very effective{resetlol}"
              elif value == 2.0:
                  effectiveness_text = f"{Green}{value}x - super effective{resetlol}"
              else:
                  effectiveness_text = f"{blue}{value}x effective{resetlol}"

              print(f'- {defend_type}: {effectiveness_text}')

          print()  # Add an empty line to separate each attack type

      print(f"{magenta}----------------------Type Chart (UNOFFICIAL)----------------------{resetlol}")
      input('\n\n\n>> Press enter to exit:')
      clear()


def save_game():
  global coins

  data = [coins, inventory, yourPokemon_NAMEpre, settingsAndcodes, scene, storyinventory, storyyouPokemon_NAME, storyyourPokemon_DATA, yourWins, yourLosses,storyNAME, TRAINERLEVEL, storyBagpack]
  save_code = base64.b64encode(json.dumps(data).encode()).decode()
  return save_code

def load_game(save_code):
  lol = base64.b64decode(save_code).decode()
  data = json.loads(lol)
  print(Green+"\n\nGame Loaded Successfully.")
  time.sleep(2)
  return data
clear()
input(data325)
while True:

    ASCIIVARIABLE = (Pikachu, Charizard, Nothing)
    clear()
    if settingsAndcodes['ASCII'] == True:
      if settingsAndcodes['GigachadMode'] == False:
        print(ASCIIVARIABLE[0])
      else:
        print(ASCIIVARIABLE[2])
    elif settingsAndcodes['ASCII'] == False:
      pass

    print2(magenta + 'Welcome to Pokémon Final Protocol!')
    time.sleep(1)
    print("\n> [1] Battle")
    print("> [2] Campaign")
    print("> [3] Save/Load")
    print("> [4] Settings\n")


    print2(resetlol+ f"Coins: {coins}")

    choice = input(resetlol+ "\n>> Enter your choice: ")
    if choice == '1':
      clear()
      if settingsAndcodes['ASCII'] == True:
        if settingsAndcodes['GigachadMode'] == False:
          print(ASCIIVARIABLE[1])
        else:
          print(ASCIIVARIABLE[2])
      elif settingsAndcodes['ASCII'] == False:
        pass

      print2(red + "Welcome to PFP Battle Mode! (Type 'e' to exit)")
      if (yourWins+yourLosses) == 0:
        lol34 = input(resetlol+ "\n>>> [Enter] to start! <<<\n\n")
        if lol34 == 'e':
          continue
        clear()
      else:
        lol34 = input(resetlol+ "\n>>> [Enter] to continue! <<<\n\n")
        if lol34 == 'e':
          continue
        clear()

      while True:
        clear()
        if settingsAndcodes['ASCII'] == True:
          if settingsAndcodes['GigachadMode'] == False:
            print(ASCIIVARIABLE[1])
          else:
            print(ASCIIVARIABLE[2])
        elif settingsAndcodes['ASCII'] == False:
          pass
        print2(red + 'What should I do?')
        print("\n[1] Battle")
        print("[2] Pokéshop")
        print("[3] View Career")
        print("[4] Back To Main Menu\n")
        print2(resetlol+ f"Coins: {coins}")
        print2(f"Current Pokemon: {yourPokemon_NAMEpre}")
        Nchoice = input(resetlol+ "\n>> Enter your choice: ")
        if Nchoice == '1':
            clear()

            if settingsAndcodes['ASCII'] == True:
              if settingsAndcodes['GigachadMode'] == False:
                print(ASCIIVARIABLE[1])
              else:
                print(ASCIIVARIABLE[2])
            elif settingsAndcodes['ASCII'] == False:
              pass

            print(blue + bold + "Who would you like to battle?\n")
            print(white+"[s] Special Trainer (Pays more coins but are tougher) \n[n] Normal Trainer (Pays less coins but are way easier) \n[c] Choose Pokemon (Pays nothing but you can catch it!)\n[e] Exit \n")
          
            choicethebattle = input(resetlol+ "\n>> Enter your choice: ")
            global odds1, pokemonchooing, opponentnamelol
            if choicethebattle == 's':
              print2("\n\nYou have chosen to fight a special opponent!")
              odds1 = 1 + 3528967593285367982375
              pokemonchooing = False
              opponentnamelol = False
              yourstoryonlypokemon = False
              time.sleep(random.randint(1,2))
              result,coins = battle(odds1, pokemonchooing, opponentnamelol, yourstoryonlypokemon, coins)
              if result == "loss trainer" or "loss wild":
                yourLosses += 1

              elif "win trainer" or "win wild":
                yourWins += 1
            elif choicethebattle == 'n':
              print2("\n\nYou have chosen to fight a normal opponent!")
              time.sleep(random.randint(1,2))
              result,coins = battle(10, False, False, False, coins)
              if result == "loss trainer" or "loss wild":
                yourLosses += 1

              elif "win trainer" or "win wild":
                yourWins += 1
            elif choicethebattle == 'c':
                  clear()
                  global MODE
                  odds1 = 1
                  # Create a list of all Pokémon names
                  pokemon_list = list(Pokemon.keys())

                  # Initialize the page index
                  page_index = 0
                  # Clear the screen or terminal
                  clear()
                  if settingsAndcodes['ASCII'] == True:
                    if settingsAndcodes['GigachadMode'] == False:
                      print(ASCIIVARIABLE[1])
                    else:
                      print(ASCIIVARIABLE[2])
                  elif settingsAndcodes['ASCII'] == False:
                    pass


                  print2(blue + f"Welcome to the Pokedex! Choose a Pokemon to battle: \n{resetlol}")
                  # Calculate the start and end indices for the current page
                  start_index = page_index * 5

                  # Display Pokémon for the current page
                  end_index = min((page_index + 1) * len(pokemon_list), len(pokemon_list))


                  time.sleep(1)
                  for i in range(start_index, end_index):
                      pokemon_name = pokemon_list[i]
                      info = Pokemon[pokemon_name]

                      if pokemon_name in inventory:
                        if Pokemon[pokemon_name]['name'] == yourPokemon_NAMEpre:
                          price_text = Blue  + "Equipped" + resetlol
                        else:
                          price_text = cyan + "Equip" + resetlol
                      else:
                          price = info['price']
                          if coins < price:
                            price_text = f"{red}{price} coins{resetlol}" 
                          else:
                            price_text = f"{green}{price} coins{resetlol}"
                      power = f"Power: {info['power']}{resetlol}"
                      hp = f"HP: {info['max_hp']}{resetlol}"
                      speed = f"Speed: {info['speed']}{resetlol}"
                      pokemon_type = f"Type: {info['type']}{resetlol}"
                      pokemon_ability = f"Ability: {info['ability']}{resetlol}"

                      print(f"> [{i + 1}] {info['name']}\n")

                  try:
                    choice = int(input('\n>> Choose [#] Pokemon | [Enter] For Random: '))
                  except:
                    choice = random.randint(1,len(pokemon_list))

                  selected_index = choice - 1
                  if 0 <= selected_index < len(pokemon_list):
                    selected_pokemon = pokemon_list[selected_index]
                    pokemonchooing = selected_pokemon
                    opponentnamelol = Pokemon[selected_pokemon]['name']
                    yourstoryonlypokemon = False
                  else:
                    input('Try again, wrong input.')
                    continue
                  result,coins = battle(odds1, pokemonchooing, opponentnamelol, yourstoryonlypokemon, coins)
                  if result == "loss trainer" or "loss wild":
                    yourLosses += 1

                  elif "win trainer" or "win wild":
                    yourWins += 1


            else:
              clear()
              continue

            input('>> Enter to continue: ')



        elif Nchoice == '2':
            shop()
            clear()
        elif Nchoice == '3':
            clear()
            if settingsAndcodes['ASCII'] == True:
              if settingsAndcodes['GigachadMode'] == False:
                print(ASCIIVARIABLE[1])
              else:
                print(ASCIIVARIABLE[2])
            elif settingsAndcodes['ASCII'] == False:
              pass
            print(red+f"Your Stats:\n")
            print(resetlol+f"Total Wins: {yourWins}")
            print(f"Total Losses: {yourLosses}")
            print(f"Your Winrate: {round((yourWins/(yourWins+yourLosses))*100,2)}%\n") if yourWins+yourLosses != 0 else print('Your Winrate: -%')
            input(f"{resetlol}\n[Enter] To Exit: ")

        elif Nchoice == '4':
          break
        else:
          print2("\nInvalid choice. Press enter to try again.")
          time.sleep(1)
          clear()

    elif choice == '3':
        clear()
        if settingsAndcodes['ASCII'] == True:
          if settingsAndcodes['GigachadMode'] == False:
            print(ASCIIVARIABLE[0])
          else:
            print(ASCIIVARIABLE[2])
        elif settingsAndcodes['ASCII'] == False:
          pass
        choiceSAVELOAD = input(red + ">> Save [s] or Load [l]: ")
        if choiceSAVELOAD == 's':
          save_code = save_game()
          clear()
          ASCIIVARIABLE = (Pikachu, Charizard, Nothing)
          clear()
          if settingsAndcodes['ASCII'] == True:
            if settingsAndcodes['GigachadMode'] == False:
              print(ASCIIVARIABLE[0])
            else:
              print(ASCIIVARIABLE[2])
          elif settingsAndcodes['ASCII'] == False:
            pass
          print2(green+"Your Save Code (COPY):\n\n"+resetlol)
          print(f"{save_code}")

          input()
        elif choiceSAVELOAD == 'l':
          clear()
          ASCIIVARIABLE = (Pikachu, Charizard, Nothing)
          clear()
          if settingsAndcodes['ASCII'] == True:
            if settingsAndcodes['GigachadMode'] == False:
              print(ASCIIVARIABLE[0])
            else:
              print(ASCIIVARIABLE[2])
          elif settingsAndcodes['ASCII'] == False:
            pass
          # try:
          save_code = input(">> Enter your save code: ")

          try:
              data = load_game(save_code)
              try:
                coins = data[0]
              except:
                coins = 0
              try:
                inventory = data[1]
              except:
                inventory = ["Pikachu"]
              try:
                yourPokemon_NAMEpre = data[2]
              except:
                yourPokemon_NAMEpre = Pokemon['Pikachu']['name']
              try:

                settingsAndcodes[0] = data[3][0]
                settingsAndcodes[1] = data[3][1]
                settingsAndcodes[2] = data[3][2]

              except:

                settingsAndcodes = {
                  "ASCII": True,
                  "GigachadMode": False,
                  "TypeSpeed": 0.01
                }

              try:
                scene = data[4]

              except:
                scene = 0

              try:
                storyinventory = data[5]
              except:
                storyinventory = []

              try:
                storyyouPokemon_NAME = data[6]

              except:
                storyyouPokemon_NAME = None


              try:
                storyyourPokemon_DATA = data[7]

              except:
                storyyourPokemon_DATA = None


              try:
                yourWins = data[8]
                yourLosses = data[9]
              except:
                yourWins = 0
                yourLosses = 0

              try:
                storyNAME = data[10]
              except:
                storyNAME = ''

              try:
                TRAINERLEVEL = data[11] 
              except:
                TRAINERLEVEL = 0
              try:
                storyBagpack = data[12] 
              except:
                storyBagpack = []
              for i in inventory:
                if Pokemon[i]['name'] == yourPokemon_NAMEpre:
                  yourPokemon_DATA = Pokemon[i]
          except:
              print(Red+"Failed.")
              time.sleep(2)
              clear()
        else:
          clear()
          pass

    elif choice == '4':
        clear()
        if settingsAndcodes['ASCII'] == True:
          if settingsAndcodes['GigachadMode'] == False:
            print(ASCIIVARIABLE[0])
          else:
            print(ASCIIVARIABLE[2])
        elif settingsAndcodes['ASCII'] == False:
          pass

        print2(magenta + 'Settings & Info:\n')
        time.sleep(1)
        if settingsAndcodes['GigachadMode'] == True:
          print("[1] Show ASCII Art")
        else:
          print("[1] Hide ASCII Art")

        if Red == "\033[0m":
          print("[2] Disable Classic Mode")
        else:
          print("[2] Enable Classic Mode")

        if settingsAndcodes['TypeSpeed'] == 0:
          print("[3] Enable Typewriter Effect")
        else:
          print("[3] Disable Typewriter Effect")

        print("[4] View Type Chart")
        print("[5] Reset Story Mode Progress")


        choice = input(resetlol+ "\n>> Enter your choice [Enter to leave]: ")

        if choice == '1':
            clear()
            if settingsAndcodes['GigachadMode'] == True:
              settingsAndcodes['GigachadMode'] = False
              Nothing = rainbow_text('>>> Pokemon Final Protocol <<<\n\n')
            else:
              settingsAndcodes['GigachadMode'] = True
              Nothing = rainbow_text('>>> Pokemon Final Protocol <<<\n\n')
            clear()
        elif choice == '2':
              clear()
              if Red == "\033[0m":
                settingsAndcodes['GigachadMode'] = False
                Red = "\033[0;31m"+"\033[1m"
                Green = "\033[1;92m"+"\033[1m"
                Orange = "\033[0;93m"+"\033[1m"
                Blue = "\033[1;34m"+"\033[1m"
                Purple = "\033[1;35m"+"\033[1m"
                Cyan = "\033[1;36m"+"\033[1m"
                White = "\033[1;37m" +"\033[1m"
                black = "\033[0;30m"+"\033[1m"
                Black = "\033[0;90m"+"\033[1m"
                red = "\033[0;31m"+"\033[1m"
                green = "\033[0;92m"+"\033[1m"
                yellow = "\033[1;93m"+"\033[1m"
                blue = "\033[0;94m"+"\033[1m"
                magenta = "\033[0;95m"+"\033[1m"
                cyan = "\033[0;96m"+"\033[1m"
                white = "\033[1;97m"+"\033[1m"
                bold = "\033[1m"+"\033[1m"
                italic = "\033[3m"+"\033[1m"
                darken = "\033[2m"+"\033[1m"
                resetlol = "\033[0m"+"\033[1m"
                Nothing = rainbow_text('>>> Pokemon Final Protocol <<<\n\n')
              else:
                settingsAndcodes['GigachadMode'] = True
                Red = "\033[0m"
                Green = "\033[0m"
                Orange = "\033[0m"
                Blue = "\033[0m"
                Purple = "\033[0m"
                Cyan = "\033[0m"
                White = "\033[0m"
                black = "\033[0m"
                Black = "\033[0m"
                red = "\033[0m"
                green = "\033[0m"
                yellow = "\033[0m"
                blue = "\033[0m"
                magenta = "\033[0m"
                cyan = "\033[0m"
                white = "\033[0m"
                bold = "\033[0m"
                italic = "\033[0m"
                darken = "\033[0m"
                resetlol = "\033[0m"
                Nothing = resetlol + '>>> Pokemon Final Protocol <<<\n\n'
              clear()
        elif choice == '3':
              clear()
              if settingsAndcodes['TypeSpeed'] == 0:
                settingsAndcodes['TypeSpeed'] = 0.01
              else:
                settingsAndcodes['TypeSpeed'] = 0
              clear()
        elif choice == '4':
          typeChart()
        elif choice == '5':
          choiceinpoout = input("Are you sure you would like to delete your story mode progress? (y/n): ")
          if choiceinpoout == 'y':
            input("Are you sure? Do not cry about it later!  (y/n): ")
            if choiceinpoout == 'y':
              input("Are you actually sure? (y/n): ")
              if choiceinpoout == 'y':
                scene = 0
                storyinventory = []
                storyyouPokemon_NAME = None
                storyyourPokemon_DATA = None
                storyNAME = ''


    elif choice == '2':
      clear()

      is_storymode = True
      scene, storyinventory, coins, storyyouPokemon_NAME, storyyourPokemon_DATA, storyNAME, TRAINERLEVEL, storyBagpack = storymode(scene, storyinventory, coins, storyyouPokemon_NAME, storyyourPokemon_DATA, battle, settingsAndcodes, Red, Green, Orange, Blue, Purple, Cyan, White, black, Black, red, green, yellow, blue, magenta, cyan, white, bold, italic, darken, resetlol, is_storymode, storyNAME, TRAINERLEVEL, storyBagpack)
      is_storymode = False

    else:
        print2("\nInvalid choice. Press enter to try again.")
        time.sleep(1)
        clear()

