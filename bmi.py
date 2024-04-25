def calculate_bmi(height, weight):
    print("Height =" + str(height))
    print("Weight =" + str(weight))
    
    bmi=weight/(height*height)

    print("BMI is " + str(bmi))
    return bmi

value=calculate_bmi(weight=57, height=1.73)

if  value< 18.5:
    print("Under Weight")
elif value > 25.0:
    print("Over Weight")
else:
    print("Normal Weight")
