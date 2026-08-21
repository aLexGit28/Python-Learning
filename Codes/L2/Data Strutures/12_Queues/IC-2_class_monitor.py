class ClassMonitor:

    def __init__(self):
        self.students = []

    # Add a student to the class list
    def add_student(self, name):
        self.students.append(name)
        print(name, "entered the class.")

    # Remove the first student
    def leave_class(self):
        if self.is_empty():
            print("No students are left in the class.")
        else:
            student = self.students.pop(0)
            print(student, "left the class.")

    # Show the students currently in the class
    def show_students(self):
        if self.is_empty():
            print("The class is empty.")
        else:
            print("\nStudents in the class:")
            for student in self.students:
                print("-", student)

    # Check if the class is empty
    def is_empty(self):
        return len(self.students) == 0