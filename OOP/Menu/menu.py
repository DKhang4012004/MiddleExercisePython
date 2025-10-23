class ShowMenu:
    @staticmethod
    def display_main_menu():
        """Hiển thị menu chính"""
        print("\n" + "=" * 50)
        print(" " * 18 + "MENU CHÍNH")
        print("=" * 50)
        print("1.  Thêm sinh viên mới")
        print("2.  Thêm sinh viên cao học")
        print("3.  Hiển thị danh sách sinh viên")
        print("4.  Xóa sinh viên")
        print("5.  Cập nhật thông tin sinh viên")
        print("6.  Tìm theo ID sinh viên")
        print("7.  Thống kê theo giới tính")
        print("8.  Thống kê theo độ tuổi")
        print("9.  Thống kê theo nơi sinh")
        print("10.  Thống kê theo chuyên ngành")
        print("11.  Thống kê theo xếp loại học tập")
        print("12.  Top sinh viên xuất sắc")
        print("0.  Thoát chương trình")
        print("=" * 50)

    @staticmethod
    def wait_for_user():
        input("\nNhấn Enter để tiếp tục...")

    @staticmethod
    def format_table_row(data, widths):
        row = "|"
        for i, item in enumerate(data):
            # Cắt chuỗi nếu quá dài
            if len(str(item)) > widths[i]:
                item = str(item)[:widths[i] - 3] + "..."
            row += f" {str(item):<{widths[i]}} |"
        return row

    @staticmethod
    def display_table_header(headers, widths):
        border = "+"
        for width in widths:
            border += "-" * (width + 2) + "+"
        print(border)

        print(ShowMenu.format_table_row(headers, widths))

        print(border)

    @staticmethod
    def display_table_header( headers, widths):
        border = "+"
        for width in widths:
            border += "-" * (width + 2) + "+"
        print(border)

        print(ShowMenu.format_table_row(headers, widths))

        print(border)

    @staticmethod
    def display_table_footer( widths):
        border = "+"
        for width in widths:
            border += "-" * (width + 2) + "+"
        print(border)

    @staticmethod
    def display_students_table(students, title="DANH SÁCH SINH VIÊN"):
        if not students:
            print("Không có sinh viên nào để hiển thị.")
            return

        print(f"\n📋 {title}")
        print("=" * 120)

        # Định nghĩa độ rộng các cột
        widths = [8, 20, 5, 8, 15, 18, 6, 12, 25]
        headers = ["ID", "Họ tên", "Tuổi", "Giới tính", "Nơi sinh", "Chuyên ngành", "GPA", "Xếp loại", "Vai trò/Đề tài"]

        ShowMenu.display_table_header(headers, widths)

        for student in students:
            extra_info = student.get_role()
            if hasattr(student, 'thesis_topic'):
                extra_info = student.thesis_topic

            row_data = [
                student.student_id,
                student.name,
                student.age,
                student.gender,
                student.birthplace,
                student.major,
                f"{student.gpa:.2f}",
                student.get_academic_level(),
                extra_info
            ]

            print(ShowMenu.format_table_row(row_data, widths))

        ShowMenu.display_table_footer(widths)
        print(f" Tổng cộng: {len(students)} sinh viên")

    @staticmethod
    def display_statistics_table( title, data_dict, value_name="Số lượng"):
        """Hiển thị thống kê dưới dạng bảng"""
        print(f"\n {title}")
        print("=" * 60)

        if not data_dict:
            print("Không có dữ liệu để thống kê.")
            return

        total = sum(data_dict.values()) if isinstance(list(data_dict.values())[0], (int, float)) else len(data_dict)

        max_key_length = max(len(str(key)) for key in data_dict.keys())
        key_width = max(15, max_key_length)
        widths = [key_width, 12, 12, 15]
        headers = ["Danh mục", value_name, "Phần trăm", "Biểu đồ"]

        ShowMenu.display_table_header(headers, widths)

        sorted_data = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)

        for key, value in sorted_data:
            if isinstance(value, (int, float)) and total > 0:
                percentage = (value / total) * 100
                bar = "█" * int(percentage // 2)
                row_data = [str(key), str(value), f"{percentage:.1f}%", bar]
            else:
                row_data = [str(key), str(value), "N/A", ""]

            print(ShowMenu.format_table_row(row_data, widths))

        ShowMenu.display_table_footer(widths)
        print(f" Tổng cộng: {total}")

    @staticmethod
    def display_top_students_table( students, n):
        if not students:
            print(" Không có dữ liệu sinh viên!")
            return

        print(f"\n TOP {min(n, len(students))} SINH VIÊN CÓ GPA CAO NHẤT")
        print("=" * 80)

        widths = [5, 8, 20, 6, 12, 18, 8]
        headers = ["Hạng", "ID", "Họ tên", "GPA", "Xếp loại", "Chuyên ngành", "Nơi sinh"]

        ShowMenu.display_table_header(headers, widths)

        for i, student in enumerate(students, 1):
            rank = str(i)

            row_data = [
                rank,
                student.student_id,
                student.name,
                f"{student.gpa:.2f}",
                student.get_academic_level(),
                student.major,
                student.birthplace
            ]

            print(ShowMenu.format_table_row(row_data, widths))

        ShowMenu.display_table_footer(widths)

    @staticmethod
    def display_header():
        print("=" * 70)
        print(" " * 15 + "HỆ THỐNG QUẢN LÝ SINH VIÊN OOP")
        print("=" * 70)

