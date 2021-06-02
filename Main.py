# Get user input
height = int(input("How Tall is the tree? "))
# Place Holder
spaces = height
hashes = 1
result = []
# The loop
for a in range(0, height):
    # placeHolder 
    spaces_show = "" 
    hashes_show = ""
    # Do some Calculation
    for b in range (0, spaces):
        spaces_show += " "
    for c in range(0, hashes):
        hashes_show += "#"
    # Print the result
    s = f"{spaces_show}{hashes_show}{spaces_show}"
    # For Holding the first line
    result.append(s)
    print(s)
    # The calculation
    spaces -= 1
    hashes += 2
# and Done
print(result[0])


