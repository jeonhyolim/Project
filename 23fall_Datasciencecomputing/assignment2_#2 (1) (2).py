import random
import time

random.seed(100)

def QSort1(arr):
    start = time.time()
    
    ### Edit Here ###
    # Quick Sort with pivot in index 0
    def loop(arr):
        def cus_compare(a, b):
            if isinstance(a, int) and isinstance(b, int):
                return a - b
            elif isinstance(a, int) and isinstance(b, str):
                return -1
            elif isinstance(a, str) and isinstance(b, int):
                return 1
            else:  # both are strings
                if a[0] == b[0]:
                    return len(a) - len(b)
                else:
                    return ord(a[0]) - ord(b[0])
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
        arr = loop(lesser_arr) + equal_arr + loop(greater_arr)
        return arr
    arr = loop(arr)  
    ################
    
    #### Do not edit here ####
    end = time.time()
    print("Qsort1 time:", end-start)
    return arr

def QSort2(arr):
    start = time.time() 
    
    ### Edit Here ###
    # Quick Sort with pivot in random index 
    def loop(arr):
        def cus_compare(a, b):
            if isinstance(a, int) and isinstance(b, int):
                return a - b
            elif isinstance(a, int) and isinstance(b, str):
                return -1
            elif isinstance(a, str) and isinstance(b, int):
                return 1
            else:  # both are strings
                if a[0] == b[0]:
                    return len(a) - len(b)
                else:
                    return ord(a[0]) - ord(b[0])
        if len(arr) <= 1:
            return arr
        pivot = random.choice(arr)
        lesser_arr, equal_arr, greater_arr = [], [], []
        for item in arr:
            comparison = cus_compare(item, pivot)
            if comparison < 0:
                lesser_arr.append(item)
            elif comparison > 0:
                greater_arr.append(item)
            else:
                equal_arr.append(item)
        arr = loop(lesser_arr) + equal_arr + loop(greater_arr)
        return arr
    arr = loop(arr)  
    ################
    
    #### Do not edit here ####
    end = time.time()
    print("Qsort2 time:", end-start)
    return arr

def QSort3(arr):
    start = time.time()
    
    ### Edit Here ###
    # Quick Sort with early stopping
    def loop(arr):
        def cus_compare(a, b):
            if isinstance(a, int) and isinstance(b, int):
                return a - b
            elif isinstance(a, int) and isinstance(b, str):
                return -1
            elif isinstance(a, str) and isinstance(b, int):
                return 1
            else:  # both are strings
                if a[0] == b[0]:
                    return len(a) - len(b)
                else:
                    return ord(a[0]) - ord(b[0])
        if len(arr) <= 1:
            return arr

        pivot = random.choice(arr)
        lesser_arr, equal_arr, greater_arr = [], [], []

        check_number = 0
        flag = True

        for i in range(len(arr)):
            comparison = cus_compare(arr[i], pivot)
            if comparison < 0:
                lesser_arr.append(arr[i])
            elif comparison > 0:
                greater_arr.append(arr[i])
            else:
                equal_arr.append(arr[i])

            #조기 종료 조건
            if i != 0 and cus_compare(arr[i-1] ,arr[i])<0:
                flag = False
        if flag :
            return arr
        arr = loop(lesser_arr) + equal_arr + loop(greater_arr)
        return arr
    arr = loop(arr)  
    #### Do not edit here ####   
    end = time.time()    
    print("QSort3 time:", end - start)

    return arr

def main():
    ### Edit Here ###
    
    # get number list
    arr = []

    while True:
        user_input = input("input number (n/N for stop): ")

        if user_input == 'n' or user_input == 'N':
            break

        arr.append(user_input)
    #del arr[-1]
    
    for i in range(len(arr)):
        try:
            arr[i] = int(arr[i])
        except ValueError:
            pass
        
    print(arr)
    
    #################

    result1 = QSort1(arr)
    result2 = QSort2(arr)
    result3 = QSort3(arr)
    
    print("QSort1 result:", result1)
    print("QSort2 result:", result2)
    print("QSort3 result:", result3)

if __name__ == "__main__":
    main()
