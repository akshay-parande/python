import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv('student_scores.csv')
X = data[['Hours_Studied', 'Attendance', 'Internal_Marks']]
y = data['Final_Score']

model = LinearRegression()
model.fit(X, y)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved as model.pkl")
