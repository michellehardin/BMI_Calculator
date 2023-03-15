class BMI_Calculator:
    def calculate(h_ft, h_in, w):
        if (h_ft < 1 or h_ft > 10):
            print("Error: Height feet outside of the range [1, 10]")
            return 0
        elif (h_in < 0 or h_in > 11):
            print("Error: Height inches outside of the range [0, 11]")
            return 0
        elif (w <= 0 or w > 1400):
            print("Error: Weight outside of the range (0, 1400]")
            return 0
        else:
            BMI = (0.45 * w)/((((h_ft * 12) + h_in) * 0.025) ** 2)
            return BMI

    def determine(BMI):
        print("BMI: ", BMI)

        if BMI > 0 and BMI < 18.5:
            print("Underweight")
        elif (BMI >= 18.5 and BMI < 25):
            print("Normal")
        elif (BMI >= 25 and BMI < 30):
            print("Overweight")
        elif (BMI >= 30):
            print("Obese")
        else:
            print("Uh-oh, outside of bounds") #just in case a zero gets by


#Input height feet, inches, and weight
#Plan: have a drop down menu for height feet and inches in web interface -- thus integer type
#Add loop so that no input is invalid
height_ft = int(input("Input height feet: "))
height_inches = int(input("Input height inches: "))
weight = float(input("What is your weight in pounds?"))

#Check input and if valid, return a BMI greater than 0.
BMI_num = BMI_Calculator.calculate(height_ft, height_inches, weight)

#If 0, exit program. Otherwise, determine the BMI classification.
if BMI_num == 0:
    print("Exit")
else:
    BMI_Calculator.determine(BMI_num)

#Testing Values
#BMI_Calculator.determine(18.5)
