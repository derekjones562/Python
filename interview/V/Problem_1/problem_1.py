import sys

args = sys.argv
in_filename = args[1]
out_filename = "{}-palindromes.txt".format(in_filename)


def is_palandrome(word):
    word = word.lower()
    is_palandrome = True
    start = 0
    end = len(word) - 1
    while start <= end:
        if word[start] != word[end]:
            is_palandrome = False
        start = start + 1
        end = end - 1
    return is_palandrome


def retrive_words(filename):
    file = open(filename, 'r')
    contents = file.read()
    file.close()
    return contents


def write_words(words):
    file = open(out_filename, 'w')
    for word in words:
        file.write("{}\n".format(word))
    file.close()


def main():
    palandromes = []
    for word in retrive_words(in_filename).split('\n'):
        if is_palandrome(word):
            palandromes.append(word)
    write_words(palandromes)




if __name__ == '__main__':
    main()
