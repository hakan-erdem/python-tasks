sentence = input("Enter your sentence: ")

dct = {}

for item in sentence:
    if item in dct:
        dct[item] += 1

    elif item not in dct:
        dct[item] = 1

print(dct)