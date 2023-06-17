# Bus bara simple project : condition --age
# input tk and call int type data and input function used!
age = int(input("Please Enter Your Real Age :",))
# used to condition : if- else - elif
if age <= 5:
    print("Paid Please : 00 tk only")
elif 5 < age <= 20:
    print("Paid Please : 15 tk only")
elif 20 < age <= 40:
    print("Paid Please : 30 tk only")
elif 40 < age <= 55:
    print("Paid Please : 40 tk only")
elif 55 < age <= 70:
    print("Paid Please : 35 tk only")
elif 70 < age <= 100:
    print("Paid Please : 25 tk only")
else:
    print("Paid Please : 05 tk only")

print("Thank You Customer")
