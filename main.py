import tkinter as tk
import requests
from PIL import ImageTk, Image
import Objects as O
import Player as P
from tkinter.ttk import Progressbar
from tkinter import Button, Tk, HORIZONTAL
from Logic import GameLogic
import Logic as L

Logic = GameLogic()

HEIGHT = 500
WIDTH = 1000
        
class Game(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(startMenu)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class startMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.frame = tk.Frame(self, height=HEIGHT, width=WIDTH).pack()

        self.menu_image = ImageTk.PhotoImage(Image.open('resources/menu.jpg'))
        self.menu_label = tk.Label(self, image=self.menu_image).place(relwidth=1, relheight=1)

        self.start_button = tk.Button(self, text='Start', font=('System', 30), command=lambda: master.switch_frame(chooseClass)).place(anchor='center', relx=.25, rely=.75)

        self.exit_button = tk.Button(self, text='Exit', font=('System', 30), command=lambda: master.destroy()).place(anchor='center', relx=.75, rely=.75)
    

class chooseClass(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.frame = tk.Frame(self, height=HEIGHT, width=WIDTH).pack()
        
        self.background_image = ImageTk.PhotoImage(Image.open('resources/class.jpg'))
        self.background_label = tk.Label(self, image=self.background_image).place(relwidth=1, relheight=1)
        
        self.class_title = tk.Label(self, text='Choose Class', font=('System',30), anchor='center').place(anchor='center', relx=.5, rely=.1)
        
        self.Hbutton = tk.Button(self, text='Hunter', font=('System', 20), command=lambda: [Logic.start(1), master.switch_frame(shopFront)]).place(anchor='center', relx=.2, rely=.85)
        self.Wbutton = tk.Button(self, text='Warlock', font=('System', 20), command=lambda: [Logic.start(2), master.switch_frame(shopFront)]).place(anchor='center', relx=.5, rely=.85)
        self.Tbutton = tk.Button(self, text='Titan', font=('System', 20), command=lambda: [Logic.start(3), master.switch_frame(shopFront)]).place(anchor='center', relx=.8, rely=.85)
        
        self.hunter_image = ImageTk.PhotoImage(Image.open('resources/hunter.jpg'))
        self.hunter_label = tk.Label(self, image=self.hunter_image).place(anchor='center',relx=.2, rely=.5)
        
        self.warlock_image = ImageTk.PhotoImage(Image.open('resources/warlock.jpg'))
        self.warlock_label = tk.Label(self, image=self.warlock_image).place(anchor='center',relx=.5, rely=.5)
        
        self.titan_image = ImageTk.PhotoImage(Image.open('resources/titan.jpg'))
        self.titan_label = tk.Label(self, image=self.titan_image).place(anchor='center',relx=.8, rely=.5)

class shopFront(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.frame = tk.Frame(self, height=HEIGHT, width=WIDTH).pack()
        
        self.background_image = ImageTk.PhotoImage(Image.open('resources/class.jpg'))
        self.background_label = tk.Label(self, image=self.background_image).place(relwidth=1, relheight=1)
        
        self.shop_title = tk.Label(self, text='Shop', font=('System', 30), anchor='center').place(anchor='center', relx=.5, rely=.1)
        
        self.exitButton = tk.Button(self, text='Exit', font=('System', 15), command= lambda: master.switch_frame(fight)).place(anchor='center', relx=.5, rely=.25)
        
        self.Weaponbutton = tk.Button(self, text='Weapons', font=('System', 20), command=lambda: [master.switch_frame(shopWeapon)]).place(anchor='center',relx=.15, rely=.85)
        self.Armourbutton = tk.Button(self, text='Armour', font=('System', 20), command=lambda: [master.switch_frame(shopArmour)]).place(anchor='center',relx=.5, rely=.85)
        self.Ammobutton = tk.Button(self, text='Ammo', font=('System', 20), command=lambda: [master.switch_frame(shopAmmo)]).place(anchor='center',relx=.8, rely=.85)
        
        self.weapon_image = ImageTk.PhotoImage(Image.open('resources/weapon.png'))
        self.weapon_label = tk.Label(self, image=self.weapon_image).place(anchor='center',relx=.15, rely=.55, height=180, width=180)
        
        self.armour_image = ImageTk.PhotoImage(Image.open('resources/armour.png'))
        self.armour_label = tk.Label(self, image=self.armour_image).place(anchor='center',relx=.5, rely=.55, height=180, width=180)
        
        self.ammo_image = ImageTk.PhotoImage(Image.open('resources/ammo.png'))
        self.ammo_label = tk.Label(self, image=self.ammo_image).place(anchor='center',relx=.8, rely=.55, height=180, width=180)
        

class shopWeapon(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.w={}
        self.wi={}
        self.money = tk.Label(self,text='Money: $' + str(P.money), font=('System', 20)).grid(row=0, column=2, padx=10, pady=10)
        self.exit_button = tk.Button(self, text="Exit", font=('System', 20), command = lambda: master.switch_frame(shopFront)).grid(row=0, column=3, padx=10, pady=10)
        for i in range(len(O.weaponList)):
            self.weaponPointer = O.weaponList[i]
            self.w['name_label' + str(i)] = tk.Label(self, text=self.weaponPointer['name'], font=('System', 20)).grid(row=1, column=i, padx=10, pady=10)
            self.wi['weapon_image' + str(i)] = ImageTk.PhotoImage(Image.open(self.weaponPointer['img']))
            self.w['image_label' + str(i)] = tk.Label(self, image = self.wi['weapon_image' + str(i)]).grid(row=2,column=i)
            self.w['damage_label' + str(i)] = tk.Label(self, text='Damage: ' + str(self.weaponPointer['damage']), font=('System', 20)).grid(row=3, column=i, padx=10, pady=10)
            self.w['mag_label' + str(i)] = tk.Label(self, text='Mag Size: ' + str(self.weaponPointer['magSize']), font=('System', 20)).grid(row=4, column=i, padx=10, pady=10)
            self.w['price_label' + str(i)] = tk.Label(self, text='Price: $' + str(self.weaponPointer['price']),font=('System', 20)).grid(row=5, column=i, padx=10, pady=10)
            self.w['owned_label' + str(i)] = tk.Label(self, text='Owned: ' + str(self.weaponPointer['owned']), font=('System', 20)).grid(row=6, column=i, padx=10, pady=10)
            if self.weaponPointer['owned'] == False:
                self.w['buy_button' + str(i)] = tk.Button(self, text='Buy', font=('System', 20), command= lambda i=i: [Logic.shop(2,i), master.switch_frame(shopWeapon)]).grid(row=7, column=i)
 
class shopArmour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.a={}
        self.ai={}
        self.money = tk.Label(self,text='Money: $' + str(P.money), font=('System', 20)).grid(row=0, column=1, padx=10, pady=10)
        self.exit_button = tk.Button(self, text="Exit", font=('System', 20), command = lambda: master.switch_frame(shopFront)).grid(row=0, column=2, padx=10, pady=10)
        for i in range(len(O.armourList)):
            self.armourPointer = O.armourList[i]
            self.a['name_label' + str(i)] = tk.Label(self, text=self.armourPointer['name'], font=('System', 20)).grid(row=1, column=i, padx=10, pady=10)
            self.ai['armour_image' + str(i)] = ImageTk.PhotoImage(Image.open(self.armourPointer['img']))
            self.a['image_label' + str(i)] = tk.Label(self, image = self.ai['armour_image' + str(i)]).grid(row=2,column=i)
            self.a['health_label' + str(i)] = tk.Label(self, text='HP Added: ' + str(self.armourPointer['hpAdded']), font=('System', 20)).grid(row=3, column=i, padx=10, pady=10)
            self.a['price_label' + str(i)] = tk.Label(self, text='Price: $' + str(self.armourPointer['price']),font=('System', 20)).grid(row=5, column=i, padx=10, pady=10)
            self.a['owned_label' + str(i)] = tk.Label(self, text='Owned: ' + str(self.armourPointer['owned']), font=('System', 20)).grid(row=6, column=i, padx=10, pady=10)
            if self.armourPointer['owned'] == False:
                self.a['buy_button' + str(i)] = tk.Button(self, text='Buy', font=('System', 20), command= lambda i=i: [Logic.shop(1,i), master.switch_frame(shopArmour)]).grid(row=7, column=i)

        
class shopAmmo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.am={}
        self.ami={}
        self.money = tk.Label(self,text='Money: $' + str(P.money), font=('System', 20)).grid(row=0, column=(len(P.weapons)//2), padx=10, pady=10)
        self.exit_button = tk.Button(self, text="Exit", font=('System', 20), command = lambda: master.switch_frame(shopFront)).grid(row=0, column=(len(P.weapons)//2)+1, padx=10, pady=10)
        
        for i in range(len(P.weapons)):
            self.ammoPointer = P.weapons[i]
            self.am['name_label' + str(i)] = tk.Label(self, text=self.ammoPointer['name'], font=('System', 20)).grid(row=1, column=i, padx=10, pady=10)
            self.ami['weapon_image' + str(i)] = ImageTk.PhotoImage(Image.open(self.ammoPointer['img']))
            self.am['image_label' + str(i)] = tk.Label(self, image = self.ami['weapon_image' + str(i)]).grid(row=2,column=i)
            self.am['ammo_label' + str(i)] = tk.Label(self, text='Ammo Left: ' + str(self.ammoPointer['ammo']), font=('System', 20)).grid(row=3, column=i, padx=10, pady=10)
            self.am['mag_label' + str(i)] = tk.Label(self, text='Mag Size: ' + str(self.ammoPointer['magSize']), font=('System', 20)).grid(row=4, column=i, padx=10, pady=10)
            self.am['price_label' + str(i)] = tk.Label(self, text='Price: $' + str((self.ammoPointer['magSize'] - self.ammoPointer['ammo']) * self.ammoPointer['ammoPrice']),font=('System', 20)).grid(row=5, column=i, padx=10, pady=10)
            if self.ammoPointer['ammo'] != self.ammoPointer['magSize']:
                self.am['buy_button' + str(i)] = tk.Button(self, text='Reload', font=('System', 20), command= lambda i=i: [Logic.shop(3,i), master.switch_frame(shopAmmo)]).grid(row=6, column=i)

class weaponSwitch(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.am={}
        self.ami={}
        self.exit_button = tk.Button(self, text="Exit", font=('System', 20), command = lambda: master.switch_frame(fight)).grid(row=0, column=(len(P.weapons)//2), padx=10, pady=10)
        
        for i in range(len(P.weapons)):
            self.ammoPointer = P.weapons[i]
            self.am['name_label' + str(i)] = tk.Label(self, text=self.ammoPointer['name'], font=('System', 20)).grid(row=1, column=i, padx=10, pady=10)
            self.ami['weapon_image' + str(i)] = ImageTk.PhotoImage(Image.open(self.ammoPointer['img']))
            self.am['image_label' + str(i)] = tk.Label(self, image = self.ami['weapon_image' + str(i)]).grid(row=2,column=i)
            self.am['ammo_label' + str(i)] = tk.Label(self, text='Ammo Left: ' + str(self.ammoPointer['ammo']), font=('System', 20)).grid(row=3, column=i, padx=10, pady=10)
            self.am['damage_label' + str(i)] = tk.Label(self, text='Damage: ' + str(self.ammoPointer['damage']), font=('System', 20)).grid(row=4, column=i, padx=10, pady=10)
            self.am['chose_button' + str(i)] = tk.Button(self, text='Select', font=('System', 20), command= lambda i=i: [fight.selectWeapon(self, i), master.switch_frame(fight)]).grid(row=6, column=i)
class Won(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.frame = tk.Frame(self, height=HEIGHT, width=WIDTH).pack()
        
        self.background_image = ImageTk.PhotoImage(Image.open('resources/class.jpg'))
        self.background_label = tk.Label(self, image=self.background_image).place(relwidth=1, relheight=1)
        
        winLabel = tk.Label(self, text='You Have Beat the Game!!', font=('system', 40)).place(anchor='center', relx=.5, rely=.3)
        Restart = tk.Button(self, text='Restart', font=('system', 20), command=lambda: master.switch_frame(startMenu)).place(anchor='center', relx=.25, rely=.6)
        Exit = tk.Button(self, text='Exit', font=('system', 20), command = lambda: master.destroy()).place(anchor='center', relx=.75, rely=.6)
class Lost(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.frame = tk.Frame(self, height=HEIGHT, width=WIDTH).pack()
        
        self.background_image = ImageTk.PhotoImage(Image.open('resources/class.jpg'))
        self.background_label = tk.Label(self, image=self.background_image).place(relwidth=1, relheight=1)
        
        loseLabel = tk.Label(self, text='You Have Been Defeated :(', font=('system', 40)).place(anchor='center', relx=.5, rely=.3)
        Restart = tk.Button(self, text='Try Again', font=('system', 20), command=lambda: master.switch_frame(startMenu)).place(anchor='center', relx=.25, rely=.6)
        Exit = tk.Button(self, text='Exit', font=('system', 20), command = lambda: master.destroy()).place(anchor='center', relx=.75, rely=.6)
   
class fight(tk.Frame):
    
    def selectWeapon(self, choice):
        O.WeaponChoice = choice
    def useSuper(self):
        O.SuperChoice = True
        Logic.battle(O.WeaponChoice, O.SuperChoice, O.e)
        O.SuperChoice = False
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.frame = tk.Frame(self, height=HEIGHT, width=WIDTH).pack()
        
        self.background_image = ImageTk.PhotoImage(Image.open('resources/class.jpg'))
        self.background_label = tk.Label(self, image=self.background_image).place(relwidth=1, relheight=1)
        enemy = O.enemiesList[O.e]
        Logic.checkHealth()
        if O.Win == True:
            winLabel = tk.Label(self, text='You Have Beat the Game!!', font=('system', 40)).place(anchor='center', relx=.5, rely=.3)
            Exit = tk.Button(self, text='Exit', font=('system', 20), fg='red',command = lambda: master.destroy()).place(anchor='center', relx=.5, rely=.6)
        elif O.Lose == True:
            loseLabel = tk.Label(self, text='You Have Been Defeated :(', font=('system', 40)).place(anchor='center', relx=.5, rely=.3)
            Exit = tk.Button(self, text='Exit', font=('system', 20), fg='red', command = lambda: master.destroy()).place(anchor='center', relx=.5, rely=.6)
        else:
         
            self.currentWeapon = P.weapons[O.WeaponChoice]
            if enemy['health'] <= 0:
                nextEnemy = tk.Label(self,text=enemy['name'] + ' Defeated!', font=('system', 15), fg='red').place(anchor='center', relx=.5, rely=.85)
                continueButtin = tk.Button(self,text='Continue', font=('system',15), fg='red', command=lambda: master.switch_frame(fight)).place(anchor='center', relx=.5, rely=.95)
            if self.currentWeapon['ammo'] <=0:
                empty = tk.Label(self, text='Out of Ammo', font=('system', 15), fg='red').place(anchor='center', relx=.5, rely=.9)
            eName = tk.Label(self, text=enemy['name'], font=('system', 20)).place(anchor='center', relx=.75, rely=.1)
            pName = tk.Label(self, text=P.type, font=('system', 20)).place(anchor='center', relx=.25, rely=.1)
            self.eImage = ImageTk.PhotoImage(Image.open(str(enemy['img'])))
            eImageLabel = tk.Label(self, image=self.eImage).place(anchor='center', relx=.75, rely=.4, width=200, height=200)
            self.pImage = ImageTk.PhotoImage(Image.open(str(P.image)))
            pImageLabel =  tk.Label(self, image=self.pImage).place(anchor='center', relx=.25, rely=.4)
            eHealthbar = Progressbar(self, orient = 'horizontal', length = enemy['maxhp'], maximum = enemy['maxhp'], mode = 'determinate', value = enemy['health']).place(anchor='center', relx=.75, rely=.7)
            pHealthbar = Progressbar(self, orient = 'horizontal', length = P.maxHp, maximum = P.maxHp, mode = 'determinate', value = P.hp).place(anchor='center', relx=.25, rely=.7)
            eDamage = tk.Label(self, text='Damage: ' + str(enemy['damage']), font=('system', 20)).place(anchor='center', relx=.75, rely=.8)
            pWeapon = tk.Label(self, text='Weapon: ' + str(self.currentWeapon['name']), font=('system', 20)).place(anchor='center', relx=.25, rely=.8)
            shopButton = tk.Button(self, text='Shop', font=('system', 20), command = lambda: master.switch_frame(shopFront)).place(anchor='center', relx=.5, rely=.7)
            attackButton = tk.Button(self, text='Attack', font=('system', 20), command = lambda: [Logic.battle(O.WeaponChoice, O.SuperChoice, O.e), master.switch_frame(fight)]).place(anchor='center', relx=.5, rely=.2)
            chargeLabel = tk.Label(self, text='Super Charge', font=('system', 10)).place(anchor='center', relx=.5, rely=.35)
            chargeBar = Progressbar(self, orient = 'horizontal', length = 100, maximum = 100, mode = 'determinate', value = P.superCharge).place(anchor='center', relx=.5, rely=.4)
            changeWeapon = tk.Button(self, text='Change Weapon', font=('system', 15), command=lambda: master.switch_frame(weaponSwitch)).place(anchor='center', relx=.25, rely=.9)
            if P.crit == True:
                crit= tk.Label(self, text='CRIT!', font=('system', 20), fg='red').place(anchor='center', relx=.75, rely=.9)
                P.crit = False
            if P.superCharge >= 100:
                useSuper = tk.Button(self, text='Use Super', font=('system', 20), command = lambda: [self.useSuper(), master.switch_frame(fight)]).place(anchor='center', relx=.5, rely=.5)
            Logic.checkHealth()
     
                        

if __name__ == "__main__":
    app = Game()
    app.mainloop()
        