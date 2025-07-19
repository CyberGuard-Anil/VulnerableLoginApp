import sqlite3
from tkinter import *
from tkinter import messagebox

def open_hacked_window():
    hacked_win = Tk()
    hacked_win.title("🔥 SYSTEM BREACHED 🔥")
    hacked_win.geometry("800x500") 
    hacked_win.configure(bg="black")

    Label(hacked_win, text="💀 YOU HAVE BEEN HACKED 💀",
          font=("Courier New", 32, "bold"), fg="red", bg="black").pack(pady=60)

    Label(hacked_win, text="This system is vulnerable to SQL Injection.",
          font=("Arial", 18), fg="white", bg="black").pack(pady=10)

    Label(hacked_win, text="(This is just a demonstration)", 
          font=("Arial", 14, "italic"), fg="gray", bg="black").pack(pady=20)

    hacked_win.mainloop()


def login():
    uname = username_entry.get()
    pwd = password_entry.get()

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{uname}' AND password = '{pwd}'"
    print("[*] Executing:", query)

    try:
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            root.destroy()
            open_hacked_window()
        else:
            messagebox.showerror("Login Failed", "❌ Invalid credentials.")
    except Exception as e:
        messagebox.showerror("Error", f"⚠️ Something went wrong:\n{e}")
    finally:
        conn.close()


root = Tk()
root.title("🔐 Secure Login Portal")
root.geometry("700x500")  
root.configure(bg="#e6f2ff")
root.resizable(False, False)

# Heading
Label(root, text="Enterprise Login Portal", 
      font=("Helvetica", 26, "bold"), fg="#003366", bg="#e6f2ff").pack(pady=40)

# Username Field
Label(root, text="Username", font=("Arial", 14), bg="#e6f2ff").pack()
username_entry = Entry(root, font=("Arial", 14), width=35)
username_entry.pack(pady=10)

# Password Field
Label(root, text="Password", font=("Arial", 14), bg="#e6f2ff").pack()
password_entry = Entry(root, show="*", font=("Arial", 14), width=35)
password_entry.pack(pady=10)

# Login Button
Button(root, text="Login", command=login, font=("Arial", 14, "bold"),
       bg="#007acc", fg="white", width=25, height=1).pack(pady=30)

# Footer
Label(root, text="Demo App – Intentionally Vulnerable to SQLi", 
      font=("Arial", 10), bg="#e6f2ff", fg="gray").pack(side=BOTTOM, pady=10)

root.mainloop()

