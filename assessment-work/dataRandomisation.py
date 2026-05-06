import numpy as np
import pandas as pd
#import random as rd

attributeArray = ["OA", "Ball Control", "Dribbling", "Tight Poss", "Low Pass", "Loft Pass", "Finishing", "Heading", "Place Kick", "Curl", "Speed", "Acceleration", "Kick Power", "Jump", "Physical", "Balance", "Stamina", "DA", "Ball Winning", "Aggression", "GK Handling", "GK Pos", "GK Kick", "GK Ref", "GK Reach"]

skillsArray = ["Stepover", "Chop Turn", "Roulette", "Sole Control", "First Time Shot", "Acrobatic Finish", "Dipping Shot", "Knuckle Shot", "One Touch Pass", "Through Pass", "Weighted Pass", "Driven Pass", "Interception", "Man Marking", "Captaincy", "Perseverance"]

errorArray = [1, 4, 7, 16, 23, 30, 41, 46, 55, 62, 71, 74, 82, 97]

data = {}

df = pd.DataFrame(columns = attributeArray + ["WFU", "WFA", "IR", "Form", "Height", "Weight", "Skill 1", "Skill 2", "Skill 3"])

df.to_csv("randomStats.csv", index = True)

def generateRandom(numPlayers) :
        
    for x in range(numPlayers) :

        randomConstant = np.random.randint(1, 101)
        print(randomConstant)

        dataArray = []

        for i in attributeArray :

            if randomConstant not in errorArray  :

                num = np.random.randint(40, 100)
                dataArray.append(num)

            else :

                print("here")
                num = np.random.randint(35, 105)
                dataArray.append(num)

        for i in range(1, 3) :

            num = np.random.randint(1, 5)
            dataArray.append(num)

        if randomConstant > 25 :

            ir = np.random.randint(1, 4)
            form = np.random.randint(1, 9)
            height = np.random.randint(150, 211)
            weight = np.random.randint(50, 121)
            skill1 = np.random.choice(skillsArray)
            skill2 = np.random.choice(skillsArray)
            skill3 = np.random.choice(skillsArray)

        elif randomConstant < 5 :

            ir = None
            form = np.random.randint(1, 9)
            height = np.random.randint(150, 211)
            weight = np.random.randint(50, 121)
            skill1 = np.random.choice(skillsArray)
            skill2 = np.random.choice(skillsArray)
            skill3 = np.random.choice(skillsArray)

        elif randomConstant < 14 :

            ir = np.random.randint(1, 4)
            form = np.random.randint(1, 9)
            height = None
            weight = np.random.randint(50, 121)
            skill1 = np.random.choice(skillsArray)
            skill2 = np.random.choice(skillsArray)
            skill3 = np.random.choice(skillsArray)

        elif randomConstant < 21 :

            ir = np.random.randint(1, 4)
            form = "Form Value"
            height = np.random.randint(150, 211)
            weight = np.random.randint(50, 121)
            skill1 = np.random.choice(skillsArray)
            skill2 = np.random.choice(skillsArray)
            skill3 = np.random.choice(skillsArray)

        else :

            ir = np.random.randint(1, 4)
            form = np.random.randint(1, 9)
            height = np.random.randint(150, 211)
            weight = "np.random.randint(50, 121)"
            skill1 = np.random.choice(skillsArray)
            skill2 = np.random.choice(skillsArray)
            skill3 = np.random.choice(skillsArray)

        dataArray += [ir, form, height, weight, skill1, skill2, skill3]
        #dataArray.append(form)

        a = pd.DataFrame([dataArray], columns = attributeArray + ["WFU", "WFA", "IR", "Form", "Height", "Weight", "Skill 1", "Skill 2", "Skill 3"])

        a.to_csv("randomStats.csv", mode = "a", index = True, header = False)

generateRandom(200)