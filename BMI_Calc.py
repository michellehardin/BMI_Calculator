height_ft = int(input("Input height feet: "))
height_inches = int(input("Input height inches: "))
weight = float(input("What is your weight in pounds?"))

class BMI_Calculator:
    def __init__(self, height_ft, height_inches, weight):
        self.height = (((height_ft * 12) + height_inches) * 0.025) ** 2
        self.weight = 0.45 * weight
        self.BMI = 0

    def calc_BMI(self):
        self.BMI = self.weight / self.height
        print("BMI: ", self.BMI)

    def determine(self):
        if self.BMI < 18.5:
            print("Underweight")
        elif (self.BMI >= 18.5 and self.BMI < 25):
            print("Normal")
        elif (self.BMI >= 25 and self.BMI < 30):
            print("Overweight")
        elif (self.BMI > 30):
            print("Obese")
        else:
            print("Uh-oh")

patient = BMI_Calculator(height_ft, height_inches, weight)
patient.calc_BMI()
patient.determine()
