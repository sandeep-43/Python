#Name : Sandeep Singh
#Student ID : C0727422

import random

def nameInput(): #A function that allows the student to enter their name
    
    while True:
        name = input("Enter the name of the student : ")
        if all(nm.isalpha() or nm.isspace() for nm in name):
            break
        else:
            print("Invalid name!!! Please re-enter the name correctly")
    return name

def getRandom(): #A function that gets two random numbers, anywhere from 1 to 500.
    num1 = random.randrange(1,500)
    num2 = random.randrange(1,500)
    return num1,num2

def displayEquation(i): #A function that displays the equation and asks the user to enter their answer.
    num1,num2 = getRandom()
    print("\nQ{}. ".format(i+1))
    print(" ",num1,"\n+",num2,"\n-----\n=\n-----")
    while True:
        try :
            userAnswer = int(input("\nAnswer : "))
            break
        except ValueError:
            print("Invalid input format!!! Please re-enter an integer value")
    correctAnswer = num1 + num2
    return userAnswer,correctAnswer

def checkandcollect(): #A function that checks to see if the answer is correct and accumulates the number correct.
    answers = []
    validation = []
    for i in range(0,10):
        userAnswer,correctAnswer = displayEquation(i)
        answers.append(userAnswer)
        if userAnswer == correctAnswer:
            validation.append(0)
        else:
            validation.append(1)
    return answers,validation
        
def results(): #A function that calculates the results
    correct = 0
    answers,validation = checkandcollect()
    for i in range(0,10):
        if validation[i]==0:
            correct += 1
    
    averageCorrect = correct/10
    percentageCorrect = averageCorrect*100
    return correct,averageCorrect,percentageCorrect

def output(name): #A function that displays the student name, the number correct, and the average correct

    correct,averageCorrect,percentageCorrect = results()

    print('\n','-'*10,"Student Report Card",'-'*10)
    print("Student Name :",name)
    print("Total correct answers :",correct)
    print("Average correct answers :",averageCorrect)
    print("Percentage correct answers :",str(percentageCorrect)+"%")
    
def main():
    name = nameInput()
    output(name)
main()
