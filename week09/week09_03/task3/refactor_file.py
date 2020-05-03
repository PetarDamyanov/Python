def read_file(file):
    f = open(file, "r")
    content = f.read()
    f.close()
    return content


def write_file(file, word):
    f = open(file, "a")
    f.write(f'{word} ')
    f.close()


def main():
    verb = read_file('verb.txt')
    for word in verb.split('\n'):
        # if len(word) <= 5:
        write_file('refactor_verb.txt', word)
    noun = read_file('text.txt')
    for word in noun.split('\n'):
        if len(word) <= 5:
            write_file('dict.txt', word)


if __name__ == '__main__':
    main()
