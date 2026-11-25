#kilometers in Miles
kilometers=float(input("Enter kilometers:"))
print("kilometers in Miles:",kilometers*0.1621324)

# Miles into kilometers

miles=float(input("Enter miles:"))
print("Miles into kilometers:",miles*1.60934)

# Celsius to fahrenheit

celsius=float(input("Enter celsius:"))
fahrenheit=(celsius*9/5) +32
print("celsius to fahrenheit:", fahrenheit)

# fahrenheit to celsisus
fahrenheit=float(input("Enter fahrenheit:"))
celsius=(fahrenheit-32)*5/9
print("fahrenheit to celsisus:", celsius)

#BMI Calcultor

weight=float(input("Enter your weight in kgs:"))
height=float(input("Enter your height in cm"))
height=height/100

bmi=weight/(height**2)

print(f"your BMI is {bmi:.2f}")

if bmi <18.5:
    print("you are  underwight, consume colories mate")
elif 18.5<=bmi<24.9:
    print("You weight is nomral.")
elif 25<=bmi<30:
    print("overwight go to gym buddy.")
else:
     print("Category: Obesity")