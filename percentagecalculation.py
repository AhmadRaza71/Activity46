print("Enter marks obtained in 4 subjects:")
math = int(input("Math: "))
science = int(input("Science: "))
english = int(input("English: "))
history = int(input("History: "))
sum = math + science + english + history
perc = (sum / 400) * 100
print("end = Percentage Mark = ")
print(perc)