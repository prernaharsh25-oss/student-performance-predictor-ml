#loading data and seperating input and output
import pandas as pd

#loading dataset from our already existing csv file 
df=pd.read_csv("student_data_realistic.csv")

#to show first 5 rows for preview purpose
print("Dataset Preview:")
print(df.head())

#Input data
X=df[["study_hours", "attendance", "assignments_completed", "internal_marks", "sleep_hours"]]

#Output or the target data
y=df["final_marks"]
#printing the input and output data
print("\nInput Features:")
print(X.head())
print("\nTarget Output:")
print(y.head())


#Spliting data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("\nTraining data shape:",X_train.shape)
print("Testing data shape:", X_test.shape)

#using linear regression to train the model so that it can learn patterns
from sklearn.linear_model import LinearRegression
#Creating model
model = LinearRegression()
#Training model
model.fit(X_train, y_train)
print("\nModel trained successfully!")


#Predict marks for the data stored for testing purpose
y_pred = model.predict(X_test)
print("\nPredicted Marks:")
print(y_pred)

#checking prediction accuracy of the model
from sklearn.metrics import mean_absolute_error, r2_score
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("\nModel Evaluation:")
print("Mean Absolute Error:", mae)
print("R2 Score:", r2)

# Predicting marks for a new student
print("\nEnter student details to predict marks:")

study_hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance (%): "))
assignments = float(input("Enter assignments completed: "))
internal_marks = float(input("Enter internal marks: "))
sleep_hours = float(input("Enter sleep hours: "))

# Creating DataFrame for input
new_student=pd.DataFrame([[study_hours, attendance, assignments, internal_marks, sleep_hours]], columns=["study_hours", "attendance", "assignments_completed", "internal_marks", "sleep_hours"])
predicted_marks = model.predict(new_student)

print("\nPredicted Final Marks:", round(predicted_marks[0], 2))

#creating a graphic representation of the model
import matplotlib.pyplot as plt
plt.scatter(df["study_hours"], df["final_marks"])
plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.title("Study Hours vs Final Marks")
plt.show()
