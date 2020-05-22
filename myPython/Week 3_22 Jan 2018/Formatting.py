
instructor = input ("Enter the professor's name : ")
subject = input ("Enter the  subject name : ")
term = input ("Enter the term : ")
year = '1998'
#print
formatting = "{} will teach {} in {}"
#formatting2 = "{1} will be taught by {0} in term {2}."
#print(formatting.format(instructor,subject,term))
#print(formatting2.format(instructor,subject,term))
print(formatting.format(subject,term,instructor))
