#To find the number of times the word is repeated
num = int(input())
words_list = []
for i in range(num):
    words_list.append(input().strip())

counts = {}

for word in words_list:
    counts[word] = counts.get(word, 0) + 1

def len_word():
    print(len(counts))
    return len(counts)
def count_word():
    for word in words_list:
        if counts[word] != 0:
            print(counts[word], end=" ")
            counts[word] = 0

