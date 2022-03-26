# Walmart-Best-Product-Pair-Prediction
Calculated the co-occurrence probabilities of different possible pair of items of Walmart using Hadoop Map Reduce. The co-occurrence probability of each pair determines if the pair can be placed next to each other or just an aisle apart.

# Mapper
The mapper can create pairs from different bill transactions of Walmart along with a number 1 with a tab space in between.

# Reducer
The reducer can count the occurrences of each pair and individual items and use this information to calculate the co-occurrence probability of each pair of items.

# Co-occurrence conditional Probability
Prob(B|A) = Count(A,B)/Count(A)

