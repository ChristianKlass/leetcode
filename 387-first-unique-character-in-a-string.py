def first_unique(s: str) -> int:
  # handle 1 character or 1st char != 2nd char
  if (len(s) == 1) or (s[0] != s[1]):
    index = 0
  # handle empty string
  elif (len(s) == 0):
    index = -1
  # handle last char
  elif (s[len(s) - 2] != s[len(s) - 1]):
    index = len(s) - 1
  # everything else
  else:
    for i in range (1, len(s) -1):
      if s[i] != s[i+1] and s[i-1] != s[i]:
        index = i
        break

  return index


def main():
    s = "123fdvamosvpmadd"

    print(first_unique(s))


if __name__ == "__main__":
    main()
