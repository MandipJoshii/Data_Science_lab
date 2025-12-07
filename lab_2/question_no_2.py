# paragraph = input("ENTER YOUR PARAGRAPH: ").split()

# print(paragraph)

# unique_word_identifier = set(paragraph)
# print(unique_word_identifier)


paragraph = input("ENTER YOUR PARAGRAPH: ").split()


unique_word_identifier = set(paragraph)
sort_paragraph = sorted(paragraph)
count_unique_word = len(unique_word_identifier)


print(f"YOUR PARAGRAPH IS : {paragraph}")
print(f"AFTER REMOVING DUPLICATED WORDS: {unique_word_identifier}")
print(f"AFTER VALUE ARE SORTED: {sort_paragraph}")
print(f"COUNT UNIQUE WORD: {count_unique_word}")
