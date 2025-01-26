def bmi(weight,height):
    val=(weight)/((height)**2)
    if (val<18.5):
        return "underweight"
    if (val>=18.5 and val<=24.9):
        return "normal"
    if (val>=25 and val<=29.9):
        return "overweight"
    if (val>=30):
        return "obese"
    
weight=float(input("Enter the weight:\n"))
height=float(input("Enter the height:\n"))
print(bmi(weight,height))