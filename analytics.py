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
    print(f"Class Average :{metrics['average']}%")
    print(f"Highest Score :{metrics['highest']}%")
    print(f"Lowest Score  :{metrics['lowest']}%")
    print(f"Pass/Fail     :{metrics['pass_count']} Passed / {metrics['fail_count']} Failed")
    print("----------------------------------------")
    print("\nCHART 1: CLASS GRADE DISTRIBUTION")
    print("---------------------------------")
    grades=get_grade_distribution(marks)
    for grade, count in grades.items():
        bar="■"*count
        print(f"Grade {grade} | {bar},(count)")
    print("---------------------------------")
def display_student_progress(student_name,exams,marks):
    print(f"\nCHART 2:student_name.upper()'S PROGRESS OVER TIME")
    print("---------------------------------")
    for i in range(len(exams)):
        exam_name=exams[i]
        score=marks[i]
        visual_blocks="█"*(score//5) 
        print(f"{exam_name:<12} ({score}%) | {visual_blocks}")
    print("---------------------------------")
    print("Scale: Each '█' represents 5% marks.")
    print("========================================")
