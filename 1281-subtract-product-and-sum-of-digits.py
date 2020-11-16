def subtract_product_and_sum(n:int) -> int:
  num_sum = 0
  product = 1

  while (n != 0):
    number = n % 10
    num_sum += number
    product *= number

    n //= 10

  print(num_sum, product)

  return product - num_sum


def main():
    num = 1234

    print(subtract_product_and_sum(num))


if __name__ == "__main__":
    main()
