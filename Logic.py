import Objects as O
import Player as P
import random
class GameLogic(object):
    # def __init__(self):
    #     self.run()
    def start(self, classChoice):
        # print(f'''
        #       Welcome Gaurdian. Climb your way to the top. Good Luck
        #       ''')
        # P.name = str(input("Enter your name: "))
        # print("Hello " + P.name)
        # classChoice = int(input(f'''
        #         Choose Class:
        #         (1) Hunter
        #         (2) Warlock
        #         (3) Titan
        #         Enter Choice: '''))
        #checks if input is out of range
        # while classChoice > 3 or classChoice < 1:
        #     print("Input out of range")
        #     classChoice = int(input(f'''
        #         Choose Class:
        #         (1) Hunter
        #         (2) Warlock
        #         (3) Titan
        #         Enter Choice: '''))
        #sets starting values
        # for player data based on class
        if classChoice == 1:
            P.Hunter()
        elif classChoice == 2:
            P.Warlock()
        elif classChoice == 3:
            P.Titan()
    
    def shop(self, shopChoice1, shopChoice2):
        # shopChoice = int(input(f'''
        #                 -----SHOP-----
        #                 Money: ${O.money}
        #                 (1) Buy Armour
        #                 (2) Buy Weapons
        #                 (3) Reload Weapon
        #                 (4) Exit
        #                 Enter Choice: '''))
        if shopChoice1 == 1:
            # print(f'''
            #             -----ARMOUR-----''')
            #prints all armour
            # for i in range(len(O.armourList)):
            #     armourPointer = O.armourList[i]
            #     print(f'''                        ({i + 1}) [{armourPointer['name']}] ${armourPointer['price']}''')
            # armourChoice = int(input("Enter Number: "))
            # #checks if choice is valid
            # while armourChoice > len(O.armourList) or armourChoice < 1:
            #     print("Input is out of range. Enter new choice")
            #     armourChoice = int(input("Enter Number: "))
            #gets selected armour info and uses it to do stuff
            armourPointer = O.armourList[(shopChoice2 - 1)]   
            if O.money >= armourPointer['price'] and armourPointer['owned'] == False:
                O.armour.append(armourPointer)
                armourPointer['owned'] = True
                O.hp += armourPointer['hpAdded']
                O.money -= armourPointer['price']
                #print("You purchased " + armourPointer['name'])
                return 'Purchase Successful'
            else:
                #print("Not enough money or already owned")
                return 'Not enough money or already owned'
                        
        elif shopChoice1 == 2:
            # print(f'''
            #             -----WEAPONS-----''')
            # #prints all weapons
            # for i in range(len(O.weaponList)):
            #     weaponPointer = O.weaponList[i]
            #     print(f'''                        ({i + 1}) [{weaponPointer['name']}] ${weaponPointer['price']}''')                   
            # weaponChoice = int(input("Enter Number: "))
            # #checks if choice is valid
            # while weaponChoice > len(O.weaponList) or weaponChoice < 1:
            #     print("Input is out of range. Enter new choice")
            #     weaponChoice = int(input("Enter Number: ")) 
            #gets chosen weapon info and does more stuff
            weaponPointer = O.weaponList[(shopChoice2 - 1)]
            if O.money >= weaponPointer['price'] and weaponPointer['owned'] == False:
                O.weapons.append(weaponPointer)
                weaponPointer['owned'] = True
                O.money -= weaponPointer['price']
                #print("You purchased " + armourPointer['name'])
                return 'Purchase Successful'
            else:
                #print("Not enough money or already owned")
                return 'Not enough money or already owned'
            
        elif shopChoice1 == 3:
            # print("Choose Weapon")
            # #lists all owned weapons
            # for i in range(len(O.weapons)):
            #     ammoPointer = O.weapons[i]
            #     print(f'''({i + 1}) [{ammoPointer['name']}] Ammo left: {ammoPointer['ammo']}''')
            # ammoChoice = int(input("Enter Number: "))
            # #checks if input is valid
            # while ammoChoice > len(O.weapons) or ammoChoice < 1:
            #     print("Input is out of range. Enter new choice")
            #     ammoChoice = int(input("Enter Number: "))  
            #gets weapons chosen and refills the magazine
            ammoPointer = O.weapons[(shopChoice2 - 1)]
            if O.money > ((ammoPointer['magSize'] - ammoPointer['ammo']) * ammoPointer['ammoPrice']) and ammoPointer['ammo'] < ammoPointer['magSize']:
                O.money -= ((ammoPointer['magSize'] - ammoPointer['ammo']) * ammoPointer['ammoPrice'])
                while ammoPointer['magSize'] > ammoPointer['ammo']:
                    ammoPointer['ammo'] += 1
                #print("Magazine Filled")
                return 'Magazine Filled'
            else:
                #print("Not enough money or mag full")
                return 'Not enough money or mag full'
        else:
            return 'Exiting Shop'
                
            
    def battle(self, weaponChoice, superChoice):
        # print("ENTERING BATTLE")
        # print(f'''
        #             HOW TO PLAY
        # You and an enemy takes turn dealing damage
        # After each turn you get access to the shop
        # Defeat all 4 enemies and win the game
        # ''')
        for e in range(len(O.enemiesList)):
            enemy = O.enemiesList[e]
            O.hp = O.maxHp
            print("NEW ENEMY: " + enemy['name'])
            #loops battle sequence until enemy or player dies
            while O.hp > 0 and enemy['health'] > 0:
                self.shop()
                #choose weapon to use
                print(f'''
                      CHOOSE WEAPON FOR ATTACK''')
                for i in range(len(O.weapons)):
                    weaponPointer = O.weapons[i]
                    print(f'''
                      ({i + 1}) [{weaponPointer['name']}] Damage: {weaponPointer['damage']} Ammo: {weaponPointer['ammo']}''')
                weaponChoice = int(input("Enter Number: "))
                #checks if input is valid
                while weaponChoice > len(O.weapons) or weaponChoice < 1:
                    print("Input is out of range. Enter new choice")
                    weaponChoice = int(input("Enter Number: "))
                    
                     
                selectedWeapon = O.weapons[(weaponChoice - 1)]
                if selectedWeapon['ammo'] > 0:
                #deals damage based on crit or not
                    critRandom = random.randint(1,100)
                    print("")
                    if critRandom <= O.critChance:
                        enemy['health'] -= (selectedWeapon['damage'] * 1.5)
                        # print("CRIT!!! You dealt " + str((selectedWeapon['damage'] * 1.5)) + " damage")
                        selectedWeapon['ammo'] -= 1
                        #gain money for damage done
                        O.money += (selectedWeapon['damage'] * 10)
                        #super charged by damage
                        O.superCharge += (selectedWeapon['damage'] + .5)
                    else:   
                        enemy['health'] -= selectedWeapon['damage']
                        # print("You dealt " + str(selectedWeapon['damage']) + " damage")
                        selectedWeapon['ammo'] -= 1
                        #gain money for damage done
                        O.money += (selectedWeapon['damage'] * 10)
                        #super charged by damage
                        O.superCharge += (selectedWeapon['damage'] + .5)
                else:
                    # print("Out of ammo")
                    return 'out of ammo'
                
                #uses super if charge is full
                if O.superCharge >= 100:
                    playerSuper = O.super[i]
                    # superChoice = int(input(f'''
                    #         {playerSuper['name']} is charged
                    #         (1) Use Super 
                    #         (2) Keep Super
                    #         Enter Choice: '''))
                    if superChoice == 1:
                        for i in range(int(playerSuper['strength'])):
                            #print("Super dealt " + str(playerSuper['damage']))
                            enemy['health'] -= playerSuper['damage']
                        O.superCharge = 0
                #damaged by enemy
                O.hp -= enemy['damage']
                #print("You took " + str(enemy['damage']) + " damage")
                #print ui of player and enemy
                # print(f'''
                #       [{self.playerName}]            VS.          [{enemy['name']}]
                #       Weapon: {selectedWeapon['name']}            Damage: {enemy['damage']}
                #       HP: {O.hp}                            HP: {enemy['health']}
                #       Super Charge: {O.superCharge}/100
                #       Money: ${O.money}
                #       ''')
            #if player is dead go to losing
            if O.hp <= 0:
                self.endingLost()
        #wins if all enemies have been defeated
        self.endingWin()
        
    def endingWin(self):
        print("You have beat the game")
    
    def endingLost(self):
        print("You have lost the game")
        
    def run(self):
        self.start()
        self.battle()
 