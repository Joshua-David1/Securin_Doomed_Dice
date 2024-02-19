import json
Die_A = [1,2,3,4,5,6]
Die_B = [1,2,3,4,5,6]

print(f"Standard Dice A = {Die_A}\nOriginal Dice B = {Die_B}")

total_combinations = len(Die_A) * len(Die_B)


with open('possible_sum_probability.json','r') as f:
    standardProb = json.loads(f.read())

totalVals = 0
print("\nStandard Probabilities: ")
for key,val in standardProb.items():
    print(f"P(Sum = {key}) => {format(val/total_combinations * 100,'.2f')} %")
    totalVals+=1
print("\n")


diceA = []
diceB = []

def getPossibilities(number,arrStore,dice):
    if dice == "DiceA":
        if number > 4:
            return
        if len(arrStore) > 6:
            return
            
        if len(arrStore) == 6:
            if arrStore not in diceA:
                diceA.append(arrStore)
            return
        
            
        for i in range(number,5):
            getPossibilities(i,arrStore.copy() + [i],"DiceA")
    else:
        if number > 11:
            return
            
        if len(arrStore) > 6:
            return
            
        if len(arrStore) == 6:
            if arrStore not in diceB:
                diceB.append(arrStore)
            return
            
            
        for i in range(number+1,13):
            getPossibilities(i,arrStore.copy()+[i],"DiceB")
        
def undoomDice(Die_A,Die_B):
        
        
    Die_A = Die_B = [0]*6
    print("After Loki Doomed Both the Dice!")
    print(f"Doomed Dice A = {Die_A}")
    print(f"Doomed Dice B = {Die_B}\n")
    

    for i in range(1,5):
        getPossibilities(i,[i],"DiceA")
    for j in range(1,12):
        getPossibilities(j,[j],"DiceB")
    

    print("Undooming Dice A and Dice B...")
    for i in diceA:
        for j in diceB:
            mapp = {}
            count = 0
            for k in range(len(i)):
                for l in range(len(j)):
                    sum_ = mapp.get(sum([i[k],j[l]]),0)+1
                    mapp[sum([i[k],j[l]])] = sum_
            

            for key,val in mapp.items():
                if val == standardProb.get(str(key),-1):
                    count+=1
    
            if count == totalVals:
                return i,j,mapp
New_Die_A,New_Die_B,mapp = undoomDice(Die_A,Die_B)
print(f"Transformed Dice A -> {New_Die_A}")
print(f"Transformed Dice B -> {New_Die_B}")

print("\nProbability of Dice After Transforming:")
for key,val in mapp.items():
    print(f"P(Sum = {key}) => {format(val/total_combinations * 100,'.2f')} %")