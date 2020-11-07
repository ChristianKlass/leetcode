def two_sum(nums, target):
    answer = []
    nums_reversed = list(reversed(nums))
    for i in nums_reversed:
        for j in nums_reversed:
            print(i, " ", j)
            
            if i != j and i + j == target:
                answer.insert(0, nums.index(i))
                answer.insert(1, nums.index(j))

                break
        if len(answer) == 2:
            break

    return answer


def main():
    nums = [3, 3]
    target = 6
    print(two_sum(nums, target))


if __name__ == "__main__":
    main()
