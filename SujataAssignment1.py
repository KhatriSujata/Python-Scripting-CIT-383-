# Program written by Sujata Khatri.
# This program  computes the average number of hours a student spends on Scripting and
# Math assignments over a long weekend.

# It ask the user to provide how many
# students there are in the class as well as the number of days in the long week
# and stores them in list

TotalStudent = int(input("Enter the number of students:"))
# while loop to enter correct number of student and days as mentioned
while TotalStudent <= 0:
    TotalStudent = int(input("Enter the number of student(must be greater than 1):"))

TotalDays = int(input("Enter the number of days in the long week:"))
while TotalDays <= 0 or TotalDays > 7:
    TotalDays = int(input("Enter the number of days in the long week(must be 1-7):"))
# list for storing the numbers and hours
ScriptingList = []
MathList = []

# for loop for each student #for loop for each day
for i in range(1, TotalStudent + 1):
    for j in range(1, TotalDays + 1):
        ScriptingHours = float(input("Enter the number of hours spent on scripting:"))
        # while loop to enter correct number of Scripting and Math hours as mentioned
        while 0 > ScriptingHours or ScriptingHours > 9:
            ScriptingHours = float(input("Enter the number of hours spent on scripting(should be positive and should not exceed 9):"))
        MathHours = float(input("Enter the number of hours spent on math:"))
        while 0 > MathHours or MathHours > 9:
            MathHours = float(input("Enter the number of hours spent on math(should be positive and should not exceed 9):"))
        # append to add scripting and math hours to the list created above
        ScriptingList.append(ScriptingHours)
        MathList.append(MathHours)

# setting initial number to zero to hold sum of hours all students spend on scripting and math
OverallScriptingTime = 0
OverallMathTime = 0
# creating output labels with print statement
print("Student" + "           " + "Avg Scripting Time" + "      " + "Avg. Math Time" + "    " + "Most Time Spent")
print("------------      -----------------        --------------    -------------")

# for loop for each number of student.
# setting initial number to zero to hold sum of hours a student spend on scripting and math.
for e in range(1, TotalStudent + 1):
    TotalScriptingTime = 0
    TotalMathTime = 0
    # for loop for each day.
    # using pop for adding scripting hours for current day to student's scripting sum by removing the first elements
    # from the list.
    # using pop adding math hours for current day to student's math sum by removing the first elements from the list.
    # if and elif to determine most time spent.
    for f in range(1, TotalDays + 1):
        TotalScriptingTime = TotalScriptingTime + ScriptingList.pop(0)
        TotalMathTime = TotalMathTime + MathList.pop(0)
    if TotalScriptingTime > TotalMathTime:
        MostTimeSpent = "Scripting"
    elif TotalScriptingTime < TotalMathTime:
        MostTimeSpent = "Math"
    else:
        MostTimeSpent = "Same"
    AvgScriptingTime = TotalScriptingTime / TotalDays  # computing average scripting time.
    AvgMathTime = TotalMathTime / TotalDays  # computing average math time.

    print("{:>3} {:>23.2f} {:>25.2f}        {}".format(e, AvgScriptingTime, AvgMathTime,
                                                       MostTimeSpent))  # print statement to print required output.

    OverallScriptingTime = OverallScriptingTime + TotalScriptingTime  # computing overall scripting time.
    OverallMathTime = OverallMathTime + TotalMathTime  # computing overall scripting time.

# computing overall scripting average.
# computing overall math average.
# if and elif to determine most time spent.
overallScriptingAvg = OverallScriptingTime / (TotalDays * TotalStudent)
overallMathAvg = OverallMathTime / (TotalDays * TotalStudent)
if overallScriptingAvg > overallMathAvg:
    MostTimeSpent = "Scripting"
elif overallScriptingAvg < overallMathAvg:
    MostTimeSpent = "Math"
else:
    MostTimeSpent = "Same"
# print statement to print required output.
print("____________      _________________        ______________    _____________")
print("Overall Avg. {:>14.2f} {:>25.2f}        {}".format(overallScriptingAvg, overallMathAvg, MostTimeSpent))





