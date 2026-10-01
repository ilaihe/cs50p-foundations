tweet = input("Tweet: ")


output = ""

for character in tweet:
    if character.lower() not in ["a", "e", "i", "o", "u"]:
        output += character

print("Output: ", output)
