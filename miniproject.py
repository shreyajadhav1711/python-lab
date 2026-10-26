
import sqlite3

# Connect to database (created automatically)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL,
    email TEXT NOT NULL,
    marks REAL NOT NULL
)
""")
conn.commit()


def add_student():
    print("\n--- Add Student ---")
    try:
        name = input("Enter student name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        age = int(input("Enter age: "))
        if age <= 0:
            print("Age must be positive.")
            return

        course = input("Enter course: ").strip()
        email = input("Enter email: ").strip()
        marks = float(input("Enter marks (0-100): "))

        if not course or not email:
            print("Course and email cannot be empty.")
            return
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        cursor.execute("""
            INSERT INTO students (name, age, course, email, marks)
            VALUES (?, ?, ?, ?, ?)
        """, (name, age, course, email, marks))
        conn.commit()

        print("Student added successfully!")
        print("Student ID:", cursor.lastrowid)

    except ValueError:
        print("Invalid input. Enter numbers for age and marks.")


def view_students():
    print("\n--- All Students ---")
    cursor.execute("SELECT * FROM students ORDER BY id")
    students = cursor.fetchall()

    if not students:
        print("No student records found.")
        return

    print("-" * 90)
    print(f"{'ID':<5}{'Name':<20}{'Age':<7}"
          f"{'Course':<18}{'Email':<25}{'Marks':<8}")
    print("-" * 90)

    for student in students:
        sid, name, age, course, email, marks = student
        print(f"{sid:<5}{name[:19]:<20}{age:<7}"
              f"{course[:17]:<18}{email[:24]:<25}{marks:<8.2f}")

    print("-" * 90)


def search_student():
    print("\n--- Search Student ---")
    print("1. Search by ID")
    print("2. Search by name")

    choice = input("Choose option: ").strip()

    if choice == "1":
        try:
            sid = int(input("Enter student ID: "))
            cursor.execute(
                "SELECT * FROM students WHERE id = ?", (sid,)
            )
        except ValueError:
            print("Please enter a valid ID.")
            return

    elif choice == "2":
        name = input("Enter student name: ").strip()
        cursor.execute(
            "SELECT * FROM students WHERE name LIKE ?",
            ("%" + name + "%",)
        )
    else:
        print("Invalid option.")
        return

    results = cursor.fetchall()

    if results:
        for student in results:
            print("\nID:", student[0])
            print("Name:", student[1])
            print("Age:", student[2])
            print("Course:", student[3])
            print("Email:", student[4])
            print("Marks:", student[5])
    else:
        print("No matching student found.")


def update_student():
    print("\n--- Update Student ---")

    try:
        sid = int(input("Enter student ID to update: "))
    except ValueError:
        print("Invalid student ID.")
        return

    cursor.execute("SELECT * FROM students WHERE id = ?", (sid,))
    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the current value.")

    name = input(f"Name [{student[1]}]: ").strip() or student[1]
    age_input = input(f"Age [{student[2]}]: ").strip()
    course = input(f"Course [{student[3]}]: ").strip() or student[3]
    email = input(f"Email [{student[4]}]: ").strip() or student[4]
    marks_input = input(f"Marks [{student[5]}]: ").strip()

    try:
        age = int(age_input) if age_input else student[2]
        marks = float(marks_input) if marks_input else student[5]

        if age <= 0:
            print("Age must be positive.")
            return
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Invalid age or marks.")
        return

    cursor.execute("""
        UPDATE students
        SET name = ?, age = ?, course = ?, email = ?, marks = ?
        WHERE id = ?
    """, (name, age, course, email, marks, sid))

    conn.commit()
    print("Student updated successfully!")


def delete_student():
    print("\n--- Delete Student ---")

    try:
        sid = int(input("Enter student ID to delete: "))
    except ValueError:
        print("Invalid student ID.")
        return

    cursor.execute("SELECT name FROM students WHERE id = ?", (sid,))
    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        return

    confirm = input(
        f"Delete student '{student[0]}'? (y/n): "
    ).strip().lower()

    if confirm == "y":
        cursor.execute("DELETE FROM students WHERE id = ?", (sid,))
        conn.commit()
        print("Student deleted successfully!")
    else:
        print("Deletion cancelled.")


def show_statistics():
    print("\n--- Student Statistics ---")

    cursor.execute("SELECT COUNT(*), AVG(marks) FROM students")
    total, average = cursor.fetchone()

    print("Total students:", total)
    if average is not None:
        print(f"Average marks: {average:.2f}")
    else:
        print("Average marks: No records available.")

    cursor.execute("""
        SELECT name, marks
        FROM students
        ORDER BY marks DESC, id ASC
        LIMIT 1
    """)
    topper = cursor.fetchone()

    if topper:
        print(f"Highest scorer: {topper[0]} ({topper[1]:.2f} marks)")


def main():
    while True:
        print("\n================================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. View Statistics")
        print("7. Exit")
        print("================================")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            show_statistics()
        elif choice == "7":
            conn.close()
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nApplication closed.")
        conn.close()
