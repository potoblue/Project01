# import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium

total_df = pd.read_csv("station_total_utf8.csv")
senior_df = pd.read_csv("senior_total_utf8.csv")


# ------------------
# 확인용
print(total_df.head())
print(total_df.columns)
print(senior_df.head())
print(senior_df.columns)
# ------------------

