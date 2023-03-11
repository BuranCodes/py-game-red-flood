#-----Red Flood-----#
import logging
import os
import platform
import random

"""
Version v.0.1 - Alpha Build
- Fixed the order of how the combat should go and added ---- to tell the player to keep going
- Healing system, score and as well time record will be implemented later.
- Player's dialogue got recently impemented
- This is a preview version, the changes will be made later.

Version v.0.2 - Early Build
- Fixed the loop and value bugs
- Included day counting, simple economy system, and as well victory counter to emphasize the goal of collecting as many points as possible
- Fixed the logging bug where it failed to write, and as well added a new line everytime to make it readable.
- Removed unnecessary variables that were already used!

Removed inappropriate wordings, revised text.

Version v.0.3 - Revisit
- Multi-platform support
- Fixed bug where the exhaustion would go below zero.
"""

global cls # To be used in any function.


#------Logging Config
logging.basicConfig(filename='playerData.log', level=logging.DEBUG, format="%(asctime)s %(message)s")
#------Logging Config

if (platform.system() == "Linux"):
    cls = lambda: os.system("clear")
elif (platform.system() == "Windows"):
    cls = lambda: os.system("cls")
elif (platform.system() == "Darwin"):
    cls = lambda: os.system("clear")





playerHurt = ("Ouch!", "Oof!", "Oops!", "Ugh!", "Agh!", "Ack!", "Hnghh!", "Ngh!", "Augh!", "Ah!", "Ough!", "Ow!")

playerRelieved = ("Ah...", "That was close...", "Damn...", "I need to calm...", "I should take rest...")

playerCombat = ("Gah!", "Ura!", "Charge!", "Die, you filthy!", "Eeeee!", "Uuuuu!", "Die!")

playerIntroduction = ("""It's been 50 years since the Great Holy War that ravaged the entire once-the-united Empire. Plague, famine, mass exodus and 
wars have struck since then, and you are one of the member of a surviving clan, a kinship, a family. One day, you take the sword, 
bow and armor to set yourself in a quest, the great test of time against you.""")

playerCharacter = ("A chronically alcoholic veteran knight", "A distressed, attractive nekomimi witch", "A young dragon adventurer", "A king of the fallen kingdom")

enemyFight = ("You have approached an enemy in the cave. What will you do? ", "You have approached a flying beast circling over you. What will you do?",
"You have approached an enemy in the valley. What will you do?", "You have stubbed your toe against a sleeping beast, and it's waking up right now. What will you do?",
"You have encountered a hideous being in the river. What will you do?", "You have encountered a DND-addicted mage in the basement. What will you do?")

enemyWin = ("You have won!", "You achieved victory!", "You slapped your enemy hard!", "Your heroism just got bigger, the enemy got killed!",
"You killed a bastard!", "You have asserted your dominance against the poor enemy!", "You have stabbed an enemy succesfully!", "The enemy died from shock and blood loss!")

enemyDefeat = ("You have been vanquished...", "You died of septic shock after getting poisoned...",
"You have died of severe bleeding...", "You contracted Ligma and died on spot soon...", "You have been decimated...", "You got killed on spot...")

enemyEscape = ("You have escaped the enemy!", "You distracted the enemy and managed to escape!", "You taunted enemy and got away with it!",
"You knocked your enemy out unconsciously and managed to escape!", "Another creature has crossed in, and you managed to escape!")


def MainMenu():
    global playerName
    global inGameDays
    global playerVictoryRounds
    global playerScore
    global playerExhaust
    global playerCoins
    global playerHP
    global playerAlive
    cls()
    print("Welcome to Red Flood! This is a console based combat game where you have to fight as long as possible, until you succumb in the end!")
    while True:
        try:    
            MenuInput = int(input("What would you like to do? \n1 Play\n2 About\n3 Scoreboard\n4 Leave\n"))
            if MenuInput == 1:
                cls()
                playerName = input("All right, let's play! Tell us your name! ")
                print("Alright, your name is {}! Let's go...".format(playerName))
                playerName = playerName
                input()
                cls()
                inGameDays = 0
                playerVictoryRounds = 0
                playerScore = 0
                playerExhaust = 0
                float(playerExhaust)
                playerCoins = 0
                playerAlive = True
                playerHP = 20 # data here!!!

                gamePlay()
            elif MenuInput == 2:
                cls()
                print("""\n\n#----------------------------------------------------
#   Name of the program: Red Flood
#   Purpose: Console-based game, user has to survive longest.
#
#   Author: BuranCodes
#
#   Official date of creation: 06/04/2021
#   ------------Free to use--------------
#   Created with the idea of getting used to programming by
#   being involved in different basic fields, to educate
#   myself, and with the strong determination, as well
#   many thanks to my friends for assisting me :]
#----------------------------------------------------\n\n""")
                input()
                cls()
            elif MenuInput == 3:
                cls()
                print("Data will be loaded...\n")
                f = open("playerData.log", "r")
                print(f.read())
                f.close
            elif MenuInput == 4:
                cls()
                print("Bye!")
                quit(0)
        except ValueError:
            cls()
            print("Your choice has to be just a number, try again!")

