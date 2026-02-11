def main():
    user_input = input()
    lucky_digits:int = 0

    for n in range(len(user_input)):
        if int(user_input[n]) == 7 or int(user_input[n]) == 4:
            lucky_digits += 1

    if lucky_digits == 4 or lucky_digits == 7:
        print('YES')

    else:
        print('NO')

if __name__ == '__main__':
    main()