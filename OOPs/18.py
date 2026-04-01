class School:
    name = 'St. Andrews School'
    principal = 'Mrs. Sahiba Khan'
    address = 'Agra'

    @classmethod
    def school_info(cls):
        print(f'School name = {cls.name} \nPrincipal = {cls.principal} \nAddress = {cls.address}\nTotal Students = {cls.total_students()}')
        

    @staticmethod
    def total_students():
        return len(students)

    @classmethod
    def change_principal(cls):
        cls.principal = input('Enter new principal name: ')

    def __init__(self):
        self.name = input('Enter student name: ')
        self.subject = input('Enter student subject: ')
        self.marks = list(map(int, input('Enter marks separated by space: ').split()))
        self.phone = input("Enter Phone No.: ")
        self.email = input("Enter Email Address: ")

    def student_info(self):
        self.grade = self.calculate_grade()
        self.result = self.is_pass(self.grade)
        print(f'Name = {self.name} \nSubject = {self.subject} \nMarks = {self.marks} \nPhone No. = {self.phone} \nEmail Address = {self.email}')
        print(f'Grade = {self.grade}')
        print(f'Exam Status: {self.result}')

    def calculate_grade(self):
        total = sum(self.marks)
        average = total / len(self.marks)
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    @staticmethod
    def is_pass(grade):
        if grade == 'F':
            return 'Fail'
        return 'Pass'

    def change_phone_no(self):
        self.phone = input("Enter new Number: ")

    def change_email(self):
        self.email = input("Enter new Email: ")

def create_student():
        student = School()
        return student

students = {}
while True:
    print("1. Create Student\n2. View Student\n3. View School Info\n4. Exit\n\n")
    main_choice = int(input("Enter your Main Choice: "))
    if main_choice == 1:
        key = f's{len(students)+1}'
        students[key] = create_student()
        print(f"Student created with ID: {key}")
    elif main_choice == 2:
        obj = input("Enter student ID: ")
        if obj not in students:
            print("No student available with ID " + obj)
        else:
            stu = students[obj]
            stu.student_info()
            while True:
                print("\n1. Change Phone No. \n2. Change Email \n3. Exit \n\n")
                choice = int(input("Enter Your Choice: "))

                if choice == 1:
                    stu.change_phone_no()
                elif choice == 2:
                    stu.change_email()
                elif choice == 3:
                    print("..............Exit..................")
                    break
                else:
                    print("Invalid choice. Please try again.")

    elif main_choice == 3:
        print(f'1. School info\n2. Change Principal\n3. Exit\n\n')
        choice = int(input("Enter your Choice: "))
        if choice == 1:
            School.school_info()
        elif choice == 2:
            School.change_principal()
        elif choice == 3:
            print("\n\t\t\t....Exit .....")
            break
        else:
            print("\n\nIncorrect Input")

    elif main_choice == 4:
        print("\n\t\t\t....Exit .....")
        break
    else:
        print(students)





    