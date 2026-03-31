Diabetes Predictor App

A web application that predicts the likelihood of diabetes using a Machine Learning model trained on health-related data. 

Check out the live website https://diabetes-predictor-exun.onrender.com/

Features
* Input health details through a user-friendly form
* Predicts diabetes using a trained Logistic Regression model
* Handles both numerical and categorical inputs
* Real-time prediction results
* Clean and simple interface

Tech Stack
* Python
* Flask
* Pandas
* Scikit-learn
* HTML, CSS

Input Parameters
* Age
* BMI
* Fasting Sugar
* HbA1c
* Gender
* Hypertension (Tension)
* Family History

Model Training
* Dataset loaded using Pandas
* Missing values handled by removing null rows
* Features and target separated
* Categorical variables converted using Pandas get_dummies() (one-hot encoding)
* Data split into training and testing sets using train_test_split
* Model trained using Logistic Regression
* Model evaluated using classification report
* Trained model saved using pickle (diab.pkl)

How It Works
1. User enters health details in the web form
2. App collects numerical and categorical inputs
3. Categorical inputs are transformed using one-hot encoding logic
4. Inputs are combined into a structured feature vector
5. Pre-trained model (diab.pkl) is loaded
6. Model predicts diabetes outcome
7. Result is displayed to the user

Model Details
* Algorithm: Logistic Regression
* Trained using Scikit-learn
* Uses both numerical and encoded categorical features
* Outputs binary classification (Yes / No)
