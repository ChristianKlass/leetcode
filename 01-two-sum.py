def two_sum(nums, target):
    answer = []

    nums_reversed = list(reversed(nums))

    for i in nums:
        for j in nums_reversed:
            # print(i, " ", j)
            
            if i + j == target:
                answer.insert(0, nums.index(i)) 
                answer.insert(1, nums.index(j, nums.index(i)+1))
                break
        if len(answer) == 2:
            break

    return answer


def main():
    nums = [2,7,11,15]
    target = 9
    print(two_sum(nums, target))


if __name__ == "__main__":
    main()
