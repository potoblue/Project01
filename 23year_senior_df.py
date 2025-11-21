# import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import platform

plt.rcParams['font.family'] = 'Malgun Gothic'  
plt.rcParams['axes.unicode_minus'] = False     


total_df = pd.read_csv("station_total_utf8.csv")
senior_df = pd.read_csv("senior_total_utf8.csv")
senior_care_df = pd.read_csv("senior_care_utf8.csv")
sme_df = pd.read_csv("sme.csv")
park_df = pd.read_csv("TB_PTP_PRK_M.csv")


