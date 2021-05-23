import tkinter
root=tkinter.Tk()
def loginbtn_Click():
     varPassword.set(varEmailId.get())
     print("Email Id",varEmailId.get()," Password",varPassword.get())

root.title("Login Form")

lableEmailId=tkinter.Label(master=root, text="Email id")
lableEmailId.grid(row=0,column=0)

lablePassword=tkinter.Label(master=root,text="Password")
lablePassword.grid(row=1,column=0)

varEmailId=tkinter.StringVar()
Entrybox_1=tkinter.Entry(master=root,text="varEmailId")
Entrybox_1.grid(row=0,column=1)

varPassword=tkinter.StringVar()
Entrybox_2=tkinter.Entry(master=root,text="varPassword")
Entrybox_2.grid(row=1,column=1)


loginbtn=tkinter.Button(master=root,text="Login", command=loginbtn_Click)
loginbtn.grid(row=2,column=3)


root.minsize(400,300)
root.maxsize(400,300)
root.geometry("400x300+100+50")

root.mainloop()


