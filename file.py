import tkinter as tk
from tkinter import messagebox


# =========================
# PERSON CLASS
# =========================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        print(f"Name: {self.name} Age: {self.age}")


# =========================
# STUDENT CLASS
# =========================

class Student(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id
        self.marks = []

    def add_marks(self, marks):
        self.marks.extend(marks)

    def calculate_average(self):
        total = sum(self.marks)
        average = total / len(self.marks)
        return average

    def show_student(self):
        print(
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"ID: {self.id}\n"
            f"Marks: {self.marks}"
        )

    @staticmethod
    def check_result(average):
        if average >= 80:
            return "Grade A"
        elif average >= 70:
            return "Grade B"
        elif average >= 60:
            return "Grade C"
        else:
            return "Fail"


# =========================
# SCHOLARSHIP STUDENT CLASS
# =========================

class ScholarshipStudent(Student):
    def __init__(self, name, age, id, scholarship_amount):
        super().__init__(name, age, id)
        self.scholarship_amount = scholarship_amount

    def add_scholarship(self, amount):
        self.scholarship_amount += amount

    def show_scholarship(self):
        return f"Scholarship: {self.scholarship_amount}"

    def show_student(self):
        return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"ID: {self.id}\n"
            f"Marks: {self.marks}\n"
            f"Scholarship: {self.scholarship_amount}"
        )


# =========================
# GUI FUNCTIONS
# =========================

student = None


def create_student():
    global student

    try:
        name = name_entry.get()
        age = int(age_entry.get())
        student_id = id_entry.get()
        scholarship = int(scholarship_entry.get())

        marks_text = marks_entry.get()
        marks = [int(mark.strip()) for mark in marks_text.split(",")]

        if name == "" or student_id == "":
            messagebox.showerror("Error", "Please enter all information.")
            return

        student = ScholarshipStudent(
            name,
            age,
            student_id,
            scholarship
        )

        student.add_marks(marks)

        average = student.calculate_average()
        grade = student.check_result(average)

        result_text = (
            f"Name: {student.name}\n"
            f"Age: {student.age}\n"
            f"Student ID: {student.id}\n"
            f"Marks: {student.marks}\n"
            f"Average: {average:.2f}\n"
            f"Result: {grade}\n"
            f"Scholarship: {student.scholarship_amount}"
        )

        result_label.config(text=result_text)

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Age, Scholarship and Marks must contain numbers."
        )

    except ZeroDivisionError:
        messagebox.showerror(
            "Error",
            "Please enter at least one mark."
        )


def clear_data():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    scholarship_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)

    result_label.config(text="Student information will appear here.")


# =========================
# GUI WINDOW
# =========================

root = tk.Tk()

root.title("Student Management System")
root.geometry("700x700")
root.resizable(False, False)


# =========================
# TITLE
# =========================

title_label = tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 22, "bold"),
    fg="blue"
)

title_label.pack(pady=20)


# =========================
# NAME
# =========================

tk.Label(
    root,
    text="Name",
    font=("Arial", 12)
).pack()

name_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 12)
)

name_entry.pack(pady=5)


# =========================
# AGE
# =========================

tk.Label(
    root,
    text="Age",
    font=("Arial", 12)
).pack()

age_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 12)
)

age_entry.pack(pady=5)


# =========================
# STUDENT ID
# =========================

tk.Label(
    root,
    text="Student ID",
    font=("Arial", 12)
).pack()

id_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 12)
)

id_entry.pack(pady=5)


# =========================
# SCHOLARSHIP
# =========================

tk.Label(
    root,
    text="Scholarship",
    font=("Arial", 12)
).pack()

scholarship_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 12)
)

scholarship_entry.pack(pady=5)


# =========================
# MARKS
# =========================

tk.Label(
    root,
    text="Marks (example: 22,77,90)",
    font=("Arial", 12)

).pack()

marks_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 12)
)

marks_entry.pack(pady=5)


# =========================
# BUTTONS
# =========================

button_frame = tk.Frame(root)
button_frame.pack(pady=15)


create_button = tk.Button(
    button_frame,
    text="Create Student",
    font=("Arial", 12, "bold"),
    command=create_student,
    background="green",
    foreground="white"
)

create_button.pack(side="left", padx=10)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    command=clear_data,
    background="red",
    foreground="white"
)

clear_button.pack(side="left", padx=10)


# =========================
# RESULT
# =========================

tk.Label(
    root,
    text="Student Result",
    font=("Arial", 16, "bold" ,"underline" ,"italic")
).pack(pady=10)


result_label = tk.Label(
    root,
    text="Student information will appear here.",
    font=("Arial", 12),
    justify="left"
)

result_label.pack(pady=10)


# =========================
# START GUI
# =========================

root.mainloop()