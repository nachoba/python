# Introducing Python
# Chapter 01 :: A Taste of Py
# -----------------------------------------------------------------------------


# list in Python
cliches = [
    "At the end of the day",
    "Having said that",
    "The fact of the matter is",
    "Be that as it may",
    "The bottom line is",
    "If you will", ]

print("The size of the list is: ", len(cliches))
print("Now let's list all cliches:\n")
for item in range(0, len(cliches) - 1):
    print("\t",cliches[item])


print("\n\n")

# dictionaries in Pytho
quotes = {
    "Moe": "A wise guy, eh?",
    "Larry": "Ow!",
    "Curly": "Nyuk, nyuk!",
    }

print("The size of the dictionary is: ", len(quotes))
print("We choose Larry as our Stooge")
stooge = "Larry"
print("\t", stooge, "says:", quotes[stooge])
print("\n\n")
