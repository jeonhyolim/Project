def OPCount(num: int) -> int:
    ### Edit Here ###
    
    # calculate minimum operation count
    d = [0]*(num+1)

    for i in range(2,num+1):
        d[i] = d[i - 1] + 1
        if i%3==0:
            d[i]=min(d[i//3]+1, d[i])
        if i%2==0:
            d[i]=min(d[i//2]+1, d[i])
    return d[num]

def main():
    ### Edit Here ###
    
    # get input
    num = int(input('Input X: ')) 
    #################
    
    count = OPCount(num)
    
    print("result:", count)

if __name__ == "__main__":
    main()
