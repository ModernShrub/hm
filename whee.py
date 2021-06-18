from tkinter import *
import random

root=Tk()
root.title("whee")
root.geometry("500x500")
root.configure(background = "light goldenrod")

giftlistvar = ["Passport", "Pen", "Pizza", "Donut", "Plushie", "Money card", "Shirt"]

gift_list = Label(root, bg="azure2")
gift_list["text"] = "Gifts : " + str(giftlistvar)
no = Label(root, bg="azure2")
no["text"] = "Which gift will you get????"

def randomlist() :
  giftno = random.sample(range(1,8),1)
  no["text"] = "You got item number " + str(giftno) + "! Congrats!"
    
btn=Button(root, text="Click Here!",command=randomlist, bg="PaleTurquoise2")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

gift_list.place(relx=0.5,rely=0.4,anchor=CENTER)
no.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()


