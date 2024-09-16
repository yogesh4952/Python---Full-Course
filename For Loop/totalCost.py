prices = [200,125,125.365]

total_cost = 0

for item in prices:
    total_cost = item+total_cost;
print(total_cost)

for x in range(4):
    for y in range(3):
        print(f'({x},{y})')