from OOP.Controller.terminal_controller import StudentTerminalController
from OOP.Menu.menu import ShowMenu
def showView():
    controller = StudentTerminalController()
    while True:
        ShowMenu.display_main_menu()
        choice = input("Chọn một tùy chọn (0-12): ")
        if choice == '1':
            controller.add_new_student()
            ShowMenu.wait_for_user()
        elif choice == '2':
            controller.add_graduate_student()
            ShowMenu.wait_for_user()
        elif choice == '3':
            controller.load_data()
            ShowMenu.wait_for_user()

        elif choice == '4':
            controller.delete_student()
            ShowMenu.wait_for_user()

        elif choice == '5':
            controller.update_student()
            ShowMenu.wait_for_user()

        elif choice == '6':
            controller.search_by_id()
            ShowMenu.wait_for_user()

        elif choice == '7':
            controller.handle_statistics_gender()

        elif choice == '8':
            controller.handle_statistics_age()

        elif choice == '9':
            controller.handle_statistics_birthplace()

        elif choice == '10':
            controller.handle_statistics_major()

        elif choice == '11':
            controller.handle_statistics_academic_performance()

        elif choice == '12':
            controller.handle_top_excellent_students()
        elif choice == '0':
            print("Thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

