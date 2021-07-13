if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    
def second_largest_number(arr):
    unique_nums = set(arr)
    sorted_nums = sorted(unique_nums, reverse=True)
    print(sorted_nums[1])
    

second_largest_number(arr)



