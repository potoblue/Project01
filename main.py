# import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import platform

plt.rcParams['font.family'] = 'Malgun Gothic'  
plt.rcParams['axes.unicode_minus'] = False     


total22_df = pd.read_csv("전연령22_utf8.csv", low_memory=False)
senior22_df = pd.read_csv("노인승하차22_utf8.csv", low_memory=False)
total23_df = pd.read_csv("전연령23_utf8.csv", low_memory=False)
senior23_df = pd.read_csv("노인승하차23_utf8.csv", low_memory=False)
total24_df = pd.read_csv("전연령24_utf8.csv", low_memory=False)
senior24_df = pd.read_csv("노인승하차24_utf8.csv", low_memory=False)
# senior_care_df = pd.read_csv("senior_care_utf8.csv", low_memory=False)
sme_df = pd.read_csv("sme.csv", low_memory=False)
park_df = pd.read_csv("TB_PTP_PRK_M.csv", low_memory=False)
safety_df = pd.read_csv("안전사고_utf.csv", low_memory=False)


# 역별 승하차인원           => total22_df, total24_df
# 65세 노인 승하차인원      => senior22_df, senior24_df
# 노인요양시설(요양원)      => senior_care_df
# 종사자, 사업체 수         => sme_df
# 안전사고                  => safety_df

# ------------------
# 확인용
print(total23_df.head())
# ------------------


"""# 2. [핵심] 역번호를 활용해 '호선' 컬럼 생성
# 서울교통공사 역번호 규칙을 반영하여 호선 정보를 만듭니다.
def get_line_number(station_id):
    sid = str(station_id)
    if sid.startswith('1'): return '1호선'
    if sid.startswith('2') and len(sid) == 3: return '2호선'
    if sid.startswith('3'): return '3호선'
    if sid.startswith('4'): return '4호선'
    if sid.startswith('25'): return '5호선'
    if sid.startswith('26'): return '6호선'
    if sid.startswith('27'): return '7호선'
    if sid.startswith('28'): return '8호선'
    return '기타'

senior_df['호선'] = senior_df['역번호'].apply(get_line_number) # 역번호를 get line number함수에 적용하여 새로운 컬럼값인 호선을 저장

# 3. 시간대 컬럼 정의 및 일일 총 승객수 계산
time_cols = [
    '06시간대이전', '06-07시간대', '07-08시간대', '08-09시간대', '09-10시간대',
    '10-11시간대', '11-12시간대', '12-13시간대', '13-14시간대', '14-15시간대',
    '15-16시간대', '16-17시간대', '17-18시간대', '18-19시간대', '19-20시간대',
    '20-21시간대', '21-22시간대', '22-23시간대', '23-24시간대', '24시간대이후'
]

# 데이터 정제: 숫자형으로 변환 (NaN 또는 이상 값 0 처리)
for col in time_cols:
    senior_df[col] = pd.to_numeric(senior_df[col], errors='coerce').fillna(0)
senior_df[time_cols] = senior_df[time_cols].apply(pd.to_numeric, errors='coerce').fillna(0) 
# 데이터가 숫자형이 아닌 문자열로 되어 있을 가능성 때문에 안전상의 이유로 숫자형으로 변환, errors= coerce는 숫자열로 변환 불가 시 NaN으로 처리
                                                                                  # 그 후 fillna(0)을 통해 NaN의 값을 0으로 처리

# '일일총승객수' 새 컬럼 생성 (가로 합산)
senior_df['일일총승객수'] = senior_df[time_cols].sum(axis=1)


# 4. 1~8호선 필터링 및 승하차별 평균 계산
target_lines = ['1호선', '2호선', '3호선', '4호선', '5호선', '6호선', '7호선', '8호선']
senior_df = senior_df[senior_df['호선'].isin(target_lines)]

# [핵심] 호선별 + 승하차구분별 평균 계산
result_df = senior_df.groupby(['호선', '승하차구분'])['일일총승객수'].mean().reset_index()

# -------------------------------------------------------
# 5. 시각화 (Grouped Bar Plot)
# -------------------------------------------------------

plt.figure(figsize=(14, 7))

# hue='승하차구분'으로 승차와 하차 막대를 분리하여 그립니다.
sns.barplot(x='호선', y='일일총승객수', hue='승하차구분', data=result_df, palette='Set1')

plt.title('호선별 평균 승차 vs 하차 인원 비교', fontsize=16)
plt.xlabel('호선', fontsize=12)
plt.ylabel('평균 승객 수 (명/일/역)', fontsize=12)
plt.legend(title='구분')

# 막대 위에 숫자 표시
for p in plt.gca().patches:
    height = p.get_height()
    if height > 0: 
        plt.gca().text(p.get_x() + p.get_width()/2., height + 100, 
                       f'{int(height):,}', 
                       ha='center', va='bottom', fontsize=9)

plt.show()
for p in plt.gca().patches:
    height = p.get_height()
    if height > 0: 
        plt.gca().text(p.get_x() + p.get_width()/2., height + 100, 
                       f'{int(height):,}', 
                       ha='center', va='bottom', fontsize=9)

plt.show()"""