from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def make_df_team(year, table_list_team, team_n):
    df = pd.DataFrame(index=range(0,team_n), columns=['시즌', '순위', '팀', '경기수','승점','승','패','세트득실률',
                                                      '점수득실률', '세트수','공격성공률', '블로킹 (세트당)','서브(세트당)', '득점'])
    df['시즌'] = f'{str(year)}_{str(year+1)[2:]}' 
    df['순위'] = list(range(1,team_n+1)) 
    
    for i in range(0,team_n): 
        for j in range(0,12):
            df.iloc[i,j+2] =table_list_team[i].find_all('td')[j].text # j=0 -> 경기수,

    team_name = []
    for i in range(0,team_n): 
        team_name.append(table_list_team[i].find_all('td')[0].find_all('span')[1].text) # 팀

    df['팀'] = team_name
    df['승점'] = df['승점'].apply(lambda x : x.replace("\n",'').replace(" ", ""))
    return df


def make_df_player(year, player_list_final, player_num):
    df = pd.DataFrame(index=range(0, player_num), columns=['시즌', '순위', '선수', '팀', '득점', '공격성공률', '서브',
                                                       '블로킹 (세트당)','수비 (세트당)', '리시브효율'])
    df['시즌'] =f'{str(year)}_{str(year+1)[2:]}' 
    df['순위'] = list(range(1,player_num+1)) 
    
    for i in range(0, player_num): 
        for j in range(len(df.columns)-3):
            df.iloc[i,j+3] =player_list_final[i].find_all('td')[j].text # j=0 -> 경기수,  # 득점 table_list_team[i].find_all('td')[j].text

    # 선수, 팀
    team_name = [] 
    player_name = []
    team_namee = []
    for i in range(0, player_num):
        team_name.append(player_list_final[i].find_all('td')[0].find_all('div')[0].text.replace("\n",'').replace(" ", ""))
    #print(team_name)

    for i in range(0, player_num):
        temp = team_name[i].split('(')
        #print(temp)
        player_name.append(temp[0])
        team_namee.append(temp[1].replace(')', ''))
    
    df['팀'] = team_namee
    df['선수'] = player_name
    return df

def crawler():
    #### Your Code Here ####
    man_woman = ['kovo', 'wkovo']
    year_list = list(range(2005, 2023))
    for gender in man_woman:
        for year in year_list:
            url = f"https://sports.news.naver.com/volleyball/record/index?category={gender}&year={year}"
            print(url)
            a = urlopen(url)
            soup = BeautifulSoup(a.read(), "html.parser")

            # 1. 팀
            table_list = soup.find_all(attrs={'id':'regularTeamRecordList_table'})
            table_list_team = table_list[0].find_all('tr')

            # 팀 개수 세기
            a = BeautifulSoup(str(table_list_team), 'html.parser')
            items = a.select("tr")
            
            make_df_team(year, table_list_team, len(items)).to_csv(f'{year}_{"man" if gender == man_woman[0] else "woman" }_TeamRecord.csv', encoding='cp949')

            # 2. player
            player_list = soup.find_all(attrs={'id':"playerRecordTable"}) 
            player_list_final = player_list[0].find_all('tr')

            # 2.1 player 수 세기
            a_player = BeautifulSoup(str(player_list), 'html.parser')
            items_player = a_player.select("tr")
            #print(len(items_player))

            make_df_player(year, player_list_final, len(items_player)).to_csv(f'{year}_{"man" if gender == man_woman[0] else "woman" }_PlayerRecord.csv', encoding='cp949')
    ######################### 


if __name__ == '__main__':
    crawler()

