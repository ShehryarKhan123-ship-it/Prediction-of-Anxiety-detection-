Student Anxiety Detection Project

This project aims to detect student anxiety levels using machine learning techniques.

1. Introduction

Problem Statement: Student anxiety is a growing concern, impacting academic performance and overall well-being. This project seeks to develop a model that can effectively predict student anxiety levels based on key factors.

Methodology:
Data Collection:
Utilized a dataset containing information about students, including timestamp, age, and study hours.
Modified the dataset to include anxiety-related factors such as Satisfaction with Life Scale (SWLS), Generalized Anxiety Disorder (GAD), and Social Phobia (SP).

Data Preprocessing:
Cleaned and prepared the dataset for model training.
Handled missing values and outliers.

Model Development:
Developed three separate Linear Regression models:
Model 1: Predicted anxiety based on timestamp.
Model 2: Predicted anxiety based on age.
Model 3: Predicted anxiety based on study hours.

Model Evaluation:
Evaluated the performance of each model using appropriate metrics (e.g., R-squared, Mean Squared Error).
Visualized the model predictions and compared their performance.

2. Project Structure

data/: Contains the original and modified datasets (e.g., original_data.csv, modified_data.csv).
src/: Contains the source code files:
data_preprocessing.py: Handles data cleaning, transformation, and feature engineering.
model_training.py: Trains and evaluates the three Linear Regression models.
visualization.py: Creates visualizations for model predictions and comparisons.
results/: Stores the model outputs, visualizations, and evaluation metrics.

3.Results
The project includes visualizations that compare the predictions of the three Linear Regression models.
The results section provides insights into the factors that most significantly influence student anxiety levels based on the model predictions.

4.Future Work
Explore more sophisticated machine learning models, such as Support Vector Regression or Random Forest.
Incorporate additional features, such as academic performance, sleep quality, and social support.
Develop a more robust and user-friendly interface for the anxiety detection system.
