import tkinter as tk
import requests
from Logic import GameLogic
import Logic as L
from PIL import ImageTk, Image
import Objects as O
from Player import PlayerData

Logic = GameLogic()
P = PlayerData()

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

        self.desitny_label = tk.Label(self, text='DESTINY', font=('System', 40), anchor='n').place(relx=.38, rely=.05)

        self.start_button = tk.Button(self, text='Start', font=('System', 30), command=lambda: master.switch_frame(chooseClass)).place(relx=.2, rely=.75)

        self.exit_button = tk.Button(self, text='Exit', font=('System', 30), command=lambda: master.destroy()).place(relx=.7, rely=.75)
    

class chooseClass(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.frame = tk.Frame(self, height=HEIGHT, width=WIDTH).pack()
        
        self.background_image = ImageTk.PhotoImage(Image.open('resources/class.jpg'))
        self.background_label = tk.Label(self, image=self.background_image).place(relwidth=1, relheight=1)
        
        self.class_title = tk.Label(self, text='Choose Class', font=('System',30), anchor='center').place(relx=.37, rely=.1)
        
        self.Hbutton = tk.Button(self, text='Hunter', font=('System', 20), command=lambda: [Logic.start(1), master.switch_frame(shopFront)]).place(relx=.15, rely=.72)
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
        self.money = tk.Label(self,text='Money: $' + str(P.money), font=('System', 30)).grid(row=0, column=2, padx=10, pady=10)
        self.exit_button = tk.Button(self, text="Exit", font=('System', 30), command = lambda: master.switch_frame(shopFront)).grid(row=0, column=3, padx=10, pady=10)
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
                self.w['buy_button' + str(i)] = tk.Button(self, text='Buy', font=('System', 20), command=lambda: Logic.shop(2,i)).grid(row=7, column=i)
            
class shopArmour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.frame = tk.Frame(self, height=HEIGHT, width=WIDTH).pack()
        
        self.background_image = ImageTk.PhotoImage(Image.open('resources/class.jpg'))
        self.background_label = tk.Label(self, image=self.background_image).place(relwidth=1, relheight=1)
        
        self.weaponFrame = tk.Frame(self, height=HEIGHT*.75, width=WIDTH*.75).place(anchor='c',relx=0.5,rely=0.5)

        
class shopAmmo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.frame = tk.Frame(self, height=HEIGHT, width=WIDTH).pack()
        
        self.background_image = ImageTk.PhotoImage(Image.open('resources/class.jpg'))
        self.background_label = tk.Label(self, image=self.background_image).place(relwidth=1, relheight=1)


class fight(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)


if __name__ == "__main__":
    app = Game()
    app.mainloop()
        