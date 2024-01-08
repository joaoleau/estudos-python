
if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    nums = [x,y,z]
    
    combs = [
        [a,b,c]
        for a in range(nums[0]+1)
        for b in range(nums[1]+1)
        for c in range(nums[2]+1)
        if a+b+c!=n
    ]
    
    print(combs)