import sys, os

# this is here to quickly link to the file path to the main folder instead of scripts
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
sys.path.append(os.path.join(project_root, "in_game_data"))


import json
import random
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import time
import sys
import base64
import pygame
pygame.init()
from in_game_data.allpokemon import *

gengar = f'''
    {Purple} @@@                                         @@
     {Purple}@  @@                                     @@  @            
      @   @@ @            @   @  @           @@    @             
       @      @   @  @  @@@@@@@@@@@  @ @    @     @            
        @@      @@ @@@@@           @@ @@@@@@     @             
          @@                                    @                             
            @                                  @                            
            @    {red}@@                      @@ {Purple}   @               
           @    {red}@@@@@                  @@@@{Purple}     @              
          @      {red}@@@@@@@             @@@@@@@ {Purple}    @              
         @       {red}@@@@@@{blue}@{red}@          @@{blue}@{red}@@@@@@ {Purple}     @             
        @       {red} @@@@@@{blue}@{red}@@        @@@{blue}@{red}@@@@@  {Purple}      @           
       @           {red}@@@@@@@         @@@@@@@  {Purple}        @          
      @                                              @
     @            {black}@@@@@              @@@@@{black}@{Purple}           @         
     @            {black}@{white}@@{black}@{white}@{black}@@@@@@@@@@@@@@@{white}@{black}@{white}@@{black}@{Purple}           @         
    @             {black}@{white}@@{black}@{white}@@@@{black}@{white}@@@{black}@{white}@@@{black}@{white}@@@@{black}@{white}@@{black}@{Purple}            @       
   @               {black}@{white}@{black}@{white}@@@@{black}@{white}@@@{black}@{white}@@@{black}@{white}@@@@{black}@{white}@{black}@{Purple}              @       
   @                 {black}@{white}@@@@{black}@{white}@@@{black}@{white}@@@{black}@{white}@@@@{black}@{white}{black}@{Purple}               @       
   @       @           {black}@{white}@@{black}@{white}@@@{black}@{white}@@@{black}@{white}@@@{black}@{Purple}         @       @       
   @       @             {black}@@@@@@@@@@@@@{Purple}          @       @             
    @@     @@                                   @@     @@       
     @@@@@@  @                                 @  @@@@@@                  
             @             @@@@@@@             @                   
              @          @@       @@          @                          
              @          @         @          @                 
               @       @@           @@       @               
                @@@@@@@               @@@@@@@                ⠀⠀⠀⠀⠀⠀⠀⠀                                                                    

                  
  '''
newRainbow = rainbow_text('>>> Pokemon Final Protocol (Story Mode) <<<\n\n')


