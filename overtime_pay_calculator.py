#INSTRUCTION: Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
#The code used is attached below
hrs = input("Enter Hours:")
h = float(hrs)
rate = input ("What is your rate per hour")
rate_per_hour = float (rate)
if h > 40:
    extra_hour = float (h - 40)
    extra_pay = float(rate_per_hour * 1.5 * extra_hour)
    standard_pay = float (rate_per_hour * 40)
    gross_pay = extra_pay + standard_pay
else: gross_pay = rate_per_hour * h
print (gross_pay)
