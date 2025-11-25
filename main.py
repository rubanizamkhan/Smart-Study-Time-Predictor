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

print("\nSMART STUDY TIME PREDICTOR")
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
