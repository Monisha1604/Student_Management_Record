import streamlit as st

st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓"
)


# Linked List Node
class Student:
    def __init__(self, roll_no, name, age, course):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course
        self.next = None


# Linked List
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

    def get_students(self):
        students = []
        current = self.head

        while current is not None:
            students.append({
                "Roll No": current.roll_no,
                "Name": current.name,
                "Age": current.age,
                "Course": current.course
            })
            current = current.next

        return students

    def search_student(self, roll_no):
        current = self.head

        while current is not None:
            if current.roll_no == roll_no:
                return current

            current = current.next

        return None

    def update_student(self, roll_no, name, age, course):
        student = self.search_student(roll_no)

        if student is not None:
            student.name = name
            student.age = age
            student.course = course
            return True

        return False

    def delete_student(self, roll_no):
        current = self.head
        previous = None

        while current is not None:
            if current.roll_no == roll_no:

                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                return True

            previous = current
            current = current.next

        return False


# Keep data during website interaction
if "system" not in st.session_state:
    st.session_state.system = StudentManagementSystem()

system = st.session_state.system


# Website title
st.title("🎓 Student Management System")
st.write("### Data Structure Used: Linked List")


# Menu
choice = st.sidebar.selectbox(
    "Select Operation",
    [
        "Home",
        "Add Student",
        "Display Students",
        "Search Student",
        "Update Student",
        "Delete Student"
    ]
)


# Home
if choice == "Home":
    st.subheader("Welcome!")

    st.write(
        "This website is a Data Structures project "
        "that uses a Linked List to manage student records."
    )

    st.info(
        "Use the menu on the left to add, display, "
        "search, update, or delete students."
    )


# Add Student
elif choice == "Add Student":
    st.subheader("➕ Add Student")

    roll_no = st.text_input("Roll Number")
    name = st.text_input("Student Name")
    age = st.number_input("Age", min_value=1, max_value=100, value=18)
    course = st.text_input("Course")

    if st.button("Add Student"):
        if roll_no and name and course:
            if system.search_student(roll_no) is not None:
                st.error("Roll number already exists.")
            else:
                system.add_student(roll_no, name, age, course)
                st.success("Student added successfully!")
        else:
            st.warning("Please fill in all fields.")


# Display Students
elif choice == "Display Students":
    st.subheader("📋 Student Records")

    students = system.get_students()

    if students:
        st.table(students)
    else:
        st.info("No student records found.")


# Search Student
elif choice == "Search Student":
    st.subheader("🔍 Search Student")

    roll_no = st.text_input("Enter Roll Number")

    if st.button("Search"):
        student = system.search_student(roll_no)

        if student is not None:
            st.success("Student Found!")

            st.write("**Roll Number:**", student.roll_no)
            st.write("**Name:**", student.name)
            st.write("**Age:**", student.age)
            st.write("**Course:**", student.course)
        else:
            st.error("Student not found.")


# Update Student
elif choice == "Update Student":
    st.subheader("✏️ Update Student")

    roll_no = st.text_input("Enter Roll Number")

    name = st.text_input("New Name")
    age = st.number_input(
        "New Age",
        min_value=1,
        max_value=100,
        value=18
    )
    course = st.text_input("New Course")

    if st.button("Update Student"):
        if roll_no and name and course:
            if system.update_student(
                roll_no,
                name,
                age,
                course
            ):
                st.success("Student updated successfully!")
            else:
                st.error("Student not found.")
        else:
            st.warning("Please fill in all fields.")


# Delete Student
elif choice == "Delete Student":
    st.subheader("🗑️ Delete Student")

    roll_no = st.text_input("Enter Roll Number")

    if st.button("Delete Student"):
        if roll_no:
            if system.delete_student(roll_no):
                st.success("Student deleted successfully!")
            else:
                st.error("Student not found.")
        else:
            st.warning("Please enter a roll number.")