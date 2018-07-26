import pandas as pd
import numpy as np
import re
from pandas.core.frame import DataFrame

df = pd.read_csv("Hoses.csv")
listkeyword = []
temp = []
i = 0

for row in df["NAME"]:
    if re.findall(r"(.*)\"", row) != []:
        print(re.findall(r"(.*)\"", row))
        temp.append(re.findall(r"(.*)\"", row))
    else:
        temp.append('+')

i=0
for row in df["NAME"]:
    i = i + 1
    if temp[i-1] == '+':
        print(re.findall(r"(.*)/", row) + ['/']+ re.findall(r"/(\d*)",  row))
        temp[i-1] = ["".join(re.findall(r"([A-Z]?\d* *\d*)/", row) + ['/']+ re.findall(r"/(\d*)",  row))]

i=0
for row in df["NAME"]:
    i = i + 1
    if re.findall(r"(\d* *-* *\d*[.]?\d* *)MM", row) != []:
        print(re.findall(r"(\d* *-* *\d*[.]?\d* *)MM", row))
        temp[i - 1] = (re.findall(r"(\d* *-* *\d*[.]?\d* *)MM", row))

i=0
for row in df["NAME"]:
    i = i + 1
    if re.findall(r"(\d* *-* *\d*[.]?\d* *)mm", row) != []:
        print(re.findall(r"(\d* *-* *\d*[.]?\d* *)mm", row))
        temp[i - 1] = (re.findall(r"(\d* *-* *\d*[.]?\d* *)mm", row))

i=0
for row in df["NAME"]:
    i = i + 1
    if re.findall(r"PSI - (.*)MTR", row) != []:
        print(re.findall(r"PSI - (.*)MTR", row))
        temp[i - 1] = re.findall(r"PSI - (.*)MTR", row)

i=0
for row in df["NAME"]:
    i = i + 1
    if re.findall(r"DN (.*)", row) != []:
        print(re.findall(r"DN (.*)", row))
        temp[i - 1] = "WARNING"



df['Size List'] = temp



df.to_csv('C:/Users/Administrator/Desktop/output1.csv', sep=',')


###### function for remove [] #############
#temp2 = []
#for row in temp:
    #temp2.append(",".join(row))