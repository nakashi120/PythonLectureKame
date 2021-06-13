age = 23

age_alcohol = 20
age_drive = 18

if age >= age_alcohol:
    print("You can drink beer")
elif age < age_drive:
    print("You cannot even drive")
else:
    print("You are not allowed to drink beer but you can drive only if you have a driver's license")

if not 0 < age < 120:
    print('the value is invalid')

