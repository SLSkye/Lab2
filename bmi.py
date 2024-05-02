def calculate_bmi(height, weight):
    print("Height =" + str(height))
    print("Weight =" + str(weight))
    
    bmi=weight/(height*height)

    print("BMI is " + str(bmi))

    if  bmi< 18.5:
        print("Under Weight")
        retVal = -1
    elif bmi > 25.0:
        print("Over Weight")
        retVal = 1
    else:
        print("Normal Weight")
        retVal = 0

    return retVal
