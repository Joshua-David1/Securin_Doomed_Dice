# Securin Doomed Dice Challenge!

## PART A

### How to run

```rb
git clone https://github.com/Joshua-David1/Securin_Doomed_Dice.git
cd Securin_Doomed_Dice
python3 part-A.py
```

### Logic

1) To Find out the total combinations, we first have to see how many faces are there for each of the 2 Dice. Dice A has 6 faces [1,2,3,4,5,6] and Dice B also has 6 faces [1,2,3,4,5,6]. To fnd out the total combinations possible , we have to multiply number of faces of Dice A * number of faces of Dice B. Hence the total combinations are 6*6 which is equal to 36. <br>
2) Here, Each Value of Dice A must be mapped with every other value of Dice B and then adding both the mapped values for each iteration would result in distribution matrix. This can be done with the time complexity of O(n*m) since we would be needing two for loops... One 'for loop' is to loop through Dice A and the other 'for loop' is to loop through Dice B. Since Dice A has a face of 'n' sides and Dice B has a face of 'm' sides, the time complexity is O(n*m). <br>
3) To calculate the probability of all the sums occuring, a hash_map is used to keep track of the occurence of a particular sum. Once done, each number of sums would be divided by the total_combinations available, to get the probability.

## PART B

### How to run

```rb
git clone https://github.com/Joshua-David1/Securin_Doomed_Dice.git
cd Securin_Doomed_Dice
python3 part-B.py
```

### Logic

## Part A Output
<img width="1262" alt="Screenshot 2024-02-20 at 10 42 44 AM" src="https://github.com/Joshua-David1/Securin_Doomed_Dice/assets/69303816/6078f21f-a9df-4763-8680-2589ca62b949">

## Part B Output
<img width="659" alt="Screenshot 2024-02-20 at 10 45 09 AM" src="https://github.com/Joshua-David1/Securin_Doomed_Dice/assets/69303816/f500c93d-20b3-4191-b31d-cff7b6c4472f">
