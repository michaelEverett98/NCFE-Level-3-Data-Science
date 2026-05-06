import pandas as pd

dfMay = pd.read_excel("MayK.xlsx")
dfJune = pd.read_excel("JuneK.xlsx")
dfJuly = pd.read_excel("JulyK.xlsx")
dfAugust = pd.read_excel("AugustK.xlsx")

dfConcat = pd.concat([dfMay, dfJuly, dfJune, dfAugust])
dfConcat = pd.DataFrame(dfConcat)
#expenditureArray = [dfMay, dfJune, dfJuly, dfAugust]

dfConcat.to_excel("Test1P.xlsx", index = True)

'''dfConcat = pd.DataFrame()

for i in expenditureArray :

    #i = i.drop(["LONDON BOROUGH OF ENFIELD", "Payment Date", "Transaction Number"], axis = 1)

    #dfConcat = dfConcat._append(i)
    dfConcat = dfConcat.concat(i)'''

#dfConcat.to_excel("Concatenated_expenditure_data_unfiltered.xlsx", index = True)

#dfRead = pd.read_excel("Concatenated_expenditure_data_unfiltered.xlsx")

#columns = dfConcat.dtypes
#print(columns)

#dfTrim = dfConcat.drop(["LONDON BOROUGH OF ENFIELD", "Payment Date", "Transaction Number"], axis = 1)

#exit()

dfTrimSet = set(dfConcat["Service Area Categorisation "])
print(dfTrimSet)

expenditureCategory = {}
dictLength = []

for i in dfTrimSet:

    expenditureCategory[str(i)] = []

print(expenditureCategory)

for i in range(len(dfConcat)) :

    x = dfConcat["Service Area Categorisation "][i]

    #print(x, "one")
    #print(expenditureCategory, "two")

    if x in expenditureCategory :

        #print(x)
        expenditureCategory[x].append(float(dfConcat["Net Amount"][i]))
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

newDf.to_excel("testingpp.xlsx", index = True)


#dfConcat.to_excel("Concatenated_expenditure_data_unfiltered.xlsx", index = True)