def YourGrade():
    grade = int(input("Enter in your grade % that is 0-100: "))
    if grade > 100 or grade < 0:
        'Error. Grade is not in the range'
    elif grade >= 90:
        print('Your grade is A')
    elif grade >= 80:
        print('Your grade is B')
    elif grade >= 70:
        print('Your grade is C')
    elif grade >= 60:
        print('Your grade is D')
    else:
        print('Your grade is F')

YourGrade()
