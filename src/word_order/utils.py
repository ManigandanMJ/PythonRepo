#To find the number of times the word is repeated
import logging
logging.basicConfig(filename = "c:\\logs\\word_order_log.log",filemode ='w',)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

num = int(input())
words_list = []
for i in range(num):
    log.info("Appending the list values")
    words_list.append(input().strip())

counts = {}

for word in words_list:
    log.info("Word is added to word deictionary")
    counts[word] = counts.get(word, 0) + 1

def len_word():
    log.info("Finding the length of dict")
    print(len(counts))
    return len(counts)
def count_word():
    for word in words_list:
        log.info("verifies if word in list")
        if counts[word] != 0:
            print(counts[word], end=" ")
            counts[word] = 0

