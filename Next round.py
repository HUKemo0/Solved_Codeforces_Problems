def main():
    partecipants, index = map(int, input().split())

    result = 0

    user_input = input()
    int_list = [int(num) for num in user_input.split()]

    for n in int_list:
        if n >= int_list[index-1] and n > 0:
            result += 1

    print(result)

if __name__ == '__main__':
    main()