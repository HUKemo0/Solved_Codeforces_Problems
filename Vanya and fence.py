def main():
  numberOfFriends, wallHight = map(int, input().split())
  total = 0
  friendsList = list(map(int, input().split()))
  for num in range(numberOfFriends):
    if friendsList[num] > wallHight:
      total += 2
    else:
      total += 1

  print(total)

if __name__ == '__main__':
  main()