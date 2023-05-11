
# helper functions:

def wordCount(data):
    return len(data.split())

def sentenceCount(data):
    return len(data.split(". "))

def letterCount(data):
    letter_map = {}
    data = data.lower()

    for x in data:
        if x not in letter_map:
            letter_map[x] = 1
        else:
            letter_map[x] += 1
    # print(letter_map)
    return letter_map

def createReport(filename):

    with open(filename) as f:
        file_contents = f.read()

    words = wordCount(file_contents)
    count_map = letterCount(file_contents)
    sentences = sentenceCount(file_contents)

    with open("report.txt", "w") as wf:
        wf.write(f"--- Begin report of {filename} ---\n\n")
        wf.write(f"{words} words found in the document.\n")
        wf.write(f"{sentences} sentences found in the document.\n")
        wf.write("\n")

        for k, v in sorted(count_map.items()):
            if k.isalpha():
                wf.write(f"The '{k}' character was found {v} times.\n")

        wf.write("\n--- End report ---")


# Main Code goes here
filename = "books/frankenstein.txt"
createReport(filename)

    


