# Create a dictionary from the list with same key:value pairs, such as: {"key": "key"}.

lst = ["NY", "FL", "CA", "VT"]
dict = {i: i for i in lst}
print(dict)

# First, create a range from 100 to 160 with steps of 10.
# Second, using dict comprehension, create a dictionary where each number in the range is
# the key and each item divided by 100 is the value.

R = range(100, 160, 10)
dict = {i: i / 100 for i in R}
print(dict)

# Using dict comprehension and a conditional argument create a dictionary from
# the current dictionary where only the key:value pairs with value above 2000 are taken to the new dictionary.

dict1 = {"MFX": 4950, "EXTRA": 2400, "DIFF": 1800, "XPO": 1700}
dict2 = {i: dict1[i] for i in dict1 if dict1[i] > 2000}
print(dict2)
