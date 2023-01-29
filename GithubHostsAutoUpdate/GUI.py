import tkinter as tk
import AutoUpdateGithubHosts
import os

root = tk.Tk()
root.title("Github Hosts Update")

root.geometry("300x100")

Tip1 = tk.Label(root, text="IP").grid(column=0, row=0)
IP = tk.Entry(root, width=30)
IP.grid(column=1, row=0)
Tip2 = tk.Label(root, text="Username").grid(column=0, row=1)
Username = tk.Entry(root, width=30)
Username.grid(column=1, row=1)
Tip3 = tk.Label(root, text="Password").grid(column=0, row=2)
Password = tk.Entry(root, width=30)
Password.grid(column=1, row=2)

def Submit():
    AutoUpdateGithubHosts.Update(IP.get(), Username.get(), Password.get())
def ClearUp():
    os.system("cls" if os.name == "nt" else "clear")

Submit = tk.Button(root, text="Submit", command=Submit).grid(column=0, row=3)
ClearUp = tk.Button(root, text="ClearUp", command=ClearUp).grid(column=1, row=3)
root.mainloop()