def binary_search(arr, avg_score):
    #### Your Code Here ####
    # start : 초기는 0으로 설정
    # end : 초기값은 arr의 length 값으로 설정
    def Qsort(arr):
        def cus_compare(a, b):
            if isinstance(a, float) and isinstance(b, float):
                return a - b
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        lesser_arr, equal_arr, greater_arr = [], [], []
        for item in arr:
            comparison = cus_compare(item, pivot)
            if comparison < 0:
                lesser_arr.append(item)
            elif comparison > 0:
                greater_arr.append(item)
            else:
                equal_arr.append(item)
        arr = Qsort(lesser_arr) + equal_arr + Qsort(greater_arr)
        return arr
    
    arr = Qsort(arr) 
    start = 0
    end = len(arr) #34

    if avg_score in arr:
        rank = len(arr) - arr.index(avg_score)
        return rank
    else:
        while start < end:
            mid = (start+end)//2
            print(mid, start, end)
            #print(f"Mid: {mid}")
        
            if arr[mid] >= avg_score:
                end = mid
            else:
                start = mid + 1
            
        rank =len(arr)-start+1
        ########################
        return rank


#### Your Code Here ####
# 파일 불러오기 코드 작성
# scores : score.txt 파일에서 읽어온 전체 학생들의 평균 점수를 저장하는 list
scores=[]
with open("score.txt", "r") as f:
    for line in f:
        scores.append(float(line.strip()))

mid, fin = input('Input your mid score and final score: ').split()
my_score = (float(mid)+float(fin))/2 #중간고사와 기말고사 점수 입력받고 평균을 구하는 코드 작성


########################

rank = binary_search(scores, my_score)
print(f'{my_score}은 {rank}등 입니다')

