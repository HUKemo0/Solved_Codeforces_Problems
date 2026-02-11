def test(word):
    if len(word) > 10:
        print(f"{word[0]}{len(word)-2}{word[len(word)-1]}")
    
    else:
        print(word)

number = int(input())
i=1
while i <= number:
    word = input().lower()
    test(word)
    i+=1