from tkinter import *

from tkinter import messagebox

root=Tk()
root.geometry("400x400")
login_label=Label(root,text="login")
login_label.place(x=20,y=40)
entry_login=Entry(root)
entry_login.place(x=90,y=40)
password_label=Label(root,text=" password")
password_label.place(x=20,y=80)
entry_password=Entry(root,show="*")
entry_password.place(x=90,y=80)
login="user@user"
password="user123"
tries=3

def check():
    
    if(entry_login.get()==login and entry_password.get()==password):
        messagebox.showinfo(f"success ",message=f"hello your password is correct")
        root.destroy()
        root2=Tk()
        root2.geometry("400x400")
        lbl=Label(root2,text="welcome")
        lbl.pack()
        root2.mainloop()
    else:
        global tries
        tries=tries-1
        messagebox.showwarning(f"failed ",message=f"hello your password is incorrect")
        if(tries==0):
            messagebox.showerror(f"failed ",message=f"your account is blocked")
            
            root.destroy()
        
        
    
button=Button(root,text="click",command=check)
button.place(x=30,y=120)







root.mainloop()