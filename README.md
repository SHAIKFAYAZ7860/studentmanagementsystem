# 🎓 Student Management System (Python + Tkinter + MySQL)

A complete desktop-based Student Management System built using **Python**, **Tkinter GUI**, and **MySQL** database.  
This application allows users to **add, view, search, update, and delete student records** in a clean GUI interface.

---

## 🚀 Features

- ✔ Add New Student  
- ✔ View All Students  
- ✔ Search Student by ID  
- ✔ Update Student Details  
- ✔ Delete Student  
- ✔ MySQL Database Integration  
- ✔ Modern Tkinter GUI  
- ✔ Auto-refresh table after every action  

---

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter (GUI)**
- **MySQL**
- **mysql-connector-python**

---

## 📂 Project Structure

```

student_management_system/
│
├── main.py          # Main application file (GUI + MySQL connection)
├── README.md        # Documentation
└── requirements.txt # Optional (dependencies)

````

---

## 🗄️ MySQL Database Setup

Run the following SQL commands:

```sql
CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    course VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
````

---

## 📦 Installation & Setup

### 1️⃣ Install Dependencies

```
pip install mysql-connector-python
```

### 2️⃣ Update MySQL Password

In `main.py` update this part:

```python
password="YOUR_MYSQL_PASSWORD"
```

(Example: `Techno@799`)

### 3️⃣ Run the Project

```
python main.py
```

---

## 🖥️ Application Screens (Add your screenshots here)

Example:

```
/screenshots/
    home.png
    add_student.png
    view_students.png
```

---

## ✨ Functionality Overview

### ✔ Add Student

* Enter Name, Age, Course, Email
* Click **Add**

### ✔ View All Students

* Displays table with all students

### ✔ Search Student

* Enter Student ID
* Click **Search**

### ✔ Update Student

* Select Student ID
* Update inputs
* Click **Update**

### ✔ Delete Student

* Enter Student ID
* Click **Delete**

---

## 👨‍💻 Developer

**Shaik Fayaz**
📍 Rayavaram, Andhra Pradesh
🔗 GitHub: [SHAIKFAYAZ7860](https://github.com/SHAIKFAYAZ7860)

---

## ⭐ Support
    
If you find this useful, please give it a ⭐ on GitHub!

---

## 📜 License

This project is open-source and free to use.

```# ✅ Your README is fuldd screenshots section”**.
```
