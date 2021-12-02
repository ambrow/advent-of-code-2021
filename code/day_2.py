import pandas as pd
import constants # note: python constants saved in a separate file for ease of use

# load input
directions = pd.read_csv(constants.wd + "/inputs/input_2.csv")

# part 1
# dataframe operations for the win
directions[['direction', 'value']] = directions.direction.str.split(" ", expand=True)
directions['value'] = directions.value.apply(int)
directions_grouped = directions.groupby(['direction']).value.sum().reset_index()

d = pd.Series(directions_grouped.value.values, index=directions_grouped.direction).to_dict()

print(f"depth: {d['down'] - d['up']}")
print(f"x: {d['forward']}")

print(f"multiplication: {(d['down'] - d['up']) * d['forward']}")

# part 2
# for loop because my brain isn't working any faster than that
dirs = directions.direction.tolist()
vals = directions.value.tolist()
X = 0
aim = 0
depth = 0
for i in range(0,len(dirs)):
    if dirs[i] == 'forward':
        X += vals[i]
        depth += (aim*vals[i])
    elif dirs[i] == 'up':
        aim += (-1*vals[i])
    else:
        aim += vals[i]

print(f"horizontal postion: {X}")
print(f"depth: {depth}")
print(f"multiplied: {X*depth}")

