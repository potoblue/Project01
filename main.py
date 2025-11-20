# import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium

total_df = pd.read_csv("station_total_utf8.csv")
senior_df = pd.read_csv("senior_total_utf8.csv")
senior_care_df = pd.read_csv("senior_care_utf8.csv")
sme_df = pd.read_csv("sme.csv")
park_df = pd.read_csv("TB_PTP_PRK_M.csv")

# 역별 승하차인원           => total_df
# 65세 노인 승하차인원      => senior_df
# 노인요양시설(요양원)      => senior_care_df
# 종사자, 사업체 수         => sme_df

# ------------------
# 확인용
print(total_df.head())
print(total_df.columns)
print(senior_df.head())
print(senior_df.columns)
print(senior_care_df.head())
print(senior_care_df.columns)
print(sme_df.head())
print(sme_df.columns)
print(park_df.head())
# ------------------

