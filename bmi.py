name1 = "Fat Man"
height1 = 1.9
weight1 = 110

name2 = "Thin Man"
height2 = 2.6
weight2 = 65

def bmi_calc(name, height, weight):
    bmi = weight / (height * height)
    print(f"{name}'s BMI is {bmi}.")
    if bmi < 25:
        print(f"{name} is not overweight.")
    else:
        print(f"{name} is overweight.")
    if bmi < 18:
        print(f"{name} is underweight.")
    else:
        print(f"{name} is not underweight.")

bmi_calc(name1, height1, weight1)
bmi_calc(name2, height2, weight2)
