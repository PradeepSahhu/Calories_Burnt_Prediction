# -*- coding: utf-8 -*-
"""Completed_Project-Calories_burnt.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CwdoX3XLU_tyEWQdsFFHdFaWFNUQMoBa

## Importing all the Dependencies
"""

# importing all the necessary modules.


import numpy as np # used to make numpy arrays -- > list of values...
import pandas as pd # used to make dataframes --> structures tables...
import matplotlib.pyplot as plt # data visualization...
import seaborn as sns # both of data visualization
from sklearn.model_selection import train_test_split # splitting our data into train and test set.
from xgboost import XGBRegressor # regression ---> it is a machine learning algorithms
from sklearn import metrics # it is used to evaluate our model.

"""## Data collection and pre-processing"""

# Loading the data from csv file to a pandas dataframe
calories = pd.read_csv("calories.csv")
type(calories)

# print the first five rows of the dataframe
calories.head(10)

# exercise data
exercise_data= pd.read_csv("exercise.csv")

exercise_data.head(10)

"""## combine the calories and exercise dataframe. (combining the two dataframe)"""

calories_data = pd.concat([exercise_data, calories['Calories']], axis=1) 
#1 refers columns, 0 refers rows

print(calories_data)
calories_data.head()

# checking the number of rows and columns
calories_data.shape
calories_data.shape[0] # 0 refers rows.
#calories_data.shape[1] # 1 refers columns. # 15000 rows good data size.

# getting some information about the data
calories_data.info() # to find all the missing values
# null values means missing data either we can remove them or else we can find the average of the data.

# checking for the missing values
calories_data.isnull().sum()
# if their is any missing value then either we will fill that missing values with
# fillna() either with mean, mode , or median
# we can drop the missing values with dropna()

"""## Data Analysis"""

# get some statistical measures about the data
# we can't find the statistical value of text data.
calories_data.describe()

"""# Data Visualization"""

sns.set()

# plotting the gender column in count plot
sns.countplot(calories_data['Gender'])  # countplot is good for categorical data because etiher male or female

# as age varies that's why we used distribution plot
# finding the distribution of "Age" column
sns.distplot(calories_data["Age"])

# more people fall in the category of 20 and least people fall in the category of 80.
# less people exercise as they get older

# finding the distribution of "Height" column
sns.distplot(calories_data["Height"])
# more people fall under the category of 160-180.
# when the values varies, we use distribution plot. (distplot)

# finding the distribution of "Weight" column
sns.distplot(calories_data["Weight"])
# more people in the catory of 60

# finding the distribution of "Duration" column
sns.distplot(calories_data["Duration"])

# the below distribution plot shows the duration exercise of the people.

# finding the distribution of "Heart_Rate" column
sns.distplot(calories_data["Heart_Rate"])

# the below graph shows the heart_rate of people during exercise.

"""## Finding the corelation in the dataset

###1. Positive correlation
###2. Negative correlation
"""

correlation = calories_data.corr()
# positive correlation means the value of one parameter depends upon the other
# if one is increasing the other is also increasing
# or the relationship between two features. (independent variables)

# negative correlation means, if one is increasing the other is decreasing or vice-versa.

# Construction a heatmap to understand the correlation

plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')

# Each column is compared to other column if the value is 1 then they are positively correlated and if the 
# value is very less then it means they are negatively correlated.
# if the value is 0 then their is no correlation at all.

# Duration, heart_rate, body_temp and calories all these are correlated.
# we can't find the correlation between text value.

"""## Converting the Text Data to numberical Values"""

calories_data.replace({"Gender":{'male': 0, 'female':1}}, inplace=True)
# print(calories_data)

calories_data.head()

"""## seperating Features and Target"""

# features ---> independent variables and target ---> our target variables.

# droping useless (not needed columns) like user_id and seperating our target column which is calories.
x = calories_data.drop(columns=['User_ID', 'Calories'], axis=1)
y = calories_data['Calories']

print(x)

print(y)

"""Splitting the data into training data and test data"""

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=2)

#x_train.sort_index(axis=1,inplace=True)
#x_test.sort_index(axis=1,inplace=True)

x_train = np.array(x_train)
x_test = np.array(x_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

print(x.shape,x_train.shape, x_test.shape)

"""## Model Training

XGBoost Regressor
"""

# loading the model
model = XGBRegressor()

# training the model with x_train
model.fit(x_train, y_train)

"""## Evaluation

## Prediction on test data
"""

test_data_prediction = model.predict(x_test)

print(test_data_prediction)

"""# mean absolute Error"""

mean_absolute_error = metrics.mean_absolute_error(y_test, test_data_prediction)

print("mean absolute error", mean_absolute_error)