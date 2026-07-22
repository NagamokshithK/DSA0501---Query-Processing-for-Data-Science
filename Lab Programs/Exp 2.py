import pandas as pd
df = pd.read_csv("Exp 2.csv")
result = df.groupby("EMPLOYEE_ID").size()
print(result[result >= 2].index)
