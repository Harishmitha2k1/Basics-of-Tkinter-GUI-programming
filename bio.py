import tkinter
parent=tkinter.Tk()
def sel():
 select="" + str(v.get())
 label.config(text=select)
v=tkinter.StringVar()
parent.title("Personal Details")
parent.geometry("400x400")

name=tkinter.Label(parent,text="Name:",font=('TimesNewRoman 12'),fg="blue")
name.place(x=50,y=48)
e1=tkinter.Entry(parent,font=('TimesNewRoman 12'),fg="brown")
e1.place(x=155,y=47)

age=tkinter.Label(parent,text="Age:",font=('TimesNewRoman 12'),fg="blue")
age.place(x=50,y=98)
e2=tkinter.Entry(parent,font=('TimesNewRoman 12'),fg="brown")
e2.place(x=155,y=97)

ph=tkinter.Label(parent,text="PhoneNumber:",font=('TimesNewRoman 12'),fg="blue")
ph.place(x=50,y=148)
e3=tkinter.Entry(parent,font=('TimesNewRoman 12'),fg="brown")
e3.place(x=155,y=150)

gen=tkinter.Label(parent,text="Gender:",font=('TimesNewRoman 12'),fg="blue")
gen.place(x=50,y=198)
e4=tkinter.Radiobutton(parent,text="Male",fg="red",activebackground="pink",variable=v,value="Male",command=sel)
e4.place(x=150,y=197)
e5=tkinter.Radiobutton(parent,text="Female",fg="red",activebackground="pink",variable=v,value="Female",command=sel)
e5.place(x=150,y=227)

label=tkinter.Label(parent)
chk=tkinter.Label(parent,text="Languages Known:",font=('TimesNewRoman 12'),fg="blue")
chk.place(x=50,y=285)
chck1 = tkinter.IntVar()  
chck2 = tkinter.IntVar()  
chck3 = tkinter.IntVar()
chk1=tkinter.Checkbutton(parent,text="C Programming",activebackground="pink",font=('TimesNewRoman 12'),fg="red",variable=chck1)
chk1.place(x=150,y=310)
chk2=tkinter.Checkbutton(parent,text="Java Programming",activebackground="pink",font=('TimesNewRoman 12'),fg="red",variable=chck2)
chk2.place(x=150,y=350)
chk3=tkinter.Checkbutton(parent,text="Python Programming",activebackground="pink",font=('TimesNewRoman 12'),fg="red",variable=chck3)
chk3.place(x=150,y=392)


bl=tkinter.Label(parent,text="Blood Group:",font=('TimesNewRoman 11'),fg="blue")
bl.place(x=50,y=435)
option=["Select","A","B","A+","AB+","AB-"]
var=tkinter.StringVar()
var.set(option[0])
opt = tkinter.OptionMenu(parent, var, *option)
opt.config(width=5, font=('TimesNewRoman', 12))
opt.place(x=165,y=430)
def open():
 child=tkinter.Toplevel(parent)
 child.geometry("400x400")
 n1=tkinter.Label(child,text=e1.get(),font=('TimesNewRoman 12'),fg="blue")
 n1.place(x=50,y=48)
 a1=tkinter.Label(child,text=e2.get(),font=('TimesNewRoman 12'),fg="blue")
 a1.place(x=50,y=98)
 ph1=tkinter.Label(child,text=e3.get(),font=('TimesNewRoman 12'),fg="blue")
 ph1.place(x=50,y=148)
 gen=tkinter.Label(child,text=v.get(),font=('TimesNewRoman 12'),fg="blue")
 gen.place(x=50,y=200)
 
 lang1=""
 lang2=""
 lang3=""
 if(chck1.get()==1):
   lang1="C Programming"
 if(chck2.get()==1):
   lang2="Java Programming"
 if(chck3.get()==1):
   lang3="Python Programming"
 lang = lang1 + lang2 + lang3
 chk=tkinter.Label(child,text= "" + lang,font=('TimesNewRoman 12'),fg="blue")
 chk.place(x=50,y=245)
btn1=tkinter.Button(parent,text="Submit",bg="black",fg="white",width=10,activebackground="green",command=open)
btn1.place(x=150,y=500)
parent.mainloop()