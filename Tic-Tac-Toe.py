
>>> from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('Tic-Tac-Toe')


#x person starts game so true
clicked= True
count= 0
#after winning Switch buttons
def Switch():
    A1.config(state=DISABLED)
    A2.config(state=DISABLED)
    A3.config(state=DISABLED)

    A4.config(state=DISABLED)
    A5.config(state=DISABLED)
    A6.config(state=DISABLED)

    A7.config(state=DISABLED)
    A8.config(state=DISABLED)
    A9.config(state=DISABLED)
    reset()
#check to see if someone won
def verify():
    global winner
    winner= False
#wins of player who chose x
    if A1["text"]==A2["text"]==A3["text"]=="x":
        A1.config(bg="green")
        A2.config(bg="green")
        A3.config(bg="green")
        messagebox.showinfo("winner","Player x wins")
        Switch()
    elif A4["text"]==A5["text"]==A6["text"]=="x":
        A4.config(bg="green")
        A5.config(bg="green")
        A6.config(bg="green")
        messagebox.showinfo("winner","Player with x wins")
        Switch()
    elif A7["text"]==A8["text"]==A9["text"]=="x":
        A7.config(bg="green")
        A8.config(bg="green")
        A9.config(bg="green")
        messagebox.showinfo("winner","Player with x wins")
        Switch()
    elif A1["text"]==A4["text"]=="x" and A7["text"]=="x":
        A1.config(bg="green")
        A4.config(bg="green")
        A7.config(bg="green")
        messagebox.showinfo("winner","Player with x wins")
        Switch()
    elif A2["text"]=="x" and A5["text"]=="x" and A8["text"]=="x":
        A2.config(bg="green")
        A5.config(bg="green")
        A8.config(bg="green")
        messagebox.showinfo("winner","Player with x wins")
        Switch()
    elif A3["text"]==A6["text"]==A9["text"]=="x":
        A3.config(bg="green")
        A6.config(bg="green")
        A9.config(bg="green")
        messagebox.showinfo("winner","Player with x wins")
        Switch()
    elif A1["text"]==A5["text"]==A9["text"]=="x":
        A1.config(bg="green")
        A5.config(bg="green")
        A9.config(bg="green")
        messagebox.showinfo("winner","Player with x wins")
        Switch()
    elif A3["text"]==A5["text"]==A7["text"]=="x":
        A3.config(bg="green")
        A5.config(bg="green")
        A7.config(bg="green")
        messagebox.showinfo("winner","Player with x wins")
        Switch()
#to check if player o wins
    elif A1["text"]==A2["text"]==A3["text"]=="o":
        A1.config(bg="green")
        A2.config(bg="green")
        A3.config(bg="green")
        messagebox.showinfo("winner","Player o wins")
        Switch()
    elif A4["text"]==A5["text"]==A6["text"]=="o":
        A4.config(bg="green")
        A5.config(bg="green")
        A6.config(bg="green")
        messagebox.showinfo("winner","Player with o wins")
        Switch()
    elif A7["text"]==A8["text"]==A9["text"]=="o":
        A7.config(bg="green")
        A8.config(bg="green")
        A9.config(bg="green")
        messagebox.showinfo("winner","Player with o wins")
        Switch()
    elif A1["text"]==A4["text"]==A7["text"]=="o":
        A1.config(bg="green")
        A4.config(bg="green")
        A7.config(bg="green")
        messagebox.showinfo("winner","Player with o wins")
        Switch()
    elif A2["text"]==A5["text"]==A8["text"]=="o":
        A2.config(bg="green")
        A5.config(bg="green")
        A8.config(bg="green")
        messagebox.showinfo("winner","Player with o wins")
        Switch()
    elif A3["text"]==A6["text"]==A9["text"]=="o":
        A3.config(bg="green")
        A6.config(bg="green")
        A9.config(bg="green")
        messagebox.showinfo("winner","Player with o wins")
        Switch()
    elif A1["text"]==A5["text"]==A9["text"]=="o":
        A1.config(bg="green")
        A5.config(bg="green")
        A9.config(bg="green")
        messagebox.showinfo("winner","Player with o wins")
        Switch()
    elif A3["text"]==A5["text"]==A7["text"]=="o":
        A3.config(bg="green")
        A5.config(bg="green")
        A7.config(bg="green")
        messagebox.showinfo("winner","Player with o wins")
        Switch()

    elif count==9 and winner== False:
        messagebox.showinfo("Tic-Tac-Toe","It's a tie\n no one wins")
        Switch()
        

#after clicking buttons
def Click(a):
    global clicked, count
    if a["text"]==" " and clicked== True:
        a["text"]="x"
        clicked= False
        count +=1
        verify()
    elif a["text"]==" " and clicked== False:
        a["text"]="o"
        clicked= True
        count+=1
        verify()
    else:
        messagebox.showerror("Tic-Tac-Toe","That box has already been selected\nslelect another box")
        

    

def reset():
    winner=False
    global count
    count=0
    global clicked
    clicked=True
    global A1,A2,A3,A4,A5,A6,A7,A8,A9
    A1=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:Click(A1))
    A1.grid(row=0,column=1)
    A2=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:Click(A2))
    A2.grid(row=0,column=2)
    A3=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:Click(A3))
    A3.grid(row=0,column=3)

    A4=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:Click(A4))
    A4.grid(row=1,column=1)
    A5=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:Click(A5))
    A5.grid(row=1,column=2)
    A6=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:Click(A6))
    A6.grid(row=1,column=3)

    A7=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:Click(A7))
    A7.grid(row=2,column=1)
    A8=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:Click(A8))
    A8.grid(row=2,column=2)
    A9=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:Click(A9))    
    A9.grid(row=2,column=3)
   
#buttons of game
A1=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:Click(A1))
A1.grid(row=0,column=1)
A2=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:Click(A2))
A2.grid(row=0,column=2)
A3=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:Click(A3))
A3.grid(row=0,column=3)

A4=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:Click(A4))
A4.grid(row=1,column=1)
A5=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:Click(A5))
A5.grid(row=1,column=2)
A6=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:Click(A6))
A6.grid(row=1,column=3)

A7=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:Click(A7))
A7.grid(row=2,column=1)
A8=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:Click(A8))
A8.grid(row=2,column=2)
A9=Button(root,text=" ",font=("Helvetica",20),height=3,width=6,command=lambda:Click(A9))    
A9.grid(row=2,column=3)

#creating options to reset  the game
my_menu=Menu(root)
root.config(menu=my_menu)

options_menu=Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="options",menu=options_menu)
options_menu.add_command(label="Reset Game",command=reset)


root.mainloop()
