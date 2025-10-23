
import os
import sys
from OOP.Service.student_management import StudentManagementSystem
from OOP.Menu.menu import ShowMenu
from OOP.Model import Student,GraduateStudent

class StudentTerminalController:

    def __init__(self):
        self.system = StudentManagementSystem()
        self.data_file = "../students_data.txt"
        self.running = True

    def add_new_student(self):
        self.system.add_student()

    def add_graduate_student(self):
        self.system.add_studentV2()

    def delete_student(self):
        self.system.deleteStudent()

    def load_data(self):
        ShowMenu.display_students_table(self.system.load_from_file(self.data_file))

    def update_student(self):
        self.system.UpdateStudent()

    def search_by_id(self):
        search_id = input("Nhập ID sinh viên cần tìm: ").strip()
        found_students = self.system.find_st_by_id(search_id)
        if found_students:
            ShowMenu.display_students_table(found_students, "KẾT QUẢ TÌM KIẾM THEO ID")
        else:
            print(f" Không tìm thấy sinh viên có ID: {search_id}")

    def handle_statistics_gender(self):
        gender_stats = self.system.count_students_by_gender()
        ShowMenu.display_statistics_table("THỐNG KÊ THEO GIỚI TÍNH", gender_stats)
        ShowMenu.wait_for_user()

    def handle_statistics_age(self):
        age_stats = self.system.get_age_statistics()
        students = self.system.get_all_students()

        print("\n THỐNG KÊ ĐỘ TUỔI")
        print("=" * 40)

        if students:
            print(f"Tuổi nhỏ nhất    : {age_stats['min']:3} tuổi")
            print(f"Tuổi lớn nhất    : {age_stats['max']:3} tuổi")
            print(f"Tuổi trung bình  : {age_stats['avg']:5.1f} tuổi")

            # Thống kê theo nhóm tuổi
            age_groups = {"18-20": 0, "21-23": 0, "24-26": 0, "27+": 0}
            for student in students:
                age = student.age
                if 18 <= age <= 20:
                    age_groups["18-20"] += 1
                elif 21 <= age <= 23:
                    age_groups["21-23"] += 1
                elif 24 <= age <= 26:
                    age_groups["24-26"] += 1
                else:
                    age_groups["27+"] += 1

            ShowMenu.display_statistics_table("PHÂN BỐ THEO NHÓM TUỔI", age_groups)
        else:
            print("Không có dữ liệu để thống kê.")
        ShowMenu.wait_for_user()

    def handle_statistics_birthplace(self):
        birthplace_stats = self.system.count_students_by_birthplace()
        ShowMenu.display_statistics_table("THỐNG KÊ THEO NỚI SINH", birthplace_stats)
        ShowMenu.wait_for_user()

    def handle_statistics_major(self):
        students = self.system.get_all_students()
        majors = {}
        for student in students:
            majors[student.major] = majors.get(student.major, 0) + 1

        ShowMenu.display_statistics_table("THỐNG KÊ THEO CHUYÊN NGÀNH", majors)
        ShowMenu.wait_for_user()

    def handle_statistics_academic_performance(self):
        students = self.system.get_all_students()
        levels = ["Xuất sắc", "Giỏi", "Khá", "Trung bình", "Yếu"]
        level_stats = {}

        for level in levels:
            level_students = self.system.get_students_by_academic_level(level)
            level_stats[level] = len(level_students)

        ShowMenu.display_statistics_table("THỐNG KÊ XẾP LOẠI HỌC TẬP", level_stats)
        ShowMenu.wait_for_user()

    def handle_top_excellent_students(self):
        try:
            n = int(input("Nhập số lượng sinh viên muốn hiển thị: "))
            if n <= 0:
                print(" Số lượng phải lớn hơn 0!")
            else:
                top_students = self.system.get_top_students(n)
                if top_students:
                    ShowMenu.display_top_students_table(top_students, n)
                else:
                    print(" Không có dữ liệu sinh viên!")
        except ValueError:
            print(" Vui lòng nhập số hợp lệ!")
        ShowMenu.wait_for_user()



