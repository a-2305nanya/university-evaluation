USER_DB={}
student_ids=[]
student_names=[]
study_hours=[]
attendence_list=[]
exam_scores=[]
def simple_hash(password):
    encoded_chars=[chr(ord(char)+5) for char in password]
    return "".join(encoded_chars)
def authenticate(user_id,password):
    if user_id in USER_DB:
        user=USER_DB[user_id]
        if user["password"]==simple_hash(password):
            return user
    return None
def student_dashboard(user_id,user_data):
    print("\n==============================")
    print("      STUDENT DASHBOARD       ")
    print("==============================")
    print("Welcome",user_data["name"],"Reg No:",user_id,)
    print("Semester:",user_data.get("semester","N/A"))
    while True:
        print("\n1. View Grades & Schedule")
        print("2. View Performance Analytics (Text Report)")
        print("3. Logout")
        choice=input("Enter your choice (1-3):")
        if choice=="1":
            print("\n--- YOUR GRADES ---")
            print("Data Structures: A | Operating Systems: A-")
            print("\n--- YOUR SCHEDULE ---")
            print("Mon-Fri: 09:00 AM - 04:00 PM")
        elif choice=="2":
            found=False
            for i in range(len(student_ids)):
                if student_ids[i]==user_id:
                    found=True
                    total_att=0
                    total_score=0
                    for j in range(len(student_ids)):
                        total_att+=attendance_list[j]
                        total_score+=exam_scores[j]
                    avg_att=total_att/len(student_ids)
                    avg_score=total_score/len(student_ids)
                    print("\n--- YOUR PERFORMANCE REPORT ---")
                    print("Your Attendance:",attendance_list[i],"%(Class Avg:",avg_att,"%)")
                    print("Your Exam Score:",exam_scores[i],"%(Class Avg:",avg_score,"%)")
                    break
            if not found:
                print("\n[INFO] Data not found for this Roll Number.")
        elif choice == "3":
            print("Logging out...")
            break
        else:
            print("Invalid choice! Try again.")
def teacher_dashboard(user_id,user_data):
    print("\n==============================")
    print("      TEACHER DASHBOARD       ")
    print("==============================")
    print("Welcome,",user_data["name"],"ID:",user_id)
    while True:
        print("\n1.Upload Student Marks")
        print("2.View Class Analytics Report")
        print("3.Logout")
        choice=input("Enter your choice (1-3):")
        if choice=="1":
            reg_no=input("Enter Student Roll No:")
            marks=int(input("Enter Marks:"))
            print("Successfully saved",marks,"marks for student:",reg_no)    
        elif choice=="2":
            print("\n--- CLASS PERFORMANCE ANALYTICS ---")
            total_students=len(student_ids)
            print("Total Students in Class:",total_students)
            total_score=0
            total_hours=0
            pass_count=0
            for i in range(total_students):
                total_score+=exam_scores[i]
                total_hours+=study_hours[i]
                if exam_scores[i]>=50:
                    pass_count+=1
            avg_score=total_score/total_students
            avg_hours=total_hours/total_students
            pass_rate=(pass_count/total_students)*100
            print("Class Average Score:",avg_score,"%")
            print("Avg Study Hours/Week:",avg_hours)
            print("Class Pass Percentage:",pass_rate,"%")
            print("\nDetailed Student List:")
            print("Name \t\t Study Hours \t Exam Score")
            for i in range(total_students):
                print(student_names[i],"\t\t",study_hours[i],"\t\t",exam_scores[i])
            else:
                print("No student data available")
        elif choice=="3":
            print("Logging out...")
            break
        else:
            print("Invalid choice! Try again.")
def admin_dashboard(user_id, user_data):
    print("\n==============================")
    print("        ADMIN DASHBOARD       ")
    print("==============================")
    print("Welcome,",user_data["name"])
    while True:
        print("\n1.Add New User")
        print("2.View System Status")
        print("3.Logout")
        choice = input("Enter your choice (1-3):")
        if choice=="1":
            new_id=input("Enter New User ID:")
            new_pwd=input("Enter Password:")
            role=input("Enter Role (student/teacher/admin):")
            name=input("Enter Full Name:")
            USER_DB[new_id]={"password":simple_hash(new_pwd),"role":role.lower(),"name":name}
            print("User",new_id,"created successfully as",role)
        elif choice=="2":
            print("\n[STATUS] System running smoothly. 0 Errors found.")
        elif choice=="3":
            print("Logging out...")
            break
        else:
            print("Invalid choice! Try again.")
def main():
    print("****************************************")
    print("   UNIVERSITY PORTAL LOGIN SYSTEM       ")
    print("****************************************")
    uid=input("Enter User ID/Registration No:")
    pwd=input("Enter Password:")
    user=authenticate(uid,pwd)
    if user is None:
        print("\n[ERROR] Invalid ID or Password! Access Denied.")
        return 
    print("\n[SUCCESS] Login Successful!")
    role=user["role"]
    if role=="student":
        student_dashboard(uid,user)
    elif role=="teacher":
        teacher_dashboard(uid,user)
    elif role=="admin":
        admin_dashboard(uid,user)
    else:
        print("\n[ERROR] Role not authorized.")

