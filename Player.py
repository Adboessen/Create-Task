import Objects as O

type = ''
weapons = []
super = []
armour = []
maxHp = 0
hp = 0
exp = 0
money = 0
critChance = 0
superCharge = 0

def Hunter(self):
    type = 'Hunter'
    weapons = [O.AceofSpades]
    super = [O.goldenGun]
    armour = []
    maxHp = 100
    hp = 100
    exp = 0
    money = 0
    critChance = 45
    superCharge = 0
    
def Warlock(self):
    type = 'Warlock'
    weapons = [O.HardLight]
    super = [O.novaBomb]
    armour = []
    maxHp = 130
    hp = 130
    exp = 0
    money = 0
    critChance = 20
    superCharge = 0
    
def Titan(self):
    type = 'Titan'
    weapons=[O.Recluse]
    super=[O.hammerofSol]
    armour = []
    maxHp = 200
    hp = 200
    exp = 0
    money = 0
    critChance = 10
    superCharge = 0 