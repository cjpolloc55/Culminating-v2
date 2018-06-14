#Python: Text Based Royale
from random import randint

#item list
'''
bigLaser = 10
mediumLaser = 11
smallLaser = 12
shieldPotion = 13
healthPotion = 14
'''
#Damage Values
'''
big laser = 100dmg 
medium laser = 50dmg
small laser = 25dmg
medpack = 25 health
medicine bag = 100 health 
'''

#Location List


def locMenu():
	'''displays menu for locations'''
	print("Select a drop location")
	print("1. Togie Town")
	print("2. Stangie Skyscrapers")
	print("3. Luke's Landing")
	print("4. Kyle's Kingdom")


	

  


def itemRNG():
        ''' a function determining what items you find'''
        item = randint(10, 12)
        global dmg
        if item == 10:
                print ("--------------------------------------")
                print("You found a Big Laser!")
                
                dmg = dmg + 75


        if item == 11:
                dmg = dmg + 50
                print ("--------------------------------------")
                print("You found a Medium Laser")
                


        if item == 12:
                print ("--------------------------------------")
                print("You found a small laser")
                
                dmg = dmg + 25
def healthRng():
        global healthItem
        item = randint (1,4)
        if item == 1 or 2 or 3:
                print ("--------------------------------------")
                print ("You have found a medpack")
                healthItem = 25
        elif item == 4:
                print ("--------------------------------------")
                print ("You have found a Medicine Bag")
                healthItem = 100

def menu ():
        '''function that displays the players actions'''
        print ("Select what you would like to do")
        print ("1. Fight an enemy nearby")
        print ("2. Heal")
        print ("3. Loot")
        print ("4. Move to the next area")
  

def fightMenu ():
        ''' a function that displays your options while in a fight'''
        print ("Select what you would like to do")
        print ("1. Shoot")
        print ("2. View Health")
        print ("3. View enemy Health")
        print ("4. Run Away")
        print ("5. Heal")


backpack = []

healthItem = 0
health = 100
enemyHealth = 100
dmg = 0
for i in range(0, 1):
        locMenu()
        locChoice = input("Where we dropping boys?")


        if locChoice == "1":
                enemyCount = randint(1, 3)
                itemRNG()
                healthRng()
                print ("--------------------------------------")
                print ("Your weapon does",dmg,"damage")
                print("There are", enemyCount, "enemies around")
                print ("You can heal for",healthItem,"damage")
                print ("--------------------------------------")
        elif locChoice == "2":
                enemyCount = randint(4, 8)
                itemRNG()
                healthRng()
                print ("--------------------------------------")
                print ("Your weapon does",dmg,"damage")
                print("There are", enemyCount, "enemies around")
                print ("You can heal for",healthItem,"damage")
                print ("--------------------------------------")

        elif locChoice == "3":
                enemyCount = randint(1, 4)
                itemRNG()
                healthRng()
                print ("--------------------------------------")
                print ("Your weapon does",dmg,"damage")
                print("There are", enemyCount, "enemies around")
                print ("You can heal for",healthItem,"damage")
                print ("--------------------------------------")

        elif locChoice == "4":
                enemyCount = randint(2, 8)
                itemRNG()
                healthRng()
                print ("--------------------------------------")
                print ("Your weapon does",dmg,"damage")
                print("There are", enemyCount, "enemies around")
                print ("You can heal for",healthItem,"damage")
                print ("--------------------------------------")

while True: #Fighting Menu
        menu()
        print ("--------------------------------------")
        actChoice = input("What would you like to do?")
        if actChoice == "1":
                while True:
                        fightMenu()
                        print ("--------------------------------------")
                        fightChoice = input("What would you like to do?")
                        print ("--------------------------------------")
                        if fightChoice == "1":
                                enemyHealth = enemyHealth - dmg
                                print ("--------------------------------------")
                                print ("You did",dmg,"damage!")
                                enemyDmg = randint (25,75)
                                health = health - enemyDmg
                                print ("You have taken",enemyDmg,"damage!")
                                print ("--------------------------------------")
                        

                        elif fightChoice == "2":
                                print ("--------------------------------------")
                                print ("Your Health is",health)
                                print ("--------------------------------------")

                        elif fightChoice == "3":
                                print ("--------------------------------------")
                                print("Your enemies health is",enemyHealth)
                                print ("--------------------------------------")

                        elif fightChoice == "4":
                                success = randint (1,2)
                                if success == 2:
                                        break
        
                                elif success == 1:
                                        print ("--------------------------------------")
                                        print ("Enemy evaded!")
                                        print ("--------------------------------------")
                        elif fightChoice == "5":
                                health = health + healthItem
                                print ("--------------------------------------")
                                print ("Your health is now",health)
                                print ("--------------------------------------")
                                healthItem = healthItem - healthItem
                        if enemyHealth <= 0:
                                print ("--------------------------------------")
                                print ("You killed him")
                                enemyCount = enemyCount - 1
                                enemyHealth = 100 
                                print ("There are",enemyCount,"enemies remaining the the area")
                                print ("--------------------------------------")
                                break
                        if health <= 0:
                                print ("--------------------------------------")
                                print ("You have died!")
                                print ("--------------------------------------")
                                print ("Game Over!")
                                quit ()
                                                
                                        
                    

  
  
