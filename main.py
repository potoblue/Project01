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
# rain_df = pd.read_csv("rain20_25.csv", encoding='cp949', sep=None, engine="python")
# rain_df.to_csv("rain20_25_utf8.csv", encoding='utf-8-sig', index=False)

# weather_df = pd.read_csv("weather20_25.csv", encoding='cp949', sep=None, engine="python")
# weather_df.to_csv("weath20_25_utf8.csv", encoding='utf-8-sig', index=False)

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

# --------------------

group_columns = ['월','역번호','승하차구분', '역명']
time_columns = [
    '06시간대이전', '06-07시간대', '07-08시간대', '08-09시간대', '09-10시간대',
    '10-11시간대', '11-12시간대', '12-13시간대', '13-14시간대', '14-15시간대',
    '15-16시간대', '16-17시간대', '17-18시간대', '18-19시간대', '19-20시간대',
    '20-21시간대', '21-22시간대', '22-23시간대', '23-24시간대', '24시간대이후'
]

#2022
# 1. total_df에서 '승차'만 필터링할 때 .copy()를 사용하여 경고를 방지합니다.
senior22_df_2022 = senior22_df.copy()
senior22_df_2022.columns = senior22_df_2022.columns.str.strip()

senior22_df_2022['수송일자'] = pd.to_datetime(senior22_df_2022['수송일자'])
senior22_df_2022['수송일자'] = pd.to_datetime(senior22_df_2022['수송일자'])
senior22_df_2022['월'] = senior22_df_2022['수송일자'].dt.month
senior22_df_2022['월'] = senior22_df_2022['월'].ffill()
monthly_totol_2022 = senior22_df_2022.groupby(group_columns)[time_columns].sum()
tmp_senior22_df_2022 = monthly_totol_2022.loc[:,'06시간대이전' : '24시간대이후'].sum(axis=1)

#인덱스들을 컬럼으로 다시 변환 
reset_senior23_df_2022 = tmp_senior22_df_2022.reset_index(name = '승객수')
#승차 하차 구분
up_total_df_2022 = reset_senior23_df_2022[(reset_senior23_df_2022['승하차구분'] == '승차')].copy()
dw_total_df_2022 = reset_senior23_df_2022[(reset_senior23_df_2022['승하차구분'] == '하차')].copy()

#2023
# 1. total_df에서 '승차'만 필터링할 때 .copy()를 사용하여 경고를 방지합니다.
senior23_df_2023 = senior23_df.copy()
senior23_df_2023.columns = senior23_df_2023.columns.str.strip()

senior23_df_2023['수송일자'] = pd.to_datetime(senior23_df_2023['수송일자'])
senior23_df_2023['수송일자'] = pd.to_datetime(senior23_df_2023['수송일자'])
senior23_df_2023['월'] = senior23_df_2023['수송일자'].dt.month
senior23_df_2023['월'] = senior23_df_2023['월'].ffill()
monthly_totol_2023 = senior23_df_2023.groupby(group_columns)[time_columns].sum()
tmp_senior23_df_2023 = monthly_totol_2023.loc[:,'06시간대이전' : '24시간대이후'].sum(axis=1)

#인덱스들을 컬럼으로 다시 변환 
reset_senior23_df_2023 = tmp_senior23_df_2023.reset_index(name = '승객수')
#승차 하차 구분
up_total_df_2023 = reset_senior23_df_2023[(reset_senior23_df_2023['승하차구분'] == '승차')].copy()
dw_total_df_2023 = reset_senior23_df_2023[(reset_senior23_df_2023['승하차구분'] == '하차')].copy()

#2022
# 1. total_df에서 '승차'만 필터링할 때 .copy()를 사용하여 경고를 방지합니다.
senior24_df_2024 = senior24_df.copy()
senior24_df_2024.columns = senior24_df_2024.columns.str.strip() #값에 빈칸이 있는지 확인

