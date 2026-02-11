def test(weight):
    if weight == 1 or weight == 0 or weight == 2:
        print("NO")
        return

    elif weight%2 == 0:
        print("YES")
        return
    
    else:
        print("NO")
        return




weight = input()
test(int(weight))
