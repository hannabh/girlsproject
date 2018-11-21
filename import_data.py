import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("gender_development.csv", index_col = 1)
print(data.head(5))

print(data.loc["Germany", "Expected Years of Education (Female)"])

print(data.index)
print(data.index[3])
print(data.loc["Denmark"])

education_male = float(data.loc["Oman", "Expected Years of Education (Female)"])
education_female = float(data.loc["Oman", "Expected Years of Education (Male)"])
df = pd.DataFrame({"lab":["Expected Years of Education \n (Female)", "Expected Years of Education \n (Male)"], 'val':[education_female, education_male]})
df.plot(kind = "bar", x='lab', y='val', rot=0)
plt.show(block=True)