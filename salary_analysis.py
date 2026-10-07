#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 17:19:16 2026

@author: buseguldalii
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

data = [
    (83000, 8.7, "paid"),
    (88000, 8.1, "unpaid"),
    (48000, 0.7, "paid"),
    (76000, 6.0, "unpaid"),
    (69000, 6.5, "unpaid"),
    (76000, 7.5, "unpaid"),
    (60000, 2.5, "paid"),
    (83000, 10.0, "paid"),
    (48000, 1.9, "unpaid"),
    (63000, 4.2, "unpaid")
]

#first step is to plot the data

#split x and y
tenures = [row[1] for row in data]
salaries = [row[0] for row in data]

#creating scatter diagram
plt.scatter(tenures, salaries, color='black', marker='o', s=20)
plt.title("Salary by Year")
plt.xlabel("Years Experience")
plt.ylabel("Salary")

plt.show()

#more experience more income
#grouping salaries by tenure
# Keys are years, values are lists of the salaries for each tenure.
'''salary_by_tenure =  defaultdict(list)

for salary, tenure in salaries_and_tenures :
    salary_by_tenure[tenure].append(salary)
    
# Keys are years, each value is average salary for that tenure.
average_salary_by_tenure = {
    tenure : sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
    }   

This turns out to be not particularly useful, as none of the users
 have the same tenure, 
We should bucket the years of experience

'''
#statistical bucketing

df = pd.DataFrame(data, columns=["Salary", "Tenure", "Account_Status"])

# dividing the data into 3 equal-sized statistical bins based on quantiles
df["Experience_level"] = pd.qcut(df["Tenure"], q=3, labels=["Junior","Mid","Senior"])

# Calculating the average salary for each statistical bin
average_salaries = df.groupby("Experience_level", observed=False)["Salary"].mean().reset_index()

print("\n--- Statistically Grouped Salary Analysis ---")
print(average_salaries)


#Paid Accounts

'''
def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0 :
        return "paid"
    elif years_experience < 8.5 :
        return "unpaid"
    else:
        return "paid"
    not a great way to express so we will do ML'''
  
#(label encoding for variable y)

encoder = LabelEncoder()
df["Status_Encoded"] = encoder.fit_transform(df["Account_Status"])

#according to the alphabetic status paid = 0 ,unpaid = 1

X = df[["Tenure", "Salary"]]
y = df["Status_Encoded"]
#Model structure

knn_model = KNeighborsClassifier(n_neighbors=3)
#n_neighbors should be an odd number

#spliting for training

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#training
knn_model.fit(X_train, y_train)

#test
gerçek_test_tahminleri = knn_model.predict(X_test)

#CConfusion Matrix real vs model prediction
cm = confusion_matrix(y_test, gerçek_test_tahminleri)
print("Confusion Matrix")
print(cm)
# Çıktı formatı: 
# [[True zeros, false ones], 
#  [false zeros, true ones]]

#Detailed Error Rates 

rapor = classification_report(y_test, gerçek_test_tahminleri, target_names=["Paid (0)", "Unpaid (1)"],zero_division=0)
print("\n--- Sınıflandırma Raporu ---")
print(rapor)




















