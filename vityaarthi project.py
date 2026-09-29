USER_DB={"admin1":{"password":"admin123","role":"admin","name":"System Administrator"},"T101":{"password":"teacher123","role":"teacher","name":"Prof. Alan Turing"},"23BCN1001":{"password":"student123","role":"student","name":"John Doe","semester":"Fall 2026"}}
student_ids=["23BCN1001","23BCN1002","23BCN1003","23BCN1004","23BCN1005"]
student_names=["John Doe","Jane Smith","Bob Johnson","Alice Brown","Charlie Green"]
study_hours=[10,15,5,12,8]
attendance_list=[85,90,65,95,70]
exam_scores=[78,88,45,92,58]
def simple_hash(password):
    encoded_chars = [chr(ord(char) + 5) for char in password]
    return "".join(encoded_chars)
def authenticate(user_id, password):
    if user_id in USER_DB:
        user = USER_DB[user_id]
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
if __name__=="__main__":
    main()
EVALUATION_DB:Dict[str,dict]={}
def calculate_letter_grade(pct:float)->str:
    """Maps percentage score to standard letter grade."""
    if pct>=90:
        return "A"
    elif pct>=80:
        return "B"
    elif pct>=70:
        return "C"
    elif pct>=60:
        return "D"
    else:
        return "F"

def calculate_gpa(pct:float)->float:
    """Calculates 4.0 scale GPA based on percentage."""
    if pct>=90:
        return 4.0
    elif pct>=80:
        return 3.0
    elif pct>=70:
        return 2.0
    elif pct>=60:
        return 1.0
    else:
        return 0.0
def create_evaluation(student_id:str,course_id:str,title:str,score:float,max_score:float=100.0,weight:float=1.0)->str:
    """[CREATE] Records a new assignment/exam evaluation."""
    if score<0 or score>max_score:
        raise ValueError(f"Score must be between 0 and {max_score}.")
    if weight<=0:
        raise ValueError("Weight must be greater than 0.")
    eval_id="EVAL-{str(uuid.uuid4())[:6].upper()}"
    EVALUATION_DB[eval_id]={"eval_id":eval_id,"student_id":student_id,"course_id":course_id,"title":title,"score":float(score),"max_score":float(max_score),"weight":float(weight)}
    return eval_id
def get_student_evaluations(student_id:str,course_id:Optional[str]=None)->List[dict]:
    """[READ] Retrieves all evaluations for a student (optionally filtered by course)."""
    return [e for e in EVALUATION_DB.values() if e["student_id"]==student_id and (course_id is None or e["course_id"]==course_id)]
def update_evaluation(eval_id:str,score:Optional[float]=None,title:Optional[str]=None,weight:Optional[float]=None)->bool:
    """[UPDATE] Modifies an existing evaluation record."""
    record=EVALUATION_DB.get(eval_id)
    if not record:
        return False
    if score is not None:
        if score<0 or score>record["max_score"]:
            raise ValueError("Score must be between 0 and {record['max_score']}.")
        record["score"]=float(score)
    if title is not None:
        record["title"]=title
    if weight is not None:
        if weight<=0:
            raise ValueError("Weight must be greater than 0.")
        record["weight"]=float(weight)
    return True
def delete_evaluation(eval_id:str)->bool:
    """[DELETE] Removes an evaluation record."""
    if eval_id in EVALUATION_DB:
        del EVALUATION_DB[eval_id]
        return True
    return False
def calculate_student_course_score(student_id:str,course_id:str)->Optional[float]:
    """Calculates total weighted percentage score for a student in a specific course."""
    evals=get_student_evaluations(student_id,course_id)
    if not evals:
        return None
    total_weighted=sum((e["score"]/e["max_score"])*100*e["weight"] for e in evals)
    total_weight=sum(e["weight"] for e in evals)
    return round(total_weighted / total_weight, 2) if total_weight > 0 else 0.0
def calculate_class_analytics(course_id:str,all_student_ids:List[str])->dict:
    """Calculates class mean average, highest score, and student participation for a course."""
    scores=[]
    for sid in all_student_ids:
        score=calculate_student_course_score(sid,course_id)
        if score is not None:
            scores.append((sid,score))
    if not scores:
        return{"average":0.0,"highest":0.0,"total_students":0}
    avg_score=sum(s[1] for s in scores)/len(scores)
    max_score=max(s[1] for s in scores)
    return {"average":round(avg_score,2),"highest":round(max_score,2),"total_students":len(scores)}
def student_evaluation_view(student_id:str,all_student_ids:List[str]):
    """Student Dashboard view for evaluations and class comparisons."""
    course_id=input("Enter Course ID (e.g., CS101): ").strip().upper()
    evals=get_student_evaluations(student_id,course_id)
    if not evals:
        print("\n[!] No evaluation records found for course '{course_id}'.")
        return
    print("\n--- Assessment Breakdown for {course_id} ---")
    for e in evals:
        print(" • {e['title']}: {e['score']}/{e['max_score']} (Weight: {e['weight']})")
    overall=calculate_student_course_score(student_id,course_id)
    grade=calculate_letter_grade(overall)
    gpa=calculate_gpa(overall)
    stats=calculate_class_analytics(course_id,all_student_ids)
    print("\n--- Performance Summary ---")
    print("Your Score:{overall}% | Grade:{grade} | GPA:{gpa}")
    print("Class Average:{stats['average']}%")
    print("Top Class Score:{stats['highest']}%")
