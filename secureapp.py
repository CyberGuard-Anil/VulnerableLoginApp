import sqlite3
from tkinter import *
from tkinter import messagebox

def open_safe_window():
    safe_win = Tk()
    safe_win.title("✅ ACCESS GRANTED")
    safe_win.geometry("800x500") 
    safe_win.configure(bg="white")

    Label(safe_win, text="🎉 LOGIN SUCCESSFUL 🎉",
          font=("Courier New", 32, "bold"), fg="green", bg="white").pack(pady=60)

    Label(safe_win, text="This system is protected against SQL Injection.",
          font=("Arial", 18), fg="#333", bg="white").pack(pady=10)

    Label(safe_win, text="(Demo of a secure login system)", 
          font=("Arial", 14, "italic"), fg="gray", bg="white").pack(pady=20)

    safe_win.mainloop()


def login():
    uname = username_entry.get()
    pwd = password_entry.get()

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    print("[*] Executing secure query with parameterized input...")

    try:
        
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (uname, pwd))
        result = cursor.fetchone()

        if result:
            root.destroy()
            open_safe_window()
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


Label(root, text="Enterprise Login Portal", 
      font=("Helvetica", 26, "bold"), fg="#003366", bg="#e6f2ff").pack(pady=40)


Label(root, text="Username", font=("Arial", 14), bg="#e6f2ff").pack()
username_entry = Entry(root, font=("Arial", 14), width=35)
username_entry.pack(pady=10)


Label(root, text="Password", font=("Arial", 14), bg="#e6f2ff").pack()
password_entry = Entry(root, show="*", font=("Arial", 14), width=35)
password_entry.pack(pady=10)


Button(root, text="Login", command=login, font=("Arial", 14, "bold"),
       bg="#28a745", fg="white", width=25, height=1).pack(pady=30)


Label(root, text="Demo App – Protected Against SQLi", 
      font=("Arial", 10), bg="#e6f2ff", fg="gray").pack(side=BOTTOM, pady=10)

root.mainloop()

