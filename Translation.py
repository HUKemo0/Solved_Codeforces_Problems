def main():
    word_s = input()
    word_t = input()
    temp_word = ''

    for n in range(len(word_s)):
        temp_word += word_s[len(word_s)- 1 - n]

    if word_t == temp_word:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()