from fastapi import FastAPI
app = FastAPI()

#Welcome massages
@app.get("/")
def root():
    return {"message": "Welcome!"}


#First methode - About 
@app.get("/abouts")
def about_me():
    return {
        "Name": "Rayaan Tasnim",
        "Age":"13",
        "Class":"Seven (7)", 
        "GitHub Repo": "74",
        "CodeForces Rating": "519",
    }

#Second methode - My courses
@app.get("/course")
def my_courses():
    return {
        "School": "Unique Progressive School",
        "Dreamers Academy: Track": "Professional Programmer",
        "Level": "Python OOP",
        "Class": "Object Oriented Programming",
    }

#Third methode - Student
@app.get("/student")
def student():
    return{
        "My name": "Rayaan Tasnim",
        "Age":"13",
        "My Course":"Professional Programmer",
        "My level" : "Python OOP"
    }