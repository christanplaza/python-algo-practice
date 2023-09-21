# This code will determine if there are at most three letters in the string S
# that appears in the string "ABCDE".

# First, we create two variables: N and S.
# N is the number of characters in the string S.
# S is the string that we are going to check.

N = int(input())
S = input()

# Next, we create a dictionary called `letters_count`.
# The keys of the dictionary are the letters in the string "ABCDE", and the values
# are the number of times each letter appears in the string S.
# We initialize all of the values to 0.

letters_count = {letter : 0 for letter in "ABCDE"}

# Next, we iterate over the string S.
# For each letter in the string, we increment the count of the corresponding letter
# in the dictionary `letters_count`.

for s in S:
    letters_count[s] += 1

# Finally, we create a list called `count_list`.
# The elements of the list are the values of the dictionary `letters_count`.

count_list = list(letters_count.values())
print(count_list)

# We check if the number of elements in the list `count_list` that are equal to 0 is
# less than or equal to 2. 
# If it is, then we print the string "Yes".
# Otherwise, we print the string "No".

print('Yes') if count_list.count(0) <= 2 else print('No')