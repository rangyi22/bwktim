word = input("Input a word : ")
word_list = list(word)
#print(word_list)
for idx in range(len(word_list)):  # _ -> meaningless reserved word
    print(word_list.pop())
    print(word_list)