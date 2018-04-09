import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from math import floor, cell
from pylab import rcParams
from subprocess import check_output

data = pd.read_csv('..input/student_mat.csv')
data.columns
plt.figure(figsize=(15,15))
sns.heatmap(data.corr(), annot = True,fmt = ".2f", cbar = True)
plt.xticks(rotation=90)
plt.yticks(rotation=0)

data['Dalc'] = data['Dalc'] + data['Walc']
list[]
for i in range(11):
    list.append(len(data[data.Dalc == i]))
ax = sns.barplot(x = [0,1,2,3,4,5,6,7,8,9,10], y = list)
plt.ylabel('Number of Students')
plt.xlabel('Weekly alcohol consumption')

label = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
colors = ['lime', 'blue', 'orange', 'cyan', 'grey', 'purple', 'brown', 'red', 'teal']

explode = [0, 0, 0, 0, 0, 0, 0, 0, 0]
size =[]

for i in range(2, 11):
    sizes.append(sum(data[data.Dalc == i].G3))
total_grade = sum(sizes)
average = total_grade/float(len(data))
plt.pie(sizes,explode=explode, colors=colors, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Total grade :' +str(total_grade))
plt.xlabel('Students grade distribution according to alcohol consumption')

list = []
for i in range(2, 11):
    list.append(sum(data[data.Dalc == i].G3)/float(len(data.Dalc == i)))
ax = sns.barplot(x = [0,1,2,3,4,5,6,7,8,9,10], y = list)
plt.ylabel('Average Gradesof students')
plt.xlabel('Weekly alcohol consumption')
