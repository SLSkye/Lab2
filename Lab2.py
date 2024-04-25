print("ET0735 (DevOps for AIOT) - Lab 2 - Introduction to Python")
def funcName(parameter1,parameter2):
    print("this is a dummy function")
    return 10

def display_main_menu():
    print("Enter some numbers separated by commas(e.g. 5, 67, 32)")

def get_user_input():
    userIn = input()
    afterSplit = userIn.split(",")
    ListFloats= list(map(float,afterSplit))
    print(ListFloats)
    return ListFloats

def calc_average_temperature(ListFloats):
    average = sum(ListFloats)/len(ListFloats)
    return average

def main():
    display_main_menu()
    numberList = get_user_input()
    print(numberList)

    averageTemp = calc_average_temperature(numberList)
    print(averageTemp)    


if __name__ == "__main__":
    main()