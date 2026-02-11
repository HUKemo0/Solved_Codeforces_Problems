def main():
    number, abstract = [int(x) for x in input().split()]

    for n in range(1, abstract + 1):
        if (number / 5) % 2 == 0:
            number = int(number / 10)

        else:
            number -= 1

    print(number)

if __name__ == '__main__':
    main()