from abc import ABC, abstractmethod
from OOP.Model.Person import Person

class Student(Person):

    def __init__(self, student_id: str, name: str, age: int, gender: str,
                 birthplace: str, major: str, gpa: float):
        super().__init__(name, age, gender, birthplace)  # Inheritance
        self.__student_id = student_id  # Encapsulation
        self.__major = major
        self.__gpa = gpa

    @property
    def student_id(self) -> str:
        return self.__student_id

    @property
    def major(self) -> str:
        return self.__major

    @property
    def gpa(self) -> float:
        return self.__gpa

    # Setter methods
    @student_id.setter
    def student_id(self, value: str):
        if value and isinstance(value, str):
            self.__student_id = value

    @major.setter
    def major(self, value: str):
        if value and isinstance(value, str):
            self.__major = value

    @gpa.setter
    def gpa(self, value: float):
        if isinstance(value, (int, float)) and 0 <= value <= 4.0:
            self.__gpa = value

    # Implementing abstract methods (Polymorphism)
    def get_info(self) -> str:
        return f"ID: {self.__student_id}, Tên: {self.name}, Tuổi: {self.age}, " \
               f"Giới tính: {self.gender}, Nơi sinh: {self.birthplace}, " \
               f"Chuyên ngành: {self.__major}, GPA: {self.__gpa}"

    def get_role(self) -> str:
        return "Sinh viên"

    # Method to check academic performance
    def get_academic_level(self) -> str:
        if self.__gpa >= 3.6:
            return "Xuất sắc"
        elif self.__gpa >= 3.2:
            return "Giỏi"
        elif self.__gpa >= 2.5:
            return "Khá"
        elif self.__gpa >= 2.0:
            return "Trung bình"
        else:
            return "Yếu"