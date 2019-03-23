#Playing With DataSets @ BY VEDANT BAHEL

#importing pandas
import pandas as pd

#import dataset
dataset= pd.read_csv("Admission_Predict.csv")

print(dataset.shape)
# output-- (400,9)
# That Means that dataset has 400 rows and 9 Columns

print(dataset.columns)
# Output -- Index(['Serial No.', 'GRE Score', 'TOEFL Score', 'University Rating', 'SOP',
#       'LOR ', 'CGPA', 'Research', 'Chance of Admit '],
#      dtype='object') 
# That means it returns the column names or heading of the dataset

# Slicing of Datasets
column1= dataset.iloc[:,0]
print(column1)

#Head and Tail Function
#Head(x)- Returns the top x number of rows of that dataset
#Tail(x)- Returns the bottom x number of rows of that dataset
print(dataset.head(5))
print(dataset.tail(5))

#info function- Returns the information of dataset as follows:
print(dataset.info())

#Extracting  a specific column by it's name: Object Name "Series"
column5= dataset['SOP']