import pandas as pd
import matplotlib as plot

data = pd.read_csv("gender_development.csv", index_col = 1)
print(data.head(5))

print(data.loc["Germany", "Expected Years of Education (Female)"])
