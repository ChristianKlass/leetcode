def restore_string(s:str, indices:[]) -> str:
  out = ""

  for index, res in enumerate(indices):
    out += s[res]
    print (index, res, s[res])

  return out


def main():
    some_string = "codeleet"
    indices = [4,5,6,7,0,2,1,3]

    print(restore_string(some_string, indices))


if __name__ == "__main__":
    main()

