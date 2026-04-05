class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, g):
        self.grades.append(g)

    def show(self):
        print(self.name, self.grades)


def menu():
    student = None

    while True:
        print("1 create")
        print("2 add grade")
        print("3 show")
        print("0 exit")

        c = input("> ")

        if c == "1":
            name = input("name: ")
            student = Student(name)

        elif c == "2":
            if student:
                g = int(input("grade: "))
                student.add_grade(g)
            else:
                print("no student")

        elif c == "3":
            if student:
                student.show()
            else:
                print("no student")

        elif c == "0":
            break


menu()