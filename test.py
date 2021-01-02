from text_rpg_maker import *
import random,time,json,os 

redc = "\033[0;91m"
green = "\033[0;92m"
yellowc = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
white = "\033[0;97m"
blue_back="\033[0;44m"
grey_back="\033[0;40m"

class Char:
    def __init__(self, name, hp, strenght, dex, con, intelligence, wis, cha): 
        self.name = name
        self.hp = hp
        self.str = strenght
        self.dex = dex
        self.con = con
        self.int = intelligence
        self.wis = wis
        self.cha = cha
        self.red = False

while True:
  print(blue_back+"Welcome to Text Based RPG Creator")
  input()
  print(blue+"\n What's your name traveler ?")
  namero=input("> "+white)
  os.system("clear")
  input()
  print(blue+"\n I don't remember your race what was that ?")
  print(yellowc+"  1. Ogre")
  print(yellowc+"  2. Elf")
  print(yellowc+"  3. Human")
  racero=input("> "+white)
  os.system("clear")
  if racero=="1":
      mychar = Char("Ogre", 100, 22, 9, 12, 6, 14, 5)
      break    
else:
    os.system("clear")

    if racero=="2":
     print(magenta+"What kind of elf are you ?")
     print(green+"  1. Dark Elf")
     print(green+"  2. Wood Elf")
     print(green+"  3. Grey Elf")
    elfro=input("> ")
    print(white+"")
    if elfro=="1":
        mychar = Char("Dark Elf", 100, 8, 17, 15, 19, 12, 10)
        break
    elif elfro=="2":
        mychar = Char("Wood Elf", 100, 18, 12, 14, 8, 10, 16)
        break
    elif elfro=="3":
        mychar = Char("Grey Elf", 100, 14, 13, 15, 17, 7, 10)
        break
    else:
        os.system("clear")
    if racero =="3":
        mychar = Char("Human", 100, 9, 9, 9, 9, 9, 9)
        break
    else:
        os.system("clear")
os.system("clear")

world = (mychar)

def goodstranger(character):
    print(green+"Take this HP Pot" + str(character.name) + " drunk this pot"+white)
    character.hp + 10

def wonfight(character):
    print(yellowc+"Drunk man started fight and"+grey_back+str(character.name)+yellowc+ "won the fight"+white)

rednum = randint(10, 37)
def red(character):
    if character.red == False:
        print(redc+"Someone started fight and"+grey_back+str(character.name)+redc+"lost the fight"+white)
        character.red = True
        character.hp -= rednum
    else:
        pass

    def quickgstranger(character):
        character.hp + 10

    def quickred(character):
        if character.red == False:
            print(redc+"Someone started fight and"+grey_back+str(character.name)+redc+"lost the fight"+white)
        character.red = True
        character.hp -= rednum
        pass
def quickprint(character):
    print(character.name + " " + str(character.str))

    def startgame(world):
        for i in range(0, 100):
            
            n1 = random.randint(1, 300)
            n2 = random.randint(0,1)

        event = ""
        if n1 < 283:
            if world[0].red == True or world[1].red == True:
                event = " "
            else:
                event = " "
        elif n1 < 284:
            print(blue_back+"Bandits trying to kill you! "+white)
            time.sleep(3)
            nVar = random.randint(0,10)
            nVar_1 = random.randint(1,100)
            nVar_2 = random.randint(1,100)
            if (world[0].cha + nVar_1) > (match[1].cha + nVar_2):
                varcharacter = world[0]
            else:
                varcharacter = world[1]
            if nVar > 3:
                print(blue+ str(varcharacter.name) + "Haydutlara yenildi")
                nVar_3 = random.randint(0,4)
                if nVar_3 > 1:
                    goal(varcharacter)
                else:
                    print(redc+"Haydutları yendin!"+white)
        else:
            print(redc+"Haydutlar kaçtı!"+white)

def quickworldday(match, json):

    for i in range(0, 100):
        n1 = random.randint(1,300)
        n2 = random.randint(0,1)

        if n1 < 283:
            if world[0].red == True or world[1].red == True:
                pass
            else:
                pass
        
        elif n1 < 284:
            nVar = random.randint(0,10)
            nVar_1 = random.randint(1,100)
            nVar_2 = random.randint(1,100)
            if (world[0].cha + nVar_1) > (world[1].cha + nVar_2):
                varcharacter = world[0]
            else:
                varcharacter = world[1]
            if nVar > 3:
                nVar_3 = random.randint(0,4)
                if nVar_3 > 1:
                    quickgstranger(varcharacter)
                else:
                    pass
            else:
                pass

            if n1 < 299:
                pass
            else:
                quickred(world[n2])

            print("End of the day")
            for i in json:
                for character in world:
                    if i == character.name:

                        print("congrats! " + character.name)

                        return json

print("\n"*15)
print(green+"Starting world...")
print(white+"______________________\n"+blue)
print("character name: "+character.name+yellowc)
input(white+"")
os.system("clear")
matchday(match)
#quickmatchday(match)
print(yellowc+"\n\n\nPress ENTER to continue")
input()
os.system("clear")
os.system("python main.py")
            
                



'''
save = input("World Name:")
race = game.ask_choices("Pick your race", ["Elf", "Ogre", "Human"])
game.say(race)
name = input("What's your name traveler ?:")
game.say(name)


file = open("characters.txt", "a")
file.write("[" + save + "]" + "\n")
file.write("Race:" + str(race) + "\n")
file.write("Character name:" + name + "\n")
file.write("---" + "\n")
file.close()

'''