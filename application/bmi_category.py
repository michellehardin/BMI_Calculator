def determine_bmi(w, h_ft, h_in): 
    bmi = round((0.45 * w)/((((h_ft * 12) + h_in) * 0.025) ** 2), 2)  
    return bmi
        
def determine_category(bmi):
    if (bmi > 0 and bmi < 18.5):
        category = "Underweight"
    elif (bmi >= 18.5 and bmi < 25):
        category = "Normal"
    elif (bmi >= 25 and bmi < 30):
        category = "Overweight"
    elif (bmi >= 30):
        category = "Obese"
    else:
        category = "ERROR"

    return category

