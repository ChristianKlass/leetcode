def two_sum(nums, target):
    answer = []

    for i in range (len(nums)):
        if i <= target:
            for j in range (len(nums)):
                if j != i and j <= target:
                    if nums[i] + nums[j] == target:
                        answer.insert(0, i) 
                        answer.insert(1, j)
                        break

            if len(answer) == 2:
                break

    return answer


def main():
    nums = [100,200]
    target = 199993
    print(two_sum(nums, target))


if __name__ == "__main__":
    main()
