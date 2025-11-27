<h1 style="font-size: 40px;">SMART STUDY TIME PREDICTOR</h1>

<h3>A simple Machine Learning project that predicts the number of study hours required based on:</h3>
Number of chapters<br>
Difficulty level<br>
Your previous score<br>
The project uses Linear Regression from scikit-learn and is designed for 1st-year B. Tech students.<br>
<h3>FEATURES</h3>
Predicts how many hours you should study.<br>
Taking 3 inputs:<br>
• Chapters<br>
• Difficulty Level (1–5)<br>
• Past Score (%)<br>
Produces a simple and easy-to-understand output.<br>
Beginner-friendly code without any complex ML concepts<br>

<h3>TECH STACK</h3>
• Python<br>
• NumPy<br>
•Scikit-learn (Linear regresssion)<br>

<h3>INSTALLATION</h3>
• install : pip install numpy scikit-learn<br>

<h3>HOW IT WORKS</h3>
1. A small sample dataset is created inside the program<br>
2. A Linear Regression model is ttrained on the dataset<br>
3. User enters :<br>
   • chapters<br>
   • difficulty<br>
   • past score<br>
4. Model predicts the study hours required<br>
   

<h3>CODE</h3>

```python
#SMART STUDY TIME PREDICTOR
#Using Linear Regression
import numpy as np
from sklearn.linear_model import LinearRegression


data=np.array([
    [5,3,60],
    [8,4,55],
    [3,2,80],
    [10,5,50],
    [7,4,65],
])

response=np.array([5,8,3,10,7])

model=LinearRegression()
model.fit(data,response)

print("\n-----------------------------------")
print("SMART STUDY TIME PREDICTOR")
print("-----------------------------------")


chapter=int(input("Enter number of chapters: "))
difficulty=int(input("Enter difficulty level (1-5): "))
past_score=int(input("Enter your previous score (%): "))

input=np.array([[chapter, difficulty, past_score]])

predicted_hour=model.predict(input)[0]

print("\n Suggested Study Time: ")
print(f"You should study approx: {predicted_hour:.2f} hours")

if predicted_hour<4:
  print("You need moderate preparation")
elif predicted_hour<7:
  print("You need good preparation")
else:
  print("You need strong preparation. Stay consistent!")
```

  <h3>OUTPUT</h3>
  
```python
SMART STUDY TIME PREDICTOR

Enter number of chapters: 5
Enter difficulty level (1-5): 3
Enter your previous score (%): 87

 Suggested Study Time: 
You should study approx: 5.00 hours
You need good preparation
```


