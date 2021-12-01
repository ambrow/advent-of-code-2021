import pandas as pd

df = pd.read_csv("input_1.csv")

# part one
single_difference = (df.column.diff() > 0).sum()
print(single_difference)

# part two
sliding_window = (df.column.rolling(3).sum().diff() > 0).sum() 
print(sliding_window)