senior24_df_2024['수송일자'] = pd.to_datetime(senior24_df_2024['수송일자']) #수송일자 값을 date 로 변환
senior24_df_2024['수송일자'] = pd.to_datetime(senior24_df_2024['수송일자'])
senior24_df_2024['월'] = senior24_df_2024['수송일자'].dt.month #날짜를 date 값으로 변환하고 월만 저장
senior24_df_2024['월'] = senior24_df_2024['월'].ffill() #컬럼에 해당되는 결측값을 값이 들어 있는 값까지 저장
monthly_totol_2024 = senior24_df_2024.groupby(group_columns)[time_columns].sum()
tmp_senior24_df_2024 = monthly_totol_2024.loc[:,'06시간대이전' : '24시간대이후'].sum(axis=1)

#인덱스들을 컬럼으로 다시 변환 
reset_senior24_df_2024 = tmp_senior24_df_2024.reset_index(name='승객수')
#승차 하차 구분
up_total_df_2024 = reset_senior24_df_2024[(reset_senior24_df_2024['승하차구분'] == '승차')].copy()
dw_total_df_2024 = reset_senior24_df_2024[(reset_senior24_df_2024['승하차구분'] == '하차')].copy()



# 1. 한글 폰트 설정 (Windows: Malgun Gothic, Mac: AppleGothic, Colab: NanumBarunGothic)
import platform
system_name = platform.system()

if system_name == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif system_name == 'Darwin': # Mac
    plt.rc('font', family='AppleGothic')
else: # Colab or Linux (나눔글꼴 설치 필요)
    plt.rc('font', family='NanumBarunGothic')

# 마이너스 기호 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

# 2. 시각화 함수 정의
def draw_yearly_trend(year, up_df, dw_df):
    # 월별 합계 집계
    up_monthly = up_df.groupby('월')['승객수'].sum()
    dw_monthly = dw_df.groupby('월')['승객수'].sum()
    
    # 그래프 그리기
    plt.figure(figsize=(12, 6))
    
    # 승차 그래프 (빨간색 점선)
    plt.plot(up_monthly.index, up_monthly.values, marker='o', linestyle='-', color='red', label='승차', linewidth=2)
    
    # 하차 그래프 (파란색 점선)
    plt.plot(dw_monthly.index, dw_monthly.values, marker='s', linestyle='--', color='blue', label='하차', linewidth=2)
    
    # 제목 및 라벨 설정
    plt.title(f'{year}년 월별 노인 지하철 승하차 인원 추이', fontsize=16)
    plt.xlabel('월', fontsize=12)
    plt.ylabel('승객 수 (명)', fontsize=12)
    
    # X축 눈금 설정 (1월 ~ 12월)
    plt.xticks(range(1, 13))
    
    # 천 단위 콤마 포맷 (Y축)
    current_values = plt.gca().get_yticks()
    plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])
    
    # 범례 및 그리드
    plt.legend(fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.6)
    
    plt.show()

# -------------------------------------------------------
# 3. 각 연도별 그래프 출력
# -------------------------------------------------------

# 2022년 시각화
print("=== 2022년 그래프 ===")
if not up_total_df_2022.empty and not dw_total_df_2022.empty:
    draw_yearly_trend(2022, up_total_df_2022, dw_total_df_2022)
else:
    print("2022년 데이터가 비어있습니다.")

# 2023년 시각화
print("=== 2023년 그래프 ===")
if not up_total_df_2023.empty and not dw_total_df_2023.empty:
    draw_yearly_trend(2023, up_total_df_2023, dw_total_df_2023)
else:
    print("2023년 데이터가 비어있습니다.")

# 2024년 시각화
print("=== 2024년 그래프 ===")
if not up_total_df_2024.empty and not dw_total_df_2024.empty:
    draw_yearly_trend(2024, up_total_df_2024, dw_total_df_2024)
else:
    print("2024년 데이터가 비어있습니다.")