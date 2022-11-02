# Add 2 inches to the son's height.
Dict ={"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}
Dict["son's height"] = Dict["son's height"] + 2
print(Dict)

# Using .items() method generate a list of tuples consisted of each key value pair.
Ans = Dict.items()
print(Ans)

# Using .get() method print the value of "son's eyes".
ans = Dict.get("son's eyes")
print(ans)

# .get() method can be used just to get the value of a key. But it has more tricks up its sleeve.
# Try to look for key: "son's age" and if nothing comes up make the .get() return "2".
ans=Dict.get("son's age", 2)
print(ans)

# Since dictionaries are mutable, they have some methods that tuples don't have.
# .clear() is one of them, and it clears the whole dictionary.
Dict.clear()
print(Dict)

# Using len function, find how many keys there are in the dictionary.
ans = len(Dict)
print(ans)

# What's the key with the highest value in the dictionary?
dict = {"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}
ans = max(dict)
print(ans)

# What's the key with the lowest value in the dictionary?
dict = {"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}
ans = min(dict)
print(ans)

