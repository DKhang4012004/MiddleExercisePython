from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict
import os
from OOP.Model.Student import Student
from OOP.Model.GraduateStudent import GraduateStudent

class StudentManagementSystem:

    def __init__(self):
        self.__students: List[Student] = []  # Encapsulation

    def add_student(self):
        print("\n" + "=" * 50)
        print("THÊM SINH VIÊN MỚI")
        print("=" * 50)

        try:
            student_id = input("Nhập ID sinh viên: ").strip()
            if not student_id:
                print(" ID sinh viên không được để trống!")
                return

            # Kiểm tra ID đã tồn tại
            existing_students = self.get_all_students()
            for s in existing_students:
                if s.student_id == student_id:
                    print(" ID sinh viên đã tồn tại!")
                    return

            name = input("Nhập họ tên: ").strip()
            age = int(input("Nhập tuổi: "))
            print("Giới tính (1-Nam, 2-Nữ): ")
            gender_choice = input("Chọn: ")
            gender = "Nam" if gender_choice == "1" else "Nữ"

            birthplace = input("Nhập nơi sinh: ").strip()
            major = input("Nhập chuyên ngành: ").strip()
            gpa = float(input("Nhập GPA (0-4.0): "))

            if not all([name, birthplace, major]) or age <= 0 or not (0 <= gpa <= 4.0):
                print(" Thông tin không hợp lệ!")
                return

            student = Student(student_id, name, age, gender, birthplace, major, gpa)
            self.__students.append(student)

            print("✅ Đã thêm sinh viên thành công!")
            print(f"📄 Thông tin: {student.get_info()}")

        except ValueError as e:
            print(f"❌ Lỗi nhập liệu: {e}")
        except Exception as e:
            print(f"❌ Có lỗi xảy ra: {e}")

    def add_studentV2(self):
        """Thêm sinh viên cao học"""
        print("\n" + "=" * 50)
        print("THÊM SINH VIÊN CAO HỌC")
        print("=" * 50)

        try:
            student_id = input("Nhập ID sinh viên cao học: ").strip()
            if not student_id:
                print(" ID sinh viên không được để trống!")
                return

            # Kiểm tra ID đã tồn tại
            existing_students = self.get_all_students()
            for s in existing_students:
                if s.student_id == student_id:
                    print(" ID sinh viên đã tồn tại!")
                    return

            name = input("Nhập họ tên: ").strip()
            age = int(input("Nhập tuổi: "))
            print("Giới tính (1-Nam, 2-Nữ): ")
            gender_choice = input("Chọn: ")
            gender = "Nam" if gender_choice == "1" else "Nữ"

            birthplace = input("Nhập nơi sinh: ").strip()
            major = input("Nhập chuyên ngành: ").strip()
            gpa = float(input("Nhập GPA (0-4.0): "))
            thesis_topic = input("Nhập đề tài luận văn: ").strip()

            if not all([name, birthplace, major, thesis_topic]) or age <= 0 or not (0 <= gpa <= 4.0):
                print(" Thông tin không hợp lệ!")
                return

            grad_student = GraduateStudent(student_id, name, age, gender,
                                           birthplace, major, gpa, thesis_topic)
            self.__students.append(grad_student)

            print(" Đã thêm sinh viên cao học thành công!")
            print(f" Thông tin: {grad_student.get_info()}")

        except ValueError as e:
            print(f" Lỗi nhập liệu: {e}")
        except Exception as e:
            print(f" Có lỗi xảy ra: {e}")

    def deleteStudent(self):
        """Xóa sinh viên theo ID"""
        print("\n" + "=" * 50)
        print("XÓA SINH VIÊN THEO ID")
        print("=" * 50)

        student_id = input("Nhập ID sinh viên cần xóa: ").strip()
        for i, student in enumerate(self.__students):
            if student.student_id == student_id:
                del self.__students[i]
                print(f"Đã xóa sinh viên với ID {student_id}")
                return
        print(f" Không tìm thấy sinh viên với ID {student_id}")

    def load_from_file(self, filename: str):
        """Load students data from text file"""
        if not(self.__students):
            if not os.path.exists(filename):
                print(f"File {filename} không tồn tại!")
                return

            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                for line in lines[1:]:  # Skip header
                    line = line.strip()
                    if line:
                        parts = line.split(',')
                        if len(parts) >= 7:
                            student_id = parts[0].strip()
                            name = parts[1].strip()
                            age = int(parts[2].strip())
                            gender = parts[3].strip()
                            birthplace = parts[4].strip()
                            major = parts[5].strip()
                            gpa = float(parts[6].strip())

                            # Check if it's a graduate student
                            if len(parts) >= 8:
                                thesis_topic = parts[7].strip()
                                student = GraduateStudent(student_id, name, age, gender,
                                                        birthplace, major, gpa, thesis_topic)
                            else:
                                student = Student(student_id, name, age, gender,
                                                birthplace, major, gpa)

                            self.__students.append(student)
                return self.__students
            except Exception as e:
                print(f"Lỗi khi đọc file: {e}")
        else:
            return self.__students

    def UpdateStudent(self):
        """Cập nhật thông tin sinh viên theo ID qua menu lựa chọn."""
        student_id=input("Nhập ID sinh viên cần cập nhật: ")
        # 1. Tìm sinh viên cần cập nhật
        student_to_update = None
        for student in self.__students:
            if student.student_id == student_id:
                student_to_update = student
                break

        # 2. Nếu không tìm thấy, thông báo và thoát
        if not student_to_update:
            print(f"Không tìm thấy sinh viên với ID {student_id}")
            return

        print(f"--- Đang cập nhật cho sinh viên: {student_to_update.name} (ID: {student_id}) ---")

        # 3. Bắt đầu vòng lặp cập nhật
        while True:
            print("\nChọn thông tin cần cập nhật:")
            print("1. Tên (Name)")
            print("2. Nơi sinh (Birthplace)")
            print("3. Điểm trung bình (GPA)")
            is_graduate = isinstance(student_to_update, GraduateStudent)
            if is_graduate:
                print("4. Đề tài luận văn (Thesis Topic)")
            print("0. Hoàn tất cập nhật")

            choice = input("Nhập lựa chọn của bạn: ")

            # 5. Xử lý lựa chọn
            if choice == '1':
                new_name = input("Nhập tên mới: ")
                student_to_update.name = new_name  # Yêu cầu 'name' property trong Person
                print("Đã cập nhật tên.")

            elif choice == '2':
                new_birthplace = input("Nhập nơi sinh mới: ")
                student_to_update.birthplace = new_birthplace  # Yêu cầu 'birthplace' property trong Person
                print("Đã cập nhật nơi sinh.")

            elif choice == '3':
                try:
                    new_gpa = float(input("Nhập GPA mới: "))
                    student_to_update.gpa = new_gpa  # Yêu cầu 'gpa' property trong Student
                    print("Đã cập nhật GPA.")
                except ValueError:
                    print("Lỗi: GPA phải là một con số.")

            elif choice == '4' and is_graduate:
                new_topic = input("Nhập đề tài luận văn mới: ")
                student_to_update.thesis_topic = new_topic  # Yêu cầu 'thesis_topic' property
                print("Đã cập nhật đề tài luận văn.")

            elif choice == '0':
                print(f"Đã hoàn tất cập nhật thông tin cho sinh viên ID {student_id}")
                break  # Thoát khỏi vòng lặp while True

            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


    def find_st_by_id(self, student_id: str) -> List[Student]:
        student_ids=[]
        for student in self.__students:
            if student.student_id == student_id:
                student_ids.append(student)
                return student_ids
        return student_ids

    def count_students_by_gender(self) -> Dict[str, int]:
        count = {'Nam': 0, 'Nữ': 0}
        for student in self.__students:
            if student.gender.lower() in ['nam', 'male']:
                count['Nam'] += 1
            elif student.gender.lower() in ['nữ', 'female']:
                count['Nữ'] += 1
        return count

    def get_age_statistics(self) -> Dict[str, float]:
        """Get age statistics"""
        if not self.__students:
            return {'min': 0, 'max': 0, 'avg': 0}

        ages = [student.age for student in self.__students]
        return {
            'min': min(ages),
            'max': max(ages),
            'avg': sum(ages) / len(ages)
        }

    def get_all_students(self) -> List[Student]:
        return self.__students

    def count_students_by_birthplace(self) -> Dict[str, int]:
        birthplace_count = {}
        for student in self.__students:
            place = student.birthplace
            birthplace_count[place] = birthplace_count.get(place, 0) + 1
        return birthplace_count

    def get_students_by_major(self, major: str) -> List[Student]:
        return [s for s in self.__students if s.major.lower() == major.lower()]

    def get_top_students(self, n: int = 5) -> List[Student]:
        sorted_students = sorted(self.__students, key=lambda s: s.gpa, reverse=True)
        return sorted_students[:n]

    def get_students_by_academic_level(self, level: str) -> List[Student]:
        return [s for s in self.__students if s.get_academic_level() == level]

    def display_all_students(self):
        print(f"\n{'='*80}")
        print("DANH SÁCH TẤT CẢ SINH VIÊN")
        print(f"{'='*80}")

        if not self.__students:
            print("Không có sinh viên nào trong hệ thống.")
            return

        for i, student in enumerate(self.__students, 1):
            print(f"{i}. {student.get_info()}")
            print(f"   Vai trò: {student.get_role()}")
            print(f"   Xếp loại học tập: {student.get_academic_level()}")
            print("-" * 80)



