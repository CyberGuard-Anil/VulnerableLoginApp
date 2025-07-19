# 🔓 VulnerableLoginApp – SQL Injection Demo using Flask

This is a **basic Flask login application** designed to demonstrate **SQL Injection (SQLi)** vulnerability and how to fix it using **parameterized queries**.

⚠️ **This app is for educational purposes only. Do NOT use this in production.**

---

## 📁 Project Structure

```

VulnerableLoginApp/
├── app.py          # ❌ Vulnerable Login App (with SQL Injection)
├── secureapp.py    # ✅ Secure Login App (with parameterized queries)
├── init\_db.py      # DB Initialization script
├── users.db        # SQLite3 Database

````

---

## ⚙️ Requirements

- Python 3.x
- Flask

### ✅ Install Flask:
```bash
pip install flask
````

---

## 🚀 How to Run

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/VulnerableLoginApp.git
cd VulnerableLoginApp
```

### 🔹 Step 2: Initialize the Database

```bash
python init_db.py
```

This will create a file called `users.db` with sample user data.

---

## 🔴 To Run the Vulnerable Version:

```bash
python app.py
```

🧨 **Try Logging in with this payload:**

* **Username:** `' OR '1'='1`
* **Password:** `anything`

> You'll bypass login without valid credentials — classic SQL Injection!

---

## ✅ To Run the Secure Version:

```bash
python secureapp.py
```

✅ This version uses **parameterized queries** to prevent SQL injection attacks.

---

## 🔐 Secure Code Snippet (Parameterized Query):

```python
cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
```

---

## 📸 Screenshots (Optional)

*You can add screenshots here of both login pages and SQLi results*

---

## 📚 Educational Purpose Only

This repo is built by [Anil Yadav](https://github.com/anilyadav-cyber) for **learning & teaching** SQL Injection in a practical way.

Please use responsibly. 🙏

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

