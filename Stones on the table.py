def main():
    number_of_rocks = int(input())
    rocks_colors = input()
    counter:int = 0

    for i in range(len(rocks_colors) - 1):
        if rocks_colors[i] == rocks_colors[i+1]:
            counter += 1
        
    print(counter)

if __name__ == '__main__':
    main()