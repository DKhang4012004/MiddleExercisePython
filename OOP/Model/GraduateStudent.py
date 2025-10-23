from OOP.Model.Student import Student
class GraduateStudent(Student):

    def __init__(self, student_id: str, name: str, age: int, gender: str,
                 birthplace: str, major: str, gpa: float, thesis_topic: str):
        super().__init__(student_id, name, age, gender, birthplace, major, gpa)
        self.__thesis_topic = thesis_topic

    @property
    def thesis_topic(self) -> str:
        return self.__thesis_topic

    @thesis_topic.setter
    def thesis_topic(self, value: str):
        if value and isinstance(value, str):
            self.__thesis_topic = value

    # Polymorphism - overriding method
    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, Đề tài luận văn: {self.__thesis_topic}"

    def get_role(self) -> str:
        return "Sinh viên cao học"