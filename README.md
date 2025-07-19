# 🔓 VulnerableLoginApp – SQL Injection Demo using Flask

A simple yet powerful **Flask-based login app** designed to **demonstrate SQL Injection (SQLi)** vulnerabilities and how to prevent them using **parameterized queries**.

> ⚠️ **Educational Use Only!**  
Do NOT use this app in production environments.

---

![python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![flask](https://img.shields.io/badge/Flask-SQLi--Demo-yellow?style=for-the-badge)
![sql-injection](https://img.shields.io/badge/SQL-Injection-critical?style=for-the-badge)

---

## 📁 Project Structure

```

VulnerableLoginApp/
├── app.py          # ❌ Vulnerable Login App (with SQL Injection)
├── secureapp.py    # ✅ Secure Login App (parameterized queries)
├── init\_db.py      # 🔧 DB Initialization script
├── users.db        # 📦 SQLite3 Database file

````

---

## ⚙️ Requirements

- Python 3.x
- Flask (`pip install flask`)

### 🔧 Install Flask:

```bash
pip install flask
````

---

## 🚀 How to Run

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/CyberGuard-Anil/VulnerableLoginApp.git
cd VulnerableLoginApp
```

### 🔹 Step 2: Initialize the Database

```bash
python init_db.py
```

✅ This will create a `users.db` SQLite database with sample credentials.

---

## 🔴 Run the Vulnerable Version (Demo SQLi)

```bash
python app.py
```

🧨 Try logging in with:

* **Username:** `' OR '1'='1`
* **Password:** `anything`

> ✅ Login will bypass without real credentials.
> 💣 This is a live demonstration of classic SQL Injection.

---

## ✅ Run the Secure Version

```bash
python secureapp.py
```

✅ This version uses **parameterized queries** to block SQL injection.

---

## 🛡️ Secure Code Snippet (Defense)

```python
cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
```

This prevents user input from interfering with the SQL query logic.

---

## 📸 Screenshot

> (Optional: Replace with your own image or demo GIF)

<img width="807" height="528" alt="image" src="https://github.com/user-attachments/assets/deea0371-5af3-4d9d-832b-50bdabe6f867" />

---

## 📚 Educational Use Only

This project is built by [Anil Yadav](https://github.com/CyberGuard-Anil)
For use in **cybersecurity training**, **ethical hacking**, and **demo labs**.

Please use responsibly and ethically. 🙏

---

## 📜 License

Licensed under the [MIT License](LICENSE)

---

> 👨‍💻 Learn Vulnerabilities | 💡 Practice Secure Coding | 🔐 Stay Ethical
> **Happy Hacking!**


