# Student Performance Predictor using Machine Learning

## Description
This project is a machine learning-based system that predicts a student's final marks based on various academic and lifestyle factors. The model analyzes inputs such as study hours, attendance, assignments completed, internal marks, and sleep hours to estimate the final exam performance of a student.
It is built using Python and uses a Linear Regression model for prediction.

---

## Objectives
- To build a machine learning model for predicting student performance
- To understand the relationship between study habits and academic results
- To apply regression techniques on structured data
- To create a simple and usable prediction system

---

## Features
- Predicts final marks based on multiple input factors
- Uses real-like dataset for training
- Provides accurate and realistic predictions
- Allows user to enter custom input via terminal
- Includes graphical visualization of data trends

---

## Inputs Required
The model requires the following inputs:

| Feature | Description |
|--------|------------|
| study_hours | Number of hours studied |
| attendance | Attendance percentage |
| assignments_completed | Number of assignments completed |
| internal_marks | Marks in internal exams |
| sleep_hours | Average sleep hours |

---

## Output Generated

The system generates the **predicted final marks** of a student based on the input values provided.

The output is a **numerical value (marks out of 100)**.

---

### Example Input
                Enter student details to predict marks:
                Enter study hours: 6
                Enter attendance (%): 85
                Enter assignments completed: 8
                Enter internal marks: 20
                Enter sleep hours: 7


---

### Corresponding Output
                Predicted Final Marks: 76.48


---

### Explanation

The model analyzes the relationship between the input features and predicts the most likely final marks using the trained Linear Regression model.

The output may contain decimal values, which are rounded for better readability.
