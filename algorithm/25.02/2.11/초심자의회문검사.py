T = int(input())
for tc in range(1, T + 1):
    word = input().strip()
    N = len(word)
    palindrome = True
    for i in range(N // 2):
        if word[i] != word[N - 1 - i]:
            palindrome = False
            break

    if palindrome:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
