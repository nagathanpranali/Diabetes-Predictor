#import lib
from pickle import load

#load the model
with open("diab.pkl", "rb") as f:
	model = load(f)

#predict
age = float(input("Enter age "))
bmi = float(input("Enter BMI "))
fs = float(input("Enter fasting sugar "))
hba1c = float(input("Enter hba1c "))

d0 = [age, bmi, fs, hba1c]

gender = int(input("Gender: 1 for female and 2 for male "))
if gender == 1:
	d1 = [1,0]
else:
	d1 = [0,1]

tension = int(input("HyperTension: 1 for No and 2 for Yes "))
if tension == 1:
	d2 = [1,0]
else:
	d2 = [0,1]


fmly = int(input("Family History: 1 for No and 2 for Yes "))
if fmly == 1:
	d3 = [1,0]
else:
	d3 = [0,1]

d = [d0 + d1 + d2 + d3]
print(d)

res = model.predict(d)
print(res)
