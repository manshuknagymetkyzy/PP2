import re
s = input()
if re.search("^[a-zA-Z0-9_]*$", s):
    print("Found a match!")
else:
    print("Not matched!")