numb = int(input("enter number: "))

divList = range(2, numb)

newList = []

for x in divList:
    if (numb%x == 0):
        newList.append(x)

convert_first_to_generator = (str(w) for w in newList)
print(' '.join(convert_first_to_generator))