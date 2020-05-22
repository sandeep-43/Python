#write a program in python to map an emp id to her/his name using intermediate key:value of salary and name .
#For example, given a key: value of 1:20000 and another key:value of 20000:"John", your program should return
# a value of John when a key of 1 is entered.



id_sal = {"1" : 20000, "2" : 26000, "3" : 31000, "4":29000}
print(id_sal)
print(id_sal["2"])
sal_nm = {20000 : "John", 26000 : "Salim", 31000 : "Alice", 29000:"Nicole"}
print(sal_nm)
print("The employee with id \"2\" is: " + sal_nm[id_sal["2"]])

