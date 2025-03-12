# let the user to enter the weight ( in kg ) and convert the input to float type for storage
weight = float (input("please enter your weight in kg: "))
# let the user to enter the height ( in m ) and convert the input to float type for storage 
height = float (input("please enter your height in m: ") )
# Pseudocode :  Calxulate the BMI value according to BMI formula
bmi = weight / (height ** 2)
# Determine the category of the BMI belongs to
if bmi < 18.5:
    result = "underweight" 
    
elif bmi > 30:
    result = "obese"

    
else:
    result = "normal weight"
# output the BMI and which kind of BMI the person is 
output = "The person's BMI is " + str(bmi) + ", and they should be considered " + result + "."
print(output)

    


