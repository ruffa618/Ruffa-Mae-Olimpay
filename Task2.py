class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, I'm {self.name}. an {self.age} year-old {self.course} student.")

student1 = Student("niqs",34, "Diploma in Program - Information Technology")
student2 = Student("Ruffa", 22, "DIP-HM")
student3 = Student("Kyla", 21, "DIP-TM )

print("Student 1:")
student1.introduce()
print("\nStudent 2:")
student2.introduce()
print("\nStudent 3:")
student3.introduce()
