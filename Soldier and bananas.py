def main():
    total:int = 0
    banana_cost, money, number_of_banana = [int(x) for x in input().split()]

    for i in range(1, number_of_banana + 1):
        total += i*banana_cost

    if total > money:
        result:int = total - money
        print(result)

    else:
        print("0")

if __name__ == '__main__':
    main()