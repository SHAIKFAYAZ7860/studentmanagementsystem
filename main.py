import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error


# -----------------------------
# MySQL Connection
# -----------------------------
def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Techno@799",  # <-- CHANGE IF NEEDED
            database="student_db"
        )
        return conn
    except Error as e:
        messagebox.showerror("Error", f"MySQL Error: {e}")
        return None


# -----------------------------
# Add Student
# -----------------------------
def add_student():
    name = entry_name.get()
    age = entry_age.get()
    course = entry_course.get()
    email = entry_email.get()

    if name == "" or age == "" or course == "":
        messagebox.showwarning("Warning", "Please fill all required fields!")
        return

    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students (name, age, course, email) VALUES (%s, %s, %s, %s)",
                (name, age, course, email)
            )
            conn.commit()
            messagebox.showinfo("Success", "Student added successfully!")
            clear_fields()
            view_students()
        except Error as e:
            messagebox.showerror("Error", f"Failed to add: {e}")
        finally:
            conn.close()


# -----------------------------
# View All Students
# -----------------------------
def view_students():
    for row in tree.get_children():
        tree.delete(row)

    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students ORDER BY id DESC")
            rows = cursor.fetchall()

            for row in rows:
                tree.insert("", tk.END, values=row)

        except Error as e:
            messagebox.showerror("Error", f"Failed to fetch data: {e}")
        finally:
            conn.close()


# -----------------------------
# Search Student
# -----------------------------
def search_student():
    sid = entry_id.get()

    if sid == "":
        messagebox.showwarning("Warning", "Enter Student ID!")
        return

    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students WHERE id=%s", (sid,))
            row = cursor.fetchone()

            for item in tree.get_children():
                tree.delete(item)

            if row:
                tree.insert("", tk.END, values=row)
            else:
                messagebox.showinfo("Not Found", "No student found.")

        except Error as e:
            messagebox.showerror("Error", f"MySQL Error: {e}")
        finally:
            conn.close()


# -----------------------------
# Update Student
# -----------------------------
def update_student():
    sid = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    course = entry_course.get()
    email = entry_email.get()

    if sid == "":
        messagebox.showwarning("Warning", "Enter Student ID!")
        return

    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE students SET name=%s, age=%s, course=%s, email=%s WHERE id=%s",
                (name, age, course, email, sid)
            )
            conn.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Success", "Student updated!")
                view_students()
            else:
                messagebox.showinfo("Not Found", "Student ID not found.")

        except Error as e:
            messagebox.showerror("Error", f"MySQL Error: {e}")
        finally:
            conn.close()


# -----------------------------
# Delete Student
# -----------------------------
def delete_student():
    sid = entry_id.get()

    if sid == "":
        messagebox.showwarning("Warning", "Enter Student ID!")
        return

    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE id=%s", (sid,))
            conn.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Deleted", "Student deleted!")
                view_students()
            else:
                messagebox.showinfo("Not Found", "Student ID not found.")

        except Error as e:
            messagebox.showerror("Error", f"MySQL Error: {e}")
        finally:
            conn.close()


# -----------------------------
# Clear Input Fields
# -----------------------------
def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_email.delete(0, tk.END)


# -----------------------------
# GUI SETUP
# -----------------------------
root = tk.Tk()
root.title("Student Management System")
root.geometry("850x600")
root.configure(bg="#eef2f3")

# Title
title = tk.Label(root, text="Student Management System",
                 font=("Arial", 22, "bold"), bg="#eef2f3", fg="#0b2a43")
title.pack(pady=10)

# Input Frame
frame = tk.Frame(root, bg="#eef2f3")
frame.pack(pady=10)

tk.Label(frame, text="Student ID", bg="#eef2f3").grid(row=0, column=0)
entry_id = tk.Entry(frame)
entry_id.grid(row=0, column=1, padx=10)

tk.Label(frame, text="Name *", bg="#eef2f3").grid(row=1, column=0)
entry_name = tk.Entry(frame)
entry_name.grid(row=1, column=1, padx=10)

tk.Label(frame, text="Age *", bg="#eef2f3").grid(row=2, column=0)
entry_age = tk.Entry(frame)
entry_age.grid(row=2, column=1, padx=10)

tk.Label(frame, text="Course *", bg="#eef2f3").grid(row=3, column=0)
entry_course = tk.Entry(frame)
entry_course.grid(row=3, column=1, padx=10)

tk.Label(frame, text="Email", bg="#eef2f3").grid(row=4, column=0)
entry_email = tk.Entry(frame)
entry_email.grid(row=4, column=1, padx=10)

# Buttons
btn_frame = tk.Frame(root, bg="#eef2f3")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=10, command=add_student, bg="#0077ff", fg="white").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="View All", width=10, command=view_students).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Search", width=10, command=search_student).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Update", width=10, command=update_student, bg="#ffaa00").grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="Delete", width=10, command=delete_student, bg="#ff4d4d", fg="white").grid(row=0, column=4, padx=5)
tk.Button(btn_frame, text="Clear", width=10, command=clear_fields).grid(row=0, column=5, padx=5)

# Table View
columns = ("ID", "Name", "Age", "Course", "Email", "Created")
tree = ttk.Treeview(root, columns=columns, show="headings", height=12)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.pack(pady=10)

# Load students initially
view_students()

root.mainloop()
