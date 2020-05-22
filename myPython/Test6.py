course=[]
noOfCourses = 3
ch= "Yes"

def courses():
    tempCourse=input("Enter the name of the course : ")
    course.append(tempCourse)
    
    
def scores_in():
    score=[]
    totalStudents= int(input("Enter number of students who took the test : "))
    for i in range(0,totalStudents):
        tempList=int(input("Enter their score : "))
        score.append(tempList)
    print_avg(score)


def avg(scoreList):
    return sum(scoreList)/len(scoreList)
    
         
def print_avg(scoreList):
    print("The avergae test score is : ", avg(scoreList))
    
while(ch=="yes" or ch=="Yes" or ch=="y" or ch=="Y"):
    
    for j in range(0,noOfCourses):
        courses()
        scores_in()
        print()
    ch= input("Do you want to re-run the program ? (Yes/No) : ")
