# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here
    content = open(filename, 'r').read()

    return content


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    texts = {}

    for word in text.split(" "):
        if word in texts:
            texts[word] += 1
        else:
            texts[word] = 1

    return texts
