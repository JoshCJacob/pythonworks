

#BMI =weight_in_kg/(height_in_meter)**2

weight_in_kg=int(input("enter the weight in kg:"))

height_in_cm=int(input("enter the height in in cm:"))

height_in_meter=height_in_cm/100

BMI=weight_in_kg/height_in_meter**2

BMI=round(BMI)

print(BMI)


if BMI<19:#0-18 range

    print("Under Weight")

elif BMI<25:#19-24 range

    print("Normal Weight")

elif BMI<30:#25-30 range

    print("Overweight") 

elif BMI>=30:#>30 

    print("Obese")           

# print under weight if bmi<19
# print normal weight if bmi 19 to <25
# print overweight if bmi 25 to <30
# print obese if bmi >=30