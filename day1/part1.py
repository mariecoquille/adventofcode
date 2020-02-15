f = open('masses.py')
total = 0
for line in f:
    line = int(line)
    fuel = line // 3
    fuel -= 2
    total += fuel
print(total)
