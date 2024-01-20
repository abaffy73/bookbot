def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(word_len(file_contents))
        #print(letter_count(file_contents))
        print("--Beginning report on frankenstein.txt--")
        report(file_contents)
        
def word_len(text):
    words = text.split()
    return len(words)

def letter_count(text):
    dicts = {}
    low_words = text.lower()
    for i in low_words:
        if not(i in dicts):
            dicts[i] = 1
        else:
            dicts[i] += 1
    return dicts

def report(text):
    words = word_len(text)
    d = letter_count(text)
    w_list = []
    for w in d.keys():
        if w.isalpha():
            w_list.append(w)
    print(f"{words} words found in the document")
    print("")
    w_list.sort()
    for w in w_list:
        print(f"The {w} character was found {d[w]} times")


main()
