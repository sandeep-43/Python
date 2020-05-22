#Student Name : Sandeep Singh
#Student ID : C0727422
def inputCourse():
    course = input("Enter the name of the course : ")
    return course

def inputScores():
    scores = []
    studentCount = int(input("How many students took the test : "))
    for i in range(0,studentCount):
        score = int(input("Enter score in subject {} : ".format(i+1)))
        scores.append(score)
    return scores

def calcAverage(marks):
    average = sum(marks)/len(marks)
    return average

def printAverage(marks):
    print("The average test score is :",calcAverage(marks))
    
def main():
    #student = {}
    ch = 'no'
    noOfCourses = 3
    while ch == 'no':
        #student.clear()
        for i in range (0,noOfCourses):
            course = inputCourse()
            marks = inputScores()
            #student[course]= marks
            printAverage(marks)
            print()
        #print(student)
        ch = input("Do you want to end program? (Enter no to process a new set of scores): ").lower()
main()
