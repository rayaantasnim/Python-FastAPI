from fastapi import FastAPI
app = FastAPI()
data = [
    {
        "student_id": 1, 
        "name": "Benjamin Qi Benq", 
        "age": 20, 
        "course": "Python"
    },
    {
        "student_id": 2, 
        "name": "Debjoti Das Soumya", 
        "age": 22, 
        "course": "Data Science"
    },
    {
        "student_id": 3, 
        "name": "Bruce Lee", 
        "age": 21, 
        "course": "Python"
    },
    {
        "student_id": 4, 
        "name": "Neil Armstrong", 
        "age": 19, 
        "course": "Web Development"
    },
    {
        "student_id": 5, 
        "name": "Gennady Korotkevich", 
        "age": 23, 
        "course": "Cyber Security"
    }
]

@app.get("/")
def home():
    return {
        "message": "Welcome !"
    }

# Task 1: Path Parameter
@app.get("/students/{student_id}")
def get_student_by_id(student_id: int):

    for student in data:

        if student["student_id"] == student_id:
            return student
        
    return {
        "message": "Student not found"
    }

# Task 2: Query Parameter
@app.get("/students")
def get_students_by_course(course: str):
    filtered_students = []

    for student in data:

        if student["course"].lower() == course.lower():
            filtered_students.append(student)
            
    if len(filtered_students) == 0:
        return {
            "message": f"No students found enrolled in {course}"
        }
    return filtered_students

# Task 3: Combine Parameters
@app.get("/students/verify/{student_id}")
def verify_student_course(student_id: int, course: str):
    for student in data:

        if student["student_id"] == student_id:

            if student["course"].lower() == course.lower():
                return student
            
            else:
                return {
                    "message": "Student found, but enrolled in a different course"
                }
    return {
        "message": "Student not found"
    }
