import tkinter as tk
import requests
from Logic import GameLogic
import Logic as L
from PIL import ImageTk, Image
import Objects as O
import Player as P

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

        #self.desitny_label = tk.Label(self, text='DESTINY', font=('System', 40), anchor='n').place(relx=.38, rely=.05)

        self.start_button = tk.Button(self, text='Start', font=('System', 30), command=lambda: master.switch_frame(chooseClass)).place(relx=.2, rely=.75)

        self.exit_button = tk.Button(self, text='Exit', font=('System', 30), command=lambda: master.destroy()).place(relx=.7, rely=.75)
    

class chooseClass(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.frame = tk.Frame(self, height=HEIGHT, width=WIDTH).pack()
        
        self.background_image = ImageTk.PhotoImage(Image.open('resources/class.jpg'))
        self.background_label = tk.Label(self, image=self.background_image).place(relwidth=1, relheight=1)
        
        self.class_title = tk.Label(self, text='Choose Class', font=('System',30), anchor='center').place(relx=.37, rely=.1)
        
        self.Hbutton = tk.B1utton(self, text='Hunter', font=('System', 20), command=lambda: [Logic.start(1), master.switch_frame(shopFront)]).place(relx=.15, rely=.72)
        self.Wbutton = tk.Button(self, text='Warlock', font=('System', 20), command=lambda: [Logic.start(2), master.switch_frame(shopFront)]).place(relx=.45, rely=.72)
        self.Tbutton = tk.Button(self, text='Titan', font=('System', 20), command=lambda: [Logic.start(3), master.switch_frame(shopFront)]).place(relx=.77, rely=.72)
        
        self.hunter_image = ImageTk.PhotoImage(Image.open('resources/hunter.jpg'))
        self.hunter_label = tk.Label(self, image=self.hunter_image).place(relx=.11, rely=.3)
        
        self.warlock_image = ImageTk.PhotoImage(Image.open('resources/warlock.jpg'))
        self.warlock_label = tk.Label(self, image=self.warlock_image).place(relx=.41, rely=.3)
        
        self.titan_image = ImageTk.PhotoImage(Image.open('resources/titan.jpg'))
        self.titan_label = tk.Label(self, image=self.titan_image).place(relx=.71, rely=.3)

class shopFront(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.frame = tk.Frame(self, height=HEIGHT, width=WIDTH).pack()
        
        self.background_image = ImageTk.PhotoImage(Image.open('resources/class.jpg'))
        self.background_label = tk.Label(self, image=self.background_image).place(relwidth=1, relheight=1)
        
        self.shop_title = tk.Label(self, text='Shop', font=('System', 30), anchor='center').place(relx=.45, rely=.1)
        
        self.exitButton = tk.Button(self, text='Exit', font=('System', 15), command= lambda: master.switch_frame(fight)).place(relx=.475, rely=.25)
        
        self.Weaponbutton = tk.Button(self, text='Weapons', font=('System', 20), command=lambda: [master.switch_frame(shopWeapon)]).place(relx=.15, rely=.72)
        self.Armourbutton = tk.Button(self, text='Armour', font=('System', 20), command=lambda: [master.switch_frame(shopArmour)]).place(relx=.45, rely=.72)
        self.Ammobutton = tk.Button(self, text='Ammo', font=('System', 20), command=lambda: [master.switch_frame(shopAmmo)]).place(relx=.77, rely=.72)
        
        self.weapon_image = ImageTk.PhotoImage(Image.open('resources/weapon.png'))
        self.weapon_label = tk.Label(self, image=self.weapon_image).place(relx=.11, rely=.4)
        
        self.armour_image = ImageTk.PhotoImage(Image.open('resources/armour.png'))
        self.armour_label = tk.Label(self, image=self.armour_image).place(relx=.41, rely=.35)
        
        self.ammo_image = ImageTk.PhotoImage(Image.open('resources/ammo.png'))
        self.ammo_label = tk.Label(self, image=self.ammo_image).place(relx=.71, rely=.3)
        

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
                self.w['buy_button' + str(i)] = tk.Button(self, text='Buy', font=('System', 20), command= lambda i=i: [Logic.shop(2,i), master.switch_frame(shopFront)]).grid(row=7, column=i)
 
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
                self.a['buy_button' + str(i)] = tk.Button(self, text='Buy', font=('System', 20), command= lambda i=i: [Logic.shop(1,i), master.switch_frame(shopFront)]).grid(row=7, column=i)

        
class shopAmmo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.am={}
        self.ami={}
        self.money = tk.Label(self,text='Money: $' + str(P.money), font=('System', 20)).grid(row=0, column=len(P.weapons)//2, padx=10, pady=10)
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
                self.am['buy_button' + str(i)] = tk.Button(self, text='Reload', font=('System', 20), command= lambda i=i: [Logic.shop(3,i), master.switch_frame(shopFront)]).grid(row=6, column=i)
    
class fight(tk.Frame):
    self.selectedWeapon = -1
    self.superSelect = False

    def weaponSelect(self, weapon):
        selectedWeaopn = weapon
    def Super(self, Schoice):
        superSelect = Schoice
    def weaponPopup(self):
        popup = tk.Tk()
        f={}
        fi={}
        for i in range(len(P.weapons)):
            weaponPointer = P.weapons[i]
            f['name_label' + str(i)] = tk.Label(popup, text=weaponPointer['name'], font=('System', 20)).grid(row=1, column=i, padx=10, pady=10)
            fi['weapon_image' + str(i)] = ImageTk.PhotoImage(Image.open(weaponPointer['img']))
            f['image_label' + str(i)] = tk.Label(popup, image = fi['weapon_image' + str(i)]).grid(row=2,column=i)
            f['ammo_label' + str(i)] = tk.Label(popup, text='Ammo Left: ' + str(weaponPointer['ammo']), font=('System', 20)).grid(row=3, column=i, padx=10, pady=10)          
            f['select_button' + str(i)] = tk.Button(popup, text='Select', command=lambda i=i: self.weaponSelect(i)).grid(row=4, column=i, padx=10, pady=10)   
        popup.mainloop()
    
    def superPopup(self):
        popoup = tk.Tk()
        playerSuper = P.super[0]
        superName = tk.Label(popoup, text=playerSuper['name'], font=('system', 20)).grid(row=1, column=1)
        superImage = ImageTk.PhotoImage(Image.open(playerSuper['img']))
        ImageLabel = tk.Label(popoup, image= superImage).grid(row=2, column=1)
        yesButton = tk.Button(popoup, text='Yes', font=('system', 20), command= self.Super(True)).grid(row=3, column=1)
        noButton = tk.Button(popoup, text='No', font=('system', 20), command= self.Super(False)).grid(row=4, column=1)
        popup.mainloop()
  
           
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.frame = tk.Frame(self, height=HEIGHT, width=WIDTH).pack()
        
        self.background_image = ImageTk.PhotoImage(Image.open('resources/class.jpg'))
        self.background_label = tk.Label(self, image=self.background_image).place(relwidth=1, relheight=1)

        for e in range(len(O.enemiesList)):
            enemy = O.enemiesList[e]
            P.hp = P.maxHp
            while P.hp > 0 and enemy['health'] > 0:
                if O.superCharge >= 100:
                    self.superPopup()
                eName = tk.Label(self, text=enemy['name'], font=('system', 20)).place()
                pName = tk.Label(self, text=P.type, font=('system', 20)).place()
                eImage = ImageTk.PhotoImage(Image.open(enemy['img']))
                eImageLabel = tk.Label(self, image=eImage).place()
                pImage = ImageTk.PhotoImage(Image.open(P.image))
                pImageLabel =  tk.Label(self, image=pImage).place()
                eHealthbar = tk.Progressbar(self, orient = 'HORIZONTAL', length = 100, mode = 'determinate').place()
                pHealthbar = tk.Progressbar(self, orient = 'HORIZONTAL', length = P.maxHp, mode = 'determinate').place()
                eHealthbar['value'] = enemy['health']
                pHealthbar['value'] = P.hp
                eDamage = tk.Label(self, text='Damage: ' + enemy['damage'], font=('system', 20)).place()
                self.weaponPopup()
                Logic.battle(selectedWeapon, superSelect)
                master.switch_frame(shopFront)
            if P.hp <= 0:
                Logic.endingLost()
            Logic.endingWin()

                   
        

if __name__ == "__main__":
    app = Game()
    app.mainloop()
        