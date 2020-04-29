import Objects as O

class PlayerData(object):
    def __init__(self):
        PlayerData.type = ''
        PlayerData.weapons = []
        PlayerData.super = []
        PlayerData.armour = []
        PlayerData.maxHp = 0
        PlayerData.hp = 0
        PlayerData.exp = 0
        PlayerData.money = 0
        PlayerData.critChance = 0
        PlayerData.superCharge = 0
        
    def Hunter(self):
        PlayerData.type = 'Hunter'
        PlayerData.weapons = [O.AceofSpades]
        O.AceofSpades['owned'] = True
        PlayerData.super = [O.goldenGun]
        PlayerData.armour = []
        PlayerData.maxHp = 100
        PlayerData.hp = 100
        PlayerData.exp = 0
        PlayerData.money = 0
        PlayerData.critChance = 45
        PlayerData.superCharge = 0
 
    def Warlock(self):
        PlayerData.type = 'Warlock'
        PlayerData.weapons = [O.HardLight]
        O.HardLight['owned'] = True
        PlayerData.super = [O.novaBomb]
        PlayerData.armour = []
        PlayerData.maxHp = 130
        PlayerData.hp = 130
        PlayerData.exp = 0
        PlayerData.money = 0
        PlayerData.critChance = 20
        PlayerData.superCharge = 0

    def Titan(self):
        PlayerData.type = 'Titan'
        PlayerData.weapons=[O.Recluse]
        O.Recluse['owned'] = True
        PlayerData.super=[O.hammerofSol]
        PlayerData.armour = []
        PlayerData.maxHp = 200
        PlayerData.hp = 200
        PlayerData.exp = 0
        PlayerData.money = 0
        PlayerData.critChance = 10
        PlayerData.superCharge = 0 