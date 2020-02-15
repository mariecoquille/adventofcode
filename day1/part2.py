f = open('masses.py')

def calculating_fuel(mass) :
    mass = int(mass)
    fuel = mass // 3 - 2
    extra_fuel = fuel // 3 -2
    while extra_fuel > 0:
        fuel += extra_fuel
        extra_fuel = extra_fuel // 3 - 2
    return fuel

total = 0

for line in f:
    result = calculating_fuel(line)
    total += result

print(total)
