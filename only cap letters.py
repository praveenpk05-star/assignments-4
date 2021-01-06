import re
stringA = "PyThoN"


# Find characters
res = "".join(re.findall("[A-Z]+", stringA))

print("Result: ", res)