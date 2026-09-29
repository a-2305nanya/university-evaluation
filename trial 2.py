import analytics as an
import authentication as at
import evaluation as ev
def initialize_db():
    at.USER_DB={"admin1":{"password":at.simple_hash("admin123"),"role":"admin","name":"System Administrator"},"T101":{"password":at.simple_hash("teacher123"),"role":"teacher","name":"Prof. Alan Turing",},"23BCN1001":{"password":at.simple_hash("student123"),"role":"student","name":"John Doe","semester":"Fall 2026"}}
    at.student_ids=["23BCN1001","23BCN1002","23BCN1003","23BCN1004","23BCN1005"]
    at.student_names=["John Doe","Jane Smith","Bob Johnson","Alice Brown","Charlie Green"]
    at.study_hours=[10,15,5,12,8]
    at.attendance_list=[85,90,65,95,70]
    at.exam_scores=[78,88,45,92,58]
def main_menu():
    initialize_db()
    while True:
        print(
            """
--- MAIN MENU ---
1. Authentication
2. Evaluation and display
3. Analytics
4. Exit"""
        )
        try:
            choice=int(input("CHOOSE AN OPTION FROM THE MENU: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        if choice==1:
            at.main()
        elif choice==2:
            ev.teacher_evaluation_menu(at.USER_DB)
        elif choice==3:
            an.display_dashboard(at.exam_scores)
        elif choice==4:
            print("Exiting application...")
            break
        else:
            print("Invalid selection. Try again.")
if __name__=="__main__":
    main_menu()
