def main():
    user_input:str = input()

    result:str = user_input[:0] + user_input[0].upper() + user_input[1:]

    print(result)

if __name__ == '__main__':
    main()