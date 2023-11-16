# 2023711994_전효림_데이터사이언스 컴퓨팅_중간고사 대체 과제
# 롤체지지 https://lolchess.gg/leaderboards?region=kr&mode=ranked 
# 대상: 국가별 챌린저~그랜드마스터 순위, 플레이어id, 티어, 승률, 게임수, 이긴횟수, 순위 방어 횟수 등

import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from datetime import datetime
import os
import time

def make_df(a, person_n, region_name, page):

    # 추후 csv에 저장할 빈데이터 프레임 형성
    df = pd.DataFrame(index=range(0,person_n), columns=['크롤링사이트','순위', '닉네임', '티어', 'LP','승률','Top4%','게임 수','승','Top4'])
    df['크롤링사이트'] = region_name # 지역은 추후 data concat할 때 편하게 하려고 만들어줌
    rank = []
    nickname = []
    tier = []
    lp = []
    winrate = []
    top4rate = []
    plays = []
    wins = []
    top4 = []

    # 순위가 모두 1~100으로 저장된다는 문제점이 있음, page 수에 따라서 값을 변경하고 아래 크롤링 때 변환해서 더해주도록 함
#    if page ==1:
#        p_add = 0 # 빈 값으로 바꾸기
#        p_add = int(p_add)
#    else:
#        p_add = (page-1)*100
#        p_add = int(p_add)

#    print(p_add)

    # 크롤링하며 데이터 값을 저장해줌
    for i in range(1,person_n+1): # person_n은 한 페이지에 몇명이있는지 숫자 세어야 함
        temp_list = a[i].select("span")
        if len(temp_list) == 5:
            temp_rank = temp_list[0].text
            temp_rank = temp_rank.replace('#', '')
            temp_rank_int = int(temp_rank)
            rank_fin =  temp_rank_int # p_add +
            #print(p_add)
            rank.append(rank_fin) 
            nickname.append(temp_list[1].text)
            tier.append(temp_list[2].text)
            lp.append(temp_list[4].text)
            winrate.append(a[i].find(attrs = {"class":"winRate"}).text)
            top4rate.append(a[i].find(attrs = {"class" : "topRate"}).text)
            plays.append(a[i].find(attrs = {"class":"plays"} ).text)
            wins.append(a[i].find(attrs = {"class":"wins"}).text)
            top4.append(a[i].find(attrs = { "class" :"top4" }).text)
        elif len(temp_list) == 6: # 길이가 6인 경우는 순위 상승 값이 포함된 경우이므로, temp_list의 인덱스를 1씩 더하여 크롤링한다
            temp_rank = temp_list[1].text
            temp_rank = temp_rank.replace('#', '')
            temp_rank_int = int(temp_rank)
            rank_fin =  temp_rank_int # + p_add
            #print(p_add)
            rank.append(rank_fin) 
            nickname.append(temp_list[2].text)
            tier.append(temp_list[3].text)
            lp.append(temp_list[5].text)
            winrate.append(a[i].find(attrs = {"class":"winRate"}).text)
            top4rate.append(a[i].find(attrs = {"class" : "topRate"}).text)
            plays.append(a[i].find(attrs = {"class":"plays"} ).text)
            wins.append(a[i].find(attrs = {"class":"wins"}).text)
            top4.append(a[i].find(attrs = { "class" :"top4" }).text)

    # 크롤링하여 구한 리스트들을 데이터 프레임의 각 열로 넣어준다
    df['순위'] = rank
    df['닉네임'] = nickname
    df['티어'] = tier
    df['LP'] = lp
    df['승률'] = winrate
    df['Top4%'] = top4rate
    df['게임 수'] = plays
    df['승'] = wins
    df['Top4'] = top4

    return df

def crawler():
    start_time = time.time() # 시작 시간

    # 1. 웹사이트 입력 기능 (사용자가 원하는 값만 크롤링)
    tier_list_str = input("크롤링할 티어들을 쉼표로 구분하여 입력하세요 (예: challenger, grandmaster): ")
    region_list_str = input("크롤링할 지역들을 쉼표로 구분하여 입력하세요 (예: br, eune): ")

    tier_list = tier_list_str.split(',')
    region_list = region_list_str.split(',')

    # 전체 크롤링
    #tier_list=['challenger', 'grandmaster']
    #region_list=[ 'br' , 'eune', 'euw', 'jp', 'kr', 'lan', 'las', 'na', 'oce', 'tr', 'ru', 'ph', 'sg', 'th', 'tw', 'vn']# ,'global'] 
    for tier in range(len(tier_list)):
        for region in range(len(region_list)):
            url = f'https://lolchess.gg/leaderboards?region={region_list[region]}&mode=ranked&tier={tier_list[tier]}&page='#1'
            #print(url)
            for i in range(1, 11):
                temp_url = url + str(i)
                print(temp_url)
                driver = webdriver.Chrome()
                driver.get(temp_url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                driver.quit()
                a = soup.select('tr',attrs={'class':'css-1k9ek97 e1a1fqys2'}) # 표가 담겨져있는 값을 가져온다
                page = i # 랭크에 써줄 값 (3페이지의 경우 -> 3)
                if len(a) == 1:
                    print('끝남') # 페이지가 없는 경우에 break로 종료한다
                    break
                else:
                    if len(a) == 102:
                        person_n = 100
                    else:
                        person_n = len(a)-1
                    region_name = region_list[region]

                    # 2. 웹페이지 저장 시 고유한 정의를 통한 분류
                    df_result = make_df(a, person_n, region_name, page)
                    directory = f'C:/Users/wjsgy/OneDrive/바탕 화면/데사컴/mid_crawling_result/'
                    if not os.path.exists(directory+f'{tier_list[tier]}'): # tier 별로 구분해서 데이터를 저장하도록 함 (고유한 정의를 통한 데이터 분류)
                        os.makedirs(directory+f'{tier_list[tier]}')
                    save_time = datetime.now()
                    formatted_time = save_time.strftime("%Y%m%d%H%M%S")
                    df_result.to_csv(directory+f'{tier_list[tier]}/{tier_list[tier]}_{region_list[region]}_page{i}_{formatted_time}.csv', index=False, encoding='utf-8-sig') # 3. 출력 CSV파일의 이름
                    
                    # 4. 완료 후 크롤링 결과, 소요 시간 안내
                    end_time = time.time() # 종료시간
                    total_time = end_time - start_time # 걸린 시간
                    rounded_total_time = round(total_time, 3) # 시간 깔끔하게 보이게 반올림
                    formatted_total_time = "{:.3f}".format(rounded_total_time)

                    print('--------------------------------------------------------------------------------------------------------')
                    print(f'해당 {tier_list[tier]}_{region_list[region]}_page{i} 페이지를 크롤링하는데 소요된 시간은 {formatted_total_time}초입니다')
                    print('크롤링 결과는 다음과 같습니다')
                    print(df_result)
                    print('--------------------------------------------------------------------------------------------------------')

if __name__ == '__main__':
    crawler()