#from application.bmi_category import determine_category

def test_error():
    bmi = 0
    assert determine_category(bmi) == "ERROR"

def test_underweight1():
    bmi = 0.1
    assert determine_category(bmi) == "Underweight"

def test_underweight2():
    bmi = 10
    assert determine_category(bmi) == "Underweight"

def test_underweight3():
    bmi = 18.4
    assert determine_category(bmi) == "Underweight"

def test_normal1():
    bmi = 18.5
    assert determine_category(bmi) == "Normal"

def test_normal2():
    bmi = 21
    assert determine_category(bmi) == "Normal"

def test_normal3():
    bmi = 24.9
    assert determine_category(bmi) == "Normal"

def test_overweight1():
    bmi = 25
    assert determine_category(bmi) == "Overweight"

def test_overweight2():
    bmi = 27
    assert determine_category(bmi) == "Overweight"

def test_overweight3():
    bmi = 29.9
    assert determine_category(bmi) == "Overweight"

def test_obese(): 
    bmi = 30
    assert determine_category(bmi) == "Obese"
