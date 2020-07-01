def check_marks(m):
    if m >= 90:
        return print(True)
    elif m < 90:
        raise Exception("Marks less than 90 ")

for i in range(0,1):
    marks = int(input("Enter the marks\n"))
    check_marks(marks)
