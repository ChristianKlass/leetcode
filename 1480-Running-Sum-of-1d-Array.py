def runningSum(nums):
  sum_list = []
  sum_list.append(nums[0])

  for i in range(1, len(nums)):
    # nums[i] = nums[i] + nums[i-1]
    # Strangely, just doing the above is LESS efficient than making a new list and appending.

    sum_list.append(sum_list[i - 1] + nums[i])

  return sum_list


def main():
    num_list = [1, 2, 3, 4]

    print(runningSum(num_list))


if __name__ == "__main__":
    main()
