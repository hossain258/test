height = float(input("Enter your height in m:  "))
weight = float(input("Enter your weight in kg :  "))
bmi = round(weight / height ** 2)
if bmi <18.5 :
    print(f"your bmi is  {bmi}  ,you are underweight")
elif bmi < 25 :
    print(f"your bmi is  {bmi}  ,you have normal weight")
elif bmi < 30 :
    print(f"your bmi is  {bmi}  ,you are slightly over weight")
elif bmi < 35 :
    print(f"your bmi is  {bmi}  ,you are obse")
else:
    print(f"your bmi is  {bmi}  ,you are clinically obse")

    