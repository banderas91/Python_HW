import csv
import traceback

class NameDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not all(x.isalpha() or x.isspace() for x in value):
            raise ValueError(f"{self.name} должно содержать только буквы и пробелы")
        if not value.istitle():
            raise ValueError(f"{self.name} должно начинаться с заглавной буквы")
        instance.__dict__[self.name] = value

class Student:
    first_name = NameDescriptor()
    last_name = NameDescriptor()
    middle_name = NameDescriptor()

    def __init__(self, first_name, last_name, middle_name, csv_file):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.subjects = {}
        with open(csv_file) as f:
            reader = csv.reader(f)
            for row in reader:
                subject = row[0]
                self.subjects[subject] = {"grades": [], "tests": []}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        if not 2 <= grade <= 5:
            raise ValueError("Оценка должна быть от 2 до 5")
        self.subjects[subject]["grades"].append(grade)

    def add_test(self, subject, test):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        if not 0 <= test <= 100:
            raise ValueError("Результат теста должен быть от 0 до 100")
        self.subjects[subject]["tests"].append(test)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Предмет {subject} не найден")
        tests = self.subjects[subject]["tests"]
        if not tests:
            return None
        return sum(tests) / len(tests)

    def get_average_grade(self):
        grades = []
        for subject in self.subjects.values():
            grades.extend(subject["grades"])
        if not grades:
            return None
        return sum(grades) / len(grades)





try:
    student = Student("Иван", "Иванов", "Иванович", "subjects.csv")
except Exception as e:
    print("Произошла ошибка:")
    traceback.print_exc()

student.add_grade("Математика", 5)
student.add_grade("Математика", 4)
student.add_test("Математика", 85)
student.add_test("Математика", 90)

student.add_grade("Физика", 4)
student.add_grade("Физика", 3)
student.add_test("Физика", 75)
student.add_test("Физика", 80)

print(student.get_average_test_score("Математика")) 

print(student.get_average_grade()) 
