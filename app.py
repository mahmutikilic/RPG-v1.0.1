import tkinter as tk
from tkinter import END,messagebox, PhotoImage
import random as r
import clipboard as c

# === count var was set to 8 ===
count = 8

#===== to minus or plus count var button functions =====
def countplus():
    global count
    count += 1
    PasslengthLabel.config(text = f"{count}")
    if count != 1:
        buttonminus['state']="normal"

    if count >=10:
        buttonplus.place(x = 305, y = 50)
    
    if count >= 100:
        buttonplus.place(x = 325, y = 50)

def countminus():
    global count
    count -= 1
    PasslengthLabel.config(text = f"{count}")
    if count == 1:
        buttonminus['state']="disabled"

    if count <= 99:
        buttonplus.place(x = 305, y = 50)
    return count

# === copy functions ===
def copylabel():
    if createdPassEntry.get() == "Copy text...":
        c.copy("You didn't create any password!")
    else:
        c.copy(createdPassEntry.get())

# ======= with checkbox values, 
# funcions return random password string together checkButtonCheck funcitons =======
def returnPass(a,b,c,d,e,count):
    passString = "0123456789abcdefghijklmnoprstuvyzwxABCDEFGHIJKLMNOPRSTUVYZWX()!?*'-.,[]{}\|/£#$%&½^><+=_ "
    passresult =""
    if a == 0 and b == 0 and c == 0 and d == 0 and e == 0:
        message_box = messagebox.showerror(title="Error!",message="Complexity choose error!")
    if a == 1:
        passresult += "".join(passString[:10])
    
    if b == 1:
        passresult += "".join(passString[10:35])

    if c == 1:
        passresult += "".join(passString[35:60])

    if d == 1:
        passresult += "".join(passString[60:69])

    if e == 1:
        passresult += "".join(passString[69:])

    randomResult = "".join(r.choices(passresult, k=int(count)))
    return randomResult

def checkButtonCheck():
    createdPassEntry.delete(0,END)
    createdPassEntry.insert(string = f"{returnPass(numbers.get(),minLatters.get(),maxLatters.get(),characs.get(),specsChars.get(),count)}",index = 0)

window = tk.Tk() 
window.title("Randomize Password Creator v1.1")
window.geometry("300x200") #ilk yatay sonra dikey, x y 
window.minsize(375,220) # en fazla azalabileceği ölçüler, en fazla artailecek ölçüler için window.maxsize(400,300)
window.resizable(0,0) # büyüme ve küçülmeyi kapatma x ve ys de
# window.state("normal") ilk açılışta nasıl olması gerektiği 

copyIcon=PhotoImage(file = r"copy2.png")
passLenghtnotify = messagebox.showinfo(title="Minimum password Length", message="Default password length is set to 8.")
metin1 = tk.Label(text = "| Pass Complexity | Pass Lenght |",font=("Helvetica", 18))
metin1.place(x=5, y=5)
# ======= CheckBox var and places ======
numbers,minLatters,maxLatters,characs,specsChars = tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()
rdb0 = tk.Checkbutton(window,text="124568", onvalue=1, offvalue=0, variable=numbers).place(x=20,y=30)
rdb1= tk.Checkbutton(window,text = "abczyx", onvalue=1, offvalue=0, variable=minLatters).place(x= 20, y= 50)
rdb2= tk.Checkbutton(window,text = "ABCZYX", onvalue=1, offvalue=0, variable=maxLatters).place(x= 20, y = 70)
rdb3= tk.Checkbutton(window,text = "()!?*'-.,", onvalue=1, offvalue=0, variable=characs).place(x= 20, y = 90)
rdb4= tk.Checkbutton(window,text = "[]{}\|/£#$%&½^><+=_", onvalue=1, offvalue=0, variable = specsChars).place(x= 20, y = 110)
button=tk.Button(window, text = "Create Password", command=checkButtonCheck, bg="gray", fg="white").place(x=60, y = 150)
notiftext= tk.Label(window, text = "Click Button and Copy pass", fg="gray",font="bold 15").place(x= 10, y = 180)
createdPassEntry = tk.Entry(window, width =20)
createdPassEntry.insert(string = "Copy text...", index = 0)
createdPassEntry.place(x = 170, y = 154)
PasslengthLabel= tk.Label(window, text = count, fg="gray",font="bold 20")
PasslengthLabel.place(x= 265, y = 45)
copybutton=tk.Button(window, image=copyIcon,command=copylabel).place(x = 298, y = 140)
# ======= Plus and Minus Button =================
buttonplus=tk.Button(window, text = " + ", command=countplus, bg="gray", fg="white")
buttonplus.place(x = 290, y = 50)
buttonminus=tk.Button(window, text = " - ", command=countminus, bg="gray", fg="white")
buttonminus.place(x = 240, y = 50)
window.mainloop()
