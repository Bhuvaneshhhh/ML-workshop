def find_occurrence(text, word):
    words = text.split()
    count = words.count(word)
    return count

text = "yellow mellow yellow fellow"
word = "yellow"
n = find_occurrence(text, word)
print(n,"is the number of times", word,"has been repeated.")
