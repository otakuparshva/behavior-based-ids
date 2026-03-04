import tkinter as tk
from app.auth_backend import login
from app.database import init_db

init_db()

def handle_login():
    username = entry_user.get()
    password = entry_pass.get()

    result = login(username, password)

    label_result.config(text=f"Login {result}")

root = tk.Tk()
root.title("Secure Login System")
root.geometry("300x200")

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Login", command=handle_login).pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()