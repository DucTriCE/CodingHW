with open('../input.txt','r') as f:
    lines = f.readlines()
gas = list(map(int, lines[0].split(',')))
cost = list(map(int, lines[1].split(',')))

# Smart way
start_idx = 0
tank = 0
total = 0

for i in range(len(gas)):
    tank += gas[i]-cost[i]
    if tank<0:
        total+=tank
        start_idx=i+1
        tank=0

print(-1) if tank+total<0 else print(start_idx)