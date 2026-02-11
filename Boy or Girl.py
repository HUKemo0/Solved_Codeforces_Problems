def main():
  string = input()

  for letter in string:
    for rest in string[string.find(letter)+1:]:
      if letter == rest:
        string = string[:string.find(rest)] + string[string.find(rest)+1:]

  if len(string)%2 == 0:
    print("CHAT WITH HER!")
  else:
    print("IGNORE HIM!")

if __name__ == '__main__':
  main()