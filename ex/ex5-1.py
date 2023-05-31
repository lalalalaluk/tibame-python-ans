n = list(input())

ans = []
stored_words = []
for i in n[::-1]:
    if i in stored_words:
        continue
    else:
        stored_words.append(i)

print(''.join(stored_words[::-1]))
