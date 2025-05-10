
![Library Management System](https://github.com/saksham801/Library-Mangement-System/blob/26d6de18b1a4a3f198e1897aea3936ad2a84e6af/ChatGPT%20Image%20May%204%2C%202025%2C%2010_27_15%20PM.png)


# <img src="https://github.com/saksham801/Library-Mangement-System/blob/5424e4fe8f2d458cafe7a894efb25d1203167d94/ChatGPT%20Image%20May%2010%2C%202025%2C%2008_19_17%20PM.svg" alt="Logo" width="40" style="vertical-align: middle"> Library Management System...
#Library Management System (Console-Based in Python)

A fully functional **Library Management System** built in Python..." alt="Logo" width="200">
</div>



A fully functional **Library Management System** built in Python that runs in the terminal and offers two separate user roles: **Admins** and **General Users**. This project simulates a real-world library system including book reservation, issuing, returning, and account management.

> **Made for learning, testing, and managing a simplified library interface through code.**

---

## ✨ Features at a Glance

| Admin Features | User Features |
| -------------- | ------------- |
| Register/Login | Register/Login |
| Add/Delete Books | Search Books |
| Issue/Return Books | Reserve/Return Books |
| View Book Status | View Issued Books |
| Update Credentials | Update Credentials |

---

## 🧩 Project Architecture

```
LibraryManagementSystem/
├── Welcome.py         # Entry point for menu & navigation
├── admin.py           # Admin registration & credential system
├── user.py            # User registration & credential system
├── book.py            # Book CRUD operations
├── umangement.py      # User-side book interaction logic
├── lmangement.py      # Admin-side inventory & records
├── main.py            # Optional module for test integration
```

Each module has been designed to handle one responsibility, making the code modular, maintainable, and scalable.

---

## 🛠️ Requirements

- Python 3.7 or higher
- Runs entirely on the **standard library** (no pip installs needed!)

---

## ⚙️ Installation & Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/LibraryManagementSystem.git
   cd LibraryManagementSystem
   ```

2. **(Optional) Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Run the Project**

   ```bash
   python Welcome.py
   ```

   You will be prompted with:

   ```
   1. Library Admin
   2. User Login
   ```

---

## 🧑‍💻 Usage Instructions

### ➤ For Admins:

- Register or Login
- Add new books with details like title, author, and ID
- Issue or return books for users
- View all reserved/issued books
- Update login credentials

### ➤ For Users:

- Register or Login
- Search or reserve available books
- Return borrowed books
- View your current issued books
- Update your account information

---

## 🔍 How It Works (Behind the Scenes)

- Data is stored using **in-memory data structures** (lists & dictionaries)
- Functions are imported across modules using clean architecture
- Modular design keeps admin and user functionality separate
- Easy to extend by adding file storage (JSON/CSV) or a database (SQLite)

---

## 🧪 Modules in Detail

### 1. `Welcome.py`
**Acts as the starting point**. Displays the main menu and directs users to Admin or User interfaces.

### 2. `admin.py`
Handles **Admin registration, login, password recovery, and profile updates**.

### 3. `user.py`
Handles **User registration, login, password recovery, and profile updates**.

### 4. `book.py`
Responsible for **book inventory operations** — adding, removing, issuing, returning, and listing books.

### 5. `umangement.py`
Manages **user-specific book actions** like reservation and viewing issued books.

### 6. `lmangement.py`
Used by admins to **monitor issued and reserved books** and track the entire inventory status.

### 7. `main.py`
Optional module to **test and debug functions independently**.

---

## 💡 Expansion Ideas

- Add **JSON or SQLite** for persistent storage
- Include **due dates** and **fine calculation**
- Implement a **Tkinter GUI** or **Flask Web Interface**
- Add **role-based access controls**
- Include **logging and exception handling**

---

## ⚠️ Common Errors & Fixes

**Error:**
```
AttributeError: 'NoneType' object has no attribute 'get'
```

**Reason:** A function (like `login()`) is returning `None` due to incorrect input or logic.

**Fix:** Ensure the function returns a dictionary or object with attributes, and validate all input paths.

---

## 📬 Contact

For any help, suggestions, or contributions:

**Email:** [dubeysaksham801@gmail.com](mailto:dubeysaksham801@gmail.com)

I welcome collaboration, feedback, or improvements from learners and developers alike!

---

## 📝 License

This project is open-source and free to use for learning, modification, and personal projects. Attribution is appreciated.

---

## ⭐ Final Words

This project is perfect for:
- Students learning **Python basics**
- Practice with **functions, modules, and CLI apps**
- Building your **first major Python project**

> Made with passion for learning and sharing. Happy coding!
