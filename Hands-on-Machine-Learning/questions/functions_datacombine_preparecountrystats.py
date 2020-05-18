# 이후 필요한 작업에 따라 아래의 함수를 변형하여 사용할 수 있음.

def prepare_country_stats(oecd_bli, gdp_per_capita):

    # data 구조 확인 및 준비
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"] # 필요한 부분만 불러옴.
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value") # 데이터 재구조화.

    # column, index 이름 설정
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index("Country", inplace=True)

    # dataframe 합치기
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                  left_index=True, right_index=True)

    # 정렬
    full_country_stats.sort_values(by="GDP per capita", inplace=True)

    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
    return full_country_stats[["GDP per capita", 'Life satisfaction']].iloc[keep_indices]