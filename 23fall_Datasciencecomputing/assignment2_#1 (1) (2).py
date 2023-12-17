import random

def bubble_sort(lcm_list):

    ### Edit Here ###
    n = len(lcm_list)
    
    for i in range(n-1, -1, -1):
        for j in range(0, i):
            if lcm_list[j] > lcm_list[j + 1]:
                lcm_list[j], lcm_list[j + 1] = lcm_list[j + 1], lcm_list[j]
    #################
    
    return lcm_list


def insert_sort(lcm_list):

    ### Edit Here ###
    n = len(lcm_list)
    for i in range(1, n):  
        key = lcm_list[i]
        j = i - 1
        
        while j >=0 and lcm_list[j] < key:
            lcm_list[j+1] = lcm_list[j] 
            j -= 1 
        
        lcm_list[j+1] = key  
    #################

    return lcm_list


def lcm_sort(random_list):
    lcm_list = []

    ### Edit Here ###
    for i in range(len(random_list)):
        for j in range(i + 1, len(random_list)):
            num1 = random_list[i]
            num2 = random_list[j]
            product = num1 * num2
            
            # 최대 공약수
            a, b = num1, num2
            while b:
                a, b = b, a % b
            gcd = a
            
            # 최소 공배수
            lcm = product // gcd
            
            lcm_list.append(lcm)
    #################

    return lcm_list




#### Do not edit here ####
random.seed(100)
random_list = random.sample(range(2, 50), 10)
print(f'Initial List is: {random_list}\n')
unsorted_lcmlist = lcm_sort(random_list)
print(f'List of Least Common Multiple is: {unsorted_lcmlist}\n')
ac_sorted = bubble_sort(unsorted_lcmlist)
print(f'Sorted in Ascending Order: {ac_sorted}\n')
dc_sorted = insert_sort(unsorted_lcmlist)
print(f'Sorted in Descending Order: {dc_sorted}\n')