# why do I keep spamming these

def gameEnd(): # Game over
    if playerVictoryRounds >= 50:
        print("Well done, you have stood against the test of time! Your recorded name is {}, the score {}, last recorded exhaustion {} and longest time reached is {} days.\n".format(playerName, playerScore, round(playerExhaust, 2), inGameDays))
        input()
        cls()
        logging.debug(" Recorded name is {}, the score {}, last recorded exhaustion {} and longest time reached is {} days.\n".format(playerName, playerScore, playerExhaust, inGameDays))
    else:
        randomDeath = random.choice(enemyDefeat)
        print(randomDeath)
        print("You have met a terrible end, haven't you? Your recorded name is {}, the score {}, last recorded exhaustion {} and longest time reached is {} days.\n".format(playerName, playerScore, playerExhaust, inGameDays))
        input()
        cls()
        logging.debug(" Recorded name is {}, the score {}, last recorded exhaustion {} and longest time reached is {} days.\n".format(playerName, playerScore, playerExhaust, inGameDays))

def gamePlay(): # Actual game interface
    global playerExhaust
    global inGameDays
    global playerVictoryRounds

    print(playerIntroduction)
    input("\n Continue...")

    cls()
    print("All right!")
    while playerAlive == True:
        playerExhaust = round(playerExhaust, 2)
        inGameDays += 1
        if playerExhaust < 0:
            playerExhaust = 0
        if playerVictoryRounds >= 50:
            break
        try:
            print("\nYou have currently {} HP and {} exhaustion, {} coins. It's been {} days. Please pick the choice:\n1 Fight\n2 Tavern\n3 Shop".format(playerHP, playerExhaust, playerCoins, inGameDays))
            playerMove = int(input())

            if playerMove == 1:
                if playerExhaust >= 20:
                    print("You are too exhausted to fight!")

                elif playerExhaust < 20:
                    playerVictoryRounds += 1
                    cls()
                    print("\n\n")
                    playerFight()

            elif playerMove == 2:
                playerVictoryRounds += 1
                cls()
                print("\n\n")
                playerTavern()

            elif playerMove == 3:
                playerVictoryRounds += 1
                cls()
                print ("\n\n")
                playerShop()

        except ValueError:
            cls()
            print("Please try using a number only!")
    if playerAlive == False:
        gameEnd()
    if playerVictoryRounds >= 50:
        gameEnd()

def playerFight(): # Fighting an enemy, and returning to gameEnd() if you lose
    global playerCoins
    global playerHP
    global playerExhaust
    global playerAlive
    global playerScore

    enemyHP = random.randint(1,10)
    playerScore += 1

    print(random.choice(enemyFight), "The enemy has {}HP.".format(enemyHP))
    while enemyHP > 0:
        if playerHP <= 0:
            playerAlive = not playerAlive
            print("It's over.")
            break

        print("What will you do? Fight, Flee, Heal, Spell --- You have {} HP and {} exhaustion.".format(playerHP, playerExhaust))

        playerChoice = input()
        playerChoice = playerChoice.lower()

        if playerChoice == "fight":
            playerDamage = random.randint(0,10)
            enemyHP -= playerDamage
            if enemyHP<0: enemyHP=0
            print("You dealt {} damage against the enemy! The enemy lost {} HP! {}".format(playerDamage, playerDamage, random.choice(playerCombat)))
            print("The enemy has currently {} HP left.".format(enemyHP))

            if enemyHP == 0:
                print(random.choice(enemyWin), random.choice(playerRelieved))
                enemyLoot = random.randint(1,10)
                playerCoins += enemyLoot
                enemyScoreGive = random.randint(1,5)
                playerScore += enemyScoreGive
                print("You gained {} coins and {} score!".format(enemyLoot, enemyScoreGive))
                break

            enemyDamage = random.randint(0,10)
            print("Enemy dealt {} damage against you! You lost {} HP! {}".format(enemyDamage, enemyDamage, random.choice(playerHurt)))
            playerHP -= enemyDamage
            playerExhaust += enemyDamage / 2
            if playerHP<0: playerHP=0
            print("\n")
        if playerChoice == "flee":
            playerFleeChance = random.randint(0,1)

            if playerFleeChance == 0:
                print("You failed to flee!")
                enemyDamage = random.randint(0,10)
                print("Enemy dealt {} damage against you! You lost {} HP! {}".format(enemyDamage, enemyDamage, random.choice(playerHurt)))
                playerHP -= enemyDamage
                playerExhaust += enemyDamage / 2
                if playerHP<0: playerHP=0
                print("\n")

            elif playerFleeChance == 1:
                print(random.choice(enemyEscape), "1 score gained!")
                playerScore += 1
                break

        if playerChoice == "heal":
            playerHealAmount = random.randint(0,5)
            playerHP += playerHealAmount
            healScore = random.randint(1,3)
            playerScore += healScore
            print("You manage to get away and healed with {} HP, totalling it to {} HP! You received {} score for succesful heal.".format(playerHealAmount, playerHP, healScore))

        if playerChoice == "spell":
            playerSpellChance = random.randint(0,1)

            if playerSpellChance == 0:
                print("You fail to cast a spell!")
                enemyDamage = random.randint(0,10)
                print("Enemy dealt {} damage against you! You lost {} HP! {}".format(enemyDamage, enemyDamage, random.choice(playerHurt)))
                playerHP -= enemyDamage
                playerExhaust += enemyDamage / 2
                if playerHP<0: playerHP=0
                print("\n")

            elif playerSpellChance == 1:
                spellScore = random.randint(1,3)
                print("You manage to cast a spell, thus killing the enemy! You gained {} score.".format(spellScore))
                playerSpellDamage = 100
                enemyHP -= playerSpellDamage
                if enemyHP<0: enemyHP=0
                


