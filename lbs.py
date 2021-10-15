#lbs = kg * 2.2
#kg = lbs / 2.2
def convert(weight, unit):
    if unit == "K":
        lbs = weight * 2.2
        print("Weight in Lbs:", lbs)
    elif unit == "L":
        kg = weight / 2.2
        print("Weight in Kg:", kg)

input1 = float(input("Weight: "))
input2 = input("(K)g or (L)bs: ").upper()
convert(input1, input2)
