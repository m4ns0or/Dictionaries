# Dictionaries don't have index orders, so speaking about them regarding their first item or last item is not very
# correct. Next time you print a dictionary it may have a different order than you saw before. Instead they have
# keys, and we can use keys to call their values.

Dict = {"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}

# When was Plato born?
Ans = Dict["born"]
print(Ans)

# Change Plato's birth year from B.C. 427 to B.C. 428.
Dict["born"] = -428
print(Dict["born"])

# Dictionaries can have nested data too. Also, you can add a new key
# to a dictionary as they are mutable (changeable). Try to add the key "work" to dict with values shown below.
# "work": ["Apology", "Phaedo", "Republic", "Symposium"]
Dict["work"] = ["Apology", "Phaedo", "Republic", "Symposium"]
print(Dict)


