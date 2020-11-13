def longest_substring(s: str) -> int:
    if len(s) <= 1:
        return len(s)

    str_len = len(s)
    

    # longest = ""
    # current = ""
    # for i in s:
    #     if i in current:
    #         if len(longest) < len(current):
    #             longest = current

    #         current = i
    #     else:
    #         current += i

    # print(longest, current)
    # if len(longest) < len(current):
    #     longest = current

    return len(longest)


def main():
    s = "dvdf"
    print(longest_substring(s))


if __name__ == "__main__":
    main()
