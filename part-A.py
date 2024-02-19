
import json

DiceA = [1,2,3,4,5,6]
DiceB = [1,2,3,4,5,6]

possible_combi = len(DiceA) * len(DiceB)

print(f"\nQ1. How many total combinations are possible? Show the math along with the code!")
print(f'A1.Total Combinations Possible are -> {possible_combi}, Since Dice A has {len(DiceA)} sides and Dice B has {len(DiceB)} sides')

distribution= [[[i, j] for j in range(1, 7)] for i in range(1, 7)]

print("\nQ2.Calculate and display the distribution of all possible combinations that can be obtained when rolling both Die A and Die B together. Show the math along with the code!") 
print('A2.Distribution Matrix:')
[print(val) for val in distribution]
print("\n")
combiSum = [[i + j for j in range(1, 7)] for i in range(1, 7)]
print('A2.Sum Distribution Matrix:')
[print(val) for val in combiSum]


hash_map = {}
oneDCombiSum = [val for row in combiSum for val in row]
for val in oneDCombiSum:
    v = hash_map.get(val,0)+1
    hash_map[val] = v
maxSum,minSum = max(oneDCombiSum),min(oneDCombiSum)
print(f"\nQ3.Calculate the Probability of all Possible Sums occurring among the number of combinations from (2).")
print('A3.Probability Distribution for all Possible Sums:')
[print(f'P(Sum = {i}): => {format(hash_map[i] / possible_combi * 100,".2f")} %') for i in range(minSum, maxSum)]
probabilityJson = json.dumps(hash_map,indent=4)
with open('possible_sum_probability.json','w') as f:
    f.write(probabilityJson)
    
