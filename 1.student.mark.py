class Entity:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show(self):
        return f"ID: {self.id}, Name: {self.name}"

class Student(Entity):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self.dob = dob

    def show(self):
        return super().show() + f", Date of Birth: {self.dob}"

class Course(Entity):
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

# Nhập sinh viên
def input_students():
    n = int(input("Enter number of students: "))
    for _ in range(n):
        id = input("Enter student ID: ")
        if id not in students:
            name = input("Enter student name: ")
            dob = input("Enter student DoB: ")
            students[id] = Student(id, name, dob)
        else:
            print("ID already exists.")

# Nhập khóa học
def input_courses():
    n = int(input("Enter number of courses: "))
    for _ in range(n):
        id = input("Enter course ID: ")
        if id not in courses:
            name = input("Enter course name: ")
            courses[id] = Course(id, name)
        else:
            print("ID already exists.")

# Nhập điểm cho sinh viên
def input_marks():
    course_id = input("Enter course ID: ")
    if course_id not in courses:
        print("Invalid course ID.")
        return

    student_id = input("Enter student ID: ")
    if student_id not in students:
        print("Invalid student ID.")
        return

    mark = float(input("Enter mark: "))
    marks[(student_id, course_id)] = Mark(student_id, course_id, mark)

# Liệt kê sinh viên và khóa học
def list_courses():
    for course in courses.values():
        print(course.show())

def list_students():
    for student in students.values():
        print(student.show())

# Hiển thị điểm
def show_marks():
    course_id = input("Enter course ID to show marks: ")
    if course_id not in courses:
        print("Invalid course ID.")
        return
    for (student_id, cid), mark in marks.items():
        if cid == course_id:
            print(f"Student {student_id} - Mark: {mark.get_mark()}")


while True:
    print("\n1. Input Students\n2. Input Courses\n3. List Students\n4. List Courses\n5. Input Marks\n6. Show Marks\n0. Exit")
    choice = int(input("Choose an option: "))
    
    if choice == 1: input_students()
    elif choice == 2: input_courses()
    elif choice == 3: list_students()
    elif choice == 4: list_courses()
    elif choice == 5: input_marks()
    elif choice == 6: show_marks()
    elif choice == 0: break
    else: print("Invalid choice.")
