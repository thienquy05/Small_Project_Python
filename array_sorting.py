#strip spaces from each word
items = [x.strip() for x in input("Enter an array: ").split(',')]
items.sort()
print(','.join(items))