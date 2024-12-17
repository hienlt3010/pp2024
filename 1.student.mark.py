class Class:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show(self):
        return f"ID: {self.id}, Name: {self.name}"

class Student(Class):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self.dob = dob

    def show(self):
        return super().show() + f", Date of Birth: {self.dob}"

class Course(Class):
    pass

class Mark:
    def __init__(self, student_id, course_id, mark=None):
        self.student_id = student_id
        self.course_id = course_id
        self.mark = mark

    def set_mark(self, mark):
        self.mark = mark

    def get_mark(self):
        return self.mark

# Danh sách sinh viên, khóa học và điểm
students = {}
courses = {}
marks = {}

# Hàm nhập sinh viên
def input_students():
    number_of_students = int(input("Enter the number of students: "))
    for _ in range(number_of_students):
        student_id = input("Enter student's ID: ")
        if student_id not in students:
            student_name = input("Enter student's name: ")
            dob = input("Enter student's date of birth: ")
            students[student_id] = Student(student_id, student_name, dob)
        else:
            print("Student ID already exists.")

# Hàm nhập khóa học
def input_courses():
    number_of_courses = int(input("Enter the number of courses: "))
    for _ in range(number_of_courses):
        course_id = input("Enter course's ID: ")
        if course_id not in courses:
            course_name = input("Enter course's name: ")
            courses[course_id] = Course(course_id, course_name)
        else:
            print("Course ID already exists.")

# Nhập điểm cho sinh viên
def input_marks():
    print("\nList of courses:")
    for course in courses.values():
        print(course.show())
    course_id = input("Select course id to input mark: ")
    if course_id not in courses:
        print("Invalid course id.")
        return
    
    print("\nList of students:")
    for student in students.values():
        print(student.show())
    student_id = input("Select student id to input mark: ")
    if student_id not in students:
        print("Invalid student id.")
        return
    
    mark_value = float(input("Enter mark: "))
    
    if student_id not in marks:
        marks[student_id] = {}

    marks[student_id][course_id] = Mark(student_id, course_id, mark_value)
    print("Mark entered successfully.\n")

# Liệt kê danh sách khóa học
def list_courses():
    print("\nList of courses:")
    for course in courses.values():
        print(course.show())

# Liệt kê danh sách sinh viên
def list_students():
    print("\nList of students:")
    for student in students.values():
        print(student.show())

# Hiển thị điểm của sinh viên trong một khóa học
def show_student_marks():
    course_id = input("\nSelect course id to show marks: ")
    if course_id not in courses:
        print("Invalid course id.")
        return
    
    print(f"\nCourse: {courses[course_id].name}")
    
    marks_found = False
    for student_id, student_marks in marks.items():
        if course_id in student_marks:
            print(f"Student ID: {student_id}, Mark: {student_marks[course_id].get_mark()}")
            marks_found = True

    if not marks_found:
        print("No marks found for this course.")


while True:
    print("\n---ENTER YOUR CHOICE---")
    print("--0. EXIT THE PROGRAM--")
    print("--1. INPUT STUDENTS----")
    print("--2. INPUT COURSES-----")
    print("--3. LIST COURSES------")
    print("--4. LIST STUDENTS-----")
    print("--5. INPUT MARK--------")
    print("--6. SHOW MARK---------\n")

    choice = int(input())
    
    if choice == 0:
        break
    
    elif choice == 1:
        input_students()
    
    elif choice == 2:
        input_courses()
    
    elif choice == 3:
        list_courses()
    
    elif choice == 4:
        list_students()
    
    elif choice == 5:
        input_marks()
    
    elif choice == 6:
        show_student_marks()
    
    else:
        print("Invalid choice.")
