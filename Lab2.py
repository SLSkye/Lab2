

def display_main_menu():
    print("Enter some numbers separated by commas(e.g. 5, 67, 32)")

def get_user_input():
    userIn = input()
    afterSplit = userIn.split(",")
    ListFloats= list(map(float,afterSplit))
    return ListFloats
    
def calc_average_temperature(ListFloats):
    average = sum(ListFloats)/len(ListFloats)
    return average
def calc_min_max_temperature(ListFloats):
    ListFloats.sort()
    mini = ListFloats[0]
    maxi = ListFloats[-1]
    return mini, maxi

def calc_median_temperature(ListFloats):
    ListFloats.sort()
    reminder = len(ListFloats)%2
    if reminder > 0:
        med = (len(ListFloats)/2) - 0.5
        medint = int(med)
        median = ListFloats[medint]
    else:
        med1 = (len(ListFloats)/2) -1
        med2 = (len(ListFloats)/2)  
        medint1 = int(med1)
        medint2 = int(med2)
        m1 = ListFloats[medint1]
        m2 = ListFloats[medint2]

        median = ((m1+m2)/2)

    return median

    
def main():
    display_main_menu()
    numberList = get_user_input()
    print(numberList)

    averageTemp = calc_average_temperature(numberList)
    print("Average is " + str(averageTemp))    

    minTemp, maxTemp = calc_min_max_temperature(numberList)
    Minimum = int(minTemp)
    Maximum = int(maxTemp)
    print("Min temp: " + str(Minimum))
    print("Max temp: " + str(Maximum))

    calculatedMedian = calc_median_temperature(numberList)
    print("Median is " + str(calculatedMedian))

if __name__ == "__main__":
    main()