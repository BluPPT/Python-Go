#km = miles * 1.6
#miles = kg / 1.6
def convert(number, unit):
    if unit == "K":
        miles = number * 1.6
        print("Distance in Miles:", miles)
    elif unit == "M":
        km = number / 1.6
        print("Distance im Km:", km)

input1 = float(input("Distance: "))
input2 = input("(K)m or (M)iles: ").upper()
convert(input1, input2)
