def main():
    number_of_letters = int(input())
    user_input = input()
    anton:int = 0

    for n in range(len(user_input)):
        if user_input[n] == 'A':
            anton += 1
        
    if len(user_input) / 2 > anton:
        print('Danik')

    elif len(user_input) / 2 < anton:
        print('Anton')

    else:
        print('Friendship')

if __name__ == '__main__':
    main()