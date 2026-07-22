import pandas as pd
df=pd.read_csv("Exp 1.csv")
distinct_dept = df["DEPARTMENT_ID"].unique()
print("Distinct Department IDs:")
print(distinct_dept)
