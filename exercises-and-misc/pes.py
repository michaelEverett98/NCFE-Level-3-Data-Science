import numpy as np
import pandas as pd

attributeArray = ["OA", "Ball Control", "Dribbling", "Tight Poss", "Low Pass", "Loft Pass", "Finishing", "Heading", "Place Kick", "Curl", "Speed", "Acceleration", "Kick Power", "Jump", "Physical", "Balance", "Stamina", "DA", "Ball Winning", "Aggression", "GK Handling", "GK Pos", "GK Kick", "GK Ref", "GK Reach"]

data = {}

df = pd.DataFrame(columns = attributeArray + ["WFU", "WFA", "IR", "Form", "Height", "Weight", "Skill 1", "Skill 2", "Skill 3"])

df.to_csv("Hatfelt.csv", index = True)

def generateAttributes(numPlayers) :
        
    for x in range(numPlayers + 1) :

        dataArray = []

        for i in attributeArray :

            num = np.random.randint(40, 100)
            dataArray.append(num)

        for i in range(1, 3) :

            num = np.random.randint(1, 5)
            dataArray.append(num)

        ir = np.random.randint(1, 4)
        form = np.random.randint(1, 9)
        height = np.random.randint(150, 211)
        weight = np.random.randint(50, 121)
        skill1 = np.random.randint(1, 30)
        skill2 = np.random.randint(1, 30)
        skill3 = np.random.randint(1, 30)

        dataArray += [ir, form, height, weight, skill1, skill2, skill3]
        #dataArray.append(form)

        a = pd.DataFrame([dataArray], columns = attributeArray + ["WFU", "WFA", "IR", "Form", "Height", "Weight", "Skill 1", "Skill 2", "Skill 3"])

        a.to_csv("Hatfelt.csv", mode = "a", index = True, header = False)

generateAttributes(18)