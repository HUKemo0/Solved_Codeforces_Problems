def main():
    user_input:str = input()
    lower:int = 0
    upper:int = 0

    for i in range(len(user_input)):

        if user_input[i].islower():
            lower += 1

        else:
            upper += 1

    if lower >= upper:
        print(user_input.lower())

    elif lower < upper:
        print(user_input.upper())

if __name__ == '__main__':
    main()
