totalCourses=3
courses=[]
marks=[]
inputList={}
def course():
    course_internal=input("Enter name of the courses : ")
    courses.append(course_internal)
    return courses

def scores(totalSubjects):
    for j in range(0,totalSubjects):
        mark_internal=int(input("Enter student marks : "))
        marks.append(mark_internal)
        return marks
    
def avg():
    print("calculating average...")
    return sum(marks)/totalSubjects

def avg_print():
    print("Displaying the results...")
    print("The average is ",avg())

ch = 'yes'

while(ch=='yes'):
    
    for i in range(0,totalCourses):
        courses=course()
        totalSubjects=int(input("Enter total subjects the students appeared for : "))
        marks=scores(totalSubjects)
        inputList(courses,marks)
        


    
    ch=input("Do you want ot start again? 'yes/no'")
