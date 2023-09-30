#Assignment-1-Control Structures-Question
#print with double quotes
print("Welcome to Assignment-1")

#print with single quotes
print('Welcome to Assignment-1')

#Add
Num1= 10
Num2= 30
add=Num1+Num2
print("Add=", add)

#BMI
bmi=float(input("Enter the BMI Index:"))
if(bmi<16):
    print("Severely Underweight")
elif(bmi<18):
    print("Underweight")
elif(bmi<25):
    print("Normal")
else:
    print("Overweight")