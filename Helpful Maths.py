def main():
  string = input()
  result = ""
  numbers_list = []
  numbers_list = string.split('+')
  numbers_list.sort()
  for num in numbers_list:
    result += f"{num}+"
  print(result[:len(result)-1])

if __name__ == '__main__':
  main()