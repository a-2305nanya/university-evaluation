from typing import List,Optional
import uuid
EVALUATION_DB={}
def calculate_letter_grade(pct:float)->str:
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
    if score<0 or score>max_score:
        raise ValueError(f"Score must be between 0 and {max_score}.")
    if weight<=0:
        raise ValueError("Weight must be greater than 0.")
    eval_id=f"EVAL-{str(uuid.uuid4())[:6].upper()}"
    EVALUATION_DB[eval_id]={"eval_id":eval_id,"student_id":student_id,"course_id":course_id,"title":title,"score":float(score),"max_score":float(max_score),"weight":float(weight)}
    return eval_id
def get_student_evaluations(student_id:str,course_id:Optional[str]=None)->List[dict]:
    return [e for e in EVALUATION_DB.values() if e["student_id"]==student_id and (course_id is None or e["course_id"]==course_id)]
def update_evaluation(eval_id:str,score:Optional[float]=None,title:Optional[str]=None,weight:Optional[float]=None)->bool:
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
    if eval_id in EVALUATION_DB:
        del EVALUATION_DB[eval_id]
        return True
    return False
def calculate_student_course_score(student_id:str,course_id:str)->Optional[float]:
    evals=get_student_evaluations(student_id,course_id)
    if not evals:
        return None
    total_weighted=sum((e["score"]/e["max_score"])*100*e["weight"] for e in evals)
    total_weight=sum(e["weight"] for e in evals)
    return round(total_weighted/total_weight,2) if total_weight > 0 else 0.0
def calculate_class_analytics(course_id:str,all_student_ids:List[str])->dict:
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
    course_id=input("Enter Course ID (e.g., CS101): ").strip().upper()
    evals=get_student_evaluations(student_id,course_id)
    if not evals:
        print(f"\n[!] No evaluation records found for course '{course_id}'.")
        return
    print(f"\n---Assessment Breakdown for {course_id}---")
    for e in evals:
        print(f" • {e['title']}: {e['score']}/{e['max_score']} (Weight: {e['weight']})")
    overall=calculate_student_course_score(student_id,course_id)
    grade=calculate_letter_grade(overall)
    gpa=calculate_gpa(overall)
    stats=calculate_class_analytics(course_id,all_student_ids)
    print("\n--- Performance Summary ---")
    print(f"Your Score:{overall}% | Grade:{grade} | GPA:{gpa}")
    print(f"Class Average:{stats['average']}%")
    print(f"Top Class Score:{stats['highest']}%")
def teacher_evaluation_menu(all_students_db:dict):
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
                print(f"[SUCCESS] Record saved with ID: {eval_id}")
            except ValueError as err:
                print(f"[ERROR] Invalid input: {err}")
        elif choice=="2":
            cid=input("Enter Course ID: ").strip().upper()
            student_ids=[uid for uid, data in all_students_db.items() if data.get("role")=="student"]
            print("\n--- Marksheet for {cid} ---")
            print(f"{'Student ID':<15} {'Name':<20} {'Overall Score':<15} {'Grade':<10}")
            print("-"*60)
            for sid in student_ids:
                score=calculate_student_course_score(sid, cid)
                if score is not None:
                    name=all_students_db[sid]["name"]
                    grade=calculate_letter_grade(score)
                    print(f"{sid:<15} {name:<20} {score:<15}% {grade:<10}")
            stats=calculate_class_analytics(cid,student_ids)
            print("-"*60)
            print(f"Class Mean Average:{stats['average']}% | Evaluated Students: {stats['total_students']}")
        elif choice=="3":
            eval_id=input("Enter Evaluation ID to Update (e.g., EVAL-XXXXXX): ").strip()
            new_score=input("Enter New Score (press Enter to skip): ").strip()
            score_val=float(new_score) if new_score else None
            if update_evaluation(eval_id,score=score_val):
                print(f"[SUCCESS] Record {eval_id} updated successfully.")
            else:
                print("[ERROR] Record not found or invalid data.")
        elif choice=="4":
            eval_id=input("Enter Evaluation ID to Delete: ").strip()
            if delete_evaluation(eval_id):
                print(f"[SUCCESS] Record {eval_id} deleted successfully.")
            else:
                print("[ERROR] Evaluation ID not found.")
        elif choice=="5":
            break
