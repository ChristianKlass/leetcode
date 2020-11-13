def runningSum(nums):

  for i in range(1, len(nums)):
    nums[i] += nums[i - 1]

  return nums


def main():
    num_list = [1, 2, 3, 4]

    print(runningSum(num_list))


if __name__ == "__main__":
    main()
