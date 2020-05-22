#Student Name : Sandeep Singh
#Student ID : C0727422

import csv

def readData():
    result = {}
    with open("world_cup_champions.txt") as myfile:
        testreader = csv.reader(myfile,delimiter = ",")
        
        for row in testreader :
            key = row[1]
            if key in result:
                result[key].append(row[0])
            else:
                result[key] = [row[0]]

        del result["Country"]
        return result

def output(result):
    print("FIFA World Cup Winners\n")
    print("Country\tWins\tYears")
    print("=======\t====\t=====")

    newresult = dict(sorted(result.items()))
    for key,value in newresult.items() :
         tempValues = ", ".join(value)
         print(key+"\t"+str(len(value))+"\t"+tempValues)
        
def main():
    data = readData()
    output(data)
main()

#Input Data is as follows :
#Year,Country,Coach,Captain
#1930,Uruguay,Alberto Suppici,José Nasazzi
#1934,Italy,Vittorio Pozzo,Gianpiero Combi
#1938,Italy,Vittorio Pozzo,Giuseppe Meazza
#2002,Brazil,Luiz Felipe Scolari,Cafu
#2006,Italy,Marcello Lippi,Fabio Cannavaro
#2010,Spain,Vicente del Bosque,Iker Casillas
#2014,Germany,Joachim Löw,Philipp Lahm
