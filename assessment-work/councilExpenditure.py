# ==================================================
#           NCFE Level 3 Data Unit 1: Task 1
# ==================================================

import pandas as pd
import numpy as np

#pd.set_option("display.max_rows", None)
#pd.set_option("display.width", None)

df = pd.read_excel("August.xlsx")

#df = pd.read_csv("May.xlsx", header = 0, sep = ",")

dfTrim = df.drop(["LONDON BOROUGH OF ENFIELD", "Payment Date", "Transaction Number"], axis = 1)

print(dfTrim)
print(len(dfTrim))

dfTrimSet = set(dfTrim["Service Area Categorisation "])
print(dfTrimSet)

expenditureCategory = {}
dictLength = []

for i in dfTrimSet:

    expenditureCategory[str(i)] = []

print(expenditureCategory)

for i in range(len(dfTrim)) :

    x = dfTrim["Service Area Categorisation "][i]

    if x in expenditureCategory :

        #print(x)
        expenditureCategory[x].append(float(dfTrim["Net Amount"][i]))
    #print(i)


for i in expenditureCategory.keys():

    dictLength.append(len(expenditureCategory.get(i)))

print(dictLength)

newDf = pd.DataFrame()
newDf.insert(loc = 0, column = "debug", value = None)

maxLength = max(dictLength)

for x in range(maxLength) :

    newDf.loc[x] = [None]

for ind, i in enumerate(expenditureCategory.keys()) :

    valueArray = []

    for index, x in enumerate(expenditureCategory.get(i)) :
    
        valueArray.append(x)

    newDf.insert(loc = ind + 1, column = i, value = pd.Series(valueArray))
    
#print(newDf)

newDf.to_excel("AugustK.xlsx", index = True)


# ==================================================
# ==================================================
# ==================================================
# ==================================================
# ==================================================

'''for i in range(len(dfTrim)) :

    #test += 1
    #print(dfTrim["Expenses Type"][i])
    if dfTrim["Expenses Type"][i] not in expenditureCategory :

        expenditureCategory.append(dfTrim["Expenses Type"][i])'''