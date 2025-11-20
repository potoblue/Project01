import pandas as pd

total_df = pd.read_csv("station_total_utf8.csv")
senior_df = pd.read_csv("senior_total_utf8.csv")


# ------------------
# 확인용
print(total_df.head())
print(total_df.columns)
print(senior_df.head())
print(senior_df.columns)
# ------------------