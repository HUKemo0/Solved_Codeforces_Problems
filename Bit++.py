def main():
    x:int = 0
    n:int = 0
    n = int(input())

    for i in range(0,n):
        statment = input()

        if statment == '++X' or statment == 'X++' or statment == 'x++' or statment == '++x':
            x+=1
        else:
            x-=1

    print(x)

if __name__ == "__main__":
    main()