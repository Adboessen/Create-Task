import Objects as O
import Player as P
import random

class GameLogic(object):
    def __init__(self):
        GameLogic.purchase = False
    def start(self, classChoice):
        #sets starting values
        # for player data based on class
        if classChoice == 1:
            P.type = 'Hunter'
            P.image = 'resources/Hunter.jpg'
            P.weapons = [O.AceofSpades]
            O.AceofSpades['owned'] = True
            P.super = [O.goldenGun]
            P.armour = []
            P.maxHp = 100
            P.hp = 100
            P.exp = 0
            P.money = 1000
            P.critChance = 30
            P.superCharge = 100
        elif classChoice == 2:
            P.type = 'Warlock'
            P.image = 'resources/Warlock.jpg'
            P.weapons = [O.HardLight]
            O.HardLight['owned'] = True
            P.super = [O.novaBomb]
            P.armour = []
            P.maxHp = 130
            P.hp = 130
            P.exp = 0
            P.money = 0
            P.critChance = 20
            P.superCharge = 0
        elif classChoice == 3:
            P.type = 'Titan'
            P.image = 'resources/Titan.jpg'
            P.weapons=[O.Recluse]
            O.Recluse['owned'] = True
            P.super=[O.hammerofSol]
            P.armour = []
            P.maxHp = 200
            P.hp = 200
            P.exp = 0
            P.money = 0
            P.critChance = 10
            P.superCharge = 0        
    
    def shop(self, shopChoice1, shopChoice2):
       
        if shopChoice1 == 1:
           
            GameLogic.purchase = False
            armourPointer = O.armourList[(shopChoice2)]   
            if P.money >= armourPointer['price'] and armourPointer['owned'] == False:
                P.armour.append(armourPointer)
                armourPointer['owned'] = True
                P.hp += armourPointer['hpAdded']
                P.money -= armourPointer['price']
                GameLogic.purchase = True
                         
        elif shopChoice1 == 2:
            
            weaponPointer = O.weaponList[(shopChoice2)]
            if P.money >= weaponPointer['price'] and weaponPointer['owned'] == False:
                P.weapons.append(weaponPointer)
                weaponPointer['owned'] = True
                P.money -= weaponPointer['price']        
            
        elif shopChoice1 == 3:
           
            ammoPointer = P.weapons[(shopChoice2)]
            if P.money > ((ammoPointer['magSize'] - ammoPointer['ammo']) * ammoPointer['ammoPrice']) and ammoPointer['ammo'] < ammoPointer['magSize']:
                P.money -= ((ammoPointer['magSize'] - ammoPointer['ammo']) * ammoPointer['ammoPrice'])
                while ammoPointer['magSize'] > ammoPointer['ammo']:
                    ammoPointer['ammo'] += 1
                
            
    def battle(self, weaponChoice, superChoice, enemy):
       
        currentEnemy = O.enemiesList[enemy]
        #P.hp = P.maxHp
        playerSuper = P.super[0]
           
        if superChoice == True:
            for i in range(int(playerSuper['strength'])):
                currentEnemy['health'] -= playerSuper['damage']
            P.superCharge = 0
        
        elif superChoice == False:           
                     
            selectedWeapon = P.weapons[weaponChoice]
            if selectedWeapon['ammo'] > 0:
                #deals damage based on crit or not
                P.crit = False
                critRandom = random.randint(1,100)
                if critRandom <= P.critChance:
                    P.crit = True
                    currentEnemy['health'] -= (selectedWeapon['damage'] * 1.5)
                        # print("CRIT!!! You dealt " + str((selectedWeapon['damage'] * 1.5)) + " damage")
                    selectedWeapon['ammo'] -= 1
                        #gain money for damage done
                    P.money += (selectedWeapon['damage'] * 10)
                        #super charged by damage
                    P.superCharge += (selectedWeapon['damage'] + .5)
                    P.hp -= currentEnemy['damage']
                else:   
                    currentEnemy['health'] -= selectedWeapon['damage']
                        # print("You dealt " + str(selectedWeapon['damage']) + " damage")
                    selectedWeapon['ammo'] -= 1
                        #gain money for damage done
                    P.money += (selectedWeapon['damage'] * 10)
                        #super charged by damage
                    P.superCharge += (selectedWeapon['damage'] + .5)
                    P.hp -= currentEnemy['damage']
    
    def checkHealth(self):
        currentEnemy = O.enemiesList[O.e]
        if currentEnemy['health'] <= 0:
            O.e += 1
            P.hp = P.maxHp
        if P.hp <= 0:
            O.Lose = True
        if P.hp > 0 and O.e >= 4:
            O.Win = True
                         
 