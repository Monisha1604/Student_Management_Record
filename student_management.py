class Student:
    def __init__(self, roll_no, name, age, course):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course
        self.next = None


class StudentManagementSystem:
    def __init__(self):
        self.head = None

    def add_student(self, roll_no, name, age, course):
        new_student = Student(roll_no, name, age, course)

        if self.head is None:
            self.head = new_student
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_student

        print("Student added successfully!")

    def display_students(self):
        if self.head is None:
            print("No student records found.")
            return

        current = self.head

        print("\n--- Student Records ---")

        while current is not None:
            print("Roll No :", current.roll_no)
            print("Name    :", current.name)
            print("Age     :", current.age)
            print("Course  :", current.course)
            print("-----------------------")

            current = current.next

    def search_student(self, roll_no):
        current = self.head

        while current is not None:
            if current.roll_no == roll_no:
                print("\nStudent Found!")
                print("Roll No :", current.roll_no)
                print("Name    :", current.name)
                print("Age     :", current.age)
                print("Course  :", current.course)
                return

            current = current.next

        print("Student not found.")

    def update_student(self, roll_no):
        current = self.head

        while current is not None:
            if current.roll_no == roll_no:
                print("\nStudent found!")

                current.name = input("Enter new name: ")
                current.age = input("Enter new age: ")
                current.course = input("Enter new course: ")

                print("Student updated successfully!")
                return

            current = current.next

        print("Student not found.")

    def delete_student(self, roll_no):
        current = self.head
        previous = None

        while current is not None:
            if current.roll_no == roll_no:

                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                print("Student deleted successfully!")
                return

            previous = current
            current = current.next

        print("Student not found.")


def main():
    system = StudentManagementSystem()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            roll_no = input("Enter roll number: ")
            name = input("Enter student name: ")
            age = input("Enter age: ")
            course = input("Enter course: ")

            system.add_student(roll_no, name, age, course)

        elif choice == "2":
            system.display_students()

        elif choice == "3":
            roll_no = input("Enter roll number to search: ")
            system.search_student(roll_no)

        elif choice == "4":
            roll_no = input("Enter roll number to update: ")
            system.update_student(roll_no)

        elif choice == "5":
            roll_no = input("Enter roll number to delete: ")
            system.delete_student(roll_no)

        elif choice == "6":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()