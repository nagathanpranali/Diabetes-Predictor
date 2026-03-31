#import lib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from pickle import dump

#load the data
data = pd.read_csv("diabetes.csv")
print(data)

#check for null data
print(data.isnull().sum())
data.dropna(inplace=True)
print(data.isnull().sum())

#features and target
features = data.drop(["Diabetes"], axis="columns")
target = data["Diabetes"]
print(features)
print(target)

#handle cat data
nfeatures = pd.get_dummies(features)
print(nfeatures)
#age bmi fs hbA1c gen_f gen_m hy_no hy_y fmly_no fmly_yes

#train and test
x_train, x_test, y_train, y_test = train_test_split(nfeatures.values, target)

#model
model = LogisticRegression()
model.fit(x_train, y_train)

#performance
cr = classification_report(y_test, model.predict(x_test))
print(cr)
print(data["Diabetes"].value_counts())

#model save
with open("diab.pkl", "wb") as f:
	dump(model, f)
	print("model saved")