def storymode(scene, storyinventory, coins, storyyouPokemon_NAME, storyyourPokemon_DATA, battle, settingsAndcodes, Red, Green, Orange, Blue, Purple, Cyan, White, black, Black, red, green, yellow, blue, magenta, cyan, white, bold, italic, darken, resetlol, is_storymode, storyNAME, TRAINERLEVEL, storyBagpack):
      def LevelUp(TRAINERLEVELx):
        TRAINERLEVELx += 1
        if TRAINERLEVELx > 10 and 'UPGRADE1' not in storyBagpack:
          TRAINERLEVELx = 10
          print2(blue+f"I have reached the max level I can at this time."+"\n")
        if TRAINERLEVELx > 20 and 'UPGRADE2' not in storyBagpack:
          TRAINERLEVELx = 20
          print2(blue+f"I have reached the max level I can at this time."+"\n")
        if TRAINERLEVELx > 30 and 'UPGRADE3' not in storyBagpack:
          TRAINERLEVELx = 30
          print2(blue+f"I have reached the max level I can at this time."+"\n")
        if TRAINERLEVELx > 40 and 'UPGRADE4' not in storyBagpack:
          TRAINERLEVELx = 40
          print2(blue+f"I have reached the max level I can at this time."+"\n")
        if TRAINERLEVELx > 50 and 'UPGRADE5' not in storyBagpack:
          TRAINERLEVELx = 50
          print2(blue+f"I have reached the max level I can at this time."+"\n")
        if TRAINERLEVELx > 60 and 'UPGRADE6' not in storyBagpack:
          TRAINERLEVELx = 60
          print2(blue+f"I have reached the max level I can at this time."+"\n")
        if TRAINERLEVELx > 70 and 'UPGRADE7' not in storyBagpack:
          TRAINERLEVELx = 70
          print2(blue+f"I have reached the max level I can at this time."+"\n")
        if TRAINERLEVELx > 80 and 'UPGRADE8' not in storyBagpack:
          TRAINERLEVELx = 80
          print2(blue+f"I have reached the max level I can at this time."+"\n")
        return TRAINERLEVELx
  
      def showStuff():
        print2(resetlol+ f"Coins: {coins}")
        print2(resetlol+ f"Trainer Lvl: {TRAINERLEVEL}")
        print2(f"Current Pokemon: {storyyouPokemon_NAME}\n")
        
      def PokemonPC():
        clear()
        global MODE
        MODE = 0
        # Create a list of all Pokémon names
        pokemon_list = list(Pokemon.keys())
  
        # Initialize the page index
        page_index = 0
  
        while True:
            # Clear the screen or terminal
            clear()
  
            if settingsAndcodes['ASCII'] == True:
                if settingsAndcodes['GigachadMode'] == False:
                    print(gengar)
                else:
                    print(newRainbow)
            elif settingsAndcodes['ASCII'] == False:
                pass
  
  
            
            print2(blue + f"{magenta+'Nurse Joy'+resetlol}: Welcome to the Pokemon Center! All your Pokemon are stored here and healed 24/7 thanks to the IPG! Please choose your Pokemon Companion:{resetlol} \n\n")
            # Calculate the start and end indices for the current page
            start_index = page_index * 5
  
            # Display Pokémon for the current page
            if MODE == 3 or MODE == 4:
              end_index = min((page_index + 1) * len(pokemon_list), len(pokemon_list))
            elif MODE == 0 or MODE == 23:
              end_index = min((page_index + 1) *len(pokemon_list), len(pokemon_list))
  
            time.sleep(1)
            for i in range(start_index, end_index):
  
                pokemon_name = pokemon_list[i]
                info = Pokemon[pokemon_name]
  
                if pokemon_name in storyinventory:
                  if Pokemon[pokemon_name]['name'] == storyyouPokemon_NAME:
                    price_text = Blue  + "Equipped" + resetlol
                  else:
                    price_text = cyan + "Equip" + resetlol
                else:
                    price = info['price']
                    if coins < price:
                      price_text = f"{red}{price} coins{resetlol}"  
                    elif pokemon_name in storyinventory:
                      price_text = f"{blue}{price} coins{resetlol}"
                    else:
                      price_text = f"{green}{price} coins{resetlol}"
                power = f"Power: {info['power']}{resetlol}"
                hp = f"HP: {info['max_hp']}{resetlol}"
                speed = f"Speed: {info['speed']}{resetlol}"
                pokemon_type = f"Type: {info['type']}{resetlol}"
                pokemon_ability = f"Ability: {info['ability']}{resetlol}"
  
                if MODE == 1:
                  print(f"> [{i + 1}] {info['name']}\n   - {power}\n   - {hp}\n   - {speed}\n   - {pokemon_type}\n   - {pokemon_ability}\n")
                elif MODE == 0:
                  if pokemon_name in storyinventory:
                    print(f"> [{i + 1}] {info['name']} ({info['secondname']})\n")
                elif MODE == 23:
                  if pokemon_name in storyinventory:
                    print(f"> [{i + 1}] {info['name']}\n   - {power}\n   - {hp}\n   - {speed}\n   - {pokemon_type}\n   - {pokemon_ability}\n")
                elif MODE == 2:
                  print(f"> [{i + 1}] {info['name']} ({price_text})\n")
                elif MODE == 3:
                  if 'coins' in price_text:
                      print(f"> [{i + 1}] {info['name']}\n")
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
              choice = input("\n>> [#] Select Pokemon | [e] Exit: ")
  
            elif MODE == 4:
              choice = input("\n>> [#] Select Pokemon | [e] Exit: ")
            elif MODE == 0:
              choice = input("\n>> [#] Select Pokemon | [e] Exit: ")
  
  

            if choice.lower() == "e":
              clear()
              refreshpageascii()
              return False
              break
            elif choice == '#':
              print2(blue + "Please select a Pokemon via the number associated with it!")
  
            elif choice.isdigit():
                # Check if the user selected a Pokémon to buy
                selected_index = int(choice) - 1
                if 0 <= selected_index < len(pokemon_list):
                    selected_pokemon = pokemon_list[selected_index]
                    if selected_pokemon in storyinventory:
                          price = Pokemon[selected_pokemon]["price"]
                          clear()
                          price = Pokemon[selected_pokemon]['price']
                          if coins < price:
                            price_text = f"{red}{price} coins{resetlol}"
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
                                  print(gengar)
                              else:
                                  print(newRainbow)
                          elif settingsAndcodes['ASCII'] == False:
                              pass
                          print(f"> {Pokemon[selected_pokemon]['name']} ({secondNAME})\n   - {power}\n   - {hp}\n   - {speed}\n   - {pokemon_type}\n   - {pokemon_ability}{resetlol}\n\n")
                          if selected_pokemon not in storyinventory:
                            pass
                          else:
                            lol431 = input(white+'\n>> [Enter] To Equip: ')
                            if selected_pokemon in storyinventory:
                              MONDATA = Pokemon[selected_pokemon]
                              selectedMON = MONDATA['name']
                              print(selectedMON, MONDATA)
                              return selectedMON, MONDATA
                              break
                            break
  
            else:
                clear()
                refreshpageascii()
                return False
                break
      def refreshpageascii():
        clear()
        if settingsAndcodes['ASCII'] == True:
          if settingsAndcodes['GigachadMode'] == False:
            print(gengar)
          else:
            print(rainbow_text('>>> Pokemon Final Protocol (Story Mode) <<<\n\n'))
        elif settingsAndcodes['ASCII'] == False:
          pass
    
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

      #ALL NPCs THAT MATTER
      DEV = green+'Forgetful Dev'+resetlol 
      Unknown = red+'???'+resetlol
      Devore = yellow+'Dr. DeVore'+resetlol
      Mom = Purple+'Mom'+resetlol
      Dad = yellow+'Dad'+resetlol
      Carter = Purple+'Carter'+resetlol
      Guard = Blue+'Guard'+resetlol
      Opponent = magenta+'Opponent'+resetlol
      Davidson = green+'Davidson'+resetlol 
      clear()
      refreshpageascii()
    
      print2(blue + "Welcome to PFP Story Mode! (Type 'e' to exit)")
      if storyNAME == '':
        lol34 = input(resetlol+ "\n>>> [Enter] to start! <<<\n\n")
        if lol34 == 'e':
          return scene, storyinventory, coins, storyyouPokemon_NAME, storyyourPokemon_DATA, storyNAME, TRAINERLEVEL, storyBagpack
        clear()
      else:
        lol34 = input(resetlol+ "\n>>> [Enter] to continue! <<<\n\n")
        if lol34 == 'e':
          return scene, storyinventory, coins, storyyouPokemon_NAME, storyyourPokemon_DATA, storyNAME, TRAINERLEVEL, storyBagpack
        clear()


      while True:
        if 5==5:
          if storyNAME == '':
              
            refreshpageascii()
            while True:
              print(f'{DEV}: Beep Boop Bop, erhm, sorry what was your name again?\n\n')
              storyNAME = input('Enter your name: ')
              if storyNAME == '':
                pass
              else:
                break
  
            
            print(f'\n{DEV}: What color do you want your name to be? {resetlol}\n\n[1] {red}Red {resetlol}\n[2] {Blue}Blue {resetlol}\n[3] {Green}Green {resetlol}\n[4] {yellow}Yellow {resetlol}\n[5] {Purple}Purple {resetlol}\n[6] {galaxy_text("Galaxy")} {resetlol}\n[7] {rainbow_text("Rainbow")} {resetlol}\n[8] {black}Black {resetlol}\n[9] {red_black("Dark-Side")}')
              
  
            while True:
              color=input(f'\n\n{DEV}: Enter your choice: ')
              if color == '1':
                storyNAME = red + storyNAME + resetlol
                break
              elif color == '2':
                storyNAME = Blue + storyNAME + resetlol
                break
              elif color == '3':
                storyNAME = Green + storyNAME + resetlol
                break
              elif color == '4':
                storyNAME = yellow + storyNAME + resetlol
                break
              elif color == '5':
                storyNAME = Purple + storyNAME + resetlol
                break
              elif color == '6':
                storyNAME = galaxy_text(storyNAME)
                break
              elif color == '7':
                storyNAME = rainbow_text(storyNAME)
                break
              elif color == '8':
                storyNAME = black + storyNAME + resetlol
                break
              elif color == '9':
                storyNAME = red_black(storyNAME)
                break
              else:
                pass
  
                
            print2(f'\n{DEV}: {storyNAME}! I remember! Lets start your adventure, press enter.')
            input()
            
          if scene == 0:
            refreshpageascii()
            print2(blue+ f"{Devore}: Hey there {storyNAME}! I am the Professor of Damas Town, your home! Welcome to the facinating world of Pokémon. This world is inhabited by creatures called Pokémon! For some people, Pokémon are pets. Other use them for fights. Myself… I study Pokémon as a profession.\n")
            input()
            print2("...\n")
            input()
            print2(red+"huh?\n")
            input()
            print2(green + "You were teleported to an unknown place...\n")
            input()
            scene += 1
          if scene == 1:
            refreshpageascii()
            print2(blue+italic+f"Where am I?\n")
            input()
            print2(Red+f"{Unknown}: It seems like we have a guest here."+"\n")
            input()
            print2(Green+ f"{storyNAME}: Who are you? And where is {Devore}?"+"\n")
            input()
            print2(Red+f"{Unknown}: It is time to destroy you..."+"\n")
            input()
            print2(blue+"Oh no oh no oh no, what do I do?? Wait, it seems like I have a bag with me for some reason, lets see..."+"\n")
            input()
            scene += 1
          if scene == 2:
  
              refreshpageascii()
              print2(white+f"The Bag Contains: \n\n[1] {Pokemon['Torchic']['name']}\n[2] {Pokemon['Froakie']['name']}\n[3] {Pokemon['Bulbasaur']['name']}\n[4] {Pokemon['Pichu']['name']}\n"+"\n")
  
              while True:
                  choice = input(white+f"Please Choose A Pokemon [#]: "+"\n")
                  if choice == '1':
                    storyyouPokemon_NAME = Pokemon['Torchic']['name']
                    storyyourPokemon_DATA = Pokemon['Torchic']
                    storyinventory.append('Torchic')
                  elif choice == '2':
                    storyyouPokemon_NAME = Pokemon['Froakie']['name']
                    storyyourPokemon_DATA = Pokemon['Froakie']
                    storyinventory.append('Froakie')
                  elif choice == '3':              
                    storyyouPokemon_NAME = Pokemon['Bulbasaur']['name']
                    storyyourPokemon_DATA = Pokemon['Bulbasaur']
                    storyinventory.append('Bulbasaur')
                  elif choice == '4':
                    storyyouPokemon_NAME = Pokemon['Pichu']['name']
                    storyyourPokemon_DATA = Pokemon['Pichu']
                    storyinventory.append('Pichu')
                    
                  else:
                    continue
                  break
              print2(f"You chose {storyyouPokemon_NAME}."+"\n")
              print2(Red+f"???: Time to {italic}destroy{Red} you."+"\n")
              input()
              result,coins = battle(65658, 'Gastly', '???', storyyourPokemon_DATA, coins)
              input()
              if result == 'win trainer':
                print2(f"{Unknown}: Well done. I am still gonna trap you in my system for eternity..."+"\n")
                TRAINERLEVEL = LevelUp(TRAINERLEVEL)
                input()
              else:
                print2(f"{Unknown}: Awww, too bad! Gastly, use CURSE..."+"\n")
                input()
              scene +=1
          if scene == 3:
              refreshpageascii()
              
              
              print2(f"{storyNAME}: "+red+"AHHHHHHH!\n")
              input()
              print2(white+"Huh?\n")
              input()
            
              print2(green + f"You woke up. Seems like it was just a bad dream. Today is Trainer Day, you will get your very own starter from {Devore}{green}. You checked the clock.\n")
              input()
              print2(blue+"Phew! I woke up exactly at 9:00 AM, seems like I won't be missing the Starter Ceremony. Jeez though man, that dream was crazy."+"\n")
              input()
              print2(green + "You wake up and start brushing your teeth. You take a shower and dress up in proper attire, wear your shoes, and eat breakfast. You are all ready.\n")
              input()
              print2(green + f"{Mom}: Goodbye Honey, I will miss you so much. Stay safe out here.\n")
              print2(green + f"{Dad}: Goodbye my Champ, go conquer the world!\n")
              input()
              
              refreshpageascii()
              print2(blue+f"{storyNAME}: I will miss you guys so much, goodbye!")
              input(" \n")
              print2(green+"You left to begin your journey.")
              input(" \n")
              scene += 1
          if scene == 4:
            while True:
              refreshpageascii()
              print(blue+f"What should I do? \n\n[1] Go to Professor's lab \n[2] Go in the wild \n[3] Go to the Pokemon Center \n[4] Back to Main Menu \n")
              print2(resetlol+ f"Coins: {coins}")
              print2(resetlol+ f"Trainer Lvl: {TRAINERLEVEL}")
              print2(f"Current Pokemon: None\n")
              inputlol = input(white+f">> Enter your choice: ")
              if inputlol == '1':
                refreshpageascii()
                print2(green+f"You walk over to the {Devore}{green}'s lab and entered it.\n")
                input()
                break
              if inputlol == '2':
                refreshpageascii()
                print2(blue+f"I don't have a Pokemon yet!\n")
                input()
              if inputlol == '3':
                refreshpageascii()
                print2(blue+f"I don't have a Pokemon yet!\n")
                input()
                
              if inputlol == '4':
                break
            if inputlol == '4':
              break
            scene += 1
          if scene == 5:
            refreshpageascii()
            print2(blue+ f"{Devore}: Hey there {storyNAME}! I am the Professor of Damas Town, your home! Welcome to the facinating world of Pokémon. This world is inhabited by creatures called Pokémon! For some people, Pokémon are pets. Other use them for fights. Myself… I study Pokémon as a profession.\n")
            input()
            print2(blue+ f"{Devore}: Sigh, I know you know me and everything I said, unfortunetly the Intermultiversetic Poke Government (IPG) requires all professors to say that line, anyways, it seems like you are the one of the few trainer from this town who decided to attend, and I am proud of you.\n")
            input()
            print2(blue+ f"{Devore}: I want to make Damas Town a proud place, you are my only hope, {storyNAME}. Unfortunetly out of the 4 starters, only 2 are left! As your uncle, you are my favourite! Since it seems like no one else will be coming, you can have both!\n")
            input()
            print2(blue+ f"{Carter}: HEY WAIT FOR ME!\n")
            input()
            print2(green+f"Carter entered."+"\n")
            input()
            print2(blue+ f"{Carter}: You here? Come on I thought cowards weren't allowed to be Pokemon Trainers. Anyway, hey {Devore}, I am {Carter}. I want a starter Pokemon!\n")
            input()
            print2(blue+ f"{Devore}: {storyNAME}, you know him? I guess you are only getting one starter then. Sorry my newphew! {Carter}, you better let {storyNAME} pick a Pokemon first since he came first!\n")
            input()
            print2(blue+ f"{Carter}: UGHH. Fine!\n")
            input()
            refreshpageascii()
            print2(green+ f"You go check out the two starters avalable!\n")

            if storyyouPokemon_NAME == Pokemon['Torchic']['name']:
              urPokemon = 'Torchic'
              otherPokemon = 'Froakie'
            elif storyyouPokemon_NAME == Pokemon['Froakie']['name']:
              urPokemon = 'Froakie'
              otherPokemon = 'Bulbasaur'
            elif storyyouPokemon_NAME == Pokemon['Bulbasaur']['name']:
              urPokemon = 'Bulbasaur'
              otherPokemon = 'Torchic'
            elif storyyouPokemon_NAME == Pokemon['Pichu']['name']:
              urPokemon = 'Pichu'
              otherPokemon = 'Bulbasaur'
            
            print2(blue+ f"It seems there is a {Pokemon[urPokemon]['name']}{blue} and a {Pokemon[otherPokemon]['name']}{blue}. Oh my goodness, they are the same Pokemon from my dream. Lets choose {Pokemon[urPokemon]['name']}{blue} since he saved my life in my dream!\n")
            print2(green + f"You got a {urPokemon}{green}! He really seems to be attached to you and loves you very much. Perhaps you two were meant to be!\n")
            input()
            print2(blue+ f"{Carter}: {otherPokemon}, you are mine!\n")
            print2(green + f"Carter got a {otherPokemon}{green}! Their personality match a lot!\n")
            input()
            refreshpageascii()
            print2(blue+ f"{Devore}: Well guys, let me tell you a few things about the laws in the Intermultiversetic Poke Government (IPG), unfortuently they have determined that you can only hold 1 Pokemon at a time and to catch a wild Pokemon, you have to buy a Pokeball via coins during the battle (every thing works digitally now and the pokeball is teleported to you). This was due to severe technological malfunctions after the galactic attack that took place, which killed millions of Pokemon that were in the PC and the trainer's party, and which caused the economy to collapse. \n\n{Devore}: However there are also laws they made which benifit us a lot, such as auto healing Pokemon after battle, no more levels (replaced by a trainer level), how Pokemon Centers physically hold your Pokemon rather than digitally, and through a new 4th dimensional technology which teleports them safely accross the universes. It is said that the attack was from several unions of Pokemon Multiverses who aim to take over existance. But anyway, lets lighten up the mood a little bit. I will give both of you 100 coins to get started!"+"\n")
            input()
            coins += 100
            print2(green+"You recieved 100 coins!"+"\n")
            input()
            scene += 1
            
          if scene == 6:
            
            while True:
                refreshpageascii()
                print(blue+f"What should I do? \n\n[1] Say Bye to Dr.Devore & Carter and Leave.\n[2] Battle Carter before you leave  \n[3] Back to Main Menu \n")
                showStuff()
                inputlol = input(white+f">> Enter your choice: ")
                if inputlol == '1':
                  refreshpageascii()
                  print2(blue+ f"{Carter}: Hey, you are not leaving without battling me first!\n")
                  print2(f"{Devore}: SIGH! Not the second time today!"+"\n")
                  input()
                  break
                if inputlol == '2':
                  refreshpageascii()
                  print2(blue+ f"{storyNAME}: Hey {Carter}! Lets have a battle, it will our first time!\n")
                  print2(blue+ f"{Carter}: I will crush you! Lets GO.\n")
                  print2(f"{Devore}: SIGH! Not the second time today!"+"\n")
                  input()
                  break
                if inputlol == '3':
                  break
            if inputlol == '3':
              break
            
            result,coins = battle(1, otherPokemon, 'Carter', storyyourPokemon_DATA, coins)
            input()
            if result == 'win trainer':
              print2(f"{Carter}: NOOOOO! you got me..."+"\n")
              TRAINERLEVEL = LevelUp(TRAINERLEVEL)
              input()
              refreshpageascii()
            else:
              print2(f"{Carter}: Haha, thats what I thought."+"\n")

              input()
              refreshpageascii()
  
            print2(f"{Carter}: Well, {storyNAME}. Your not very good at this. See you later."+"\n")
            print2(green+f"Carter left."+"\n")
            input()
            print2(f"{Devore}: Anyways, that was quite the battle and definetly better than the previous two trainers that came in earlier today. {storyNAME}, dont let {Carter}'s words get to you. He clearly seems to be in an anger state by the way he acts for his age LOL! Anyways champ, I hope you and {Carter} make Damas Town proud! I have to go now to talk with your father about my ongoing legal battle with the, uhm, don't worry about it, but I believe your father will definetly help me get through this since he is the Pokelawyer in this region! But anyways thats me and my brother's business, you should head to Rocket City next, it is kind of dangerous though so be careful, good luck nephew!"+"\n")
            input()
            print2(f"{storyNAME}: Goodbye Uncle!"+"\n")
            print2(green+f"You left."+"\n")
            input()
            clear()
            scene +=1
          if scene == 7:
            while True:
              refreshpageascii()
              print(blue+f"What should I do? \n\n[1] Go to the Pokemon Center \n[2] Head to Rocket City \n[3] Back to Main Menu\n")
              showStuff()
              inputlol = input(white+f">> Enter your choice: ")
              if inputlol == '1':
                refreshpageascii()
                PokemonCenter = PokemonPC()
                if PokemonCenter != False:
                  storyyouPokemon_NAME, storyyourPokemon_DATA = PokemonCenter
              if inputlol == '2':
                refreshpageascii()
                print2(blue+f"Lets start my journey! It seems the city is in the next route, I have to go throught Route 1 first.\n")
                
                input()
                print2(green+f"Welcome to Route 1!\n")
                input()

                break
              if inputlol == '3':
                break
              
            if inputlol == '3':
                break
            scene += 1
          if scene == 8:
            while True:
              refreshpageascii()
              print(blue+f"What should I do? \n\n[1] Head to route 2\n[2] Battle trainers in route 1 \n[3] Go in the wild grass  \n[4] Go back to Damas Town\n[5] Back to Main Menu\n")
              showStuff()
              
              inputlol = input(white+f">> Enter your choice: ")
              if inputlol == '1':
                 refreshpageascii()
                 print2(green+'You entered the local route pathway.\n')
                 if TRAINERLEVEL >= 5:
                    print2(f"{Guard}: Hey I am the Local Route Guard. Seems like you meet the requirement of at least having a level of 5 in your trainer card, you may pass through! Stay safe!"+"\n")
                    input()
                   
                    print2(green+'Welcome to Route 2!')
                   
                    input()
                    if 'UPGRADE1' in storyBagpack:
                      break
                    print2(green+f'{Davidson}: Hold on!')
                    input()
                    print2(green+f'{Davidson}: {storyNAME}! I am Davidson, your federal IPG agent!\n')
                    input()
                    print2(green+f'{Davidson}: ...')
                    input()
                    print2(green+f'{Davidson}: Listen friend, I have been assigned by the IPG to come here today. We are being open about it because something is up with you.\n')
                    input()
                    print2(green+f'{storyNAME}: The hell? What are you talking about???\n')
                    input()
                    print2(green+f'{Davidson}: *Sigh*. I have to tell you from the start.\n')
                    input()
                    refreshpageascii()
                    print2(magenta+f'{Davidson}: Ever since the catastrophic galactic attack that happened, hundreds of millions died, the IPG has been spying on the citizens of the South Pokeverse, where the intruders entered from. \n')
                    input()
                    print2(green+f'{storyNAME}: And what does that have to do with me?\n')
                    input()
                    print2(magenta+f'{Davidson}: Well according to the Darkrai that IPG uses to spy the dreams of citizens, it seems like yours was the odd one out. You battled a Gastly who belonged to a trainer who was trying to kill you. Then we realized after looking through our human data that he was not of our Galacticverse Union, but from a different one.\n')
                    input()
                    print2(magenta+f'{Davidson}: We have identified him as Intruder8472, and he alone has killed a million of our citizens alone, and we have been looking for him for the past year. We are not sure of which enemy Union he belongs to, or how he got here. But it seems like you are the only person who has physically witnessed him. {storyNAME}, when you were sleeping, your body was fluctuating and was hologramic, which according to our sciences means that you were in a different dimension at that time. You were physically battling Intruder8472.\n')
                    input()
                    print2(green+f'{storyNAME}: What about my Pokemon? My starter Pokemon is the same Pokemon that was defending me in this dimension.\n')
                    input()
                    if 'Torchic' in storyinventory:
                      urPokemon = 'Torchic'
                    elif 'Froakie' in storyinventory:
                      urPokemon = 'Froakie'
                    elif 'Bulbasaur' in storyinventory:
                      urPokemon = 'Bulbasaur'
                    elif 'Pichu' in storyinventory:
                      urPokemon = 'Pichu'
                    print2(magenta+f'{Davidson}: And thats the main reason I am here today. {storyNAME}, unfortunely I am required to confiscate your {urPokemon}. He is not from this dimension, it seems like all the starter Pokemons that were given in DAMAS Town are not from our Galacticverse. Our authorities have just now detained Dr. Devore, your uncle, as a suspect and have confiscated the Pokemon of the 3 other trainers today that came from Damas, including someone you may know, Carter.\n')
                    input()
                   
                    break
                   
                 else:
                   print2(f"{Guard}: Hey I am the Local Route Guard. Unfortunely I cannot let you go through, you must reach a trainer level of 5 to pass! Battle some more trainers in the previous route!"+"\n")
                   input()
                   print2(green+'You left.')
                   input()
              if inputlol == '2':
                refreshpageascii()
                route1Poke = ["Pidgey", "Pidgeotto", "Ratata", "Eevee"]
                print2(blue+f"...\n")
                selected = random.choice(route1Poke)
                input()
                result,coins = battle(1, selected, False, storyyourPokemon_DATA, coins)
                input()
                if result == 'win trainer':
                  print2(f"{Opponent}: Wow, can't believe I lost! Good job though."+"\n")
                  TRAINERLEVEL = LevelUp(TRAINERLEVEL)
                  input()
                  refreshpageascii()
                else:
                  print2(f"{Opponent}: Better luck next time!"+"\n")

                  input()
                  refreshpageascii()
              if inputlol == '3':
                refreshpageascii()
                route1Wild = ["Pidgey", "Pidgeotto", "Ratata", "Eevee"]
                print2(blue+f"...\n")
                selected = random.choice(route1Wild)
                input()
                result,coins = battle(1, selected, Pokemon[selected]['name'], storyyourPokemon_DATA, coins)
                
                input()
                TRAINERLEVEL = LevelUp(TRAINERLEVEL) if result == "win wild" else TRAINERLEVEL
              if inputlol == '4':
                scene -= 1
                break
              if inputlol == '5':
                break

            if inputlol == '4':
                continue
            if inputlol == '5':
                break
            scene += 1
            if 'UPGRADE1' in storyBagpack:
              scene += 1
      
          if scene == 9:
            refreshpageascii()
            while True:
              print2(blue+f"Should I comply with Davidson's order? \n\n[1] Yes\n[2] No \n[3] Back to Main Menu\n")
              showStuff()
              xik = input('Enter your choice: ')

              if xik == '1':
                refreshpageascii()
                print2(green+f'{Davidson}: You have made a good choice today. Here I will give you 250 coins for being a good citizen and this starter Pokemon is gonna help us a lot in our research. {storyNAME}, do expect us to ask you questions later on and be sure to report to us if you see/feel something unexpected or one of our identified intruders. Thank you for your complaiance today.')
                input()
                if 'Torchic' in storyinventory:
                  urPokemon = 'Torchic'
                elif 'Froakie' in storyinventory:
                  urPokemon = 'Froakie'
                elif 'Bulbasaur' in storyinventory:
                  urPokemon = 'Bulbasaur'
                elif 'Pichu' in storyinventory:
                  urPokemon = 'Pichu'
                print2(red+f"You lost {urPokemon}!"+"\n")
                print2(green+"You recieved 250 coins!"+"\n")
                coins += 250
                storyBagpack.append('UPGRADE1')
                if urPokemon == 'Torchic':
                  storyinventory.remove('Torchic')
                  kkkkk = 'Combusken'
                  storyinventory.append('Combusken')
                  storyyouPokemon_NAME = Pokemon['Combusken']['name']
                  storyyouPokemon_DATA = Pokemon['Combusken']
                if urPokemon == 'Froakie':
                  storyinventory.remove('Froakie')
                  storyinventory.append('Frogadier')
                  kkkkk = 'Frogadier'
                  
                  storyyouPokemon_NAME = Pokemon['Frogadier']['name']
                  storyyouPokemon_DATA = Pokemon['Frogadier']
                if urPokemon == 'Pichu':
                  storyinventory.remove('Pichu')
                  storyinventory.append('Pikachu')
                  kkkkk = 'Pikachu'
                  storyyouPokemon_NAME = Pokemon['Pikachu']['name']
                  storyyouPokemon_DATA = Pokemon['Pikachu']
                if urPokemon == 'Bulbasaur':
                  storyinventory.remove('Bulbasaur')
                  storyinventory.append('Ivysaur')
                  kkkkk = 'Ivysaur'
                  storyyouPokemon_NAME = Pokemon['Ivysaur']['name']
                  storyyouPokemon_DATA = Pokemon['Ivysaur']
                input()
                print2(green+f'{Davidson}: And as an compensation, you will recieve an evolved form of your starter Pokemon.\n')
                print2(green+f"You got {kkkkk}!"+"\n")
                print2(green+f'{Davidson}: Have a good day, {storyNAME}. Damas Town will be alright. Dont worry.')
                input()
                break
              elif xik == '2':
                refreshpageascii()
                print2(green+f'{Davidson}: *Sigh* I didnt wanna do this.')
                result,coins = battle(1, 'Zygarde - Complete', 'Davidson', storyyourPokemon_DATA, coins)
                if result == 'win trainer':
                  print2(f"{Davidson}: BRO ARE YOU HACKING? Alright listen man, just play by what happens next. JESUS man its just a game.\n"+"\n")
                  TRAINERLEVEL = LevelUp(TRAINERLEVEL)
                  input()
                  refreshpageascii()
                else:
                  print2(f"{Davidson}: Thats what I thought.\n"+"\n")

                  input()
                  refreshpageascii()
                print2(green+f'{Davidson}: You have made a poor choice today. Your Pokemon has been confiscated. {storyNAME}, do expect us to ask you questions later on and be sure to report to us if you see/feel something unexpected or one of our identified intruders. Thank you for your complaiance today.\n')
                input()
                if 'Torchic' in storyinventory:
                  urPokemon = 'Torchic'
                elif 'Froakie' in storyinventory:
                  urPokemon = 'Froakie'
                elif 'Bulbasaur' in storyinventory:
                  urPokemon = 'Bulbasaur'
                elif 'Pichu' in storyinventory:
                  urPokemon = 'Pichu'
                print2(red+f"You lost {urPokemon}!"+"\n")
                storyBagpack.append('UPGRADE1')
                if urPokemon == 'Torchic':
                  storyinventory.remove('Torchic')
                  kkkkk = 'Combusken'
                  storyinventory.append('Combusken')
                  storyyouPokemon_NAME = Pokemon['Combusken']['name']
                  storyyouPokemon_DATA = Pokemon['Combusken']
                if urPokemon == 'Froakie':
                  storyinventory.remove('Froakie')
                  storyinventory.append('Frogadier')
                  kkkkk = 'Frogadier'

                  storyyouPokemon_NAME = Pokemon['Frogadier']['name']
                  storyyouPokemon_DATA = Pokemon['Frogadier']
                if urPokemon == 'Pichu':
                  storyinventory.remove('Pichu')
                  storyinventory.append('Pikachu')
                  kkkkk = 'Pikachu'
                  storyyouPokemon_NAME = Pokemon['Pikachu']['name']
                  storyyouPokemon_DATA = Pokemon['Pikachu']
                if urPokemon == 'Bulbasaur':
                  storyinventory.remove('Bulbasaur')
                  storyinventory.append('Ivysaur')
                  kkkkk = 'Ivysaur'
                  storyyouPokemon_NAME = Pokemon['Ivysaur']['name']
                  storyyouPokemon_DATA = Pokemon['Ivysaur']
                input()
                print2(green+f'{Davidson}: And as an compensation, you will recieve an evolved form of your starter Pokemon.\n')
                print2(green+f"You got {kkkkk}!"+"\n")
                print2(green+f'{Davidson}: Have a good day, {storyNAME}. Your uncle and peers will be alright if they are truly innocent. May justice be served. Peace.\n')
                input()
                break                
              elif xik == '3':
                refreshpageascii()
                break
              else:
                refreshpageascii()
                pass
                    
            if xik == '3':
                break
            scene +=1
          if scene == 10:
             while True:
               refreshpageascii()
               print(blue+f"What should I do? \n\n[1] Head to Rocket City\n[2] Battle trainers in route 2 \n[3] Go in the wild grass  \n[4] Go back to Route 1\n[5] Back to Main Menu\n")
               showStuff()

               inputlol = input(white+f">> Enter your choice: ")
               if inputlol == '1':
                  refreshpageascii()
                  print2(green+f"Welcome to Rocket City!\n")
                  input()
                  print2(red+f"...\n")
                  input()
                  print2(red+f"...?\n")
                  input()
                  print2(green+f"You were teleported to a different dimension.\n")
                  input()
                  print2(f"{Unknown}: It seems like we meet again.\n")
                  input()  
                  print2(f"{storyNAME}: “You tried to hurt me. Send me back to my dimension and leave me alone, or Ill defend myself.\n")
                  input()
                  print2(f"{Unknown}: {storyNAME}, please calm down, I am not here to hurt you. Please hear my side of the story.\n")
                  input()
                  print2(f"{storyNAME}: How do you know my name???\n")
                  input()
                  print2(f"{Unknown}: In our universe your name is on top of your head, so we know. Plus I have seen you before. .\n")
                  input()
                  refreshpageascii()
                  print2(f"{storyNAME}: Why are you being all nice all of a sudden??? You were trying to kill me previously.\n")
                  input()
                 
               
               if inputlol == '2':
                 refreshpageascii()
                 route1Poke = ["Fletchling", "Fletchinder", "Ratata", "Mankey"]
                 print2(blue+f"...\n")
                 selected = random.choice(route1Poke)
                 input()
                 result,coins = battle(1, selected, False, storyyourPokemon_DATA, coins)
                 input()
                 if result == 'win trainer':
                   print2(f"{Opponent}: Wow, can't believe I lost! Good job though."+"\n")
                   TRAINERLEVEL = LevelUp(TRAINERLEVEL)
                   input()
                   refreshpageascii()
                 else:
                   print2(f"{Opponent}: Better luck next time!"+"\n")

                   input()
                   refreshpageascii()
               if inputlol == '3':
                 refreshpageascii()
                 route1Wild = ["Fletchling", "Fletchinder", "Ratata", "Mankey"]
                 print2(blue+f"...\n")
                 selected = random.choice(route1Wild)
                 input()
                 result,coins = battle(1, selected, Pokemon[selected]['name'], storyyourPokemon_DATA, coins)
                 input()
                 TRAINERLEVEL = LevelUp(TRAINERLEVEL) if result == "win wild" else TRAINERLEVEL
               if inputlol == '4':
                 scene -= 2
                 break
               if inputlol == '5':
                 break

             if inputlol == '4':
                 continue
             if inputlol == '5':
                 break
             scene += 1
          if scene == 11:
             while True:
               refreshpageascii()
               print(blue+f"What should I do? \n\n[1] Battle Rocket City Gym\n[2] Go to your friend Dr. Scaymore \n[3] Go to Pokemon Center\n[4] Go back to Route 1\n[5] Back to Main Menu\n")
               showStuff()

               inputlol = input(white+f">> Enter your choice: ")
               if inputlol == '1':
                  refreshpageascii()
                  print(f"{DEV}: Thats it for now. Wait for the next update!\n")
                  input()
               if inputlol == '2':
                 refreshpageascii()
                 route1Poke = ["Fletchling", "Fletchinder", "Ratata", "Mankey"]
                 print2(blue+f"...\n")
                 selected = random.choice(route1Poke)
                 input()
                 result,coins = battle(1, selected, False, storyyourPokemon_DATA, coins)
                 input()
                 if result == 'win trainer':
                   print2(f"{Opponent}: Wow, can't believe I lost! Good job though."+"\n")
                   TRAINERLEVEL = LevelUp(TRAINERLEVEL)
                   input()
                   refreshpageascii()
                 else:
                   print2(f"{Opponent}: Better luck next time!"+"\n")

                   input()
                   refreshpageascii()
               if inputlol == '3':
                 refreshpageascii()
                 route1Wild = ["Fletchling", "Fletchinder", "Ratata", "Mankey"]
                 print2(blue+f"...\n")
                 selected = random.choice(route1Wild)
                 input()
                 result,coins = battle(1, selected, Pokemon[selected]['name'], storyyourPokemon_DATA, coins)
                 input()
                 TRAINERLEVEL = LevelUp(TRAINERLEVEL) if result == "win wild" else TRAINERLEVEL
               if inputlol == '4':
                 scene -= 2
                 break
               if inputlol == '5':
                 break

             if inputlol == '4':
                 continue
             if inputlol == '5':
                 break
             scene += 1

  
    
      return scene, storyinventory, coins, storyyouPokemon_NAME, storyyourPokemon_DATA, storyNAME, TRAINERLEVEL, storyBagpack
