from random import randint as rand

alphabet = ["a", 'b', 'c', 'd', 'e', 'f', 'g',
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def book_reader(chapter_list):
    for chapter in chapter_list:
        yield chapter
        print(chapter)


def split_chapters(book):
    return book.split("#")


def file_reader(file_name):
    file = open(file_name, "r")
    content = file.read()
    file.close()
    return content


# book = file_reader("./book/001.txt")
# chapter_list = split_chapters(book)
# book_chapters = book_reader(chapter_list)

# while True:
#     book_chapters
#     key = input()
#     if key == " ":
#         next(book_chapters)


def random_letter(alphabet):
    return alphabet[rand(0, len(alphabet) - 1)]


def generate_word(up=None):
    world_len = rand(0, 20)
    word = ""
    for letter in range(0, world_len):
        if up and letter == 0:
            word += random_letter(alphabet).upper()
        else:
            word += random_letter(alphabet)
    return word


def radnom_dots_postions(chapter_len):
    dots_list = []
    for points in range(0, int(chapter_len / 3)):
        dots_list.append(rand(3, chapter_len))
    return dots_list


def generate_chapter_content(chapter_len):
    content = ""
    dots_list = radnom_dots_postions(chapter_len)
    for words in range(0, chapter_len):
        for dots in dots_list:
            if words == dots:
                content += ".\n"
                content += generate_word(up=True)
            elif words != 0 and words + 1 != dots:
                content += " "
            elif words == 0:
                content += generate_word(up=True)
            content += generate_word()
    return content


def generate_book(chapter_count, chapter_len):
    for x in range(1, chapter_count):
        chapter = "#Chapter {0}\n".format(x)
        chapter += generate_chapter_content(chapter_len)
        yield chapter


book1 = generate_book(3, 20)
for x in book1:
    print(x)

