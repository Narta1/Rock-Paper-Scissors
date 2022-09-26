from glob import glob
import random
from tkinter import *
import sys
import os
import subprocess
from PIL import ImageTk,Image
root=Tk()
root.geometry("600x500")



bgimg=ImageTk.PhotoImage(Image.open('angryimg.png'))

limg= Label(root, image=bgimg)
limg.place(x=0,y=0)
#root.configure(bg="#0B0416")


lbl=Label(root,text="Make your choice",bg="#506c8c",fg="white",font=("Garamond Premier Pro Regular ",18))
lbl.place(x=30,y=10)
lbl3=Label(root,text="Computer's choice",bg="#506c8c",fg="white",font=("Garamond Premier Pro Regular ",18))
lbl3.place(x=30,y=50)
ent1=Entry(root,font=("Garamond Premier Pro Regular ",18),width=21)
ent1.place(x=300,y=10)
res=Label(root,text="Your result",bg="#68658f",fg="white",font=("Garamond Premier Pro Regular ",18))
res.place(x=60,y=200)
res_comp=Label(root,text="Computer's result",bg="#237785",fg="white",font=("Garamond Premier Pro Regular ",18))
res_comp.place(x=360,y=200)
lbl2=Label(root,text="",font=("Garamond Premier Pro Regular ",18),bg="white",width=19,anchor="w")
lbl2.place(x=300,y=50)
res1=0
res2=0

choices=["Rock",'Paper','Scissors']
def play():
    if not(check_winner()):
        

        global lbl2
        global res2
        global res1
        global new_lbl
        global new_lbl2


        
        user=(ent1.get()).capitalize()
        
        new_lbl3=Label(root,font=("Garamond Premier Pro Regular ",18),bg="#5b698d",width=19)
        new_lbl3.place(x=170,y=300)
        
        computer=random.choice(choices)
        lbl2=Label(root,text=computer,font=("Garamond Premier Pro Regular ",18),bg="white",width=19,anchor="w")
        lbl2.place(x=300,y=50)
        if (user=="Paper" and computer=="Rock") or (user=="Scissors" and computer=="Paper") or (user=="Rock" and computer=="Scissors")  :
            res1+=1
            new_lbl=Label(root,text=res1,font=("Garamond Premier Pro Regular ",18),bg="white",width=15)
            new_lbl.place(x=30,y=250)
        elif ent1.get()==computer:
            new_lbl3=Label(root,text="It's a draw",font=("Garamond Premier Pro Regular ",18),bg="white",width=19)
            new_lbl3.place(x=170,y=300)


        else:
            res2+=1
            new_lbl2=Label(root,text=res2,font=("Garamond Premier Pro Regular ",18),bg="white",width=15)
            new_lbl2.place(x=350,y=250)

        
       
    
def check_winner():
    stop=False
    if res1==3:
        
        ne=Label(root,text="You won!",font=("Garamond Premier Pro Regular ",18),bg="white",width=15)
        ne.place(x=200,y=450)
        stop=True
        #return 'You won!!'
    elif res2==3:
        
        
        
        ne2=Label(root,text="Computer won!",font=("Garamond Premier Pro Regular ",18),bg="white",width=15)
        ne2.place(x=200,y=450)
        stop=True
        #return 'Computer won!!'
    return stop

def game_over():
    sys.exit()
    
    
def reset():
    os.execl(sys.executable, sys.executable, *sys.argv)
    
    
    
btn=Button(root,text='Play game',command=play,bg="#416f8a",fg="white",font=("Garamond Premier Pro Regular ",18))
btn.place(x=220,y=120)

reset=Button(root,text='Reset game',command=reset,bg="#7f6093",fg="white",font=("Garamond Premier Pro Regular ",18))
reset.place(x=50,y=360)
stp=Button(root,text='Stop game',bg="#426f8a",fg="white",font=("Garamond Premier Pro Regular ",18),command=game_over)
stp.place(x=400,y=360)


root.mainloop()