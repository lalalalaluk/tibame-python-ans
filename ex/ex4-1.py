n = input()
words = n.split()
reversed_words = []
for w in words:
    reversed_words.append(w[::-1])
print(' '.join(reversed_words))