# =============================================================================
# #########from tkinter import *
# #########import sqlite3 as sq3
# #########
# #########acno = None
# #########name = None
# #########amnt = None
# #########
# #########def fetch(acno):
# #########    conn = sq3.connect("users.db")
# #########    c = conn.cursor()
# #########    result = c.execute('''SELECT pin,name,bal FROM user WHERE acno=?''', (acno,)).fetchone()
# #########    conn.close()
# #########    return result
# #########    
# ########
# ##################################################################################################################################################################
# ##################################################################################################################################################################
# ########class startScreen(Frame):
# ########    def __init__(self, master=None):
# ########        super().__init__(master)
# ########        self.pack()
# ########        self.welcome()
# ########
# ########    def welcome(self):
# ########        self.l1 = Label(root, text="Account Number", borderwidth=2, relief="groove", bg="cyan", font="arial 18")
# ########        self.l1.config(height=1, width=14)
# ########        self.l1.place(x=40, y=70)
# ########        self.e1 = Entry(root, width=10, font="arial 18")
# ########        self.e1.place(x=245, y=70)
# ########        self.l2 = Label(root, text="Enter 4 digit pin", borderwidth=2, relief="groove", bg="cyan", font="arial 18")
# ########        self.l2.config(height=1, width=14)
# ########        self.l2.place(x=40, y=110)
# ########        self.e2 = Entry(root, width=10, font="arial 18")
# ########        self.e2.place(x=245, y=110)
# ########        self.b1 = Button(root, text="Submit", font="arial 14", bg="yellow", fg="red", command=self.verify)
# ########        self.b1.place(x=303, y=170)
# ########
# ########    def verify(self):
# ########        global acno, name, amnt
# ########        try:
# ########            self.l0.place_forget()
# ########        except AttributeError:
# ########            pass
# ########        try:
# ########            pin = fetch(self.e1.get())[0]
# ########        except TypeError:
# ########            self.l0 = Label(root, text="Invalid Account Number!", font="arial 15", fg="red")
# ########            self.l0.place(x=40, y=250)
# ########            self.e1.delete(0, 'end')
# ########            self.e2.delete(0, 'end')
# ########        else:
# ########            if self.e2.get() == str(pin):
# ########                acno = self.e1.get()
# ########                name = fetch(self.e1.get())[1]
# ########                amnt = fetch(self.e1.get())[2]
# ########                self.l1.place_forget()
# ########                self.l2.place_forget()
# ########                self.e1.place_forget()
# ########                self.e2.place_forget()
# ########                self.b1.place_forget()
# ########                mainMenu(master=root)
# ########            else:
# ########                self.e1.delete(0, 'end')
# ########                self.e2.delete(0, 'end')
# ########                self.l0 = Label(root, text="Invalid password!", font="arial 15", fg="red")
# ########                self.l0.place(x=40, y=250)
# #######                
# #######
# #######
# ##################################################################################################################################################################
# ##################################################################################################################################################################
# #######class mainMenu(Frame):
# #######    def __init__(self, master=None):
# #######        super().__init__(master)
# #######        self.pack()
# #######        self.menu()
# #######
# #######    def menu(self):
# #######        self.l1 = Label(root, text="Main Menu", borderwidth=4, relief="groove", bg="spring green", font="arial 15")
# #######        self.l1.place(x=150, y=30)
# #######        self.b1 = Button(root, text="Balance Inquiry", height=2, width=20,font="arial 9", bg="misty rose", relief="ridge", command=self.f1)
# #######        self.b1.place(x=45, y=90)
# #######        self.b2 = Button(root, text="Deposit", height=2, width=20, font="arial 9", bg="misty rose", relief="ridge", command=self.f2)
# #######        self.b2.place(x=220, y=90)
# #######        self.b3 = Button(root, text="Withdrawal", height=2, width=20, font="arial 9", bg="misty rose", relief="ridge", command=self.f3)
# #######        self.b3.place(x=45, y=160)
# #######        self.b4 = Button(root, text="Pin Change", height=2, width=20, font="arial 9", bg="misty rose", relief="ridge", command=self.f4)
# #######        self.b4.place(x=220, y=160)
# #######        self.b5 = Button(root, text="Exit", height=2, width=20, font="arial 9", bg="misty rose", relief="ridge", command=self.f5)
# #######        self.b5.place(x=45, y=230)
# #######        self.l2 = Label(root, text="Welcome: "+name, font="arial 13", fg="red")
# #######        self.l2.place(x=0, y=0)
# #######
# #######    def unpack(self):
# #######        self.l1.place_forget()
# #######        self.l2.place_forget()
# #######        self.b1.place_forget()
# #######        self.b2.place_forget()
# #######        self.b3.place_forget()
# #######        self.b4.place_forget()
# #######        self.b5.place_forget()
# #######
# #######    def f1(self):
# #######        self.unpack()
# #######        balance(master=root)
# #######    
# #######    def f2(self):
# #######        self.unpack()
# #######        deposit(master=root)
# #######    
# #######    def f3(self):
# #######        self.unpack()
# #######        withdraw(master=root)
# #######
# #######    def f4(self):
# #######        self.unpack()
# #######        newpin(master=root)
# #######    
# #######    def f5(self):
# #######        self.unpack()
# #######        startScreen(master=root)
# #######    
# ######
# ######
# ##################################################################################################################################################################
# ##################################################################################################################################################################
# ######class balance(Frame):
# ######    def __init__(self, master=None):
# ######        super().__init__(master)
# ######        self.pack()
# ######        self.bal()
# ######    
# ######    def bal(self):
# ######        self.l1 = Label(root, text="Your Balance:", borderwidth=2, relief="groove", font="arial 18")
# ######        self.l1.place(x=80, y=110)
# ######        self.l2 = Label(root, text=amnt, font="arial 18")
# ######        self.l2.place(x=240, y=110)
# ######        self.b1 = Button(root, text="BACK", height=1, font="arial 13", command=self.return2)
# ######        self.b1.place(x=80, y=160)
# ######    
# ######    def return2(self):
# ######        self.l1.place_forget()
# ######        self.l2.place_forget()
# ######        self.b1.place_forget()
# ######        mainMenu(master=root)
# #####
# #####
# ##################################################################################################################################################################
# ##################################################################################################################################################################
# #####class deposit(Frame):
# #####    def __init__(self, master=None):
# #####        super().__init__(master)
# #####        self.pack()
# #####        self.Deposit()
# #####    
# #####    def Deposit(self):
# #####        self.l1 = Label(root, text="Enter Amount:", borderwidth=2, relief="groove", font="arial 18")
# #####        self.l1.place(x=55, y=130)
# #####        self.e1 = Entry(root, font="arial 18", width=10)
# #####        self.e1.place(x=220, y=130)
# #####        self.b1 = Button(root, text="ENTER", command=self.updateDB)
# #####        self.b1.place(x=310, y=180)
# #####        self.b2 = Button(root, text="BACK", command=self.goBack)
# #####        self.b2.place(x=260, y=180)
# #####    
# #####    def updateDB(self):
# #####        global amnt
# #####        try:
# #####            self.l0.place_forget()
# #####        except AttributeError:
# #####            pass
# #####        try:
# #####            amnt = amnt + int(self.e1.get())
# #####            conn = sq3.connect("users.db")
# #####            c = conn.cursor()
# #####            c.execute('''UPDATE user SET bal=? WHERE acno=?''',(amnt, acno))
# #####            conn.commit()
# #####            conn.close()
# #####            self.l1.place_forget()
# #####            self.e1.place_forget()
# #####            self.b1.place_forget()
# #####            self.b2.place_forget()
# #####            self.l2 = Label(root, text="Amount Deposited Successfully!\n\nReturning to Main Menu ...", font="arial 13", fg="blue")
# #####            self.l2.place(x=70, y=100)
# #####            root.after(3000,self.return2)
# #####        except ValueError:
# #####            self.e1.delete(0, 'end')
# #####            self.l0 = Label(root, text="Enter valid amount!", font="arial 15", fg="red")
# #####            self.l0.place(x=55, y=250)
# #####        
# #####    def return2(self):
# #####        self.l2.place_forget()
# #####        mainMenu(master=root)
# #####
# #####    def goBack(self):
# #####        try:
# #####            self.l0.place_forget()
# #####        except AttributeError:
# #####            pass
# #####        self.l1.place_forget()
# #####        self.e1.place_forget()
# #####        self.b1.place_forget()
# #####        self.b2.place_forget()
# #####        mainMenu(master=root)
# #####
# ####
# ###
# ##################################################################################################################################################################
# ##################################################################################################################################################################
# ####class withdraw(Frame):
# ####    def __init__(self, master=None):
# ####        super().__init__(master)
# ####        self.pack()
# ####        self.withDraw()
# ####    
# ####    def withDraw(self):
# ####        self.l1 = Label(root, text="Enter Amount:", borderwidth=2, relief="groove", font="arial 18")
# ####        self.l1.place(x=55, y=90)
# ####        self.e1 = Entry(root, font="arial 18", width=10)
# ####        self.e1.place(x=220, y=90)
# ####        self.b1 = Button(root, text="ENTER", command=self.updateDB)
# ####        self.b1.place(x=310, y=180)
# ####        self.b2 = Button(root, text="BACK", command=self.goBack)
# ####        self.b2.place(x=260, y=180)
# ####
# ####    def updateDB(self):
# ####        global amnt
# ####        try:
# ####            self.l0.place_forget()
# ####        except AttributeError:
# ####            pass
# ####        try:
# ####            if int(self.e1.get()) <= amnt:
# ####                amnt = amnt - int(self.e1.get())
# ####                conn = sq3.connect("users.db")
# ####                c = conn.cursor()
# ####                c.execute('''UPDATE user SET bal=? WHERE acno=?''',(amnt, acno))
# ####                conn.commit()
# ####                conn.close()
# ####                self.l1.place_forget()
# ####                self.e1.place_forget()
# ####                self.b1.place_forget()
# ####                self.b2.place_forget()
# ####                self.l2 = Label(root, text="Amount Withdrawn Successfully!\n\nReturning to Main Menu ...", font="arial 13", fg="blue")
# ####                self.l2.place(x=70, y=100)
# ####                root.after(3000, self.return2)
# ####            else:
# ####                self.l1.place_forget()
# ####                self.e1.place_forget()
# ####                self.b1.place_forget()
# ####                self.l2 = Label(root, text="Insufficient Balance!", font="arial 16", fg="red")
# ####                self.l2.place(x=100, y=120)
# ####                root.after(3000, self.return2)
# ####        except ValueError:
# ####            self.e1.delete(0, 'end')
# ####            self.l0 = Label(root, text="Enter valid amount!", font="arial 15", fg="red")
# ####            self.l0.place(x=55, y=250)
# ####        
# ####
# ####    def return2(self):
# ####        self.l2.place_forget()
# ####        mainMenu(master=root) 
# ####
# ####    def goBack(self):
# ####        try:
# ####            self.l0.place_forget()
# ####        except AttributeError:
# ####            pass
# ####        self.l1.place_forget()
# ####        self.e1.place_forget()
# ####        self.b1.place_forget()
# ####        self.b2.place_forget()
# ####        mainMenu(master=root)   
# ###
# ###
# ##################################################################################################################################################################
# ##################################################################################################################################################################
# ###class newpin(Frame):
# ###    def __init__(self, master=None):
# ###        super().__init__(master)
# ###        self.pack()
# ###        self.newPin()
# ###    
# ###    def newPin(self):
# ###        self.l1 = Label(root, text="Old Pin :", borderwidth=2, relief="groove", font="arial 18")
# ###        self.l1.place(x=60, y=60)
# ###        self.e1 = Entry(root, font="arial 18", width=10)
# ###        self.e1.place(x=170, y=60)
# ###        self.l2 = Label(root, text="New Pin:", borderwidth=2, relief="groove", font="arial 18")
# ###        self.l2.place(x=60, y=100)
# ###        self.e2 = Entry(root, font="arial 18", width=10)
# ###        self.e2.place(x=170, y=100)
# ###        self.l3 = Label(root, text="New Pin:", borderwidth=2, relief="groove", font="arial 18")
# ###        self.l3.place(x=60, y=140)
# ###        self.e3 = Entry(root, font="arial 18", width=10)
# ###        self.e3.place(x=170, y=140)
# ###        self.b1 = Button(root, text="submit", font="arial 14", command=self.process)
# ###        self.b1.place(x=233, y=180)
# ###        self.b2 = Button(root, text="back", font="arial 14", command=self.goBack)
# ###        self.b2.place(x=160, y=180)
# ###    
# ###    def process(self):
# ###        try:
# ###            self.l0.place_forget()
# ###        except:
# ###            pass
# ###        if self.e1.get() == str(fetch(acno)[0]):
# ###            if self.e2.get() == self.e3.get() and len(self.e2.get()) == 4:
# ###                conn = sq3.connect("users.db")
# ###                c = conn.cursor()
# ###                c.execute('''UPDATE user SET pin=? WHERE acno=?''', (self.e2.get(), acno))
# ###                conn.commit()
# ###                conn.close()
# ###                self.l1.place_forget()
# ###                self.l2.place_forget()
# ###                self.l3.place_forget()
# ###                self.e1.place_forget()
# ###                self.e2.place_forget()
# ###                self.e3.place_forget()
# ###                self.b1.place_forget()
# ###                self.b2.place_forget()
# ###                self.l4 = Label(root, text="Pin Updated!\n\nReturning to Main Menu ...", font="arial 13", fg="blue")
# ###                self.l4.place(x=100, y=100)
# ###                root.after(3000, self.return2)
# ###            else:
# ###                self.e2.delete(0, 'end')
# ###                self.e3.delete(0, 'end')
# ###                self.l0 = Label(root, text="Wrong! Try again ...", font="arial 15", fg="red")
# ###                self.l0.place(x=60, y=250)
# ###        else:
# ###            self.e1.delete(0, 'end')
# ###            self.e2.delete(0, 'end')
# ###            self.e3.delete(0, 'end')
# ###            self.l0 = Label(root, text="Wrong! Try again ...", font="arial 15", fg="red")
# ###            self.l0.place(x=60, y=250)
# ###    
# ###    def return2(self):
# ###        self.l4.place_forget()
# ###        mainMenu(master=root)
# ###
# ###    def goBack(self):
# ###        try:
# ###            self.l0.place_forget()
# ###        except AttributeError:
# ###            pass
# ###        self.l1.place_forget()
# ###        self.l2.place_forget()
# ###        self.l3.place_forget()
# ###        self.e1.place_forget()
# ###        self.e2.place_forget()
# ###        self.e3.place_forget()
# ###        self.b1.place_forget()
# ###        self.b2.place_forget()
# ###        mainMenu(master=root) 
# ###
# ##################################################################################################################################################################
# ##################################################################################################################################################################
# ##root = Tk()
# ##root.title("ATM")
# ##root.geometry('400x350')
# ##root.resizable(False, False)
# ##
# ##background_image = PhotoImage(file="bgr.gif")
# ##background_label = Label(root, image=background_image)
# ##background_label.place(x=0, y=0, relwidth=1, relheight=1)
# ##
# ##
# ##app = startScreen(master=root)
# ##app.mainloop()
# ###
# ##################################################################################################################################################################
# ##################################################################################################################################################################
# #
# #print("%.6f"%(5280/13))
# #print(7*60*60+21*60+37)
# #print(2*6+2*3)
# #print(4*7)
# #print(2*3.14*8)
# #print(3.14*8**2)
# =============================================================================
# =============================================================================
# #import pandas as pd
# #df=pd.read_csv("temp.csv",names=['a','b','c','d','e'])
# #print(df)
# 
# =============================================================================
# =============================================================================
# #
# #trem76bo76="ghj";
# #x="joe warren is ";
# #y=52;
# #print(x+str(y))
# =============================================================================
import tkinter

top = tk()
C = tkinter.Canvas(top, bg="blue", height=250, width=300)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")
C.pack()
top.mainloop




