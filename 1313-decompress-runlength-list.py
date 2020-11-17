def decompress_list(nums:[int]) -> []:
  answer = []
  freq = 0
  value = 0

  for i in range (0, len(nums), 2):
    freq = nums[i]
    value = nums[i+1]
    for j in range(freq):
      answer.append(value)

  return answer


def main():
    nums = [1,2,3,4]

    print(decompress_list(nums))


if __name__ == "__main__":
    main()