def teacher_evaluation_menu(all_students_db:dict):
    """Teacher Dashboard menu for performing CRUD on student grades."""
    while True:
        print("\n--- TEACHER EVALUATION MANAGEMENT ---")
        print("1. Record New Score (CREATE)")
        print("2. View Class Marksheet & Analytics (READ)")
        print("3. Edit Existing Score (UPDATE)")
        print("4. Delete Score Record (DELETE)")
        print("5. Back to Main Dashboard")
        choice=input("Select option (1-5):").strip()
        if choice=="1":
            try:
                sid=input("Enter Student ID: ").strip()
                cid=input("Enter Course ID: ").strip().upper()
                title=input("Assessment Name (e.g., Midterm): ").strip()
                score=float(input("Score Obtained: ").strip())
                max_s=float(input("Max Score (Default 100): ") or "100")
                weight=float(input("Weightage (e.g., 0.3): ") or "1.0")
                eval_id=create_evaluation(sid,cid,title,score,max_s,weight)
                print("[SUCCESS] Record saved with ID: {eval_id}")
            except ValueError as err:
                print("[ERROR] Invalid input: {err}")
        elif choice=="2":
            cid=input("Enter Course ID: ").strip().upper()
            student_ids=[uid for uid, data in all_students_db.items() if data.get("role")=="student"]
            print("\n--- Marksheet for {cid} ---")
            print("{'Student ID':<15} {'Name':<20} {'Overall Score':<15} {'Grade':<10}")
            print("-"*60)
            for sid in student_ids:
                score=calculate_student_course_score(sid, cid)
                if score is not None:
                    name=all_students_db[sid]["name"]
                    grade=calculate_letter_grade(score)
                    print("{sid:<15} {name:<20} {score:<15}% {grade:<10}")
            stats=calculate_class_analytics(cid,student_ids)
            print("-"*60)
            print("Class Mean Average:{stats['average']}% | Evaluated Students: {stats['total_students']}")
        elif choice=="3":
            eval_id=input("Enter Evaluation ID to Update (e.g., EVAL-XXXXXX): ").strip()
            new_score=input("Enter New Score (press Enter to skip): ").strip()
            score_val=float(new_score) if new_score else None
            if update_evaluation(eval_id,score=score_val):
                print("[SUCCESS] Record {eval_id} updated successfully.")
            else:
                print("[ERROR] Record not found or invalid data.")
        elif choice=="4":
            eval_id=input("Enter Evaluation ID to Delete: ").strip()
            if delete_evaluation(eval_id):
                print("[SUCCESS] Record {eval_id} deleted successfully.")
            else:
                print("[ERROR] Evaluation ID not found.")
        elif choice=="5":
            break
# analytics.py - Performance Analytics Module for Teachers

def calculate_metrics(marks,passing_mark=40):
    total_students=len(marks)
    if total_students==0:
        return None
    class_average=sum(marks)/total_students
    highest_score=max(marks)
    lowest_score=min(marks)
    pass_count=sum(1 for score in marks if score>=passing_mark)
    fail_count=total_students-pass_count
    return {"average":round(class_average,2),"highest":highest_score,"lowest":lowest_score,"pass_count":pass_count,"fail_count":fail_count}
def get_grade_distribution(marks):
    grades={"A":0,"B":0,"C":0,"D":0,"F":0}
    for score in marks:
        if score>=90:
            grades["A"]+=1
        elif score>=75:
            grades["B"]+=1
        elif score>=50:
            grades["C"]+=1
        elif score>=40:
            grades["D"]+=1
        else:
            grades["F"]+=1
    return grades
def display_dashboard(marks,passing_mark=40):
    metrics=calculate_metrics(marks,passing_mark)
    if not metrics:
        print("No student data available.")
        return
    print("\n========================================")
    print("       CLASS PERFORMANCE REPORT         ")
    print("========================================")
    print(f"Class Average : {metrics['average']}%")
    print(f"Highest Score : {metrics['highest']}%")
    print(f"Lowest Score  : {metrics['lowest']}%")
    print(f"Pass/Fail     : {metrics['pass_count']} Passed / {metrics['fail_count']} Failed")
    print("----------------------------------------")
    print("\nCHART 1: CLASS GRADE DISTRIBUTION")
    print("---------------------------------")
    grades=get_grade_distribution(marks)
    for grade, count in grades.items():
        bar="■"*count
        print(f"Grade {grade} | {bar} ({count})")
    print("---------------------------------")
def display_student_progress(student_name,exams,marks):
    print("\nCHART 2:{student_name.upper()}'S PROGRESS OVER TIME")
    print("---------------------------------")
    for i in range(len(exams)):
        exam_name=exams[i]
        score=marks[i]
        visual_blocks="█"*(score//5) 
        print("{exam_name:<12} ({score}%) | {visual_blocks}")
    print("---------------------------------")
    print("Scale: Each '█' represents 5% marks.")
    print("========================================")
