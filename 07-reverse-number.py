def reverse(x):
    reversed = ""
    is_negative = False

    if x == 0:
        return 0
    elif x < 0:
        is_negative = True

    str_number = str(abs(x))

    for i in str_number[::-1]:
      reversed = reversed + i

    answer = int(reversed)
    if is_negative:
        answer = answer * -1

    if answer >= 2147483647 or answer <= -2147483648:
        answer = 0

    return answer


def main():
    number = 12345
    print(reverse(number))


if __name__ == "__main__":
    main()

