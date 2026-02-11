def main():
    arr:int = [[0 for i in range(5)] for j in range(5)]
    index:int = [0,0]
    moves:int = 0

    for i in range(5):
        j:int = 0
        arr[i][j], arr[i][j+1], arr[i][j+2], arr[i][j+3], arr[i][j+4] = map(int, input().split())

    for i in range(5):
        for j in range(5):
            if arr[i][j] == 1:
                index[0] = i
                index[1] = j
    
    moves = abs(index[0] - 2) + abs(index[1] - 2)
    print(moves)

if __name__ == '__main__':
    main()