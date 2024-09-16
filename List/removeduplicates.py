number = [1,1,1,1,2,2,2,3,4]
uniques = []
for numbers in number:
    if numbers not in uniques:
        uniques.append(numbers)

print(uniques)