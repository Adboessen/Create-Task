import tkinter as tk
import requests
from Logic import GameLogic
from PIL import ImageTk, Image
import Objects
import Player

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
        
        self.Hbutton = tk.Button(self, text='Hunter', font=('System', 20), command=lambda: [Logic.start('1'), master.switch_frame(shopFront)]).place(relx=.15, rely=.72)
        self.Wbutton = tk.Button(self, text='Warlock', font=('System', 20), command=lambda: [Logic.start('2'), master.switch_frame(shopFront)]).place(relx=.45, rely=.72)
        self.Tbutton = tk.Button(self, text='Titan', font=('System', 20), command=lambda: [Logic.start('3'), master.switch_frame(shopFront)]).place(relx=.77, rely=.72)
        
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
        
        self.Weaponbutton = tk.Button(self, text='Weapons', font=('System', 20), command=lambda: [Logic.start('1'), master.switch_frame(shopFront)]).place(relx=.15, rely=.72)
        self.Armourbutton = tk.Button(self, text='Armour', font=('System', 20), command=lambda: [Logic.start('2'), master.switch_frame(shopFront)]).place(relx=.45, rely=.72)
        self.Ammobutton = tk.Button(self, text='Ammo', font=('System', 20), command=lambda: [Logic.start('3'), master.switch_frame(shopFront)]).place(relx=.77, rely=.72)
        
        self.weapon_image = ImageTk.PhotoImage(Image.open('resources/weapon.png'))
        self.weapon_label = tk.Label(self, image=self.weapon_image).place(relx=.11, rely=.4)
        
        self.armour_image = ImageTk.PhotoImage(Image.open('resources/armour.png'))
        self.armour_label = tk.Label(self, image=self.armour_image).place(relx=.41, rely=.35)
        
        self.ammo_image = ImageTk.PhotoImage(Image.open('resources/ammo.png'))
        self.ammo_label = tk.Label(self, image=self.ammo_image).place(relx=.71, rely=.3)
        

class shopWeapon(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        
class shopFArmour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        
class shopAmmo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

class fight(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self, master)
        self.master = master

if __name__ == "__main__":
    app = Game()
    app.mainloop()
        