def playerTavern(): # Healing, exhaustion and score system
    global playerExhaust
    global playerHP
    global playerScore
    global inGameDays
    print("Welcome to the tavern! You can heal here for a significant amount of HP, as well reduce exhaust!")
    playerTavernChoice = input("Will you take the rest? Y/N ")
    playerTavernChoice = playerTavernChoice.lower()
    if playerTavernChoice == "y" or playerTavernChoice == "yes":
        print("You are now taking a break.")
        inGameDays += 1
        playerExhaust -= random.uniform(3.0,6.0)
        playerExhaust = round(playerExhaust, 2)
        playerHP += random.randint(2,8)
        playerScore += 1
        if playerExhaust < 0: playerExhaust=0
        print("You have took a rest, your current exhaustion is {}, you have {} HP and gained 1 score, totalling to {}! You can leave now.".format(playerExhaust, playerHP, playerScore))
    elif playerTavernChoice == "n" or playerTavernChoice == "no":
        playerExhaust -= random.uniform(1.0,2.0)
        playerExhaust = round(playerExhaust, 2)
        playerHP += random.randint(0,2)
        playerScore += 1
        if playerExhaust < 0: playerExhaust=0
        print("You had a short break. Your current exhaustion is {}, you have {} HP and gained 1 score, totalling to {}! You can leave now.".format(playerExhaust, playerHP, playerScore))

def playerShop(): # Marketplace system
    global playerHP
    global playerCoins
    global playerExhaust
    global playerScore
    global inGameDays
    print("Welcome to the shop! You can buy items to use which will help you survive longer. You have {} coins.\n".format(playerCoins))
    while True:
        try:
            print("You have {} coins.\n".format(playerCoins))
            playerShopChoice = int(input("What would you like to buy?\n1 Buy potion to drink for health [5 coins]\n2 Buy snacks to reduce exhaustion [3 coins]\n3 Buy a relic [10 coins]\n4 Leave\n"))

            if playerShopChoice == 1:
                if playerCoins >= 5:
                    playerCoins -= 5
                    playerHP += 10
                    print("You have bought a potion and drank it. Your current HP is now {}!\n".format(playerHP))

                elif playerCoins < 5:
                    print("You do not have enough coins! You have only {} left!\n".format(playerCoins))

            elif playerShopChoice == 2:
                if playerCoins >= 3:
                    if playerExhaust > 0:
                        playerCoins -= 3
                        playerExhaust -= 2.5
                        if playerExhaust < 0: playerExhaust=0
                        print("You have bought a snack and ate it. Your current exhaustion is now {}!\n".format(playerExhaust))

                    elif playerExhaust <= 0:
                        print("You don't need to eat a snack, you took enough rest already! You have still {} coins left.\n".format(playerCoins))

                elif playerCoins < 3:
                    print("You do not have enough coins! You have only {} left!\n".format(playerCoins))

            elif playerShopChoice == 3:
                if playerCoins >= 10:
                    playerCoins -= 10
                    playerScore += 5
                    print("You have bought a relic and took it. Your current score is now {}!\n".format(playerScore))

                elif playerCoins < 10:
                    print("You do not have enough coins! You have only {} left!\n".format(playerCoins))

            elif playerShopChoice == 4:
                break
        except ValueError:
            print("Your choice has to be just a number, try again!\n")

MainMenu()