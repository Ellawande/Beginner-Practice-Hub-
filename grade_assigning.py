# INSTRUCTION: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table: Score Grade >= 0.9 A, >= 0.8 B, >= 0.7 C, >= 0.6 D, < 0.6 F. If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
#CODE USED IS ATTACHED BELOW

score = input("Enter Score: ")
s = float (score)
if s >= 0.9: 
    grade = "A"
    print (grade)
elif s >= 0.8:
    grade = "B"
    print (grade)
elif s >=0.7:
    grade = "C"
    print (grade)
elif s >= 0.6:
    grade = "D"
    print (grade)
elif s < 0.6:
    grade = "F"
    print (grade)
else:
    print("You have entered an invalid input")
