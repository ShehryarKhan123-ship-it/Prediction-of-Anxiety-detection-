import pandas as pd
import numpy as  np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data=pd.read_csv('anxiety.csv',encoding='latin-1')
print(data.head())

# Assuming normalized scores:
GAD_T_score = 0.7  # Normalized to 0-1
SWL_T_score = 0.3  # Normalized to 0-1
SPIN_T_score = 0.8  # Normalized to 0-1

# Assign weights (adjust as needed):
GAD_T_weight = 0.3
SWL_T_weight = 0.5
SPIN_T_weight = 0.4

# Calculate weighted average
anxiety_level = (GAD_T_score * GAD_T_weight) + (SWL_T_score * SWL_T_weight) + (SPIN_T_score * SPIN_T_weight)

print("Anxiety Level:", anxiety_level)

X = data[['Age', 'Timestamp','Hours',]]  
y = data['anxiety_level']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Visualize the results (assuming a single feature for simplicity)
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('Feature')
plt.ylabel('Anxiety Level')
plt.title('Linear Regression Model')
plt.show()