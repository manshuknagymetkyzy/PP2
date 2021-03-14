commands = input()
point = list(input().split())
x = 0
y = 0
c = False
for i in range(len(commands)):
    if(commands[i] == "L"):
        x -= 1
    elif(commands[i] == "R"):
        x += 1
    elif(commands[i] == "U"):
        y += 1
    elif(commands[i] == "D"):
        y -= 1
    if(int(point[0] == x and int(point[1]) == y)):
        c = True
        print("Passed")
        break
if(c == False):
    print("Missed")