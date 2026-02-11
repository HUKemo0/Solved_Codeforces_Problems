width, high = map(int, input().split())

if (width*high) % 2 == 0:
    print(int(width*high/2))

else:
    if high % 2 == 1 and width % 2 == 1:
        print(int((width * high - 1) / 2))

    elif high % 2 == 0:
        print(int(high/2*width))

    elif high % 2 == 1:
        print(int(high/2*width + width/2))