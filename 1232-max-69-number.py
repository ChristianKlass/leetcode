def maximum69Number (num: int) -> int:

  return int(str(num).replace("6", "9", 1))
  
def main():
  num = "696996"
  print(maximum69Number(num))


if __name__ == "__main__":
  main()
