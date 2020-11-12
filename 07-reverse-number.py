def reverse(x):
    reversed_number = ""
    is_negative = False

    if x == 0:
        return 0
    elif x < 0:
        is_negative = True

    str_number = str(abs(x))

    for i in str_number[::-1]:
        reversed_number += i

    answer = int(reversed_number)
    if answer >= 2147483647:
        answer = 0
        
    elif is_negative:
        answer = answer * -1

    return answer


def main():
    number = 12345
    print(reverse(number))


if __name__ == "__main__":
    main()

