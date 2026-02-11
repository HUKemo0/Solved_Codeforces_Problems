def multi(a:int, b:int):
    counter:int = 0
    while(a<=b):
        a *= 3
        b *= 2
        counter += 1
    return counter

def main():
    limak, bob = [int(x) for x in input().split()]
    print(multi(limak, bob))

if __name__ == '__main__':
    main()