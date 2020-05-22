def main():
    value = 11
    changevalue(value)
    print(changevalue(value))
    print("The value is ",value)
    value = changevalue(value)
    print("The value now is ",value)

def changevalue(value):
    value=value + 10
    return value

main()
    
    
