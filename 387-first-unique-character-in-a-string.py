def first_unique(s: str) -> int:
  x = ""
  index = -1
  # handle empty string
  if (len(s) == 0):
    index = -1
  # handle 1 character
  elif (len(s) == 1):
    index = 0
  # everything else
  else:
    x = s
    for i in x:
      if x.count(i) != 1:
        x = x.replace(i, '')

    if len(x) != 0:
      index = s.index(x[0])

  return index


def main():
    s = "cc"
    print(first_unique(s))


if __name__ == "__main__":
    main()
