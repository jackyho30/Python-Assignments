weight = input ("Please enter your weight (kg): ")

height = input ("Please enter your height (cm): ")

height2 = float (height) / 100

bmi = weight / height2 ** 2 

print "Your Body Mass Index (BMI) is = %.1f" % bmi, "kg/m^2"
