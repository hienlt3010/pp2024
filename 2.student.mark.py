class Person:
    def __init__(self, id, name, dob=None):
        self.id = id
        self.name = name
        self.dob = dob

    def show(self):
        return f"ID: {self.id}, Name: {self.name}, Date of Birth: {self.dob if self.dob else 'N/A'}"


class Student(Person):
    pass


class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.marks = {}

    def add_mark(self, student_id, mark):
        self.marks[student_id] = mark

    def show_marks(self):
        return f"Course: {self.name}, Marks: {self.marks}"


class Mark:
    def __init__(self, student_id, course_id, mark=None):
        self.student_id = student_id
        self.course_id = course_id
        self.mark = mark

    def set_mark(self, mark):
        self.mark = mark

    def get_mark(self):
        return self.mark


class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}

    def input_students(self):
        """Nhập danh sách sinh viên"""
        number_of_students = int(input("Enter the number of students: "))
        for _ in range(number_of_students):
            student_id = input("Enter student's ID: ")
            if student_id not in self.students:
                student_name = input("Enter student's name: ")
                dob = input("Enter student's date of birth: ")
                self.students[student_id] = Student(student_id, student_name, dob)
            else:
                print("Student ID already exists.")

    def input_courses(self):
        """Nhập danh sách khóa học"""
        number_of_courses = int(input("Enter the number of courses: "))
        for _ in range(number_of_courses):
            course_id = input("Enter course's ID: ")
            if course_id not in self.courses:
                course_name = input("Enter course's name: ")
                self.courses[course_id] = Course(course_id, course_name)
            else:
                print("Course ID already exists.")

    def input_marks(self):
        """Nhập điểm cho sinh viên trong khóa học"""
        print("\nList of courses:")
        for course in self.courses.values():
            print(f"{course.id}: {course.name}")

        course_id = input("Select course id to input mark: ")
        if course_id not in self.courses:
            print("Invalid course id.")
            return

        print("\nList of students:")
        for student in self.students.values():
            print(student.show())
        student_id = input("Select student id to input mark: ")
        if student_id not in self.students:
            print("Invalid student id.")
            return

        mark_value = float(input("Enter mark: "))
        if course_id not in self.marks:
            self.marks[course_id] = {}

        self.marks[course_id][student_id] = Mark(student_id, course_id, mark_value)
        print("Mark entered successfully.\n")

    def list_courses(self):
        """Liệt kê danh sách khóa học"""
        print("\nList of courses:")
        for course in self.courses.values():
            print(f"ID: {course.id}, Name: {course.name}")

    def list_students(self):
        """Liệt kê danh sách sinh viên"""
        print("\nList of students:")
        for student in self.students.values():
            print(student.show())

    def show_student_marks(self):
        """Hiển thị điểm của sinh viên trong một khóa học"""
        course_id = input("\nSelect course id to show marks: ")
        if course_id not in self.courses:
            print("Invalid course id.")
            return

        print(f"\nCourse: {self.courses[course_id].name}")
        marks_found = False
        for student_id, mark in self.marks.get(course_id, {}).items():
            print(f"Student ID: {student_id}, Mark: {mark.get_mark()}")
            marks_found = True

        if not marks_found:
            print("No marks found for this course.")


def main():
    system = StudentManagementSystem()

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
            system.input_students()
        elif choice == 2:
            system.input_courses()
        elif choice == 3:
            system.list_courses()
        elif choice == 4:
            system.list_students()
        elif choice == 5:
            system.input_marks()
        elif choice == 6:
            system.show_student_marks()
        else:
            print("Invalid choice.")

