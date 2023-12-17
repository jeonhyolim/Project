import random
import pandas as pd

random.seed(100)

def write_file(resident_list, names, st_address):
    #### Your Code Here ####
    # 1. 실제 거주하는 주민 이름 목록 (resident_list)을 resident.txt 파일에 저장
    file_name = './resident.txt'

    with open(file_name, 'w+') as file:
        file.write('\n'.join(resident_list))
        
    # 2. 주민 목록 (names)과 주소 (st_address)를 address.txt 파일에 저장
    file_name_add = './address.txt'
    with open(file_name_add,'w+') as file:
        for i in range(len(names)):
            adress_txt = names[i] + ": " + st_address[i]
            file.write(adress_txt + '\n')
    return


def read_file():
    #### Your Code Here ####
    openResidentList=[]
    with open("./resident.txt", "r") as f:
        for line in f:
            openResidentList.append(line.strip())

    openAddressList =[]
    with open("./address.txt", "r") as f:
        for line in f:
            openAddressList.append(line.strip())
    street_dict = dict()
    for name in openAddressList:
        nameAndAddress = name.split(":")
        #print(name)
        newAddressList = nameAndAddress[1].split(" ")
        if nameAndAddress[0] in openResidentList:
            if newAddressList[-1].isdigit():
                #실제 거주민이면서 주소도 정확
                print(f'{name} -> In resident list and correct address.')
                
                streetName = newAddressList[1] +" "+ newAddressList[2]
                if streetName in street_dict.keys():
                    street_dict[streetName] += 1
                else:
                    street_dict[streetName] = 1
                
            else:
                #실제 거주민이지만 주소 틀림
                print(f'{name} -> In resident list and wrong address.')
        else:
            if newAddressList[-1].isdigit():
                #거주민 아니지만 주소 맞음
                print(f'{name} -> Not in resident list.')
            else:
                #거주민도 아니고 주소 틀림
                print(f'{name} -> Not in resident list and wrong address.')

    for street in street_dict.keys():
        print(f"Based on the list, there are {street_dict[street]} residents in {street}")
    return



def random_create(all_names, street_list):
    #### Your Code Here ####
    # 이름 무작위 추출 및 랜덤 주소 생성
    # names : 모든 주민 주소, len(names) == 500
    # resident_list : 실제 거주민 주소, len(resident_list) == 300
    # rand_address : 랜덤으로 생성한 주소, len(rand_address) == 500

    # 이름 목록 (all_names)에서 500 개를 무작위 추출해 주민 목록 (names)으로 저장
    names = random.sample(all_names, 500) 

    # 500 중 300 개를 무작위 추출해 실제 주민 목록(resident_list, (300 개는 실제 거주하는 주민 이름이 되고, 나머지 200 개는 거주하지 않지만 잘못 포함된 사람들))
    # 300명의 실제 주민과 200명의 잘못 포함된 주민 생성
    resident_list = random.sample(names, 300)
    not_resident_list = list(set(names)-set(resident_list))

    # 거리명에서 100 를 무작위 추출한 뒤 무작위 숫자 더하기
    street_100 = random.sample(street_list, 100) # 지역 100개 무작위 추출

    # 랜덤으로 0부터 9999 사이의 숫자를 100개 생성
    random_numbers = [random.randint(0, 9999) for _ in range(100)]

    # 각 숫자를 4자리로 변환하고 결과를 리스트에 저장
    random_pick_num_100 = [f'{num:04d}' for num in random_numbers]

    rand_address_100 = []
    for i in range(len(random_pick_num_100)):
        rand_address_100.append(street_100[i]+" "+str(random_pick_num_100[i]))
        
    n = random.choice(range(11))
    for i in range(0, len(rand_address_100),n):
        n = random.choice(range(11))
        rand_address_100[i] += " " + ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for _ in range(4))

    # rand_address 100개를 -> 500개로 복제
    rand_address =random.choices(rand_address_100, k=500)
    ########################
    
    return names, resident_list, rand_address

#### Your Code Here ####
# all_names : names.txt 파일에서 읽어온 모든 이름을 저장한 list

all_names=[]
with open("all_name.txt", "r") as f:
    for line in f:
        all_names.append(line.strip())

path = 'Street_Names.csv'  #Street_Names.csv 가 저장된 경로를 넣어주세요

########################

street_nm = pd.read_csv(path)
street_list = street_nm['FullStreetName'].values.tolist()

names, resident_list, rand_address = random_create(all_names, street_list)
write_file(resident_list, names, rand_address)
read_file()

